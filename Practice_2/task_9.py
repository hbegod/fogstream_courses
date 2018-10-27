"""
Дан список чисел numbers. Если в нем есть два соседних элемента одного знака, найдите эти числа. Если соседних
элементов одного знака нет — выведите 0. Если таких пар соседей несколько — найдите первую пару.
Результат сумма пары положите в переменную result
"""

numbers = [7, -7, -8, -7, -5, -9, 10, -10, -10, 8, -10, 1]

def find_near_elements_with_same_sign(numbers):
    i = 0
    length = len(numbers)
    while i < length - 1:
        if numbers[i] > 0 and numbers[i + 1] > 0 or numbers[i] < 0 and numbers[i + 1] < 0:
            return numbers[i] + numbers[i + 1]
        i += 1
    return 0

result = find_near_elements_with_same_sign(numbers)
print(numbers)
print(result)
