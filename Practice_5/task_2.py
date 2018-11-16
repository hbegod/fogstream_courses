import math

filename = 'file.txt' # filename - хранит в себе имя файла
min = 0 # min = ...
max = 0 # max = ...

with open(filename, 'r', encoding='utf-8') as text_file:
    for line_text in text_file:
        x_coordinate1, y_coordinate1, x_coordinate2, y_coordinate2 = line_text.split(' ')
        length = math.sqrt(math.pow(int(x_coordinate2) - int(x_coordinate1), 2) + math.pow(int(y_coordinate2) - int(y_coordinate1), 2))
        if length > max:
            max = length
        if min == 0:
            min = length
        elif length < min:
            min = length

print(min)
print(max)




