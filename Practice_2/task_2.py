"""
Дана строка words. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, 
то длина первой части должна быть на один символ больше). Переставьте эти две части местами, 
результат запишите в новую строку result и выведите на экран.
"""


words = ''


def string_modification(string):
    if len(string) % 2 == 0:
        return string[int(len(string) / 2):] + string[:int(len(string) / 2)]
    else:
        return  string[int(len(string) / 2 + 1):] + string[:int(len(string) / 2 + 1)]


string = string_modification(words)
print(string)

