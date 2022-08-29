from unittest import result
import gendiff.tree


def make_dif_str(diff):
    result = ''
    name = gendiff.tree.get_name(diff)
    if gendiff.tree.is_node(diff):        
        params = sorted(gendiff.tree.get_children(diff),
        key=lambda x: gendiff.tree.get_name(x))
        result += f' {name}: \n'
        for param in params:
            result += make_dif_str(param)
    else:
        meta = gendiff.tree.get_meta(diff)        
        for key in meta.keys():
            result += f' {key} {name}: {meta[key]}\n'
    return result