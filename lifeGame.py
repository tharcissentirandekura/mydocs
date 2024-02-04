from picture import *
import picture
import time
import random
import sys

class Grid:

    def __init__(self,cols,rows,size):
        self.cols = cols
        self.rows = rows
        self.size = size
        self.positions = []
        self.gridPos = []

        random.shuffle(self.positions)
    
    def setup(self):
        new_picture(self.rows,self.cols)
        

    def background(self,color):
        set_fill_color(color)
        set_outline_color("white")
        draw_filled_rectangle(0,0,self.rows,self.cols)
    
    def drawGrid(self):


        for row in range(self.rows//self.size):
            for cols in range(self.cols//self.size):
                # set_outline_color("white")
                draw_square(self.rows// 16 + (row * self.size),self.cols//16 + (cols * self.size),self.size)
                self.positions.append([self.rows//16 + (row * self.size),self.cols//16 + (cols * self.size)])
        return grid.positions

    def matrix(self):
        for i in range(self.rows//self.size):
            for j in range(self.cols//self.size):
                self.gridPos.append(random.randrange(2))
        return grid.gridPos

    def dead(self,position,color):
        set_fill_color(color)
        set_outline_color("black")
        draw_filled_square(random.choice(position)[0],random.choice(position)[1],self.size)

    def alive(self,position,color):
        set_fill_color(color)
        set_outline_color("black")
        draw_filled_square(random.choice(position)[0],random.choice(position)[1],self.size)

    def output(self,matrix,position,color):
        grid.setup()
        grid.background('black')

        grid.drawGrid()

        for i in range(len(matrix)):
            if matrix[i] == 3:
                grid.dead(position,color)
   
            elif matrix[i] == 1:
                grid.alive(position,color)
        return matrix

             
grid = Grid(128,128,int(sys.argv[1]))
grid2 = Grid(128,128,int(sys.argv[1])) 

matrix = grid.matrix()
position = grid.positions
color = 'white'

for i in range(100):
    
    if i > 0 and i % 10 == 0:
        grid.output(matrix,position,color)
    else:
        grid2.output(matrix,position,color)

    picture.draw_on_matrix()
    time.sleep(1)

