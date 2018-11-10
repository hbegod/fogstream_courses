"""
Реализовать функцию-валидатор почтовых адресов validate(email).
Принимает строку, которая содержит адрес электронной почты.
Возвращает True, если адрес валидный, иначе возвращает False.

Валидным адресом называется такой, который удовлетворяет следующим условиям:

Имеет формат username@websitename.extension
username может содержать только латинские буквы, целые числа, нижние подчеркивания и тире
websitename содержит только латинские буквы и целые числа
Максимальная длина extension 3 символа.
"""
import re

email = 'hbegod@gmail.com'

def validate(email):
    if not '@' in email or email.count('@') > 1 or email.split('@')[0] == '':
        return False
    if not '.' in email.split('@')[1] or email.count('.') > 1 or email.split('.')[1] == '':
        return False
    username = email.split('@')[0]
    websitename = email.split('@')[1].split('.')[0]
    extension = email.split('@')[1].split('.')[1]
    if len(extension) > 3:
        return False
    if not websitename.isalnum() :
        return False
    g = re.match(email, r'[\w\d.\-]+@[\w\d.\-.\]+')
    print(g)
    print(username)
    print(websitename)
    print(extension)
    return True


print(validate(email))
