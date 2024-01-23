import image.picture2 as picture2

picture2.new_picture(800,800)

picture2.set_fill_color("black")
picture2.draw_filled_rectangle(0,0,800,800)

y = 50

x = 20

for x in range(200):
    for y in range(200):
        x += 2
        y += 2

        picture2.set_fill_color("red")
        picture2.draw_filled_circle(x ,y + 20,30)
        if x >120:
            picture2.rotate(120)
            picture2.set_fill_color("green")
            picture2.draw_filled_circle(x ,y + 30,30)

picture2.save_picture("moving.png")
