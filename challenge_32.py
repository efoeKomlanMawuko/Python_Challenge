# Ask for the radius and the depth of a cylinder and work out the total volume.
# rounded to three decimal places
import math

radius = float(input("Enter the radius of a cylinder : "))
depth = float(input("Enter the depth of a cylinder : "))
circle_area = math.pi * radius ** 2
volume = circle_area * depth
round_volume = round(volume,3)
print(round_volume)