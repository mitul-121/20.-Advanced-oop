from math import pi
class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width * self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2
    def perimeter(self):
        return 2 * pi * self.radius

s= Shape()
rectangle = Rectangle(20, 40)
circ = Circle(20)

print(s.area())
print(s.perimeter())

print(rectangle.area())
print(rectangle.perimeter())

print(circ.area())
print(circ.perimeter())

