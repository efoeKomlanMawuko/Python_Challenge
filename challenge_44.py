# Ask how many people the user wants to invite to a party. If they enter a number
# below 10, ask for the names and after each name display "[name] has been invited".
# If they enter a number which is 10 or higher, display the message "Too many people".

people_number = int(input("How many people are invited to the party : "))
if people_number < 10:
    for i in range(people_number):
        people = input("Enter people name : ")
        print(people,"has been invited")
else:
    print("Too many people")