from gendiff.consts import MARKS, TAB_SPACE


# Функция формирует отступ для вывода, согласно
# глубине вложенности и ключу изменения параметра
def spacer(indent, mark=''):
    res_str = TAB_SPACE * indent
    pos = len(res_str) - 2
    if mark not in MARKS:
        return res_str + mark
    else:
        return res_str[:pos] + mark[0] + res_str[pos + 1:]


# Функция формирует строку вывода диффа в формате stylish
def stylish(diff, indent=0):
    res = '{\n'
    for key, val in diff.items():
        if not isinstance(val, dict):
            res += spacer(indent + 1, key[:2]) + f'{key[2:]}: {val}\n'
        else:
            res += spacer(indent + 1, key[:2])
            res += f'{key[2:]}: ' + stylish(val, indent + 1) + '\n'
    res = res + spacer(indent) + '}'
    return res


def format(diff):
    return stylish(diff)
