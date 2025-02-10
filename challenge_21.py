# Ask the user to enter their name and ask them to enter their
# surname. Join them together with a space between and display the name
# and the length of whole name

name = input("Enter your name : ")
surname = input("Enter your surname : ")

full = name + " " + surname
length = len(full)
print(full)
print(length) 
