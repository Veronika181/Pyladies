from math import sqrt
from turtle import speed
from turtle import down, forward, left, right, penup, pendown, exitonclick

for i in range (0,10):
    forward(50)
    left(135)
    speed(10)
    forward(sqrt(50*50+50*50))
    right(135)
    forward(50)
    left(-135)
    forward(sqrt(50*50+50*50))
    right(135)
    forward(50)
    right(45)
    forward(sqrt(50*50+50*50)/2)
    right(90)
    forward(sqrt(50*50+50*50)/2)
    right(45)
    forward(50)
    left(90)
    forward(25)