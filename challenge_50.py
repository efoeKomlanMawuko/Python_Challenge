# Ask the user to enter a number between 10 and 20. If they enter a value under 10, 
# display the message "Too low" and ask them to try again. If they enter a value 
# above 20, display the message "Too high" and ask them to try again. Keep repeating
# this until they enter a value that is between 10 and 20 and then display the message
# "Thank you"

number = int(input("Enter a number between 10 and 20 : "))

while (number < 10 or 20 < number):
    if number < 10:
        print("Too low...")
    else :
        print("Too high...")
    number = int(input("Try again: "))
print("Thank you !")