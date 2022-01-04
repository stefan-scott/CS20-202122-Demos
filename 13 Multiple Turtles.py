# Multiple Turtles Demo
# Mr. Scott
# Jan 4, 2022
# A look at lists again and multiple turtles

import turtle
window = turtle.Screen()
window.setup(500,500)

turtle_list = []  #creates an empty list


#creating our set of 8 turtles
for i in range(8):  #[0,1,2,3,4,5,6,7]
    turtle_list.append(turtle.Turtle())
    turtle_list[i].left(i * 45)
    turtle_list[i].speed(0)

def spiral(a_turtle):
    for length in range(50, 10, -3):
        a_turtle.fd(length)
        a_turtle.left(20)

def group_spiral(all_turtles):
    #all_turtles → list of turtles
    for length in range(60, 0, -2):
        for current_turtle in all_turtles:
            current_turtle.fd(length)
            current_turtle.left(20)

group_spiral(turtle_list)

# for i in range(8):
#     spiral(turtle_list[i])