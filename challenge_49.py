# Create a variable called compnum and set the value to 50. Ask the user to
# enter a number. While their guess is not the same as the compnum value, tell
# them if their guess is too low or too high and ask them to have another guess.
# if they enter a same value as compnum, display the message "Well done, you took
# [count] attempts".
compnum = 50

number = int(input("Can you guess the number I am thinking of? "))
count = 1
while number != compnum:
    if number < compnum :
        print("Too low...")      
    else:
        print("Too high...")
    count += 1
print(f"Well done, you took {count} attempts")