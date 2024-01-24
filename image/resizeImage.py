import image.picture2 as picture2

class Resize:

    def __init__(self,image):
        self.image = image

    def copy(self):

        width = picture2.image_width(self.image)
        height = picture2.image_height(self.image)
        

        imageCopy = picture2.blank_image(width,height)

        for x in range(width):
            for y in range(height):
                red,green,blue = picture2.get_pixel(self.image,x,y)

                picture2.set_pixel(imageCopy,x,y,(red,green,blue))
    
                red = picture2.get_red(self.image, x ,y)
                green = picture2.get_green(self.image,x,y)
                blue = picture2.get_blue(self.image,x,y)
                picture2.set_pixel(imageCopy,x,y,red,green,blue//2)

        return imageCopy


if __name__ == "__main__":
    
    image = picture2.load_image("image.png")
    resize = Resize(image)
    copied = resize.copy()
    width = picture2.image_width(image)
    height = picture2.image_height(image)

    picture2.new_picture(width,height)


    picture2.draw_image(0,0,copied)  
    picture2.save_picture("copy.png")
