"""
Даны имена и средняя успеваемость учеников класса. Список students состоящий из словарей
Необходимо вывести имена одного или нескольких учеников, находящихся на предпоследнем месте по успеваемости.
Результат положите в список result
"""


students = [{'name': 'zmgi', 'grade': 1.2}, {'name': 'kafydxwyi', 'grade': 3.1},
            {'name': 'ybqukcj', 'grade': 4.3}, {'name': 'meaggmiccm', 'grade': 1.4},
            {'name': 'mxgaqihgsi', 'grade': 1.5}, {'name': 'erxxsqaoj', 'grade': 5.0},
            {'name': 'ngkit', 'grade': 1.9}, {'name': 'ytnty', 'grade': 4.7},
            {'name': 'ycboxfmvd', 'grade': 4.6}, {'name': 'kgrvynbyu', 'grade': 2.9},
            {'name': 'supkfjftty', 'grade': 4.2}, {'name': 'evsnheeomz', 'grade': 2.1},
            {'name': 'usam', 'grade': 4.7}, {'name': 'ayvqhhs', 'grade': 1.2}]

def get_bed_students_from_list(students):
    dict = {i['grade']: i for i in students}
    new_items = list(dict.values())
    sorted_students = sorted(new_items, key=lambda x: x['grade'])
    student = sorted_students[1]
    result = []
    result.append(student['name'])

    return result

result = get_bed_students_from_list(students)
print(result)
