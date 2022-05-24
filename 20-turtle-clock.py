import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

jackson = turtle.Turtle()
jackson.color("blue")
jackson.shape("turtle")
jackson.pensize(5)

for hour in range(12):
    #one hour
    jackson.penup()
    jackson.forward(100)
    jackson.pendown()
    jackson.forward(20)
    jackson.penup()
    jackson.forward(20)
    jackson.stamp()
    jackson.backward(140)
    
    jackson.left(360/12)
