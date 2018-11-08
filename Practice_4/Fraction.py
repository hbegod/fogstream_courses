import math


class Fraction:
    'Класс Дробь'

    def __init__(self, numerator, denominator):
        k = math.gcd(numerator,denominator)
        if isinstance(numerator, int):
            self.a = numerator // k
        else:
            raise ValueError('Type of numerator mast be int')
        if isinstance(denominator, int):
            self.b = denominator // k
        else:
            raise ValueError('Type of denominator mast be int')

    def __reduce_fraction(self):
        k = math.gcd(self.a, self.b)
        return Fraction(self.a // k, self.b // k)

    def __find_lcm(self, other):
        return self.b * other.b // math.gcd(self.b, other.b)


    def __add__(self, other):
        new_numerator = self.a * (self.__find_lcm(other) // self.b) + other.a * (
                self.__find_lcm(other) // other.b)
        new_denominator = self.__find_lcm(other)
        print('add')

        return Fraction(new_numerator, new_denominator).__reduce_fraction()

    def __sub__(self, other):
        new_numerator = self.a * (self.__find_lcm(other) // self.b) - other.a * (
                self.__find_lcm(other) // other.b)
        new_denominator = self.__find_lcm(other)
        print('sub')

        return Fraction(new_numerator, new_denominator).__reduce_fraction()

    def __mul__(self, other):
        new_numerator = self.a * other.a
        new_denominator = self.b * other.b
        print('mul')
        return Fraction(new_numerator, new_denominator).__reduce_fraction()

    def __lt__(self, other):
        if self.a / self.b < other.a / other.b:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.a / self.b > other.a / other.b:
            return True
        else:
            return False

    def __eq__(self, other):
        new_numerator_self = self.a * (self.__find_lcm(other) // self.b)
        new_numerator_other = other.a * (self.__find_lcm(other) // other.b)
        if new_numerator_self == new_numerator_other:
            return True
        else:
            return False

    def __ne__(self, other):
        c = not(self == other)
        return c

    def __le__(self, other):
        if self == other or self < other:
            return True
        else:
            return False

    def __ge__(self, other):
        if self == other or self > other:
            return True
        else:
            return False