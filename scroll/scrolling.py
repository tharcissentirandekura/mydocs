import picture
import sys

def background(width,height,color = sys.argv[2]):
        picture.new_picture(width,height)
        picture.set_fill_color("black")
        picture.draw_filled_rectangle(0,0,width,height)

def run(width,height):
    color = 'green'
    picture.new_picture(width,height)
    x = 1
    y = 10
    for i in range(100):
        color = "blue" if color == "green" else "green"
        picture.set_fill_color(color)
        picture.set_outline_color(color)
        picture.set_pen_width(3)
        
        picture.rotate(30)
        # picture.draw_forward(100)
        
        position = picture.get_position()
        
        if x >= dimension :
             y = y + 50
             x = 0 
        elif y >= dimension:
             y = 0
        print(x,y)
        picture.draw_filled_circle(x,y,20)
        x +=  50


       

        picture.display()


dimension = int(sys.argv[1])
color = sys.argv[2]
background(dimension,dimension,color = color)
run(dimension,dimension)