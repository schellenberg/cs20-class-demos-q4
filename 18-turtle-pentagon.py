#multiple turtle demo
import turtle
import easygui_qt as easy

#setup window
window = turtle.Screen()
window.bgcolor("lightgreen")

#figure out pensize
obii_pensize = easy.get_integer("How large should the pen be? ")

#setup turtles
obii = turtle.Turtle()
obii.shape("turtle")
obii.pensize(obii_pensize)
obii.color("pink")

david = turtle.Turtle()
david.shape("turtle")
david.color("purple")

#move david to the left side of the screen
david.penup()
david.backward(200)
david.pendown()

#draw shapes
for side_color in ["black", "white", "red", "blue", "purple"]:
    obii.color(side_color)
    obii.forward(100)
    obii.left(360/5)
    
for side in range(8):
    david.forward(75)
    david.left(360/8)
