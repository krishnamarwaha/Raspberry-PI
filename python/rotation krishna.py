
import sys
import time
from sense_hat import SenseHat

x = (255, 0, 0)
o = (255, 255, 255)

question_mark = [
    o,o,o,x,x,o,o,o,
    o,o,x,o,o,x,o,o,
    o,o,o,o,o,x,o,o,
    o,o,o,o,x,o,o,o,
    o,o,o,x,o,o,o,o,
    o,o,o,x,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,x,o,o,o,o
]

sense = SenseHat()

sense.set_pixels(question_mark)

sense.set_pixel(0, 0, 255, 0, 0)
sense.set_pixel(0, 7, 0, 255, 0)
sense.set_pixel(7, 0, 0, 0, 255)
sense.set_pixel(7, 7, 255, 0, 255)

while True:
    for r in [0, 90, 180, 270]:
        sense.set_rotation(r)
        time.sleep(0.3)
    


    


    


 

