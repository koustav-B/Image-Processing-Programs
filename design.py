import turtle
import colorsys

# Create a turtle screen
screen = turtle.Screen()
screen.title("Colorful Spiral Design")
screen.bgcolor("black")

# Create a turtle object
design_turtle = turtle.Turtle()
design_turtle.shape("turtle")
design_turtle.speed(10)  # Fastest drawing speed

# Function to draw a colorful spiral
def draw_spiral(turtle_obj, num_lines, max_length):
    for i in range(num_lines):
        # Change color using HSV color model
        color = colorsys.hsv_to_rgb(i / num_lines, 1.0, 1.0)
        turtle_obj.pencolor(color)
        turtle_obj.forward(i * max_length / num_lines)
        turtle_obj.right(59)  # Angle for the spiral effect

# Draw the spiral design
draw_spiral(design_turtle, 360, 300)

# Hide the turtle and finish
design_turtle.hideturtle()
turtle.done()
