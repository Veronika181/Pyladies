from turtle import forward, left, exitonclick, pendown, penup, right, speed
speed(15)

penup()
left(90)
forward(200)
right(90)
pendown()

for i in range(18):
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)

    left(20)

right(90)
forward(80)
for i in range(6):
    forward(30)
    left(135)
    forward(25*(1+i))
    right(180)
    forward(25*(1+i))
    left(45)

    forward(40)
    right(135)
    forward(25*(1.5+i))
    left(180)
    forward(25*(1.5+i))
    right(45)

forward(30)

exitonclick()