import turtle

window = turtle.Screen()  # Set up the window and its attributes
t = turtle.Turtle()  # Create the turtle and its attributes

t.pendown()  # Put the pen down to draw
t.forward(100)  # Move forward 100 units
t.left(90)  # Turn left 90 degrees
t.forward(100)  # Move forward 100 units
t.left(90)  # Turn left 90 degrees
t.forward(100)  # Move forward 100 units
t.left(90)  # Turn left 90 degrees
t.forward(100)  # Move forward 100 units
t.left(90)  # Turn left 90 degrees
t.penup()  # Pick up the pen to move without drawing


window.mainloop()  # Wait for user to close window
