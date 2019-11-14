from abc import abstractmethod
from math import pi, sqrt


class Figure():
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        Figure.__init__(self)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2  # полупериметр
        return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))


class Rectangle(Figure):
    def __init__(self, length, width):
        Figure.__init__(self)
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width


class Circle(Figure):
    def __init__(self, radius):
        Figure.__init__(self)
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2


tri = [93.70222348950283, 50.77844960729303, 55.56273091185004]
triangle = Triangle(*tri)
print(triangle.perimeter())
# >>> 200.0434040086459
print(triangle.area())
# >>> 1176.3615190656394
