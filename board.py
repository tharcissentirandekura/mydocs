from samplebase import SampleBase
import sys
import time

class MUltiSquare(SampleBase):

    def __init__(self, *args, **kwargs):
        super(MUltiSquare, self).__init__(*args, **kwargs)

    def run(self):

        self.red = 255
        self.green = 10
        self.blue = 20
        canvas = self.matrix.CreateFrameCanvas()  
        
        
        
        while True:
            for x in range(-1,self.matrix.width):
                #canvas =  self.matrix.SwapOnVSync(canvas) running one color at a time and change for each iteration
                for y in range(-1,self.matrix.height):
                    canvas.SetPixel((self.matrix.width //20) * x,(self.matrix.height // 20) * y,self.red,self.green,self.blue)
                canvas =  self.matrix.SwapOnVSync(canvas)
            time.sleep(2)
            print((self.red,self.green,self.blue))
            self.green = (self.green + 15 * x) % 255
            self.red = (self.red - 15 *y) % 255
            self.blue = (self.blue + 20 *y) % 255
            


if __name__ == "__main__":
    
    grid = MUltiSquare()
    if (not grid.process()):
        grid.print_help()
