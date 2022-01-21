
#is a pixel part of the wattle:
# is r > 200
# is g < 80
# is b > g
import image

img = image.Image("rooster.jpg")

rooster_w = img.get_width()
rooster_h = img.get_height()

window = image.ImageWin(rooster_w, rooster_h)

#create an empty image with the same dimensions
result_image = image.EmptyImage(rooster_w, rooster_h)

#Loop through all the rooster pixels, and copy them somewhere
for x in range(rooster_w):
    for y in range(rooster_h):
        current_pixel = img.get_pixel(0+x,y)
        
        #paste that pixel into result
        if y < rooster_h/2:  #is the pixel on the top half
            result_image.set_pixel((rooster_w - 1) - x,y,current_pixel)
        else:
            result_image.set_pixel(x,y,current_pixel)





    result_image.draw(window)

