"""
Дан список чисел numbers. Найдите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
Результат сумма индекса и элемента положите в переменную result
"""


numbers = [7, -7, -8, -7, -5, -9, 10, -10, -10, 8, -10, 1]

def get_bigest_element_and_index_sum(numbers):
    somthing = tuple(numbers)
    numbers.sort()
    bigest_number = numbers.pop(len(numbers) - 1)
    bigest_number_index = somthing.index(bigest_number)
    return bigest_number + bigest_number_index

result = get_bigest_element_and_index_sum(numbers)
print(numbers)
print(result)
