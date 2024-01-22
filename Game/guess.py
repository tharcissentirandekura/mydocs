from folders import importing_library_picture_from_scroll_folder

importing_library_picture_from_scroll_folder() # to avoid repetition of files in the same folder

from scroll.picture import *
from time import sleep
import random
import pygame
import gtts 


class GuessColor:

    def __init__(self,width,height,text = 'none'):
    
        self.width = width
        self.height = height
        self.text = text
        new_picture(self.width,self.height)

    def background_color(self):
        set_fill_color("black")
        set_outline_color("black")
        draw_filled_rectangle(0,0,self.width,self.height)
        display()
    
    def audio(self):
        pygame.init()
        pygame.mixer.init()
        audio = gtts.gTTS(self.text,lang="en")
        audio.save("audio.mp3")
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play()
        pygame.time.delay(3000)
        pygame.mixer.music.stop()
        pygame.quit()
              
    def circle(self,colors):

        for i in range(1,30,3):
            # print(i)
            color = random.choice(colors)
            self.text = color

            set_outline_color("white")
            draw_text(150,100,"The selected color is ",font_size=30)
            
            draw_text(433,100,self.text,font_size=30)
            display()
        
            set_fill_color("black")
            set_outline_color("black")
            draw_filled_rectangle(433,100,100,100)


            set_fill_color(color)
            set_outline_color(color)
            draw_filled_circle(350,350,100)
            display()

        draw_text(433,100,self.text,font_size=30)
        display()
        
        sleep(1)
            
if __name__ == "__main__":
    guess = GuessColor(800,800)
    colors = ['red','green','blue','white']
    
    while True:
        guess.background_color()
        guess.circle(colors)
        guess.audio()





