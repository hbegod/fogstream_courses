import re

filename = 'file3.txt' # filename - хранит в себе имя файла
letters = 0
words = 0
rows = 0

with open(filename, 'r', encoding='utf-8') as text_file:
    for line_text in text_file:
        rows += 1
        letters += len(re.findall(r'[a-zA-Z]',line_text))
        splited_list = line_text.split(' ')
        for splited_part in splited_list:
            if re.match(r'[a-zA-Z0-9]', splited_part):
                words += 1

print(rows)
print(letters)
print(words)
