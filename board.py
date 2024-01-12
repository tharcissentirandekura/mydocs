from samplebase import SampleBase
import sys

class MUltiSquare(SampleBase):

    def __init__(self, *args, **kwargs):
        super(MUltiSquare, self).__init__(*args, **kwargs)

    def run(self):

        self.red = 255
        self.green = 10
        self.blue = 200
        canvas = self.matrix.CreateFrameCanvas()  
        for x in range(-1,int(sys.argv[1])*2):
            for y in range(int(sys.argv[1])*2):
                canvas.SetPixel((self.matrix.width //int(sys.argv[1])) * x,(self.matrix.height // int(sys.argv[1])) * y,self.red,self.green,self.blue)

            self.green = (self.green + 20) % 255
            self.red = (self.red - 20) % 250
            canvas = offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


if __name__ == "__main__":
    
    grid = MUltiSquare()
    if (not grid.process()):
        grid.print_help()
