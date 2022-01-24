# Choose your own adventure demo
# Mr. Scott
# Jan 24, 2022
# A warm-up for our last assignment

import random

#Chapter One- Wake Up!
print("Welcome to the game. You are a a high school student")
clothing = input("You wake up - what will you wear? " \
                 "(dressy) (preppy) (super casual)")

#Chapter Two - Get to school!
print("You usually walk OR take the bus")
transport = input("Which do you do? (walk) (bus)")

if transport.lower() == "walk":
    #User chooses to Walk to School
    print("You walk to school, and remember a field trip")
    item = input("What do you grab from your locker? "\
                 "(5 dollar bill) (Comb) (Stick of Gum)")
else:
    #User chooses to ride the bus
    print("You miss your stop, and end up at the law offices")
    choice = input("You notice gum on the ground. Do you pick"\
                   "it up? (yes) (no)")
    if choice.upper() == "YES":
        item = "Stick of Gum"
        

