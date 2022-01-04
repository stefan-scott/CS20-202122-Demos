# Turtles and Regular Polygons
# Mr. Scott
# Jan 4th, 2022
# A bit of a turtle refresher

import turtle

#Basic Turtle and Window Setup
window = turtle.Screen()
window.setup(600,400)

t = turtle.Turtle()
t.pensize(2)



#Basic Shape Functions
def triangle(side_length):
    #draw a simple triangle
    for i in range(3):  # [0,1,2]
        t.forward(side_length)
        t.left(120)
        
def square(side_length):
    #draw a simple square
    for i in range(4):
        t.forward(side_length)
        t.left(90)

def pentagon(side_length):
    #draw a pentagon
    for i in range(5):
        t.forward(side_length)
        t.left(72)

def r_poly(n, side_length):
    #Draws a regular polygon
    # n → int:number of sides for the polygon
    # side_length → int: length of each side edge
    for i in range(n):
        t.forward(side_length)
        t.left(360/n)

# triangle(50)
# square(70)
# pentagon(90)
# r_poly(8, 100)

for i in range(3,20):  #[3,4,5,6,8,9]
    r_poly(i, 30)






