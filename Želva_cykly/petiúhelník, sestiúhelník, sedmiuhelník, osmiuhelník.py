from turtle import *
for i in range(9):
    if i > 4:
        for l in range(i):
            forward(200/i)
            left(360/i)
        penup()
        forward(90)
        pendown()