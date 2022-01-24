# List Method Demo
# Mr. Scott
# Jan 24, 2022
# A little bit about list methods

my_list = []  #empty list

my_list.append(34)
my_list.append(17)
my_list.append(3)

my_list.pop(1)

my_list.insert(1, 18)

#last couple things: searching and sorting
try:
    print(my_list.index(18))
except:
    print(-1)

# auto-sort...probably insertion sort
my_list.sort()

