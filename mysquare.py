
#!/usr/bin/env python
from samplebase import SampleBase

class SimpleSquare(SampleBase):
    red = 30
    green = 250
    blue = 200
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        r = (self.red + self.green + self.blue) // 2
        b  = (self.red + self.green + self.blue) // 2
        g = (self.red + self.green + self.blue) // 2
        offset_canvas = self.matrix.CreateFrameCanvas()

        while True:
            for x in range(1, 600):
                for k in range(500):
                    offset_canvas.SetPixel(x * 30, 10 * k * 4, r, g, b)

                self.green = (self.green + 20) % 255
                self.red = (self.red - 20) % 250
                offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()
