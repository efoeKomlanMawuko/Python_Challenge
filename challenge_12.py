#  Ask for two numbers. If the first one  is larger than the second, display
#  the second number first and then the first number, otherwise show the first
#  and the second.

number_1 = int(input("Enter the first number : "))
number_2 = int(input("Enter the second number : "))

if number_1 < number_2 :
    print(f"{number_1} \n{number_2}")
else:
    print(f"{number_1} \n{number_2}")

