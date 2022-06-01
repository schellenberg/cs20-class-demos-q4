import turtle

def draw_rectangle(my_turtle, length, width):
    '''Draws a rectangle with my_turtle.'''
    for side in [length, width, length, width]:
        my_turtle.forward(side)
        my_turtle.left(90)

def draw_rectangle_octagon(my_turtle, short, long):
    for rectangle in range(8):
        draw_rectangle(edvin, long, short)
        edvin.left(90)
        edvin.forward(short)
        edvin.right(90)
        edvin.left(360/8)

canvas = turtle.Screen()
edvin = turtle.Turtle()

draw_rectangle_octagon(edvin, 35, 175)