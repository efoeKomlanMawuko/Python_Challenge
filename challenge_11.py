# Task the user to enter a number over 100 and then enter a number under 10
# and tell them how many times the smaller number goes into the larger
# number in a user-friendly format.
number_1 =int(input("Enter a number over 100 : "))
number_2 =int(input("Enter a number under 10 : "))

times = number_1 // number_2

print(f"{number_2} goes {times} times in {number_1}.")