#A bit of starter code for bop-it

import microbit, time, random

choices = ["A", "B", "L", "R"]

target_action = random.choice(choices)

while True:
    #main loop
    microbit.display.show(target_action)
    #display the target action
    
    #check for an action:
    if microbit.button_a.was_pressed():
        #check if this was the correct action?
        if target_action == "A":
            #I got it correct
            #display an icon/animation showing it was correct
            print("Correct")
            target_action = random.choice(choices)