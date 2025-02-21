# Ask the user to enter a number. Keep asking until they enter 
# a value over 5 and then display the message "The last number was a 
# [number]" and stop program.

number = 0

while number <= 5:
    number = int(input("Enter a number : "))

print("The last  number was",number)