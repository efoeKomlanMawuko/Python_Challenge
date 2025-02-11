# Ask the user to enter their favourite colour, if they enter "red", "RED", or "Red"
# display the message "I like red too", otherwise display the message "I don't like [color], I prefer red"

color = input("Enter your favourite colour : ")
if color == "red" or color=="RED" or color=="Red":
    print("I like red too")
else :
    print(f"I don't like {color}, I prefer red")