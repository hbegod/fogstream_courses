import re

filename = 'file5_1.txt'    # filename - хранит в себе имя исходного файла
outfilename = 'file5_2.txt' # outfilename - хранит в себе имя файла результата

letters_dict = {}

with open(filename, 'r', encoding='utf-8') as text_file:
    for line_text in text_file:
        clean_line = re.findall(r'[a-zA-Z]', line_text)
        for letter in clean_line:
            if letters_dict.get(letter):
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1

with open(outfilename, 'w', encoding='utf-8') as out_text_file:
    for key, value in letters_dict.items():
        out_text_file.write("{0} {1}\n".format(key, value))