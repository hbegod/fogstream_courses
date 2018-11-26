import itertools
import collections



message = 'BABA KLAVA'
key = '12'

data_list_iter = ('j', 's', 'f', 'y', 'd', 'q', 'o', 'k', 'f', 'i', 'f')  # `data_list_iter` содержит генератор

result = dict(zip(itertools.count(start=0, step=2), data_list_iter))
print(result, '\n')
print(b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8'))
print(b'r\x00\x00'.decode('utf-8'))

def exec_decrypt(message_symbol, key_symbol):
    return ord(message_symbol) + key_symbol


#def decrypt(message, key):


print(ord('f'))
print(ord('r'))
print(exec_decrypt('f', 12))
print(exec_decrypt('f', 12).to_bytes(length=3, byteorder='little'))
