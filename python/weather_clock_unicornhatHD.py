#!/usr/bin/env python

import time
import datetime
import requests, json 


try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

unicorn.rotation(180)
unicorn.brightness(0.5)

secondsProgressRow = 10

# There are 4 different types of patterns used when generating
# a number that is to be placed in a rectangle 3X5 pixels. Combinations of these
# are used to create a number pattern such as:
#   * * *
#   *
#   * * *
#   *   *
#   * * *

# 1) * * * Full Row
# 2) *   * Both Sides
# 3)     * Right Side
# 4) *     Left Side

# Composition methods
def fullLine(start, row):
  for x in range(start, start+3):
    unicorn.set_pixel(x, row, 255, 255, 255)

def bothSides(start, row):
  unicorn.set_pixel(start, row, 255, 255, 255)
  unicorn.set_pixel(start+2, row, 255, 255, 255)

def leftSide(start, row):
  unicorn.set_pixel(start, row, 255, 255, 255)

def rightSide(start, row):
  unicorn.set_pixel(start+2, row, 255, 255, 255)

# Numbers
def displayZero(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  bothSides(x, y-1)
  bothSides(x, y-2)
  bothSides(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayOne(x, y):
  clearNumberPixels(x, y)
  rightSide(x, y)
  rightSide(x, y-1)
  rightSide(x, y-2)
  rightSide(x, y-3)
  rightSide(x, y-4)
  unicorn.show()

def displayTwo(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  rightSide(x, y-1)
  fullLine(x, y-2)
  leftSide(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayThree(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  rightSide(x, y-1)
  fullLine(x, y-2)
  rightSide(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayFour(x, y):
  clearNumberPixels(x, y)
  bothSides(x, y)
  bothSides(x, y-1)
  fullLine(x, y-2)
  rightSide(x, y-3)
  rightSide(x, y-4)
  unicorn.show()

def displayFive(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  leftSide(x, y-1)
  fullLine(x, y-2)
  rightSide(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displaySix(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  leftSide(x, y-1)
  fullLine(x, y-2)
  bothSides(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displaySeven(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  rightSide(x, y-1)
  rightSide(x, y-2)
  rightSide(x, y-3)
  rightSide(x, y-4)
  unicorn.show()

def displayEight(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  bothSides(x, y-1)
  fullLine(x, y-2)
  bothSides(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayNine(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  bothSides(x, y-1)
  fullLine(x, y-2)
  rightSide(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayNumber(x,y, number):
  if number == 0:
    displayZero(x,y)
  elif number == 1:
    displayOne(x,y)
  elif number == 2:
    displayTwo(x,y)
  elif number == 3:
    displayThree(x,y)
  elif number == 4:
    displayFour(x,y)
  elif number == 5:
    displayFive(x,y)
  elif number == 6:
    displaySix(x,y)
  elif number == 7:
    displaySeven(x,y)
  elif number == 8:
    displayEight(x,y)
  elif number == 9:
    displayNine(x,y)

# Clears the pixels in a rectangle. x,y is the top left corner of the rectangle
# and its dimensions are 3X5
def clearNumberPixels(x, y):
  for y1 in range(y, y-5, -1):
    for x1 in range(x, x+3):
      # print("x1 = "+str(x1)+" y1 = "+str(y1))
      unicorn.set_pixel(x1, y1, 0, 0, 0)
  unicorn.show()

def displayTimeDots(x, y):
  unicorn.set_pixel(x, y-1, 255, 0, 0)
  unicorn.set_pixel(x, y-3, 255, 0, 0)
  unicorn.show()

def displayDateDots(x, y):
  unicorn.set_pixel(x+1, y, 255, 0, 0)
  unicorn.set_pixel(x+1, y-1, 255, 0, 0)
  unicorn.set_pixel(x+1, y-2, 255, 0, 0)
  unicorn.set_pixel(x, y-2, 255, 0, 0)
  unicorn.set_pixel(x, y-3, 255, 0, 0)
  unicorn.set_pixel(x, y-4, 255, 0, 0)
  unicorn.show()  

# Gets a specific part of the current time, passed to strftime, then it is
# split into its individual numbers and converted into integers. Used to feed
# the display with numbers
def getMinuteParts():
  minute = datetime.datetime.now().strftime("%M")
  return [int(x) for x in minute]

def getTimeParts(timePart):
  parts = datetime.datetime.now().strftime(timePart)
  return [int(x) for x in parts]  

def getTemperature():
  # Enter your API key here 
  api_key = "e991c9e34f6e249c753fffc62a1ea915"

  # base_url variable to store url 
  base_url = "http://api.openweathermap.org/data/2.5/weather?"

  # Give city name 
  city_name = "location" 

  # complete_url variable to store 
  # complete url address 
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

  # get method of requests module 
  # return response object 
  response = requests.get(complete_url) 

  # json method of response object 
  # convert json format data into 
  # python format data 
  x = response.json() 

  # Now x contains list of nested dictionaries 
  # Check the value of "cod" key is equal to 
  # "404", means city is found otherwise, 
  # city is not found 
  if x["cod"] != "404": 

    # store the value of "main" 
    # key in variable y 
    y = x["main"] 

    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] - 273.15

    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 

    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z 
    weather_description = z[0]["description"] 

    # print following values 
    print(weather_description)
    return round(current_temperature)
  return 0
temp = getTemperature()

print(temp)
displayedHourParts = getTimeParts('%H')
displayedMinuteParts = getTimeParts('%M')
displayedMonthParts = getTimeParts('%m')
displayedTempParts = []

if ( temp >= 10):
  displayedTempParts.append( int(temp / 10))
  displayedTempParts.append( temp % 10)
else:
  displayedTempParts.append(0)
  displayedTempParts.append(temp)

# Display Current Time
displayNumber(0,15, displayedHourParts[0])
displayNumber(4,15, displayedHourParts[1])
displayTimeDots(7,15)
displayNumber(9,15, displayedMinuteParts[0])
displayNumber(13,15, displayedMinuteParts[1])

# Display Day and Month
displayNumber(0,4, displayedTempParts[0])
displayNumber(4,4, displayedTempParts[1])

current_milli_time = lambda: int(round(time.time() * 1000))

step = 0

try:
  while True:
    hourParts = getTimeParts('%H')
    minuteParts = getTimeParts('%M')
    dayParts = getTimeParts('%d')
    monthParts = getTimeParts('%m')

    # TIME Details
    # Only update first hour number if it is different to what is currently displayed
    if hourParts[0] != displayedHourParts[0]:
      displayedHourParts[0] = hourParts[0]
      displayNumber(0,15, hourParts[0])

    # Only update second hour number if it is different to what is currently displayed
    if hourParts[1] != displayedHourParts[1]:
      displayedHourParts[1] = hourParts[1]
      displayNumber(4,15, hourParts[1])

    # Only update first minute number if it is different to what is currently displayed
    if minuteParts[0] != displayedMinuteParts[0]:
      displayedMinuteParts[0] = minuteParts[0]
      displayNumber(9,15, minuteParts[0])

    # Only update second minute number if it is different to what is currently displayed
    if minuteParts[1] != displayedMinuteParts[1]:
      displayedMinuteParts[1] = minuteParts[1]
      displayNumber(13,15, minuteParts[1])

    # Sleep for 0.5 because the display doesn't need to update that often
    time.sleep(60)
except KeyboardInterrupt:
  unicorn.off()