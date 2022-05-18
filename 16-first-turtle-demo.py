import turtle

canvas = turtle.Screen()
canvas.bgcolor("black")

jerry = turtle.Turtle()
jerry.shape("turtle")
jerry.color("green")
jerry.pensize(4)

for side in range(4):
    jerry.forward(100)
    jerry.left(90)


canvas.exitonclick()