import turtle

def draw_triangle(a_turtle, side_length):
    '''Draw a triangle with a_turtle, with each side being
       side_length long.'''
    for side in range(3):
        a_turtle.forward(side_length)
        a_turtle.left(360/3)

canvas = turtle.Screen()
alonso = turtle.Turtle()

for shape in range(6):
    print(draw_triangle(alonso, 150))
    alonso.left(60)
