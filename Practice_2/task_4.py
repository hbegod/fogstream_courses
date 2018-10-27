"""
Дана строка words. Замените в этой строке все цифры 1 на слово one. Ответ в переменную result.
"""


words = 'Ра1зрежьте ее на две 1 равны1е части1'


def change_number_to_word(string):
    changed_string = string.replace('1','one')
    return changed_string


result = change_number_to_word(words)
print(result)
