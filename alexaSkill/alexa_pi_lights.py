import logging
import os
import time
from rpi_ws281x import PixelStrip, Color
import argparse

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

STATUSON = ['on','high']
STATUSOFF = ['off','low']


# LED strip configuration:
LED_COUNT = 64        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()


def testStrip(strip):
    """Wipe color across display a pixel at a time."""
    off = Color(0,0,0)
    for i in range(strip.numPixels()):
        red = Color(255,3*i,3*i)
        strip.setPixelColor(i, red)
        strip.show()
        time.sleep(0.1)
        strip.setPixelColor(i,off)

@ask.launch
def launch():
    speech_text = 'Welcome to Raspberry Pi Automation.'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('GpioIntent', mapping = {'status':'status'})
def Gpio_Intent(status,room):
    print( 'status is ' + status)
    if status in STATUSON:
        off = Color(0,0,0)
        red = Color(255,0,0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,red)
        strip.show()
        return statement('turning {} lights'.format(status))
    elif status in STATUSOFF:
        off = Color(0,0,0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,off)
        strip.show()
        return statement('turning {} lights'.format(status))
    elif status in ['green']:
        off = Color(0,255,0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,off)
        strip.show()
        return statement('turning {} lights'.format(status))
    elif status in ['blue']:
        off = Color(0,0,255)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,off)
        strip.show()
        return statement('turning {} lights'.format(status))    
    elif status in ['red']:
        off = Color(255,0,0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,off)
        strip.show()
        return statement('turning {} lights'.format(status))    
    elif status in ['off']:
        off = Color(0,0,0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,off)
        strip.show()
        return statement('turning {} lights'.format(status))
    elif status in ['yellow']:
        off = Color(255,242,0)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,off)
        strip.show()
        return statement('turning {} lights'.format(status))     
    elif status in ['purple']:
        off = Color(104,11,155)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,off)
        strip.show()
        return statement('turning {} lights'.format(status))
    elif status in ['pink']:
        off = Color(255,128,192)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,off)
        strip.show()
        return statement('turning {} lights'.format(status))
    else:
        return statement('Sorry Krishna I will do {} lights later'.format(status))
 
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
