# filename - хранит в себе имя файла
lect = 0
pract = 0
lab = 0
with open(filename, 'r', encoding='utf-8') as text_file:
    for line_text in text_file:
        if line_text.find("практ.") != -1:
            pract += 1
        if line_text.find('лекц.') != -1:
            lect += 1
        if line_text.find('лаб.') != -1:
            lab += 1


