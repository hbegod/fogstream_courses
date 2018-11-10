"""
Написать функцию avaranger(x), которая принимает 1 аргумент - любое число и
возвращается среднее арифметическое значение, на основании текущего числа и предыдущих,
которые были введены ранее.
"""
import statistics


def avaranger(x, list=[] ):
    """Возвращает среднее арефметическое"""
    list.append(x)
    return statistics.mean(list)


print(avaranger(10))
print(avaranger(20))
print(avaranger(30))
