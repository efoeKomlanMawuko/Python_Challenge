# Ask the user ton enter their first name and surname in lower case.
# Change the case to title case and join them together.
# Display the finish result.

name = input("Enter your first name : ")
surname = input("Enter your surname : ")
result = name.title() + " " + surname.title()
print(result)