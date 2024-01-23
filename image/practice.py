# warmupgram.py
# This program applies two filters to an image (grayscale and vertflip). 
# It's currently incomplete. Start reading about what happens at the main() 
# function near the bottom of the file, then define the copy(), grayscale(), 
# and vertflip() functions below to get the program working.

import image.picture2 as picture2

def copy(image):
    """
    Returns an exact copy of the provided image.
    
    Inputs:
        image: an RGB image, loaded via the picture module
    
    Outputs:
        imagecopy: a new image that is a copy of the inputed image.
    """
    # Get the image dimensions
    width = picture2.image_width(image)
    height = picture2.image_height(image)
    # Create a blank image to hold our copied pixel values
    imagecopy = picture2.blank_image(width, height)
    
    # Copy all the pixel values from image to imagecopy
    


    # Hints: What sequence(s) do you need for looping through all the pixels 
    # in image? What pixel values will you "get" and what pixel values will 
    # you "set"?
    
    # REPLACE THIS COMMENT WITH YOUR OWN CODE
    for x in range(width):
        for y in range(height):
            red = picture2.get_red(image,x,y)
            green = picture2.get_green(image,x,y)
            blue = picture2.get_blue(image,x,y)

            picture2.set_blue(imagecopy,x,y,blue)
            picture2.set_green(imagecopy,x,y,green)
            picture2.set_red(imagecopy,x,y,red)

    
    
    return imagecopy


def grayscale(image, width, height):
    """
    Converts an image into the grayscale version of the image (i.e. no color, 
    only shades of gray).

    Inputs:
        image: an RGB image, loaded via the picture module
        width: the width of the image
        height: the height of the image

    Output:
        imagecopy: the grayscale version of the input image
    """
    # Before we apply our image filter, we'll use the copy() function to 
    # make a duplicate of the original image. The copy() function is defined
    # above, but the logic is incomplete. Take a minute now to fill in the code
    # needed to get it working.

    # Now that the copy() function is complete, we can use it to duplicate our 
    # image.
    imagecopy = copy(image)

    # Next, let's convert this entire copy to grayscale. We can do this by 
    # looping through each of the pixels. For each pixel we will set its new 
    # color values to be the average of its RGB values. The pseudocode for 
    # this step is as follows:

    # for every pixel (x,y) in the image:
    #   1. get the red, green, and blue values
    #   2. compute the average of red, green, and blue
    #   3. set the color of the pixel in imagecopy to this average
    
    # REPLACE THIS COMMENT WITH YOUR OWN CODE
    for x in range(width):
        for  y in range(height):
       
            red_new = picture2.get_red(image,x,y)
            green_new = picture2.get_green(image,x,y)
            blue_new = picture2.get_blue(image,x,y)

            comb_color = (red_new+green_new+blue_new)//3

            picture2.set_blue(imagecopy,x,y,comb_color)
            picture2.set_red(imagecopy,x,y,comb_color)
            picture2.set_green(imagecopy,x,y,comb_color)

    return imagecopy


def vertflip(image, width, height):
    """
    Converts an image into the vertically flipped version of the image.
    
    Inputs:
        image: an RGB image, loaded via the picture module
        width: the width of the image
        height: the height of the image
    
    Output:
        imagecopy: the vertically flipped version of the input image
    """

    # Again, use the copy() function you defined above to duplicate your image.
    imagecopy = copy(image)
    
    # We are now ready to vertically flip our image. The pseudocode for this 
    # step is as follows:

    # for every pixel (x,y) in imagecopy:
    #   1. get the red, green, and blue values from the original image
    #   2. use these values to set the color of the appropriate pixel in imagecopy
    
    # REPLACE THIS COMMENT WITH YOUR OWN CODE
    for x in range(width):
        for y in range(height):
            red = picture2.get_red(image,x,y)
            green = picture2.get_green(image,x,y)
            blue = picture2.get_blue(image,x,y)

            new_y_value = height - y -1

            picture2.set_blue(imagecopy,x,new_y_value,blue)
            picture2.set_green(imagecopy,x,new_y_value,green)
            picture2.set_red(imagecopy,x,new_y_value,red)


    return imagecopy


# Please don't delete this!
def main():
    """
    This is the first function to be called when warmupgram.py is executed. 
    We'll use this function to complete some basic tasks and call our two 
    image filter functions: grayscale() and vertflip().
    """

    # Let's begin by loading a JPEG image into memory using the picture module.
    # This will only load the image, we will display it later using a separate 
    # function.
    image = picture2.load_image("image.png")

    # The picture module allows us to determine the width and height of the 
    # image. We will need these dimensions so that we can loop through every 
    # pixel and perform some filtering operation. We will also use the 
    # dimensions later to draw the image on a canvas for display.
    width = picture2.image_width(image)
    height = picture2.image_height(image)

    # Here is where we'll call our filtering functions. Neither function is 
    # defined at the moment, so the image gets returned without any changes. 
    # Add code to the body of each filtering function to get them working.
    

    copied_image = copy(image)
    gray_img = grayscale(image, width, height)
    gray_flipped_img = vertflip(gray_img, width, height)
    
    # To display the final image, we must first create a canvas of the same 
    # size. We can then draw the image on this blank canvas.
    picture2.new_picture(width, height)

    picture2.draw_image(0,0,gray_img)
    
    picture2.save_picture("new_copy.png")


# The following line tells Python to execute the main() function when the 
# file is called from the command line.
if __name__ == "__main__":
    main()