#!/usr/bin/env python
import serial
import time
import struct

EV3 = serial.Serial('/dev/rfcomm0')
EV3.flushInput()
print ("Receiving EV3 Bluetooth messages")
box  = "Mail Box"

def main():
    while True:
        rx = readMessage()
        decodeMessage(rx)
    EV3.close()

# Function definitions
def readMessage():
    global box
    while EV3.inWating() <2 :# hold until message starts to arrive
      continue
    inMessage = EV3.read(2)
    messageByets = ord(inMessage[o])
    while EV3.inWaiting() < (messageByets ):
      continue
    inMessage = inMessage + EV3.read(messageBytes )
    box = inMessage[7 : 7 + ord(inMessage[6])-1]
    payloadPointer = 9 + ord(inMessage[6])
    message = inMessage[payloadPointer:]
    return message

def decodeMessage(payload) :
    print ("Message from box",box,"is a"),
    if box == "Text" :
        print ("text message saying"),
        print (payload)

    if box == "Logic" :
        print ("logic message of"),
        logic = False
        if ord(payload[0]) == 1 :
            logic = False
        print (logic)

    if box == "Number" :
        print ("number with a value of"),
        val = struct.unpack('f',payload)
        value = val[0] # to convert from a tuple
        print (value)
    print
    main()
    
