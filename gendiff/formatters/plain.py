# Функция проверки на удаленный или добавленный ключ
def is_updated(key):
    return key[0] == '+' or key[0] == '-'


# Функция заменяет значение ключа на строку [complex value]
def complex_val(val):
    if isinstance(val, dict):
        return '[complex value]'
    elif isinstance(val, str):
        return f'\'{val}\''
    else:
        return val


# Функция формирует информационную строку о изменении значения ключа
def gen_info_str(key, val, old_val=''):
    if key[:2] == '++':
        return f'{key[2:]}\' was added with value: {complex_val(val)}'
    if key[:2] == '--':
        return f'{key[2:]}\' was removed'
    if key[:2] == '+-':
        return f'{key[2:]}\' was updated. From {old_val} to {complex_val(val)}'
    return 'conctractrin'


# Функция формирует строку вывода диффа в формате plain
def plain(diff, starting='Property \''):
    res = ''
    old_value = ''
    for key, val in diff.items():
        if key[:2] in ('  ', '-+'):
            old_value = complex_val(val)
            continue
        if isinstance(val, dict) and not is_updated(key):
            res += plain(val, starting + key + '.')
        else:
            res += starting + gen_info_str(key, val, old_value) + '\n'
    return res
