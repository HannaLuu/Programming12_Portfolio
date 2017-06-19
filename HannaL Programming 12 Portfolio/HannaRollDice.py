import random
min = 1
max = 6

roll_again = "yes"
x = 0
total_sum_rolls = x

while roll_again.lower() == "yes" or roll_again.lower() == "y":
    print ("Rolling the dice...")
    print ("The value is....")
    print (random.randint(min, max))
    total_sum_rolls = x + 1
    print ("You've rolled the dice", total_sum_rolls , "time(s)")

    roll_again = input("Roll the dice again?\n")