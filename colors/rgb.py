from folders import importing_library_picture_from_scroll_folder
importing_library_picture_from_scroll_folder() # to avoid repetition of files in the same folder

from time import sleep
from scroll.picture import *

class RGB:

    def __init__(self,width,height):

        self.width = width
        self.height = height
        new_picture(width,height)
    
    def colors(self):
        for red in range(0,270,30):
            for blue in range(0,270,30):
                for green in range(0,270,30):
                    print(red,green,blue)
                    set_fill_color(red,green,blue)
                    draw_filled_rectangle(0,0,self.width,self.height)
                    display()
                    sleep(1)
                    
if __name__ == "__main__":
    rgb = RGB(800,800)
    rgb.colors()

    


        