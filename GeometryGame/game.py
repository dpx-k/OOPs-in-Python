import math
from random import randint
# A class for creating a point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def calculate_distance(self, lowleft, upright):
        euclidean_distance = math.sqrt(((upright[0] - lowleft[0]) ** 2) + ((upright[1] - lowleft[1]) ** 2))
        return euclidean_distance

    # another way of doing this, pass the point object itself making the code more readable
    def distance(self, point):
        distance = math.sqrt(((self.x - point.x) ** 2) + ((self.y - point.y) ** 2))
        return distance

# A class for creating a Rectangle

class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
    
    def area(self): 
        return (self.upright.x - self.lowleft.y) * (self.upright.y - self.lowleft.x)

# Instanciating a rectangle with random points
rectangle = Rectangle(Point(randint(0,9), randint(0, 9)), Point(randint(0,9), randint(0, 9)))
print("Rectangle Coordinates:", rectangle.lowleft.x, ",", rectangle.lowleft.y, 'and', rectangle.upright.x, ",", rectangle.upright.y)

# Asking user input for the points 
user_input = Point(float(input("Guess X: ")), int(input("Guess Y: ")))

if user_input.falls_in_rectangle(rectangle): 
    print("Guessed Points lie in the rectangle")
else: 
    print("Points do not lie in the Rectangle")

user_area = float(input("Guess the area of the Rectangle: "))

if user_area == rectangle.area(): 
    print("You got it right")
else: 
    print("You got it wrong")
    print(f"Your area was off by {rectangle.area() - user_area}")