from sense_hat import SenseHat

sense = SenseHat()

g = (0,255,0)
r = (255,0,0)
b =(0,0,0)

creeper_pixels = [

 g,g,b,b,b,b,g,g,
 g,g,b,b,b,b,g,g,
 b,r,r,b,b,r,r,b,
 b,r,r,b,b,r,r,b,
 b,b,b,r,r,b,b,b,
 b,b,r,r,r,r,b,b,
 b,b,r,r,r,r,b,b,
 b,b,r,b,b,r,b,b
 ]
sense.set_pixels(creeper_pixels)
