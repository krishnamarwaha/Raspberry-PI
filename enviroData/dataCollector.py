#!/usr/bin/env python3

import time
import json
from pms5003 import PMS5003, ReadTimeoutError
from enviroplus import gas
from bme280 import BME280
from influxdb import InfluxDBClient

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

pms5003 = PMS5003()
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

time.sleep(0.5)
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('envdata')

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
            data['fields'] = fields
            j = [data]
            print(j)
            client.write_points(j)
        except ReadTimeoutError:
            pms5003 = PMS5003()
            print("timeout")
        time.sleep(60)

except KeyboardInterrupt:
    pass
