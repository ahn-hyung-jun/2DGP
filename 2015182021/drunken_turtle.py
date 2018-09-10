import turtle
import random

turtle.shape('turtle')
while(True):
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(100,150))
    turtle.speed(random.randint(1,10))
    turtle.stamp()
