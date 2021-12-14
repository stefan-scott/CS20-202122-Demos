# Data Collector
# Mr. Scott
# Dec 7, 2021
# Some practice using input and print

#Start by asking the user some questions and storing the results
name = input("What is your name? ")

#input ALWAYS gives us a string
years = input("How old are you (in years)? ")
years = int(years)

#if we need to convert between types:
# int()   float()   str()   bool()

age_in_days = years * 365.25

print("Hello, " + name + " you are " + str(age_in_days) + " old.")
#                                           "17,000"

# 5+5   "a"+"b"   "a"+5.0


