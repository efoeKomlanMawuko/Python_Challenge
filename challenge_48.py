# Ask for the name of somebody the user wants to invite to a party. After this
# dipslay the message "[name] has now be invited" and add 1 to the count. Then
# ask if they want to invite sombody else. Keep repeating this until the no longer
# want to invite anyone else to the party and then display how many poeple they have
# comming to the party.

count = 0
add = "y"
while add=="y":
    invite = input("Enter the name of someone you want to invite to a party : ")
    print(invite,"has now be invited")
    count += 1
    add = input("Do you want to invite someone else ? y or n : ")

print(count,"people(s) have coming to the party")