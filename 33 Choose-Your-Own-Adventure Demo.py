# Choose your own adventure demo
# Mr. Scott
# Jan 24, 2022
# A warm-up for our last assignment

import random


def game():    #Chapter One- Wake Up!
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
                       " it up? (yes) (no)")
        if choice.upper() == "YES":
            item = "Stick of Gum"
            
    #Chapter Three: Which way to go? (at law offices)
    print("You are in a hallway. You can go left or right.")
    direction = input("which way do you go? (left) (right)")

    #enforce valid input
    while direction.lower() != "right" and direction.lower() != "left":
        direction = input("which way do you go? (left) (right)")
        

    if direction.lower() == "right":
        print("You find your school group. THE END")
    else:
        #choosing to go left.
        print("You see a door open just a crack, with the light on")
        enter = input("Do you go in? (yes) (no)")
        if enter.upper() == "NO":
            print("you turn around and find your friends. THE END")
        else:
            #rest of the story must be in this branch
            #endgame 3 - job interview
            print("You are in a job interview with 1 min to prepare")
            use_item = input("Do you use your item (yes) (no)")
            chance = 45
            
            #modify based on clothing selection
            if clothing.lower() == "dressy" or clothing.lower() == "preppy":
                chance += 25
            elif clothing.lower() == "super casual":
                chance -= 30
            
            #modify based on item usage
            if use_item.lower() == "yes":
                if item.lower() == "stick of gum":
                    chance += 10
                elif item.lower() == "comb":
                    chance += 20
                elif item.lower() == "5 dollar bill":
                    chance -= 100  # chance = chance - 100
            
            #how do we figure out the conditional probabilty
            #find out the result
            random_number = random.randint(0,100)
            if chance < 0:
                print("You bomb and embarass yourself. THE END")
            else:
                if random_number < chance:
                    print("Fake it till you make it. You get the JOB!")
                else:
                    print("Interview went well, but you didnt' get it. END")
                    




