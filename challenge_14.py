# Ask a number between 10 and 20 (inclusive). If they enter a number within this range
# display the message "Thank you"
# otherwise display the message "Incorrect answer"

number = int(input("Enter a number between 10 and 20 (inclusive) : "))
if 10 <= number <= 20:
    print("Thank you !")
else :
    print("Incorrect answer !")