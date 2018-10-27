words = '  Разрежьте ее на две равные части  '


# words - хранит в себе строку с словами


def count_words(string):
    words_list = string.split(' ')
    empty_word_counter = 0
    for word in words_list:
        if word == '':
            empty_word_counter += 1
    number_of_words_in_string = len(words_list) - empty_word_counter
    print(words_list)

    return number_of_words_in_string


result = count_words(words)
print(result)
