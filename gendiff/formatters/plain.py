def is_updated(key):
    return key[0] == '+' or key[0] == '-'


def complex_val(val):
    if isinstance(val, dict):
        return '[complex value]'
    elif isinstance(val, str):
        return f'\'{val}\''
    else:
        return val


def gen_info_str(key, val, old_val=''):
    if key[:2] == '++':
        return f'{key[2:]}\' was added with value: {complex_val(val)}'
    if key[:2] == '--':
        return f'{key[2:]}\' was removed'
    if key[:2] == '+-':
        return f'{key[2:]}\' was updated. From {old_val} to {complex_val(val)}'
    return 'conctractrin'


def plain(diff, starting='Property \''):
    res= ''
    old_value = ''
    for key, val in diff.items():
        if key[:2] in  ('  ', '-+'):
            old_value = complex_val(val)            
            continue
        if isinstance(val, dict) and not is_updated(key):
            res += plain(val, starting + key + '.')
        else:
            res += starting + gen_info_str(key, val, old_value) + '\n'
    res = res.replace('None', 'null')
    res = res.replace('True', 'true').replace('False', 'false')
    return res