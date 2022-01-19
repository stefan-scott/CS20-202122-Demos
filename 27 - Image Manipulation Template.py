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
        
        
        
      
        

    img.draw(window)