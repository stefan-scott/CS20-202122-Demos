# Turtle Demo
# Mr. Scott
# Dec 17, 2021
# A first foray into using the Turtle library

import turtle       # looks for a file called turtle.py
                    # it will look in the lib  folder
                    # but it will look in the same folder as this program
                    # first
                    
# create and setup a window object
window = turtle.Screen()
window.bgcolor("burlyWood")


# create at least one turtle object
roscoe = turtle.Turtle()
roscoe.color("DarkOliveGreen")
roscoe.pensize(3)
roscoe.speed(0)  #full speed

# main set of instructions

def draw_square(side_length, line_color, pen_thickness):
    roscoe.color(line_color)
    roscoe.pensize(pen_thickness)
    
    for i in range(4):  #repeat 4    [0,1,2,3]
        roscoe.forward(side_length)
        roscoe.right(90)

# Create a function to draw a square, with parameters:
    # the width of the turtles pen
    # the turtle color
    # the length of the sides of the square that will be drawn

import random  #this should be at the very top
my_colors = ["Crimson", "CornflowerBlue", "Aquamarine", "DarkSlateBlue", "Grey"]

for length in range(100,300,5):   #[100,105,110,...,290,295]
    # print(length)
    draw_square(length, random.choice(my_colors), 3)
    roscoe.right(3)



# wait for screen to be clicked on, to close
window.exitonclick()