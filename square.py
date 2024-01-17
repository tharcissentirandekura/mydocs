import picture
import time
import sys
class DrawSquare:
    red = 30
    green = 250
    blue = 200
    
    picture.set_pen_width(1)
    
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def draw_square(self):
        
        picture.new_picture(self.width,self.height)

        picture.set_fill_color("black")
        picture.draw_filled_rectangle(0,0,64,64)
        #time.sleep(1)
        
    
        for i in range(16):
            picture.set_outline_color(self.red,self.green,self.blue)

            for k in range(35):
                picture.draw_circle(2 * (k * 3),i * 5,4)
                
                self.green = (self.green + 20) % 255
            self.red = (self.red - 20) % 250

        picture.draw_on_matrix()
        



if __name__ == "__main__":

    square = DrawSquare(int(sys.argv[1]),int(sys.argv[1]))
    picture.set_fill_color("blue")
    square.draw_square()
    #picture.draw_on_matrix()


    
