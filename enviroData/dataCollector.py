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

try:
    while True:
        try:
            data = {}
            readings = pms5003.read()
            print(readings)  
            readings = gas.read_all()
            print(readings)  
            temperature = bme280.get_temperature()
            pressure = bme280.get_pressure()
            humidity = bme280.get_humidity()
            data['measurement'] = 'enviro'
            fields = {}
            fields['temperature'] = temperature
            fields['pressure'] = pressure
            fields['humidity'] = humidity
            data['fields'] = fields
            j = [data]
            print(j)
            client.write_points(j)
        except ReadTimeoutError:
            pms5003 = PMS5003()
            print("timeout")
        time.sleep(1)

except KeyboardInterrupt:
    pass
