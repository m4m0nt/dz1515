import math


class Figure:
    def area(self):
        return 0

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return "This is a figure"


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area()})"


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.area()})"


class RightTriangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return 0.5 * self.a * self.b

    def __str__(self):
        return f"RightTriangle(a={self.a}, b={self.b}, area={self.area()})"


class Trapezoid(Figure):
    def __init__(self, a, b, height):
        self.a = a
        self.b = b
        self.height = height

    def area(self):
        return 0.5 * (self.a + self.b) * self.height

    def __str__(self):
        return f"Trapezoid(a={self.a}, b={self.b}, height={self.height}, area={self.area()})"


rectangle = Rectangle(5, 10)
print(int(rectangle))
print(str(rectangle))

circle = Circle(7)
print(int(circle))
print(str(circle))

