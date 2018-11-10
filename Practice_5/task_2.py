# filename - хранит в себе имя файла
# min = ...
# max = ...

with open(filename, 'r', encoding='utf-8') as text_file:
    for line_text in text_file:
        print(line_text)
