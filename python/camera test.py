from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/programming/Raspberry-PI/python/image2.jpg')
camera.stop_preview()
