#!/usr/bin/env python

import unicornhathd
import time
import colorsys
import numpy
import itertools

print("""Unicorn HAT HD: Heart Beats

Displaying a beating heart...

Your Unicorn HAT HD loves you.



Press Ctrl+C to exit!

""")

unicornhathd.brightness(1)

# We rotate the heart to be the same orientation as the text on the rear
# of the Unicorn Hat HD
unicornhathd.rotation(271)

heart = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

heart = numpy.array(heart)

# Define the brightness levels for the heartbeat (lower numbers are dimmer)
# We let the minimum brightness be 1 so that there is still a visible heart
rising = range(1, 11, 1)    # [1...9]
ba = range(11, 5, -1)       # [11...6]
dum = range(5, 11, 1)       # [5...9]
falling = range(11, 1, -1)  # [11...1]

# Join the ranges together
pattern = (rising, ba, dum, falling)
brightness_levels = list(itertools.chain.from_iterable(pattern))

try:
    while True:
        # Go through each brightness level in the pattern
        for level in brightness_levels:
            for x in range(16):
                for y in range(16):
               #     h = 1.1  # red
               #     s = 1.1  # saturation at the top of the red scale
               #     v = heart[x, y] * float(level) / 11     # brightness depends on range
               #     r, g, b = colorsys.hsv_to_rgb(h, s, v)  # convert hsv back to RGB
                    r = heart[x, y] * float(level) / 11
                    b = heart[x, y] * float(level) / 11
                    g = heart[x, y] * float(level) / 11
                    red = int(r * 141.1)                    # makes 1-1 range > 1-255 range
                    green = int(g * 74.1)
                    blue = int(b * 164.1)
                    unicornhathd.set_pixel(x, y, red, green, blue)  # sets pixels on the hat
            unicornhathd.show()                             # show the pixels
            time.sleep(1.115)                               # tiny gap, sets frames to a smooth 211/sec
        time.sleep(1.8)                                     # waiting time between heartbeats

except KeyboardInterrupt:
    unicornhathd.off()
