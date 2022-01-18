# Exericse 1 - Flipping a Coin
import random

def coin_flip():
    #return either "heads" or "tails"
    choice = random.randint(0,1) #0-heads  1-tails
    if choice == 0:
        return "heads"
    else:
        return "tails"


num_tails = 0  #accumulator BEFORE loop
for i in range(10000):  #100 flips
    if coin_flip() == "tails":
        num_tails +=1
    
print("You flipped", num_tails, "out of 100")























# # Basketball Results
# huskies_2pt = int(input("Huskies - how many fg? "))  # Ask for user input (6 things)
# huskies_3pt = int(input("Huskies - how many tres? "))  # don't forget to convert to ints
# huskies_1pt = int(input("Huskies - how many ft? "))
# 
# cougars_2pt = int(input("Cougars - how many fg? "))
# cougars_3pt = int(input("Cougars - how many tres? "))
# cougars_1pt = int(input("Cougars - how many ft? "))
# 
# # Calculate final score + determine winner
# huskies_total = huskies_2pt * 2 + huskies_3pt * 3 + huskies_1pt * 1
# cougars_total = cougars_2pt * 2 + cougars_3pt * 3 + cougars_1pt * 1
# 
# if huskies_total > cougars_total:
#     print("Huskies win!", huskies_total, "to", cougars_total)
# elif cougars_total > huskies_total:
#     print("Cougars win!", cougars_total, "to", huskies_total)
# else:
#     print("Tie!", cougars_total, "to", huskies_total)
#     
# #determine if game was high scoring or
# #low scoring
#     
# if huskies_total > 70 and cougars_total > 70:
#     print("That was a HIGH SCORING GAME.")
# else:
#     print("That was a LOW SCORING GAME.")