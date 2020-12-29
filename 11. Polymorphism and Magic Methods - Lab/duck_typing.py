import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * self.radius * 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.width * self.height


def print_shape_info(shape):
    print(f"Perimeter: {shape.perimeter()}, Area: {shape.area()}")


print_shape_info(Circle(2))
print_shape_info(Rectangle(2, 4))

