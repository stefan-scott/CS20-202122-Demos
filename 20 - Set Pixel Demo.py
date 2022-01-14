# Set Pixel Example Micro:bit
# Mr. Scott
# Jan 12, 2022
# Adding the ability to control specific pixels at (x,y) on the micro:bit

import microbit, random

#list to represent the 5x5 grid on the micro:bit
grid = [ [5, 0, 0, 0, 0],
         [0, 5, 0, 0, 0],
         [0, 0, 5, 0, 0],
         [0, 0, 0, 5, 0],
         [0, 0, 0, 0, 5] ]

#Functions for our GRID
def print_grid():
    #print out the grid in an easy-to-read
    #format
    for row in grid:
        print(row)

def show_grid():
    #convert our grid 2D list into a properly
    #formatted string
    result = ""
    for row in grid:
        for pixel in row:
            result = result + str(pixel)
        result = result + ":"
    result = result[0:-1] #slice off the trailing ":"
    print(result)
    microbit.display.show(microbit.Image(result))

def set_pixel(x,y,intensity):
    #set a pixel at (x,y) to brightness: intensity (0-9)
    grid[y][x] = intensity
    show_grid()

def queue_pixel(x,y,intensity):
    #queue a change for a particular x,y pixel
    grid[y][x] = intensity

def plot(x,y):
    #turn on pixel at (x,y) to full brightness
    set_pixel(x,y,9)

def unplot(x,y):
    #turn off pixel at (x,y)
    set_pixel(x,y,0)

def random_sparkle():
    x = random.randint(0,4) # int between 0 - 4
    y = random.randint(0,4)
    intensity = random.randint(0,9)
    set_pixel(x,y,intensity)
    show_grid()

def set_all(intensity):
    #fill all pixels to level "intensity"
    for x in range(5):
        #x: 0, 1, 2, 3, 4
        for y in range(5):
            #y: 0, 1, 2, 3, 4
            queue_pixel(x,y,intensity)
    show_grid()
    
set_all(9)
# while True:
#     random_sparkle()
    
    
    
    
    