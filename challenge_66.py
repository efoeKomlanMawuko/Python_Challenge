# Draw an octogone that uses a different colour (randomly 
# selected from a list of six possible colours) for each line.
import turtle
import random

colour = ["red","blue","green","yellow","black","pink"]
for i in range(0,8):
    turtle.pensize(3)
    chose_color = random.choice(colour)
    turtle.color(chose_color)
    turtle.forward(100)
    turtle.right(45)

turtle.exitonclick()
