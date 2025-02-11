# Ask for the total price of the bill, the ask how many diners there are.
# Divide the total bill by the number of diners and show how much each
# person must pay.

totalPrice = float(input("Total price of the bill : "))
personNumber = float(input("Number of diners : "))

PriceToPay = totalPrice / personNumber

print("Each person must pay :",PriceToPay)