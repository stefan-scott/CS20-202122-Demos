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

dice_images = [dice_one, dice_two, dice_three, dice_four, dice_five, dice_six]
microbit.display.show(microbit.Image(random.choice(dice_images)))

SHAKE_THRESHOLD = -300
while True:
    motion = microbit.accelerometer.get_z()
    print(motion)
    if motion > SHAKE_THRESHOLD:  #consider this a "shake"
        microbit.display.show(microbit.Image(random.choice(dice_images)))
        time.sleep(0.4) # no "shake detect" buffer time
    time.sleep(0.1)
    
    
    
    
    

