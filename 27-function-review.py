import turtle

def add_stuff(first, second):
    '''Adds the two parameters given to the function.'''
    answer = first + second
    print(answer)    
    
def draw_triangle(a_turtle, length):
    '''Draws a triangle with each side 'length' long.'''
    for side in range(3):
        a_turtle.forward(length)
        a_turtle.left(360/3)
        

canvas = turtle.Screen()
sadique = turtle.Turtle()
jeremy = turtle.Turtle()

draw_triangle(sadique, 150)
draw_triangle(jeremy, 300)