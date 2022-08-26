import math
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def SetColor(self, color):
        pass


class Point(Figure):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(self.x, self.y, self.colour)

    def SetColor(self, colour):
        self.colour = colour


class Circle(Point):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def print(self):
        print(self.x, self.y, self.radius, self.colour)

    def SetColor(self, colour):
        super().SetColor(colour)

    def CircleS(self):
        return math.pi * (self.radius ** 2)

    def SetRadius(self, radius):
        self.radius = radius


class Sphere(Circle):

    def __init__(self, x, y, radius, radius_big):
        super().__init__(x, y, radius)
        self.radius_big = radius_big

    def print(self):
        print(self.x, self.y, self.radius, self.radius_big, self.colour)

    def SetColor(self, colour):
        super().SetColor(colour)

    def CircleS(self):
        return 4 * super().CircleS()

    def SetRadius(self, radius, radius_big):
        super().SetRadius(radius)
        self.radius_big = radius_big