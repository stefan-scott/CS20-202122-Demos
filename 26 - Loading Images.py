# Loading Images
# Jan 18, 2022
# Mr. Scott
# Images Demo 2

import image

img = image.Image("sneakers.jpg")   #load image

width = img.get_width()    #extract the dimensions
height = img.get_height()

window = image.ImageWin(width, height)  #create window


#loop through all the pixels:
for x in range(width):
    for y in range(height):
        p = img.get_pixel(x,y)
        # make some change based on the pixel value
        
        new_red = p.get_red()
        new_green = p.get_green() + 50
        if new_green > 255: new_green = 255
        new_blue = p.get_blue()
        
        new_pixel = image.Pixel(new_red, new_green, new_blue)
        
        img.set_pixel(x,y, new_pixel)
        

    img.draw(window)