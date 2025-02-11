# Ask the user to enter two numbers. Use whole nomber division to divide
# the first number by the second and also work out the remainder and display the
# answer in a user-friendly way (e.g. if the enter 7 and 2 display
# "7 divided by 2 is 3 with 1 remaining")

num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
answer = num1 // num2
rest = num1 % num2
print(f"{num1} divided by {num2} is {answer} with {rest} remaining.")