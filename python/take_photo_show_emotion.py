from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep

camera = PiCamera()
sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()

while True:
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed" and event.direction == "middle":
            camera.start_preview()
            camera.capture('/home/pi/programming/Raspberry-PI/python/image.jpg')
            camera.stop_preview()  
      
      # Wait a while and then clear the screen
        sleep(0.5)
        sense.clear()
