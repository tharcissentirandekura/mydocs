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

def events():
    if event.keysym == "Up":
        print("The movement is up")

def left_rectangles(width,height):
    
    i = 0
    positioned = []
    positions =[]
    while i <= 200:
        # picture.set_fill_color("black")
        # picture.draw_filled_rectangle(110,210 + i,10,50)
        # picture.draw_filled_rectangle(width - 230,(height - 570) + i,10,50)
        positions.append(210 + i)
        positions.append((height - 570) + i)
        i += 1
        picture.set_fill_color('white')
        picture.set_outline_color("black")
        # picture.set_pen_width(4)
        picture.draw_filled_rectangle(110,positions[-2],20,60)
        picture.draw_filled_rectangle(width - 230,positions[-1],20,60)
        position = random.choice(positions)
        ball(position,color="white")
        positioned.append(position)
        rand = random.randint(10,200)
        if position + 200 <= 500:
            position += rand
            if len(positioned) > 1:

                # picture.draw_filled_circle(positions[-1] + 100,positions[-1],15)

        # ball(position,color="black")
        # print(positioned)
                ball(positioned[-2],color="black")
        # print(positioned)
        event()
        picture.display()



def ground(width,height):
    picture.set_fill_color("black")
    
    picture.set_pen_width(3)
    picture.set_outline_color("black")
    picture.set_outline_color("white")
    picture.draw_filled_rectangle(100,200,width - 300,height - 500)
    left_rectangles(width,height)
    # ball()

    # picture.display()

def main():
    width = int(sys.argv[1])
    height = int(sys.argv[1])
    while True:
        canvas(width,height)
        ground(width,height)
if __name__ == "__main__":
    main()
    