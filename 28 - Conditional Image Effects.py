# Conditional Image Effects
# Mr. Scott
# Jan 20, 2022
# Image effects using conditions

#sepia formula
# outputRed = (inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)
# outputGreen = (inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)
# outputBlue = (inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)

import image

img = image.Image("rooster.jpg")
width = img.get_width()
height = img.get_height()

window = image.ImageWin(width, height)
img.draw(window)


def sepiaEffect(p):
    # input: p → Pixel object
    # return a new Pixel object with Sepia Filter applied
    r = p.get_red()
    g = p.get_green()
    b = p.get_blue()
    
    new_r = (r * 0.393) + (g * 0.769) + (b * 0.189)
    new_g = (r * 0.349) + (g * 0.686) + (b * 0.168)
    new_b = (r * 0.272) + (g * 0.534) + (b * 0.131)
    
    output_pixel = image.Pixel(new_r, new_g, new_b)
    return output_pixel


#Time to edit the image:

for x in range(width):
    for y in range(height):
        current_pixel = img.get_pixel(x,y)
        img.set_pixel(x, y, sepiaEffect(current_pixel))
    img.draw(window)