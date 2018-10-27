"""
Дана строка words. Удалите из нее все символы, чьи индексы делятся на 3. Ответ в переменную result.
"""


words = 'ZHS WmjMNhcH DhWWpc M6t3CKm 1beChnwb zhyocP kHjZ L09FMx lQTPZIXop agiIY sN49 uTG8zFus tDHRk4xo JCYQqbFN IcY6BO7 YvZcD 8pUaa6cq J4fSH pbZdcR5KJ ExcHP'


def delete_chars_with_index_divide_by_three(string):
    list_of_chars = []
    for char in string:
        if (string.index(char) + 1) % 3 != 0 or string.index(char) == 0:
            list_of_chars.append(char)
    return str(list_of_chars)


result = delete_chars_with_index_divide_by_three(words)
print(result)
