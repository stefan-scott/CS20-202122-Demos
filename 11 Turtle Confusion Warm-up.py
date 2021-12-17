# Turtle Confusion Warm-up
# Mr. Scott
# Dec 17, 2021
# A warm-up to the turtle confusion project
import turtle       # looks for a file called turtle.py
                    # it will look in the lib  folder
                    # but it will look in the same folder as this program
                    # first
                    
# create and setup a window object
window = turtle.Screen()



# create at least one turtle object
roscoe = turtle.Turtle()



#main code
def simple_rectangle():
    #draw a rectangle, starting and ending at a corner
    for i in range(2):
        roscoe.forward(100)
        roscoe.left(90)
        roscoe.forward(45)
        roscoe.left(90)

roscoe.up()  #picks up the pen
roscoe.goto(-200,0)
roscoe.down()


#Complex Shape One:
for i in range(4):   #4 things evenly space out over 360  360/4 → 90
    simple_rectangle()
    roscoe.right(90)



