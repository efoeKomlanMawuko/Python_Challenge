# Randomly choose a number between 1 and 5. Aks the user to pick
# a number. If they guess correctly, display the message "Well done",
# otherwise tell them if they are too high or too low and ask to pick
# a second number. If they guess correctly on their second guess, display
# "Correct", otherwise display "You lose".

import random

times = 2

num = random.randint(1,5)
user_num = 0

user_num = int(input("Pick a number between 1 and 5 : "))
if user_num == num:
    print("Well done")
else:
    if user_num < num:
        print("Too low")
        times = times - 1
    else:
        print("Too high")
        times = times - 1
    user_num2 = input("Pick a second number : ")
    if user_num2== num:
        print("Correct")
    else:
        print("You lose")