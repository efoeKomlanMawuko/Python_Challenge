# Change program 37 to also ask for a number. Display their name
# (one letter at a time on each line) and repeat this for the number
# of times they entered.
name = input("Enter your name : ")
number = int(input("Enter a number : "))
for i in range(number):
    for letter in name:
        print(letter)

