# Set a variable call total to 0. Ask the user to enter five numbers and
# after each input ask them if they want that number included. If they do,
# then add the number to the total. If they do not want it included, don't
# add it to the total. After they have entered all five numbers, display the
# total
total = 0
for i in range(5):
    num = int(input("Enter a number : "))
    choice = input("Do you want to include this numbre ? y or n :")
    if choice == "y":
        total = total + num
    elif choice == "n":
        pass   
print("total = ",total)
