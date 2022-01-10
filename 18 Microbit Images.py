# Built-In Images on the Microbit
# Mr. Scott
# Jan 10, 2022
# Working with some built-in Images

import microbit, time  #cs20-microbitio

clock_images = [microbit.Image.CLOCK1,
                microbit.Image.CLOCK2,
                microbit.Image.CLOCK3,
                microbit.Image.CLOCK4,
                microbit.Image.CLOCK5,
                microbit.Image.CLOCK6,
                microbit.Image.CLOCK7,
                microbit.Image.CLOCK8,
                microbit.Image.CLOCK9,
                microbit.Image.CLOCK10,
                microbit.Image.CLOCK11,
                microbit.Image.CLOCK12]

current_index = 0   #store which clock image to draw next (pos in list)
delay_amount = 0.1

while True:
    microbit.display.show(clock_images[current_index])
    current_index += 1   #current_index = current_index + 1
    #0 1 2 3 4 5 6 7 8 9 10 11 nononono
    if current_index > 11:
        current_index = 0
    
    x_rotation = microbit.accelerometer.get_x()
    print(x_rotation)
    
    if x_rotation < -500:
        delay_amount = 0.01
    elif x_rotation >= -500 and x_rotation < 0:
        delay_amount = 0.05
    elif x_rotation < 500:
        delay_amount = 0.1
    else:
        delay_amount = 0.3
    
    time.sleep(delay_amount)
