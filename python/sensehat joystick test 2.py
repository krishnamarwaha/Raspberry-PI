from sense_hat import SenseHat

sense = SenseHat()
sense.clear
print(event.action +  " " + event.direction)
while True:
    for event in sense.stick.get_events()
