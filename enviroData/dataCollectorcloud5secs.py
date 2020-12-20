#!/usr/bin/env python3
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import json
from enviroplus import gas
from pms5003 import PMS5003, ReadTimeoutError
from enviroplus import gas
from bme280 import BME280


try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

pms5003 = PMS5003()
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

time.sleep(0.5)
token = "okO37ojfMVoBI1xcsQRmxiJgv-1TSSOzYqlnX2Au3mM23hP8nIA1qH-z2AXmPgHe0XK6oE4-ywln6o_vqBOesw=="
org = "krishna.lakhan.marwaha@gmail.com"
bucket = "krishna.lakhan.marwaha's Bucket"

client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.25

cpu_temps = [get_cpu_temperature()] * 5

try:
    while True:
        try:
            data = {}
            pm_readings = pms5003.read()
            gas_readings = gas.read_all()
            pressure = bme280.get_pressure()
            humidity = bme280.get_humidity()
            cpu_temp = get_cpu_temperature()
            # Smooth out with some averaging to decrease jitter
            cpu_temps = cpu_temps[1:] + [cpu_temp]
            avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
            raw_temp = bme280.get_temperature()
            temperature = raw_temp - ((avg_cpu_temp - raw_temp) / factor)
            
            data['measurement'] = 'enviro'
            fields = {}
            fields['temperature'] = temperature
            fields['raw_temperature'] = raw_temp
            fields['pressure'] = pressure
            fields['humidity'] = humidity
            fields['pm_1'] = pm_readings.pm_ug_per_m3(1)
            fields['pm_2.5'] = pm_readings.pm_ug_per_m3(2.5)
            fields['pm_10'] = pm_readings.pm_ug_per_m3(10)
            fields['gas'] = gas_readings
            data['fields'] = fields
            j = [data]
            print(j)
         #   client.write_points(j)
            write_api.write(bucket, org, j)
        except ReadTimeoutError:
            pms5003 = PMS5003()
            print("timeout")
        time.sleep(5)

except KeyboardInterrupt:
    pass








