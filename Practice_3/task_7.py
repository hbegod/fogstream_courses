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

email = '_j8YN@Gr5U0l1.t1'

def validate(email):
    if not re.match(r"^[A-Za-z0-9\_-]+@[A-Za-z0-9]+\.[a-zA-Z0-9]{1,3}$", email):
        return False
    return True




print(validate(email))
