import image

width = 255
height = 255

win = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

r = 255
g = 0
b = 0

# your code goes here!
for x in range(width):
    for y in range(height):  #y = 0, 1, 2, ...255
        b = y
        p = image.Pixel(r, g, b)
        img.set_pixel(x,y,p)
        
    #change r,g,b values once per column
    r -= 1
    g += 1

    img.draw(win)