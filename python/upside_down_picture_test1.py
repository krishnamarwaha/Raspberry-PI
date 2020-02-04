#!/usr/bin/env python
from picamera import PiCamera
import pantilthat
from time import sleep
import time 
import datetime
import math

t = time.time()
a = math.sin(t * 2) * 90
a = int(a)    
camera = PiCamera()
camera.rotation = 180
i = 0
while i < 10:
    camera.start_preview()
    sleep(5)
    date = datetime.datetime.now().strftime("%_%d_%Y_%H_%M_%S")
    camera.capture('/home/pi/programming/Raspberry-PI/python/images/picture'+ date +'.jpg')
    camera.stop_preview()
    i = i + 1

while True:
    # Get the time in seconds
    t = time.time()

    # G enerate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
    a = math.sin(t * 2) * 90
    
    # Cast a to int for v0.0.2
    a = int(a)

    pantilthat.pan(a)
    pantilthat.tilt(a)

    # Two decimal places is quite enough!
    print(round(a,0))

    # Sleep for a bit so we're not hammering the HAT with updates
    time.sleep(5)

