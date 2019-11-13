from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()

while True:
    for event in sense.stick.get_events():
    # Check if the joystick was pressed
        if event.action == "pressed" and event.direction == "middle":
            from picamera import PiCamera
            from time import sleep

            camera = PiCamera()

            camera.start_preview()
            camera.capture('/home/pi/Desktop/image.jpg')
            camera.stop_preview()  
               # Enter key
      
      # Wait a while and then clear the screen
        sleep(0.5)
        sense.clear()
