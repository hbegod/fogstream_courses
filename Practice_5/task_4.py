import re

filename = 'file4.txt' # filename - хранит в себе имя файла
word = 'Tnjf' # word - искомое слово
result = 0

with open(filename, 'r', encoding='utf-8') as text_file:
    for line_text in text_file:
        result += len(re.findall(word,line_text))


print(result)
