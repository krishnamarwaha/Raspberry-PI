from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

s = (163,71,69)
m = (71,55,39)
e = (121,94,67)
n = (64,0,0)
p = (255,198,188)
a = (254,68,21)
y = (255,242,0)
r = (255,0,0)
w = (0,0,0)
b = (128,255,255)
d = (0,0,128)

happy = [
      y,y,y,y,y,y,y,y,
      y,n,n,y,y,n,n,y,
      y,n,n,y,y,n,n,y,
      y,w,w,y,y,w,w,y,
      y,w,w,y,y,w,w,y,
      y,r,w,w,w,w,r,y,
      y,w,r,r,r,r,w,y,
      y,y,y,y,y,y,y,y
      ]
sense.set_pixels(happy)

sad = [
      b,b,b,b,b,b,b,b,
      b,n,n,w,w,n,n,b,
      b,n,n,w,w,n,n,b,
      b,d,d,w,w,d,d,b,
      b,d,d,w,w,d,d,b,
      b,d,d,r,r,d,d,b,
      b,d,r,r,r,r,d,b,
      b,b,b,b,b,b,b,b
      ]


angry = [
        a,a,a,a,a,a,a,a,
        a,e,e,w,w,e,e,a,
        a,n,n,w,w,n,n,a,
        a,n,n,w,w,n,n,a,
        a,w,w,w,w,w,w,a,
        a,w,r,r,r,r,w,a,
        a,r,w,w,w,w,r,a,
        a,a,a,a,a,a,a,a,
]


suprised = [
            y,y,y,y,y,y,y,y,
            y,n,n,y,y,n,n,y,
            y,n,n,y,y,n,n,y,
            y,y,y,y,y,y,y,y,
            y,y,s,s,s,s,y,y,
            y,y,s,s,s,s,y,y,
            y,y,s,s,s,s,y,y,
            y,y,y,y,y,y,y,y
]

sense.clear()
while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":


       if event.direction == "left":


          sense.set_pixels(sad)
          sleep(3)
          sense.set_pixels(happy)
          sleep(3)
          sense.set_pixels(angry)
          sleep(3)
          sense.set_pixels(suprised)
          sleep(3)

 
   