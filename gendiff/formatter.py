from gendiff.tree import get_children, get_meta, get_name, is_node


def stylish(diff, indent):
    result = ''
    if is_node(diff):
        params = sorted(get_children(diff), key=lambda x: get_name(x))
        if get_name(diff) == 'root':
            result += '{\n'
        result += f'{" " * indent}{get_name(diff)}: ' + '{\n'
        result += '\n'.join([stylish(p, indent + 1) for p in params])        
        result += ' ' * indent + '\n}'
        return result
    else:
        meta = get_meta(diff)
        for key in meta.keys():
            if isinstance(meta[key], dict):
                result += f'{" " * indent} {key} {get_name(diff)}: {meta[key]}'
            else:
                result += f'{" " * indent} {key} {get_name(diff)}: {meta[key]}'
    return result
