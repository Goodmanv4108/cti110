#P4T1-Turtle Graphic
#Veronica Goodman
#3/23/2020
#


#Did not understand this.
#for x in range(4):
#   turtle.forward(100)
#   turtle.right(90)


from turtle import Turtle, Screen

#Variables for the turtle grapgh of the square

DELTA = 3
MINIMUM = DELTA * 2
CURSORSIZE = 20

num_squares = -1

#Asking for the number of squares.

#I could not think of a way to repeat without asking the user.

while num_squares < 1:
    try:
        num_squares = int(input('Input the number of squares: '))
    except ValueError:
        print("please enter an integer.")

    if num_squares < 1:
        print("You must have at least 1 square.")
        
#How to do the squares and what is the color, shape and size.
        
screen = Screen()
turtle = Turtle("square", visible=False)
turtle.fillcolor("white")

for size in range(((num_squares - 1) * DELTA) + MINIMUM, MINIMUM - 1, -DELTA):
  turtle.goto(turtle.xcor() + DELTA/2, turtle.ycor() - DELTA/2)
  turtle.shapesize(size / CURSORSIZE)
  turtle.stamp()
  
#An exit for the python program.
  
screen.exitonclick()
