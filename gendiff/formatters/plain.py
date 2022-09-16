from gendiff.consts import (
    ADD_STR,
    RM_STR,
    UPDATED,
    NESTED,
    EQUAL,
    ADDED,
    DELETD,
    UPD_STR
)


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
        return f'{key}\' {ADD_STR} {complex_val(val)}'
    if state == DELETD:
        return f'{key}\' {RM_STR}'
    if state == UPDATED:
        old, new = val
        return f'{key}\' {UPD_STR} {complex_val(old)} to {complex_val(new)}'


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
