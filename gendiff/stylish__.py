from gendiff.tree import get_children, get_meta, get_name, is_node
import json


def make_dif_str(diff, spacer):
    result = ''
    if is_node(diff):
        params = sorted(get_children(diff), key=lambda x: get_name(x))
        if get_name(diff) == 'root':
            result += '{\n'
        else:
            result += f'{spacer} {get_name(diff)}: ' + '{\n'
            spacer += ' '
        for param in params:
            result += spacer + make_dif_str(param, spacer)
        result += spacer + '}\n'
    else:
        meta = get_meta(diff)
        for key in meta.keys():
            if type(meta[key]) is dict:
                j_string = json.dumps(meta[key], indent=3).replace('"', '')
                result += f'{spacer} {key} {get_name(diff)}: {j_string}\n'
            else:
                result += f'{spacer} {key} {get_name(diff)}: {meta[key]}\n'
    return result
