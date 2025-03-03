# Create a tuple containing the names of five countries and display the whole tuple.
# Ask the user to enter one of the countries that have been shown to them and then
# display the index number (i.e. position in the list) of that item in the tuple.

countries = ("Togo","Ghana","Benin","Ivory Coast","Gambia")
print(countries)
choice = input("Enter one of the countries that have been shown : ")
choice = choice.capitalize()
if choice in countries:
    print(countries.index(choice))