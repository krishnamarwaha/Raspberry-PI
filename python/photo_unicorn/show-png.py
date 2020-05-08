#!/usr/bin/env python
import glob
import os
import time
from sys import exit

try:
    from PIL import Image
except ImportError:
    exit('This script requires the pillow module\Install with: sudo pip install pillow')

import unicornhathd


print("""Unicorn HAT HD: Show a PNG image!

This basic example shows use of the Python Pillow library.

The tiny 16x16 bosses in lofi.png are from Oddball:
http://forums.tigsource.com/index.php?topic=8834.0

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0
Unported License.

Press Ctrl+C to exit!

""")

unicornhathd.rotation(0)
unicornhathd.brightness(0.6)

width, height = unicornhathd.get_shape()
from PIL import Image
#latest_file = max(list_of_files, key=os.path.getctime)
#smallImage = latest_file.resize((16,16), Image.BILINEAR)
#print("test")
#smallImage.save('pixel_art2.png')

img = Image.open('pixel_art2.png')

for x in range(width):
    for y in range(height):
        pixel = img.getpixel((y, x)) 
        r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
        if r or g or b:
            unicornhathd.set_pixel(x, y, r, g, b)

unicornhathd.show()

