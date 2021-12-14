# Try-Except and Functions Demo
# Mr. Scott
# Dec 9, 2021

# ask the user "add" or "subtract", then get two numbers and provide result

def add_numbers():
# Get two values from user, and print out their sum

    while True:  #equivalent of FOREVER loop
        try:
            number1 = input("Enter a number: ")   ###what type of data???
            number1 = int(number1)  #at this point, number1 is an INT (hopefully)
            break  #exits the current loop
        except:
            print("Not a valid number, please try again...")
    
    number2 = int(input("Enter a second number: "))
    
    result = number1 + number2
    print("The sum is " + str(result))
    
    
choice = input("would you like to ADD or SUBTRACT? ")
if choice == "ADD":
    add_numbers()

