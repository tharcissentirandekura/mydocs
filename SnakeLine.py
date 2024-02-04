import sys
import picture
import time
import random

picture.new_picture(128,128)
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,128,128)

red = 255
green = 200
blue = 45

sec = 0
move = 100
top = 100
bottom = 0
right = 5
left = 5
back = 64
x = 15
y = 400
right = 300
left = 300
picture.set_position(right,left)

x_position = []
i =0

red = 255
green = 200
blue = 45

rounds = 0

for j in range(500):
    i += 1
    picture.set_fill_color(red,green,blue)
    if rounds > 0 and rounds % 2 == 0:
        picture.set_outline_color(red,green,blue)
    else:
        picture.set_outline_color('white')
    picture.set_pen_width(1)
    picture.draw_forward(1)
   
    x = picture.get_position()[0]
    y =  picture.get_position()[1]
    x_position.append(x)
    picture.draw_on_matrix()
    #time.sleep(sec)
    if i > 0 and i % 5 == 0:
        picture.rotate(90)
    pos = picture.get_position()
    if pos[0] + 1 in x_position:
        picture.rotate(random.choice([90,180,270]))
        picture.draw_forward(1)
    if x >= 125 or y >= 125 or x <= 0 or y <= 0:
        picture.set_position(60,60)
        rounds +=1
    if x + 5 >= 120:
        i = 0
        picture.rotate(270)



    red = (red - 20) % 250
    blue = (blue - 20) % 250
    green = (blue + 20) % 255
