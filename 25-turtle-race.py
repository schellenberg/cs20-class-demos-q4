#turtle race
import turtle
import random

#declare constants
STARTING_LINE = -250
FINISH_LINE = 250

#setup window
window = turtle.Screen()
window.bgcolor("lightblue")

#setup two racing turtles
jackson = turtle.Turtle()
jackson.color("black")
jackson.shape("turtle")
jackson.penup()
jackson.goto(STARTING_LINE, 50)

jeremy = turtle.Turtle()
jeremy.color("white")
jeremy.shape("turtle")
jeremy.penup()
jeremy.goto(STARTING_LINE, -50)

#draw the finish line
brandon = turtle.Turtle()
brandon.penup()
brandon.goto(FINISH_LINE, 100)
brandon.pendown()
brandon.goto(FINISH_LINE, -100)
brandon.hideturtle()

#race!
while jackson.xcor() < FINISH_LINE and jeremy.xcor() < FINISH_LINE:
    jackson_step = random.randrange(1, 10) 
    jeremy_step = random.randrange(1, 10) 
    
    jackson.forward(jackson_step)
    jeremy.forward(jeremy_step)
    

#show the winner
if jackson.xcor() > jeremy.xcor():
    jackson.write("Jackson FTW! ", False, "right", ('Arial', 50, 'normal'))

elif jackson.xcor() < jeremy.xcor():
    jeremy.write("Jeremy FTW! ", False, "right", ('Arial', 50, 'normal'))
    
else:
    jackson.write("Tie! ", False, "right", ('Arial', 50, 'normal'))
    jeremy.write("Tie! ", False, "right", ('Arial', 50, 'normal'))

