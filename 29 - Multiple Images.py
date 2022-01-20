# Multiple Images
# Mr. Scott
# Jan 20, 2022
# Putting a Couple Images on the Same Canvas

import image

rooster = image.Image("rooster.jpg")
smile = image.Image("smile.png")

#get the image dimensions
rooster_w = rooster.get_width()
rooster_h = rooster.get_height()

smile_w = smile.get_width()
smile_h = smile.get_height()

window = image.ImageWin(rooster_w, rooster_h)

rooster.draw(window)

for x in range(smile_w):
    for y in range(smile_h):
        current_pixel = smile.get_pixel(x,y)
        #check if this is background or not...
        r = current_pixel.get_red()
        g = current_pixel.get_green()
        b = current_pixel.get_blue()
        
        if not(r > 250 and g > 250 and b > 250):
            #non-background pixel, so draw
            rooster.set_pixel(x+150,y+50,image.Pixel(r,g,b))
    rooster.draw(window)
            