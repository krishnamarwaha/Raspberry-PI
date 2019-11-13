from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.capture('/home/pi/programming/python/webservers/testserver/static/image.jpg')
camera.stop_preview()