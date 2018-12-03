import itertools
import collections



message = b"\x02pW\x1bbs\x1e)'xdA1\x16\x15e;E\x01;f~-|\x04[y\x1a\x00&\\h\x10u|X\x0fxYlH\x12[?\x1av5\x1cVt\x19&{\x01L="
key = b'y87sZRfU'


def exec_decrypt(message_symbol, key_symbol):
    result = message_symbol + key_symbol
    return result


def decrypt(message, key):
    key_hash_iter = itertools.cycle(key)
    list_new = list(zip(message, key_hash_iter))
    result_list = list()
    for element in list_new:
        symbol, key_symbol = element[0], element[1]
        symol_decr = exec_decrypt(symbol, key_symbol)
        result_list.append(symol_decr)
    return bytes(result_list)


result = decrypt(message, key)

print(result.decode(encoding='utf-8'))
