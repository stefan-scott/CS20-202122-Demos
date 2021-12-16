# Functions Level 3 Demo
# Mr. Scott
# Dec 15, 2021
# An overview / practice of using functions in Python


# Functions Levels One - no inputs, no return values
def hello_class():
    print("Good morning, everyone!")


# hello_class()  #calls the function to run. No input, no return


# Functions Level Two - input(s), no return values
def sum_two(num1, num2):
    print(num1 + num2)

# n1 = 5
# n2 = 10
# sum_two(n1, n2)
# sum_two(5, 10)
# 
# sum_two(10, int(input("num: ")))


# Functions Level Three - input(s) and return value(s)

def greeting(name):
    result = "Hello there, "
    result = result + name
    return result  #Function ends here.
    print("Function Complete.") #An unreachable statement

# Ways to use a return value
# 0. Don't use them
greeting("Mr. Scott")

# 1. Print it out
print(greeting("Mr. Scott"))

# 2. Store the data somewhere (variable, list, file)
current_greeting = greeting("Mr. Scott")

# 3. Use returned value as INPUT for another function
sum_two("HEY ", greeting("Mr. Scott"))



