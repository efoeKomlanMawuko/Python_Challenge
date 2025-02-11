# Ask the user to enter the radius of a circle (measurement from the center point to
# the edge). Work out the area of the circle 
import math

radius = float(input("Enter the radius of a circle : "))
area = math.pi * radius ** 2
print(area)