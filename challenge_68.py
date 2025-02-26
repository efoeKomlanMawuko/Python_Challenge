# Draw a pattern that will change each time the programme is run. 
# Use the random function to pick the number of lines, the length 
# of each line and the angle of each turn
import turtle
import random

num = random.randint(3,20)
turtle.pensize(2)
turtle.color("blue") 
for i in range (0,num):
    turtle.forward(50)
    turtle.left(360/num)


turtle.exitonclick()
