import microbit
import turtle

window = turtle.Screen()
riley = turtle.Turtle()
riley.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    if x <= -200:
        print("LEFT")
        riley.backward(3)
    elif x >= 200:
        print("RIGHT")
        riley.forward(3)
    else:
        print(x)

