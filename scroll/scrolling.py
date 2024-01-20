import picture
import sys
import time

def background(width,height,color = sys.argv[2]):
        picture.new_picture(width,height)
        picture.set_fill_color("black")
        picture.draw_filled_rectangle(0,0,width,height)

def run(width,height):
    color = 'green'
    picture.new_picture(width,height)
    x = 1
    y = 10
    while True:
        color = "blue" if color == "green" else "green"
        picture.set_fill_color(color)
        picture.set_outline_color(color)
        picture.set_pen_width(3)
        
        picture.set_position(x,y)
        
        # picture.draw_forward(40 +x)
        
        if x >= dimension :
                y = y + 50
                x = 0 
        if y >= dimension:
                y = 0
        
        picture.draw_filled_circle(x,y + x,20)
        picture.set_fill_color('black')
        picture.draw_filled_circle(x,y,20)
        x +=  50
        picture.set_position(x,y)
        # print(x,y)
        picture.display()
            
        print("positions :",picture.get_position())
dimension = int(sys.argv[1])
color = sys.argv[2]
background(dimension,dimension,color = 'black')
run(dimension,dimension)

