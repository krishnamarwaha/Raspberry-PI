from sense_hat import SenseHat
from picamera import PiCamera
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

import argparse
import urllib2
import base64
import json
import time
import datetime


sense = SenseHat()
sense.clear()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()
camera = PiCamera()

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

def parse_response(json_response):
    # print json_response
    try:
        # print json.dumps(response, indent=4, sort_keys=True)	#Print it out and make it somewhat pretty.
        anger = json_response['responses'][0]['faceAnnotations'][0]['angerLikelihood']
        surprise = json_response['responses'][0]['faceAnnotations'][0]['surpriseLikelihood']
        sorrow = json_response['responses'][0]['faceAnnotations'][0]['sorrowLikelihood']
        blurr = json_response['responses'][0]['faceAnnotations'][0]['blurredLikelihood']
        joy = json_response['responses'][0]['faceAnnotations'][0]['joyLikelihood']
        
        anger_string = (str(anger))
        surprise_string = (str(surprise))
        sorrow_string = (str(sorrow))
        # print(str(blurr))
        happy_string = (str(joy))
        
        print("Happy: " + happy_string)
        print("Angry: " + anger_string)
        print("Surprise: " + surprise_string)
        print("Sorrow: " + sorrow_string)
        # ("You look pretty. . . . tired.  You must have an infant?")
        
        if ( sorrow_string == "POSSIBLE" or sorrow_string == "LIKELY" or sorrow_string == "VERY_LIKELY"):
            sense.set_pixels(sad)
      
        if ( happy_string == "POSSIBLE" or happy_string == "LIKELY" or happy_string == "VERY_LIKELY"):
            sense.set_pixels(happy)

        if ( anger_string == "POSSIBLE" or anger_string == "LIKELY" or anger_string == "VERY_LIKELY"):
            sense.set_pixels(angry)

        if ( surprise_string == "POSSIBLE" or surprise_string == "LIKELY" or surprise_string == "VERY_LIKELY"):
            sense.set_pixels(suprised)


    except:
        ("I am sorry, I can not see your face.  May I try again?")

def show_emotion(filename):
    
    credentials = GoogleCredentials.get_application_default()
    
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open(filename, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'FACE_DETECTION',
                    'maxResults': 10
                }]
            }]
        })
        response = service_request.execute()
        parse_response(response)

while True:
    for event in sense.stick.get_events():
    # Check if the joystick was pressed
        if event.action == "pressed" and event.direction == "middle":
            now = datetime.datetime.now()
            filename = now.strftime("%Y%m%d_%H%M%S")
            filename =  '/home/pi/images/' + filename + '.jpg'
            camera.start_preview()
            camera.capture(filename)                            
            camera.stop_preview()
            show_emotion(filename)
