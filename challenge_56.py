# Randomly pick a whole number between 1 and 10. Ask the user to enter
# a number and keep entering numbers until they enter the number that was
# randomly picked.
import random


comp_num = random.randint(1,10)
correct = False
while correct==False:
    user_num = int(input("Pick a number between 1 and 10 : "))
    if comp_num == user_num:
        correct = True