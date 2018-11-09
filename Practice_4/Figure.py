# напишите реализацию классов Figure, Triangle, Rectangle, Circle
import math


class Figure:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__width = width
        self.__length = length

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius
        self.pi = 3.14159265359

    def area(self):
        return self.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * self.pi * self.__radius


class Triangle(Figure):
    def __init__(self, first_line, second_line, third_line):
        self.__first_line = first_line
        self.__second_line = second_line
        self.__third_line = third_line

    def area(self):
        return math.sqrt(self.half_perimeter() *
                         (self.half_perimeter() - self.__first_line) *
                         (self.half_perimeter() - self.__second_line) *
                         (self.half_perimeter() - self.__third_line)
                         )

    def perimeter(self):
        return self.__first_line + self.__second_line + self.__third_line

    def half_perimeter(self):
        return self.perimeter() / 2