# напишите реализацию класса Complex
import math


class Complex:
    """
    Complex class
    input:
    real
    imag
    methods
    +, -, *, /, str()
    """
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag
                       )

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __truediv__(self, other):
        real_part = (
                        (self.real * other.real + self.imag * other.imag) /
                        (math.pow(other.real, 2) + math.pow(other.imag, 2))
                    )
        imag_part = (
                        (self.imag * other.real - self.real * other.imag) /
                        (math.pow(other.real, 2) + math.pow(other.imag, 2))
                    )
        return Complex(real_part, imag_part)

    def __str__(self):
        return '({:.2f}{:+.2f}j)'.format(self.real,self.imag)