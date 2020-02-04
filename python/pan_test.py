import pantilthat
from time import sleep
import time 
from picamera import PiCamera
import datetime

camera = PiCamera()
camera.rotation = 180
a = -90
x = 15
while True:
    a = a + x
    if ( a == 90):
        x = -15
    if  ( a == -90):
        x = 15
    pantilthat.pan(a)
    time.sleep(3)
    camera.start_preview()
    date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    camera.capture('/home/pi/programming/Raspberry-PI/python/images/picture_'+ date +'.jpg')
    camera.stop_preview()
   
