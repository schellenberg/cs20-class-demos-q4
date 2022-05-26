import turtle

canvas = turtle.Screen()
canvas.bgcolor("black")

ran = turtle.Turtle()
ran.color("red")
ran.shape("turtle")
ran.penup()
#speed up the animation
ran.speed(0)

#schellenberg's method
for length in range(5, 120, 2):
    ran.stamp()
    ran.forward(length)
    ran.left(25)

#ethan's method
# length = 1
# while True:
#     ran.stamp()
#     ran.forward(length)
#     ran.left(10)
#     length = length + 0.5

#ben's method
# for length in range(51):
#     length = length * 4
#     ran.forward(length)
#     ran.left(30)
#     ran.stamp()

# eszter's version
# for i in [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10]:
#     ran.forward(50)
#     ran.left(i)
#     ran.stamp()