
def find_number_index_in_numbers(numbers, number):
    if number in numbers:
        return numbers.index(number) + 1
    else:
        for index in range(len(numbers)):
            if numbers[index] < number < numbers[index + 1]:
                return index + 1


result = find_number_index_in_numbers(numbers, number)

