
import argparse
import urllib2
import base64
import json
import time
import datetime
	
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


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
        
        if(happy_string != "VERY_UNLIKELY"):
            ("You seem happy!  Tell me why you are so happy!")
        elif(anger_string != "VERY_UNLIKELY"):
            ("Uh oh, you seem angry!  I have kids, please don't hurt me!")
        elif(surprise_string != "VERY_UNLIKELY"):
            ("You seem surprised!  ")
        else:
            ("You seem sad!  Would you like a hug?")
        
    except:
        ("I am sorry, I can not see your face.  May I try again?")
    
def take_emotion():
    print("checking google")
    credentials = GoogleCredentials.get_application_default()
    print("google checked")
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open('image.jpg', 'rb') as image:
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

take_emotion()
