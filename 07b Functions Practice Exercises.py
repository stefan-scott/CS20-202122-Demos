# Challenge One:
'''
Write a (lvl2) function called strange_math that requires 3 Arguments 
(assume they will be integers).

This function should multiply the first two, and then divide the result
by the third. Print the result.

It should work with the sample function calls below and print 
the correct output.

strange_math(4,5,2)  #should print out 10
strange_math(11,17,3)  #should print out 62  '''

def strange_math(num1, num2, num3):
    print(round(num1 * num2 / num3))

strange_math(11,17,3)



#Challenge Two:
'''
Write a (lvl3) function called bigger_than_ten that takes in a single 
arguement (an integer).
If the argument is larger than 10, return a Boolean value True.
If it is 10 or less, return False.

Store the result of this function
(you may pass in any argument value you like) in a variable called 
num_result.
'''

def bigger_than_ten(current_number):
    #Boolean Function - return True/False
    if current_number > 10:
        return True
    else:
        return False


user_number = int(input("Enter a number"))
if bigger_than_ten(user_number):
    print("That's bigger than 10!")


''' When complete:
    Work time for Temp Converter / Madlibs Project
    Human Resource Machine Exercises '''