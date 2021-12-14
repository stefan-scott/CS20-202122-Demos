# Python Day Two Warmups
# Mr. Scott
# Dec 8th, 2021
# Rectangular Area and Alarm Clock


# Exercise Two: Alarm Clock

def alarm_problem():
    start_time = 14  #24h clock
    alarm_length = 17 #time to wait
    
    end_time = start_time + alarm_length
    while end_time > 23:
        end_time = end_time - 24    #end_time -= 24   += *=  /=
    if end_time > 12:
        end_time -= 12
        print("time is: " + str(end_time) + "PM")
    else:
        print("time is",end_time,"AM")        


alarm_problem()



# # Ask the user for a width, and height. Calculate the rect area
# # report back to the user.
# 
# width = input("Enter a width: ")
# #input() ALWAYS returns a string
# 
# #conversion methods:  int()  float()  bool()  str()
# width = float(width)
# 
# height = float(input("Enter a height: "))
# 
# # Calculate the result:
# area = width * height    #  + - * /
# 
# # Report our final value:
#                        # "200"
# print("The area is " + str(area) + " units squared")
# print("The area is",area,"units squared")
