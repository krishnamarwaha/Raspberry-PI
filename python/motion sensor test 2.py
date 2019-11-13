import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)        
while True:
    i=GPIO.input(11)
    if i==0:                 
        print ("Not Sensing Motion"),i
        time.sleep(0.1)
    elif i==1:              
        print ("Motion Detected"),i
        time.sleep(0.1)
