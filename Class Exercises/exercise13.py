from abc import ABC, abstractmethod

# Base class Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass # This will be overridden in the derived classes

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius # Area of circle: π * r^2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width # Area of rectangle: length * breadth

# Creating instances of Circle and Rectangle
circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)

# Calculating and displaying the area of the shapes
print(f"Area of Circle: {circle.calculate_area()} square units")
print(f"Area of Rectangle: {rectangle.calculate_area()} square units")