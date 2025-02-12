# Alter program 35 so that it will ask the user to enter their
# name and a number and the display their name that number of times.

name = input("Enter your name : ")
number = int(input("Enter a number : "))
for i in range(number):
    print (i, name)