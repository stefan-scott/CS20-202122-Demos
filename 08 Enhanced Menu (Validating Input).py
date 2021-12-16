# Improved Menu System Demo
# Mr. Scott
# Dec 16, 2021
# Look at while loops and validating input

# Scenario: Ask the user what they would like to do
# Options:  add  subtract  ... eventually mult and divide

def add():
    print("TIME TO ADD")

def subtract():
    print("TIME TO SUBTRACT")

def multiply():
    print("TIME TO MULTIPLY")

def divide():
    print("TIME TO DIVIDE")


# START MAIN CODE HERE

def input_is_valid(choice):
    #compare choice with the contents of valid_options, and return
    #True or False
    valid_options = ["add", "subtract", "divide", "multiply"] 
    if choice in valid_options:
        return True
    else:
        return False

while True:
    user_choice = input("would you like to add or subtract? ")
    if input_is_valid(user_choice):
        break
    else:
        print("Not a valid choice. Please try again.")

#validate input...did they enter something that was expected?
#if not, ask them again.

# while user_choice != "add" and user_choice != "subtract":
#     user_choice = input("would you like to add or subtract? ")




# is user_choice located inside the list?
if user_choice == "add":
    add()
elif user_choice == "subtract":
    subtract()

