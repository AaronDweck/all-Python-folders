
from turtle import *

pen1=Screen()
pen1.bgcolor("red")

pen2=Pen()
pen2.color("blue")
pen2.shape("triangle")
pen2.penup()

speed = 1

def turnleft():
    pen2.left(30)



Pen.onkey(turnleft, 'left')


while True:
    pen2.forward(speed)
