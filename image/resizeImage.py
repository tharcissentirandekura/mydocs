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
                red,green,blue = picture.get_pixel(image,x,y)

                picture.set_pixel(imageCopy,x,y,(red,green,blue))

        return imageCopy


if __name__ == "__main__":
    
    image = picture.load_image("image.png")
    width = picture.image_width(image)
    height = picture.image_height(image)
    picture.new_picture(width,height)

    resize = Resize(image)
    copied = resize.copy()

    picture.draw_image(0,0,copied)
    #picture.display()
    picture.draw_on_matrix()
    
    #picture.save_picture("copy.png")
