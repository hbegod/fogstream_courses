# array хранит список, func - функцию, init - начальное значение
# init может как передаваться в функцию reduce, так и не передаваться
# не удаляйте функцию reduce, напишите свою реализацию

array = [2, 3, 4]
func = lambda x,y: x + y

def reduce(array, func, init = None):
    if init is None:
        result_value = array[0]
        index = 1
        while len(array) > index:
            result_value = func(result_value, array[index])
            index += 1
        return result_value
    else:
        result_value = init
        for index in array:
            result_value = func(result_value, index)
        return result_value


print(reduce(array, func, 1))
