from urllib.request import urlopen
import json
import time
from rpi_ws281x import PixelStrip, Color

apikey="e991c9e34f6e249c753fffc62a1ea915"
#lati ="52.11394"  #find your latitude and longitude from google maps. 
#longi = "0.08045"

lati = "8.839336"
longi = "39.407758"

LED_COUNT   = 64     # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#function that colours in the strip given the colour and the range
def goColour(strip, color, start, end):       
    for i in range(start, end+1):        
        strip.setPixelColor(i, color)
        strip.show()	        
		
#setup the strip
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

try:  
    goColour(strip, Color(0, 0, 0), 0, 63) #clear the strip
    oldTemp = 0   
        
    #get the data from the api website
    
    #api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your api key}
    url= "https://api.openweathermap.org/data/2.5/weather?lat="+lati+"&lon="+longi+"&units=metric&appid="+apikey 
    print(url)       
    #in case the Internet is not working: try it but then use the oldTemp just in case
    try:
        meteo=urlopen(url).read()
        meteo = meteo.decode('utf-8')
        weather = json.loads(meteo)        
        currentTemp = weather['main']['feels_like']        
    except IOError:           
        currentTemp = oldTemp
    
    oldTemp = currentTemp #set oldTemp to last known temperature
        
    #let's colour! It's always going to be < 0, white:
    goColour(strip, Color(255, 255, 255), 0,9)  #white    
    
    if currentTemp > 0:
        goColour(strip, Color(0, 0, 255), 10, 18)  # blue
    if currentTemp > 5:
        goColour(strip, Color(0, 255, 255), 19, 27)  # purple
    if currentTemp > 10:
        goColour(strip, Color(255, 0, 0), 28, 36) # green
    if currentTemp > 15:
        goColour(strip, Color(255, 255, 0), 37, 45)  # yellow
    if currentTemp > 20:
        goColour(strip, Color(100, 255, 0), 46, 54)  #orange
    if currentTemp > 25: #will this ever happen in Yorkshire??
        goColour(strip, Color(0, 255, 0), 55, 63)  # Red                  
	
except KeyboardInterrupt:
	print("Exit")
	goColour(strip, Color(0,0,0), 0, 240)
