from gendiff.consts import DELETD, ADDED, NESTED, UPDATED, EQUAL


# Функция заменяет значение ключа на строку [complex value]
def complex_val(val):
    if isinstance(val, dict):
        return '[complex value]'
    elif isinstance(val, str):
        return f'\'{val}\''
    else:
        return val


# Функция формирует информационную строку о изменении значения ключа
def gen_info_str(key, state, val):
    if state == ADDED:
        return f'{key}\' was added with value: {complex_val(val)}'
    if state == DELETD:
        return f'{key}\' was removed'
    if state == UPDATED:
        old = complex_val(val[0])
        new = complex_val(val[1])
        return f'{key}\' was updated. From {old} to {new}'


# Функция формирует строку вывода диффа в формате plain
def plain(diff, starting='Property \''):
    res = ''
    for key, val in diff.items():
        if val['state'] == EQUAL:
            continue
        if val['state'] == NESTED:
            res += plain(val['prop'], starting + key + '.')
        else:
            res += starting\
                + gen_info_str(key, val['state'], val['prop']) + '\n'
    return res


def format(diff):
    return plain(diff)
