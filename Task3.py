from math import pi
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2

s= Shape()
print(s.area())
rectangle = Rectangle(20, 40)
print(rectangle.area())
circ = Circle(20)
print(circ.area())
