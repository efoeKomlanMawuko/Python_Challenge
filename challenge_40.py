# Ask for a number below 50 and the count down from 50 to that number,
# making sure you show the number entered in the output.
number = int(input("Enter a number below 50 : "))
print("The number entered is",number)
for i in range(50-number+1):
    print(50-i)