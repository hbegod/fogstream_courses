"""
Дан список результатов попыток одного спортсмена для некоторого соревнования.
Написать функцию stronger(scores), которая считает сколько раз за сессию спортсмен показал результат лучше,
чем в прошлую попытку, то есть текущее значение превышает предыдущее.
"""


scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]


def stronger(scores):
    counter = 0
    for index in range(len(scores) - 1):
        if scores[index] < scores[index + 1]:
            counter += 1
    return counter



print(stronger(scores))
