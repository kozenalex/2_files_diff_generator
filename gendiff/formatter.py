from gendiff.tree import get_children, get_meta, get_name, is_node, is_leave


def spacer(mark, indent):
    marks = ('-', '+', '=')
    res_str = '    ' * indent
    pos = len(res_str) - 2
    if mark not in marks:
        return res_str
    else:
        return res_str[:pos] + mark + res_str[pos + 1:]


def stylish(diff, indent=0):
    res = '{\n'
    for key, val in diff.items():
        if not isinstance(val, dict):
            res += spacer(key[0], indent + 1) + f'{key[1:]}: {val}\n'
        else:
            res += spacer(key[0], indent) + f'{key[1:]}: ' + stylish(val, indent+1) +'\n'
    return res + '  ' * (indent+1) + '}'
   # res = json.dumps(diff, indent=2)
   # res = res.replace('"', '')
   # res = res.replace(',', '')
   # return res

