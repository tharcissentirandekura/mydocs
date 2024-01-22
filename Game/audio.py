import pygame
import gtts 

class PlayAudio:

    pygame.init()
    pygame.mixer.init()

    def __init__(self,text):
        self.text = text

    def convert_to_audio(self):
        audio = gtts.gTTS(self.text,lang="en")
        audio.save("audio.mp3")
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play()
        pygame.time.delay(3000)
        pygame.mixer.music.stop()
        pygame.quit()
    
color = "red"
play =  PlayAudio(f" The selected color is {color}")

play.convert_to_audio()
    





    




