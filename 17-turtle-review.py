import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

ethan = turtle.Turtle()
ethan.shape("turtle")

for side in range(3):
    ethan.forward(150)
    ethan.left(360/3)
