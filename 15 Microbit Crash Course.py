# Micro:bit Demo
# Jan 5th, 2022
# Mr. Scott
# Crash Course in Micro:bit programming

import microbit  #don't you dare
                 #save your file as microbit.py

import time, turtle, random

window = turtle.Screen()
window.setup(600,600)

#Global Variables
t = turtle.Turtle()

colors = ["CadetBlue", "Coral", "DarkGoldenRod", "DarkOliveGreen",
          "DarkOrange", "FireBrick", "GreenYellow", "RosyBrown"]

turtleSize = 3
t.color(random.choice(colors))
t.pensize(turtleSize)

#microbit.display.scroll("Hello there, CS20")

# for letter in ["S", "A", "S", "K"]:
#     microbit.display.show(letter)
#     time.sleep(0.5)
#     
# #for loops iterate over COLLECTIONS (lists, strings)
# 
# for letter in "ATCHEWAN":
#     microbit.display.show(letter)
#     time.sleep(0.2)


#  -1040      |       0      |       1040
#   LEFT      -300     FLAT     300       RIGHT

while True:
    x = microbit.accelerometer.get_x()
    if x > -300 and x < 300:
        direction = "FLAT"  
        microbit.display.show(microbit.Image.DIAMOND_SMALL)
    elif x <=300:
        direction = "LEFT"
        microbit.display.show(microbit.Image.ARROW_W)
    else:
        direction = "RIGHT"
        microbit.display.show(microbit.Image.ARROW_E)
    #print(direction)
        
    if microbit.button_a.was_pressed():
        #modify the current color
        t.color(random.choice(colors))
        
    if microbit.button_b.was_pressed():
        #modify the pen size
        turtleSize += 3  # turtleSize = turtleSize + 1   -=  *=  /=
        if turtleSize > 20:
            turtleSize = 3
        t.pensize(turtleSize)
    
    #Turtle Movement
    t.forward(10)
    if direction=="LEFT":
        t.left(20)
    elif direction=="RIGHT":
        t.right(20)
    






