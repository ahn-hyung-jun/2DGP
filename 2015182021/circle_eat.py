import turtle
import random

randx=0
randy=0

turtle.shape('turtle')
turtle.penup()
turtle.goto(randx=random.randint(-200,200), randy=random.randint(-200,200))
turtle.goto(random.randint(-200,200), random.randint(-200,200)-50)
turtle.pendown()
turtle.circle(50)
turtle.penup()

x=0
y=0

def move_up():
    turtle.setheading(90)
    turtle.forward(50)
    y=y+50

def move_down():
    turtle.setheading(270)
    turtle.forward(50)
    y=y-50
    
def move_right():
    turtle.setheading(0)
    turtle.forward(50)
    x=x+50
    
def move_left():
    turtle.setheading(180)
    turtle.forward(50)
    x=x-50
    
def restart():
    turtle.reset()




turtle.goto(x,y)
turtle.onkey(move_up, 'w')
turtle.onkey(move_down, 's')
turtle.onkey(move_right, 'd')
turtle.onkey(move_left, 'a')
turtle.onkey(restart, 'Escape')
turtle.listen()
