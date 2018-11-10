import math


class Polinome:
    'Полином '

    def __init__(self, coeficents_list):
        self.coeficents_list = coeficents_list

    def __add__(self, other):
        new_numerator = self.a * (self.__find_lcm(other) // self.b) + other.a * (
                self.__find_lcm(other) // other.b)
        new_denominator = self.__find_lcm(other)


        return Fraction(new_numerator, new_denominator).__reduce_fraction()

    def __sub__(self, other):
        new_numerator = self.a * (self.__find_lcm(other) // self.b) - other.a * (
                self.__find_lcm(other) // other.b)
        new_denominator = self.__find_lcm(other)


        return Fraction(new_numerator, new_denominator).__reduce_fraction()

    def __mul__(self, other):
        new_numerator = self.a * other.a
        new_denominator = self.b * other.b

        return Fraction(new_numerator, new_denominator).__reduce_fraction()

    def calc(x):
