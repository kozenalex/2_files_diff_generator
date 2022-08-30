from unittest import result
from gendiff.tree import *


def make_dif_str(diff):
    result = ''
    if is_node(diff):        
        params = sorted(get_children(diff), key=lambda x: get_name(x))
        if get_name(diff) == 'root':
            result += '{\n'
        else:
            spacer = get_deep(diff) * ' '                                
            result += f'{spacer}{get_name(diff)}: ' + '{\n'
        for param in params:
            spacer = get_deep(param) * ' '
            result += spacer + make_dif_str(param)
        result += '}\n'
    else:
        meta = get_meta(diff)
        spacer = get_deep(diff) * ' '        
        for key in meta.keys():
            result += f'{spacer}{key} {get_name(diff)}: {meta[key]}\n'
    return result