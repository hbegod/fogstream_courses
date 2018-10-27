"""
Дана строка words. Если в этой строке буква f встречается только один раз, то в переменную result её индекс.
Если она встречается два и более раз, то сумму индексов её первого и последнего появления в переменную result.
Если буква f в данной строке не встречается, вывести -1 в result.
"""


words = 'Раfзfрежьте ее на две равные части'


def find_f_funcktion(string):
    if string.count('f') == 1:
        f_position_in_string = string.find('f')
        return f_position_in_string
    elif string.count('f') > 1:
        f_first_position_in_string = string.find('f')
        f_last_position_in_string = string.rfind('f')
        return f_first_position_in_string + f_last_position_in_string
    else:
        return -1


result = find_f_funcktion(words)
print(result)
