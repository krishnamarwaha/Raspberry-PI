from sense_hat import SenseHat
from time import sleep
from subprocess import call

sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()
while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        call("sudo nohup shutdown -h now", shell=True)
        
