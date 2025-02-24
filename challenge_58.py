# Make a maths quiz that asks five questions randomly two whole
# numbers to make que question (eg. [num1] + [num2]). Ask the user to 
# enter the answer. If they get it rigth add a point to their score. 
# At the end of the quiz, tell them how many they got correct out of five.
import random

score = 0
for i in range(0,5):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    answr = num1 + num2
    user_answr = int(input("Enter the answer : "))
    if answr == user_answr:
        score = score + 1
print("Your score is",score,"of 5")