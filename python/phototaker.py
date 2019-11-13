from sense_hat import SenseHat
from time import sleep
from picamera import PiCamera

sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()
camera = PiCamera()

while True:
    for event in sense.stick.get_events():
    # Check if the joystick was pressed
        if event.action == "pressed" and event.direction == "middle":
            camera.start_preview()
            camera.capture('/home/pi/programming/python/webservers/testserver/static/image.jpg')                            
            camera.stop_preview()  
      
