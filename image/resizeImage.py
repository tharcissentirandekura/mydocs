import picture

class Resize:

    def __init__(self,image):
        self.image = image

    def copy(self):

        width = picture.image_width(self.image)
        height = picture.image_height(self.image)
        

        imageCopy = picture.blank_image(width,height)

        for x in range(width):
            for y in range(height):
                red,green,blue = picture.get_pixel(self.image,x,y)

                picture.set_pixel(imageCopy,x,y,(red,green,blue))
    
                red = picture.get_red(self.image, x ,y)
                green = picture.get_green(self.image,x,y)
                blue = picture.get_blue(self.image,x,y)
                picture.set_pixel(imageCopy,x,y,red,green,blue//2)

        return imageCopy


if __name__ == "__main__":
    
    image = picture.load_image("image.png")
    resize = Resize(image)
    copied = resize.copy()
    width = picture.image_width(image)
    height = picture.image_height(image)

    picture.new_picture(width,height)



    picture.draw_image(0,0,copied)  
    #picture.save_picture("copy.png")
    picture.display()
