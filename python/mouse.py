#!/usr/bin/env python
from picamera import PiCamera
import pantilthat
from time import sleep
import time 
import datetime
import math

camera = PiCamera()
camera.rotation = 180
pantilthat.pan(15)
pantilthat.tilt(+30)

i = 0
while True:
    camera.start_preview()
    sleep(2
    )
    date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    camera.capture('/home/pi/programming/Raspberry-PI/python/images/picture'+ date +'.jpg')
    camera.stop_preview()
    i = i + 1


