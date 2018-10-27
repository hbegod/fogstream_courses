words = '#меняЗовутЕгорМнеМногоЛет'

def count_words_in_hashtag(string):
    if string.startswith('#'):
        countWords = 1
        for char in string:

            if char.istitle():
                countWords += 1
        return countWords
    return 0



result = count_words_in_hashtag(words)
print(words)
print(result)
