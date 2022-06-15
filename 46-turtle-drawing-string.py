import turtle

window = turtle.Screen()
dave = turtle.Turtle()

instructions = 'F++F++F++F'
for task in instructions:
    if task == 'F':
        dave.forward(100)
    elif task == '+':
        dave.right(45)
    elif task == '-':
        dave.left(45)