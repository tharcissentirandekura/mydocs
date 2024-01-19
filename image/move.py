import picture

picture.new_picture(800,800)

picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,800,800)

y = 50

x = 20

for x in range(200):
    for y in range(200):
        x += 2
        y += 2

        picture.set_fill_color("red")
        picture.draw_filled_circle(x ,y + 20,30)
        if x >120:
            picture.rotate(120)
            picture.set_fill_color("green")
            picture.draw_filled_circle(x ,y + 30,30)

picture.save_picture("moving.png")
