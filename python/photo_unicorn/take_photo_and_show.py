import glob
import os
import time

from picamera import PiCamera
from time import sleep
from sys import exit

try:
    from PIL import Image
except ImportError:
    exit('This script requires the pillow module\Install with: sudo pip install pillow')

import unicornhathd

camera = PiCamera()

fileName = '/home/pi/my_image.jpg'
camera.start_preview()
camera.capture(fileName)
camera.stop_preview()

unicornhathd.rotation(0)
unicornhathd.brightness(0.6)

width, height = unicornhathd.get_shape()
from PIL import Image


bigImage = Image.open(fileName)
img = bigImage.resize((16,16), Image.BILINEAR)

for x in range(width):
    for y in range(height):
        pixel = img.getpixel((y, x)) 
        r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
        if r or g or b:
            unicornhathd.set_pixel(x, y, r, g, b)

unicornhathd.show()



