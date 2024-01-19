import picture
import sys
# from recursion import recursive

class MultiSquare:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def drawSquare(self):
        red = 30
        green = 250
        blue = 200

        color = "white"

        picture.set_fill_color(color)
        for x in range(-1,int(sys.argv[1]) * 2):
            for y in range(-1,int(sys.argv[1]) * 2):
                color  = "blue" if color == "white" else "white"

                picture.draw_filled_rectangle((self.width //int(sys.argv[1])) * x,(self.height // int(sys.argv[1])) * y,width//int(sys.argv[1]),height//int(sys.argv[1]))
            
                picture.set_fill_color(color)
                picture.set_outline_color("black")
                picture.set_pen_width(2)
                picture.display()

if __name__ == "__main__":
    width = 720
    height = 720
    picture.new_picture(width, height)
    picture.set_fill_color("black")
    picture.draw_filled_rectangle(0,0,width,height)
    squares = MultiSquare(width,height)

    squares.drawSquare()

