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

def set_to_blue():
    output_pixel = image.Pixel(141,222,242)
    return output_pixel

def avg_intensity(p):
    #return avg intensity of a pixel in range 0-255
    r = p.get_red()
    g = p.get_green()
    b = p.get_blue()
    avg = int((r+g+b)/3)
    return avg

def rgb_pixel(r, g, b):
    return image.Pixel(r,g,b)


def darken(p):
    #takes a pixel, reduce each channel by 50 and return
    r = p.get_red() - 50
    g = p.get_green() - 50
    b = p.get_blue() - 50
    
    if r < 0: r = 0
    if g < 0: g = 0  
    if b < 0: b = 0
    
    return image.Pixel(r,g,b)

def brighten(p):
    #takes a pixel, add 50 to each channel and return
    r = p.get_red() + 50
    g = p.get_green() + 50
    b = p.get_blue() + 50
    
    if r > 255: r = 255
    if g > 255: g = 255
    if b > 255: b = 255
    
    return image.Pixel(r,g,b)
#Time to edit the image:
# Effect Based on Pixel Location

for y in range(height):
    for x in range(width):
        current_pixel = img.get_pixel(x,y)
        
        #is this pixel on the left or the right half??
        if x < width/2:  #LEFT HALF
            img.set_pixel(x,y,darken(current_pixel))
        else:            #RIGHT HALF
            img.set_pixel(x,y,brighten(current_pixel))
    img.draw(window)
            








# Effect Based on Pixel Value

# for x in range(width):
#     for y in range(height):
#         # Change the pixel value IF it is the background
#         # Background is dark, so avg intensity should be low
#         current_pixel = img.get_pixel(x,y)
#         
#         if avg_intensity(current_pixel) < 85:   #if dark grey or darker
#             img.set_pixel(x, y, rgb_pixel(44, 129, 150))
#         elif avg_intensity(current_pixel) < 170:
#             img.set_pixel(x, y, rgb_pixel(189, 107, 237))
#         else:  # 170-255
#             img.set_pixel(x, y, rgb_pixel(255, 196, 243))
#              
#     img.draw(window)
    
    
    
    
    
    
    
    