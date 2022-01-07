# Turtle Racing Demo
# Mr. Scott
# Jan 6, 2022
# More work with the Turtle Library and Perhaps Micro:bit

import turtle, random, time, microbit

#Set up the turtle world / turtles
window = turtle.Screen()
window.setup(600,600)

racer_one = turtle.Turtle()
racer_one.color("red")

racer_two = turtle.Turtle()
racer_two.color("blue")

judge = turtle.Turtle()
judge.up()
judge.pensize(4)
judge.goto(225, 225)  #finish line is at x=225
judge.setheading(270) #point us south
judge.down()
judge.fd(450)



def determine_winner():
    if racer_one.xcor() > racer_two.xcor():
        print("Racer One Wins!")
    elif racer_two.xcor() > racer_one.xcor():
        print("Racer Two Wins!")
    else:
        print("Tie game?")


# get the turtles to their starting location
racer_one.up()
racer_one.goto(-200,100)
racer_one.down()

racer_two.up()
racer_two.setx(-200)
racer_two.sety(-100)
racer_two.down()

# #Ready to race. RACE 1 - random distance
# racer_one.fd(random.randint(20,400))
# racer_two.fd(random.randint(20,400))

# RACE 2 - random race with FOR loop
# for i in range(20):  #repeat 20
#     racer_one.fd(random.randint(10,20))
#     racer_two.fd(random.randint(10,20))

# RACE 3 - random race with WHILE loop... finish x=225
# while racer_one.xcor() < 225 and racer_two.xcor() < 225:
#     racer_one.fd(random.randint(2,8))
#     racer_two.fd(random.randint(2,8))        

# Race 4 - Computer vs Human Race (Micro:bit)
# microbit.button_a.is_pressed()  "is is the button currently down"
# microbit.button_a.was_pressed()  "has it been pressed since I last asked"

# Move forward on each button press AS LONG as the button press
# is opposite the last (A B A B A B A B)

last_pressed = ""  #no button pressed so far
player_speed = 20
microbit.button_a.was_pressed()  #returns true or false
microbit.button_b.was_pressed()  #but also resets the counter

while racer_one.xcor() < 225 and racer_two.xcor() < 225:
    racer_one.fd(random.randint(2,8))  # CPU
    #PLAYER CODE
    if microbit.button_a.was_pressed():
        if last_pressed == "B" or last_pressed == "":
            racer_two.fd(player_speed)
            last_pressed = "A"
            
    if microbit.button_b.was_pressed():
        if last_pressed == "A" or last_pressed == "":
            racer_two.fd(player_speed)
            last_pressed = "B"
        

# Race 5 - make another race where the A/B alternating buttons
# are replaced with Acceremeter positions of LEFT/RIGHT


determine_winner()
