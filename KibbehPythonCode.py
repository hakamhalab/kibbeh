import turtle
import math
r=171.8

#spread the kibbeh on the tray
turtle.speed(10)
turtle.pensize(3)
turtle.color("black","chocolate4")
turtle.begin_fill()
for i in range(0,360):
    turtle.right(1)
    turtle.forward(3)
turtle.end_fill()

turtle.speed(1)

#cut in half
turtle.right(90)
turtle.forward(2*r)    

#quarters
turtle.right(90)
turtle.penup()
turtle.hideturtle()
for i in range(0,90):
    turtle.right(1)
    turtle.forward(3)

turtle.right(90)
turtle.pendown()
turtle.showturtle()
turtle.forward(2*r)

# start quarters
turtle.penup()
turtle.hideturtle()
turtle.left(90)
for i in range(0,45):
    turtle.left(1)
    turtle.forward(3)

turtle.left(90)
turtle.pendown()
turtle.showturtle()
turtle.forward(2*r)

# finish quarters
turtle.penup()
turtle.hideturtle()
turtle.right(90)
for i in range(0,90):
    turtle.right(1)
    turtle.forward(3)
turtle.right(90)
turtle.pendown()
turtle.showturtle()
turtle.forward(2*r)
turtle.right(90)

# cut up the quarters
for i in range(0,8):
    turtle.penup()
    turtle.hideturtle()
#1
    for i in range(0,15):
        turtle.right(1)
        turtle.forward(3)
#2
    turtle.pendown()
    turtle.showturtle()
    turtle.right(120)
    turtle.forward(r/3)
#3
    turtle.penup()
    turtle.hideturtle()
    turtle.left(45)
    turtle.forward(r/3)
    #4
    turtle.pendown()
    turtle.showturtle()
    turtle.left(135)
    turtle.forward(2*r/3)
    #5
    turtle.right(135)
    turtle.forward(r/3+5)
    #6
    turtle.penup()
    turtle.hideturtle()
    turtle.right(45)
    turtle.forward(45)
    #7
    turtle.pendown()
    turtle.showturtle()
    turtle.right(130)
    turtle.forward(2/3*r-5)
    #8
    turtle.penup()
    turtle.hideturtle()
    turtle.right(110)
    for i in range(0,30):
        turtle.right(1)
        turtle.forward(3)
turtle.exitonclick()

