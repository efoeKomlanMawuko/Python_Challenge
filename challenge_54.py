# Randomly choose either heads or tails ("h" or "t"). Ask the user to make their choice.
# If their choice is the same as the randomly selected value, display the message "You win"
# otherwise display "Bad luck". At the end, tell the user if the computer selected heads or 
# tails

import random

comp_choice = random.choice(["h","t"])
print(comp_choice)

user_choice = input('Make a choice between heads or tails ("h" or "t") : ')
if user_choice == comp_choice:
    print("You win")
else:
    print("Bad luck")


print("The computer selected",comp_choice)