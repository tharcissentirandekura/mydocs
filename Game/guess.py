from folders import importing_library_picture_from_scroll_folder
importing_library_picture_from_scroll_folder() # to avoid repetition of files in the same folder

from scroll.picture import *
from time import sleep
import random

class GuessColor:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        new_picture(self.width,self.height)

    def background_color(self):
        set_fill_color("black")
        draw_filled_rectangle(0,0,self.width,self.height)
        display()
            
    
    def circle(self,color = "red"):

        positions = []
        x = 10
        y = 10

        
        for i in range(1,60,3):
            color = "red" if color == "black" else "black"
            x = random.randint(100,800)
            y = random.randint(100,800)
            # print(x,y)
            set_fill_color(color)
            draw_filled_circle(x,y,50)
            positions.append((x,y))
            display()
            sleep(1)

            GuessColor(self.width,self.height).background_color()
            set_fill_color('green')
            draw_filled_circle(x,y,50)
            display()
            sleep(1)
            set_fill_color('white')
            draw_filled_circle(x,y,50)
            
            
            


if __name__ == "__main__":
    guess = GuessColor(800,800)
    
    while True:
        guess.background_color()
        guess.circle()
        # display()




