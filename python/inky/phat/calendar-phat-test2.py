
import datetime
import calendar
import argparse
from PIL import Image, ImageDraw

from inky import InkyWHAT

parser = argparse.ArgumentParser()
parser.add_argument('--colour', '-c', type=str, required=True, choices=["red", "black", "yellow"], help="ePaper display colour")
args = parser.parse_args()

colour = args.colour

inky_display = InkyWHAT(colour)
#img = Image.open("resources/test_hello_krishna.png")
img = Image.open("resources/test16.png")
w, h = img.size
print(w)
print(h)
draw = ImageDraw.Draw(img)

inky_display.set_image(img)
inky_display.show()
