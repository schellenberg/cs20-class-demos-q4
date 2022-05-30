import turtle

def draw_square(my_turtle, side_length):
    '''Draws a square with the given turtle, each side
       being side_length long.'''
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)

def draw_inner_squares(the_turtle, small_side, buffer):
    '''Draws two squares, one inside the other, with the
       smaller square being small_side long, and with
       buffer space in between the two squares.'''
    draw_square(the_turtle, small_side)
    the_turtle.penup()
    the_turtle.backward(buffer)
    the_turtle.right(90)
    the_turtle.forward(buffer)
    the_turtle.left(90)
    the_turtle.pendown()
    draw_square(the_turtle, small_side + buffer*2)


window = turtle.Screen()
riley = turtle.Turtle()

draw_inner_squares(riley, 150, 30)