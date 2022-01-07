# A few more turtle graphic methods
# Mr. Scott
# Jan 7, 2021
# Looking at Colors, Shapes, Fills, Stamps, and Tracer

import turtle

# Basic Setup
t = turtle.Turtle()

window = turtle.Screen()
window.setup(600,600)
window.colormode(255)  #1 or 255
window.bgcolor(208, 148, 209)
window.tracer(False) #don't update the screen at all

# try out a few new things
# t.circle(5)
# t.circle(50)
# t.fd(30)
# t.dot()
# t.fd(30)
# t.dot(30)

#looking at stamp and shape "
# import random
# shapes = ["arrow", "turtle", "circle", "square",
#           "triangle", "classic"]
# t.up()
# t.goto(-300,0)
# t.shape("turtle")
# for i in range(0,80,5): #[0,5,10,15,...]
#     t.fd(i)
#     t.shape(random.choice(shapes))
#     t.stamp()

#fill in some mountains
def zigzags(r,g,b):
    t.fillcolor(r,g,b)
    t.color(r,g,b)
    t.left(45)
    t.begin_fill() 
    t.down()
    for i in range(5):  #repeat 5 - 5 peaks
        t.fd(40)
        t.right(90)
        t.fd(40)
        t.left(90)
    t.end_fill()
    t.right(45)
    t.back(200 * 2**0.5)  #sqrt(2)  

t.speed(0)
current_blue = 255
current_green = 0
for i in range(0, 360, 2):
    zigzags(0,current_green,current_blue)
    t.setheading(i)
    current_blue = current_blue - 1
    current_green = current_green + 1



