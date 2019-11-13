import random
import pygame
from sense_hat import SenseHat


sense = SenseHat()

sense.clear()

o = (208, 60, 1)
w = (255,255,255)
b = (0,0,0)
p = (50, 5 ,76)
matrix = [[b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b]]
#sense.set_pixels(sum( matrix,[]))
x = 0
y = 0
ghosts = 5
pumpkins = 3

count = 0
while count < ghosts:    
    x = random.randint(0,7)
    y = random.randint(0,7)
    if matrix[y][x] == b:
        matrix[y][x] = p
        count = count+1


count = 0
while count < pumpkins:    
    x = random.randint(0,7)
    y = random.randint(0,7)
    if matrix[y][x] == b:
        matrix[y][x] = o
        count = count+1

   


while True:
    x = random.randint(0,7)
    y = random.randint(0,7)
    if matrix[y][x] == b:
        break
    
sense.set_pixel(x, y, w)


game_over = False

ghostsFound = 0
pumpkinsFound = 0

def move_torch(event):
    global x
    global y
    global game_over
    global ghosts
    global pumpkins
    global ghostsFound
    global pumpkinsFound
    
    sense.set_pixel(x, y, b)
        
    if event.action == "pressed":
        if event.direction == "up" and y > 0:
            y -= 1
        elif event.direction =="down" and y < 7:
            y += 1
        elif event.direction =="right"and x < 7:
             x += 1
        elif event.direction =="left" and x > 0:
            x -= 1

    if matrix[y][x] == b:
        sense.set_pixel(x, y, w)
    elif matrix[y][x] == p:
        sense.set_pixel(x, y, matrix[y][x]) 
        matrix[y][x] = b
        ghostsFound = ghostsFound + 1
        print("Ghosts " + str(ghostsFound))
        
    elif matrix[y][x] == o:
        sense.set_pixel(x, y, matrix[y][x])
        matrix[y][x] = b
        pumpkinsFound = pumpkinsFound + 1
        print("Pumpkins " + str(pumpkinsFound))

    if pumpkinsFound == pumpkins:
        game_over = True

    if ghostsFound == ghosts:
        game_over = True
    
sense.stick.direction_any = move_torch

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Spooky2.mp3")
pygame.mixer.music.play()

while True:
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()
        
    if game_over:
        break

if pumpkinsFound == pumpkins:
    sense.show_message('You Win')
if ghostsFound == ghosts:
    sense.show_message('You Lose Better Luck Next Time')


