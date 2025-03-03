# Add to program 69 to ask the user to enter a number and display 
# the country in that position.

countries = ("Togo","Ghana","Benin","Ivory Coast","Gambia")
print(countries)
choice = input("Enter one of the countries that have been shown : ")
choice = choice.capitalize()
if choice in countries:
    print(countries.index(choice))

enter = int(input("Enter a number : "))
print(countries[enter])
