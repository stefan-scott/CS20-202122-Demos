# L-System Demo
# Mr. Scott
# Jan 17, 2022
# Some complex Turtle Graphics
import turtle
t = turtle.Turtle()
win = turtle.Screen()
win.setup(700,700)  #1200,900
t.speed(0)

t.up()
t.goto(-350,0)
t.down()

turtle.tracer(False)
#don't animate


def apply_rules(ch):
    #Apply rules to a single character
    if ch == "L":
        return "+RF-LFL-FR+"
    elif ch == "R":
        return "-LF+RFR+FL-"
    else:
        return ch

def process_string(original_str):
    #loop though original_str and apply
    #L-system rules
    next_str = ""
    for c in original_str:
        next_str += apply_rules(c)
    return next_str

def create_l_system(num_iters, axiom):
    #Run the L-system for num_iters generations
    start_string = axiom
    end_string = ""
    for i in range(num_iters):
        end_string = process_string(start_string)
        start_string = end_string
    return end_string

def draw_l_system(instructions, angle, distance):
    # Have the turtle interpret the L-system string
    # and visualize it
    for cmd in instructions:
        if cmd == "F":
            t.fd(distance)
        elif cmd == "B":
            t.bk(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)

#main driver code:
commands = create_l_system(7, "L")
print(commands)
draw_l_system(commands, 60, 2)

turtle.update()









# warm-up: Accumulator pattern

# def my_mult(a, b):  #4, 100  (400)
#     # calculate multiplication through
#     # repeated addition
#     #result = 0  #accumulator variable
#     result = 0
#     for i in range(b):
#         result += a
#     return result
        
        
        
        
        
        
        
    
    