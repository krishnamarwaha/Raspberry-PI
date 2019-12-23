from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne


inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 18)

line1 = "Krishna"
line2 = "Lakhan"
line3 = "Marwaha Is"
line4 = "The Best!"
w1, h1 = font.getsize(line1)
w2, h2 = font.getsize(line2)
w3, h3 = font.getsize(line3)
w4, h4 = font.getsize(line4)

h =  h1 + h2 + h3 + h4
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((20, y), line1, inky_display.RED, font)
draw.text((40, y+h1), line2, inky_display.RED, font)
draw.text((10, y+h1+h2), line3, inky_display.BLACK, font)
draw.text((60, y+h1+h2+h3), line4, inky_display.RED, font)

inky_display.set_image(img)
inky_display.show()