# Images Demo - Day 1
# Mr. Scott
# Jan 18, 2022
# First look at using image library

import image   #DO NOT save your file as image.py

width = 400
height = 300

window = image.ImageWin(width, height) #creates a window
img = image.EmptyImage(width, height) #this is an Image object


for x in range(width):
    for y in range(height):
        if x%2==0:
            this_pixel = image.Pixel(124,212,217)
            img.set_pixel(x,y,this_pixel)
        else:
            this_pixel = image.Pixel(0,0,0)
            img.set_pixel(x,y,this_pixel)


img.draw(window)







# p = image.Pixel(20, 60, 100)
# 
# print(p.get_red())
# print(p.get_green())
# 
# p.set_blue(255)
# print(p.get_blue())