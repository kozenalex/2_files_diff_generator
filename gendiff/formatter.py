def spacer(indent, mark=''):
    marks = ('-', '+', ' ')
    res_str = '    ' * indent
    pos = len(res_str) - 2
    if mark not in marks:
        return res_str + mark
    else:
        return res_str[:pos] + mark + res_str[pos + 1:]


def stylish(diff, indent=0):
    res = '{\n'
    for key, val in diff.items():
        if not isinstance(val, dict):
            res += spacer(indent + 1, key[0]) + f'{key[1:]}: {val}\n'
        else:
            res += spacer(indent + 1, key[0]) + f'{key[1:]}: ' + stylish(val, indent + 1) + '\n'
    res = res + spacer(indent) + '}'
    res = res.replace('True', 'true').replace('False', 'false').replace('None', 'null')
    return res
