# Create a list of two sports. Ask the user what their favourite sport is 
# and add this to the end of the list. Sort the list and display it.

sports = ["Football","Rugby"]
add = input("What is your favourite sport ? : ")

sports.append(add)
sports.sort()

print(sports)

