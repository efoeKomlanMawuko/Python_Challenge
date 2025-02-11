# Ask the user to enter three numbers. Add together the first two numbers and the 
# multiply this total by the third.
# Display the answer as :
# The answer is [answer]

nombre_1 = float(input("Entrer le nombre_1 : "))
nombre_2 = float(input("Entrer le nombre_2 : "))
nombre_3 = float(input("Entrer le nombre_3 : "))

resultat = (nombre_1 + nombre_2) * nombre_3
print("La réponse est",resultat)