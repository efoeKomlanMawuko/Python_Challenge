# Display the following message :
# 1) Square
# 2) Triangle 
# Enter a number:
# If the user enter 1, then it should ask them for the length of one of its
# sides and display the area. If they select 2, it should ask for the base and
# height of the triangle and display the area. If they type in anything else, it should
# give them a suitable error message.

print("1)Square \n2)Triangle")
number = input("Enter a number : ")

if number == "1":
    length = float(input("Enter the length of one of its sides : ") )
    area = length ** 2
    print("Area : ",area)
elif number == "2":
    base = float(input("Enter the base of the triangle : "))
    height = float(input("Enter the height of the triangle : "))
    area = base * height / 2
    print("Area : ",area)
else:
    print("You have enter a bad choice")