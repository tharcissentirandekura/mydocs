import picture

red = 255
green = 50
blue = 200

def recursive(width):

    picture.set_fill_color(red,green,blue)
    # for i in range(width):
    picture.draw_filled_rectangle(width,width//2,width,width)
<<<<<<< HEAD:recursion/recursion.py
=======
    picture.draw_on_matrix()

>>>>>>> save:recursion.py

if __name__ == "__main__":  
    picture.new_picture(400,400)
    picture.set_fill_color("black")
    picture.draw_filled_rectangle(0,0,400,400)
<<<<<<< HEAD:recursion/recursion.py
picture.save_picture("recursive.png")
# picture.draw_on_matrix()
=======
#picture.save_picture("recursive.png")
#picture.draw_on_matrix()
>>>>>>> save:recursion.py
