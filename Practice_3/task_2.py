"""
Написать функцию is_pow(x), принимающую 1 аргумент — число x от 2 до 1000, и возвращающую:
True если это число является целой степенью (с показателем больше 1) целого числа
False - если иначе.
"""
import math

def is_pow(x):
    for number in range(2,31):
        for pow_number in range(2,9):
            if math.pow(number, pow_number) == x:
                return True
    return False


for x in range(2, 1000):
    print(x)
    print(is_pow(x))
