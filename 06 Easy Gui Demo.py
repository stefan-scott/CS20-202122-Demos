# Easy Gui Demo
# Mr. Scott
# Dec 14, 2021

import easygui_qt as easy

# #Reading a String from the user:
# name = easy.get_string("What is your name? ", "Name Prompt")
# 
# #printing to the screen (window)
# if name == None:  #if we hit cancel previously
#     name = "Generic Person"
# easy.show_message("Hi there, " + name)
# 

# Choosing from a list:
# subjects = ["Computer Science", "Phys. Ed", "History", "Math"]
# #                  0              1            2          3
# 
# fav = easy.get_choice("Pick a class: ", "Favourite Class", subjects)

# nouns = ["chicken", "apple", "ball"]

noun1 = "apple"
verb1 = "jumped"
adjective1 = "beautiful"

# escape characters/sequences
# \n  → new line    → tab

output = f"The {noun1} {verb1} \nover the {adjective1} wall."                                                   
print(output)



