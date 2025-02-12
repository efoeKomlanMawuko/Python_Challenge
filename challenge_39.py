# Ask the user to enter a number between 1 and 12 and then display the times
# table for the number.
number = int(input("Enter a number : "))
for i in range(13):
    print(i,"*", number,"=",i*13)