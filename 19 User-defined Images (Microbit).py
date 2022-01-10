# Microbit User-Defined Images
# Mr. Scott
# Jan 10, 2022
# Make our own images

import microbit, time, random

dice_one = "44444:" \
           "40004:" \
           "40904:" \
           "40004:" \
           "44444" 

dice_two = "44444:" \
           "40004:" \
           "49094:" \
           "40004:" \
           "44444" 

dice_three = "44444:" \
             "49004:" \
             "40904:" \
             "40094:" \
             "44444"

dice_four = "44444:" \
            "40004:" \
            "40904:" \
            "40004:" \
            "44444"

dice_five = "44444:" \
            "49094:" \
            "40904:" \
            "49094:" \
            "44444"

dice_six = "44444:" \
           "49094:" \
           "49094:" \
           "49094:" \
           "44444" 


current_image = microbit.Image(dice_one)
microbit.display.show(current_image)




microbit.display.show(BANANA)