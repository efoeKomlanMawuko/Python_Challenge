# Ask the user ton enter their first name and surname in lower case.
# Change the case to title case and join them together.
# Display the finish result.

name = input("Enter your first name in lower case: ")
surname = input("Enter your surname in lower case: ")
result = name.title() + " " + surname.title()
print(result)