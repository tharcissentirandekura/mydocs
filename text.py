from samplebase import SampleBase
from rgbmatrix import graphics
import time
import sys

class Graphing(SampleBase):

    def __init__(self,*args,**kwargs):
        super(Graphing,self).__init__(*args,**kwargs)

    
    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bef")

        argument = sys.argv

        red = graphics.Color(255,0,0)
        graphics.DrawLine(canvas,10,10,22,13,red)

        green = graphics.Color(0, 255, 0)
        graphics.DrawCircle(canvas, 15, 15, 10, green)

        blue = graphics.Color(0, 0, 255)
        graphics.DrawText(canvas, font, 2, 10, blue, argument[1])

        time.sleep(5)

if __name__ == "__main__":
    graphics_test = Graphing()
    if (not graphics_test.process()):
        graphics_test.print_help()
