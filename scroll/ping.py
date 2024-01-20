import picture
import sys
import random


def canvas(width,height):
    picture.new_picture(width,height)
    picture.set_fill_color("black")
    picture.draw_filled_rectangle(0,0,width,height)

def ball(position,color = 'white'):
    picture.set_fill_color(color)
    picture.set_outline_color("black")
    # picture.set_position(position,position)
    picture.draw_filled_circle(position,position,15)

def write(score):
    # picture.set_fill_color("white")
    picture.set_outline_color("white")
    # picture.set_pen_width(5)
    picture.draw_text(100,100,score,font_size=26)
    picture.display()
# write("Burundi is the first country to be loser")
    
# positions = []
global positions
positions =[]
def left_rectangles(width,height):
    
    i = 0
    # positions =[]
    score = 0
    while i <= 210:
        
        positions.append(210 + i)
        positions.append((height - 570) + i)
        
        picture.set_fill_color('white')
        picture.set_outline_color("black")
        picture.draw_filled_rectangle(110,positions[-2],20,70)
        picture.draw_filled_rectangle(width - 230,positions[-1],20,70)
        picture.set_fill_color('red')
        picture.draw_filled_circle(random.choice(positions),random.choice(positions),10)
        
        print(score,(positions[-2],positions[-1]))
        print(score,210 + i, (height - 570)+ i)
        score += 1
        i += 7
        
        picture.display()
# while True:
#     

def ground(width,height):
    picture.set_fill_color("black")
    
    picture.set_pen_width(7)
    picture.set_outline_color("white")
    write(str('Ping Pong game mage with standard library picture'))
    picture.draw_filled_rectangle(100,200,width - 300,height - 500)
    
    left_rectangles(width,height)
    # ball()
    # write()

    # picture.display()

def main():
    width = int(sys.argv[1])
    height = int(sys.argv[1])
    while True:
        canvas(width,height)
        ground(width,height)
if __name__ == "__main__":
    main()
    