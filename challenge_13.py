# Ask the user to enter a number that is under 20.
# If they enter a number that is 20 or more, display the message "Too high",
# otherwise display "Thank you".

number = int(input("Enter a number that is under 20 : "))
if 20 <= number:
    print("Too high")
else :
    print("Thank you !")