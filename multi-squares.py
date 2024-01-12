# !/usr/bin/env python
from samplebase import SampleBase

class MUltiSquare(SampleBase):
    red = 255
    green = 10
    blue = 200
    def __init__(self, *args, **kwargs):
        super(MUltiSquare, self).__init__(*args, **kwargs)

    def run(self):
        self.red = 255
        self.green = 10
        self.blue = 200
        offset_canvas = self.matrix.CreateFrameCanvas()

        while True:
            for x in range(0, self.matrix.width):
                for k in range(0,self.matrix.width):
                    
                    offset_canvas.SetPixel(x//2, (k//2), self.red, self.green, self.blue)
                    offset_canvas.SetPixel(x//2+ (self.matrix.width)//2,k//2,self.red, self.green,self.blue)                    
                    
                    
                    offset_canvas.SetPixel(x//2, (k//2) + (self.matrix.width)//2,self.red, self.green,self.blue)
                    offset_canvas.SetPixel(x//2 + (self.matrix.width)//2 ,(k//2)+ (self.matrix.width)//2,self.red, self.green,self.blue)
                     

                    self.red = (self.red - 20) % 250
                    self.blue = (self.blue - 20) % 250
                    self.green = (self.green + 20) % 200


                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                self.blue = (self.blue - 20) % 20
                self.green = (self.green + 20) % 20


# Main function
if __name__ == "__main__":
    simple_square = MUltiSquare()
    if (not simple_square.process()):
        simple_square.print_help()


