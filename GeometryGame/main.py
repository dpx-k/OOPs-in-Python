import turtle

def create_rectangle(length, breadth, coordinates):
    x, y = coordinates

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

    counter = 2
    while counter > 0:
        my_turtle.forward(breadth)
        my_turtle.left(90)
        my_turtle.forward(length)
        my_turtle.left(90)
        counter -= 1

def take_input():
    length = float(input("Enter the length of the Rectangle: "))
    breadth = float(input("Enter the breadth of the Rectangle: "))
    x = float(input("Enter the coordinate (x): "))
    y = float(input("Enter the coordinate (y): "))
    return length, breadth, (x, y)

my_turtle = turtle.Turtle()
length, breadth, coordinates = take_input()
create_rectangle(length, breadth, coordinates)

turtle.done()