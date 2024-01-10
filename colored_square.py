# !/usr/bin/env python
from samplebase import SampleBase

class SimpleSquare(SampleBase):
    red = 255
    green = 10
    blue = 200
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        self.red = 255
        self.green = 10
        self.blue = 200
        offset_canvas = self.matrix.CreateFrameCanvas()

        

        while True:
            offset_canvas.SetPixel(self.matrix.width,self.matrix.height,0,0,0)
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
            for x in range(0, self.matrix.width):
                for k in range(0,self.matrix.width):
                    print(k,x)
                    
                    offset_canvas.SetPixel(x//2, k//2, self.red, self.green, self.blue)
                    offset_canvas.SetPixel(x//2+ (self.matrix.width)//2,k//2,self.red, self.green,self.blue)                    
                    
                    
                    offset_canvas.SetPixel(x//2, (k//2) + (self.matrix.width)//2,self.red, self.green,self.blue)
                    offset_canvas.SetPixel(x//2 + (self.matrix.width)//2 ,(k//2)+ (self.matrix.width)//2,self.red, self.green,self.blue)
                     

                    self.red = (self.red - 20) % 250
                    self.blue = (self.blue - 20) % 250
                    self.green = (self.green + 20) % 200


                    #offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                self.blue = (self.blue - 20) % 20
                self.green = (self.green + 20) % 20


# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()


