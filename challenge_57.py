# Update the program 056 so that it tells the user
# if they are too high ou too low before they pick again.
import random


comp_num = random.randint(1,10)
correct = False
while correct==False:
    user_num = int(input("Pick a number between 1 and 10 : "))
    if comp_num == user_num:
        correct = True
    elif user_num < comp_num:
        print("Too low")
    else:
        print("Too high")