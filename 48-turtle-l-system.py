import turtle

def apply_rules(letter):
    if letter == 'F':
        return 'FF'
    elif letter == 'X':
        return '--FXF++FXF++FXF--'
    else:
        return letter
    
def process_string(the_string):
    transformed = ''
    for letter in the_string:
        transformed = transformed + apply_rules(letter)
    return transformed

def create_l_system(number_of_iterations, axiom):
    the_string = axiom
    for counter in range(number_of_iterations):
        the_string = process_string(the_string)
    return the_string

def draw_l_system(some_turtle, instructions, angle, distance):
    for task in instructions:
        if task == 'F':
            some_turtle.forward(distance)
        elif task == '+':
            some_turtle.right(angle)
        elif task == '-':
            some_turtle.left(angle)


window = turtle.Screen()
dave = turtle.Turtle()
dave.speed(0)
window.tracer(2)

#go to bottom left
dave.penup()
dave.goto(-475, -450)
dave.pendown()

instructions = create_l_system(8, 'FXF--FF--FF')
draw_l_system(dave, instructions, 60, 2)
#print(instructions)
