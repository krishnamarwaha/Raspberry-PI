from picamera import PiCamera
from time import sleep
import time 
import datetime
import math
from pantilthat import PanTiltHat

a = math.sin(t * 2) * 90
a = int(a)    
camera = PiCamera()
camera.rotation = 180
i = 0
while i < 10:
    camera.start_preview()
    sleep(5)
    date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    camera.capture('/home/pi/programming/Raspberry-PI/python/images/picture'+ date +'.jpg')
    camera.stop_preview()
    i = i + 1

while i < 10: 
    sleep(5)
    pantilthat.pan(a)
    print(round(a,0))
    sleep(5)
