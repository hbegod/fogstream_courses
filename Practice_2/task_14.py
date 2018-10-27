"""
Даны два списка list_one и list_two произвольной длины каждый. Списки могут содержать как числа, так и строки.
Необходимо вывести только те элементы, которые входят как первый список, так и во второй.
Результат положите в список result
"""

list_one = [123, 'ba', 12, 'bbb', 21, 'aa', 221, 'ca', 21, 'bba', 12, 'aab', 232]
list_two = [13, 'ac', 32, 'bb', 13, 'ca', 313, 'ccb', 111, 'aa', 122]







def get_uniq_elems_from_two_lists(list_one, list_two):
    result_list = list(set(list_one) & set(list_two))

    return result_list

result = get_uniq_elems_from_two_lists(list_one, list_two)

print(result)
