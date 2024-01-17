import picture
import time

class DrawSquare:
    red = 30
    green = 250
    blue = 200
    
    picture.set_pen_width(4)
    
    def __init__(self,width,height):
        
        self.width = width
        self.height = height

    def draw_square(self):
        
        picture.new_picture(self.width,self.height)

        picture.set_fill_color("black")
        picture.draw_filled_rectangle(0,0,1400,1400)
        time.sleep(1)
        
    
        for i in range(1,16):
            picture.set_outline_color(self.red,self.green,self.blue)

            for k in range(35):
                picture.draw_circle(8 * (k * 5),i * 70,80)
                
            self.green = (self.green + 20) % 255
            self.red = (self.red - 20) % 250

        picture.save_picture("square.png")



if __name__ == "__main__":

    square = DrawSquare(1400,1400)
    picture.set_fill_color("blue")
    square.draw_square()


    
