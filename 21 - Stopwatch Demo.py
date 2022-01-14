# Stopwatch Demo
# Mr. Scott
# Jan 14, 2022
# Using the time library to measure elapsed time

import time, microbit

#epoch -> Jan 1, 1970 0:00 UTC

timer_amount = 5
start_time = time.time()
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    #print(elapsed_time)
    if elapsed_time > timer_amount:
        #will be true every 5 seconds
        print("Five Second Mark")
        start_time = time.time()