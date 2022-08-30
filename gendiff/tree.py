def make_leave(name, meta = {}):
    return {
        'name': name,
        'type': 'leave',
        'meta': meta
    }


def make_node(name, children = []):
    return {
        'name': name,
        'type': 'node',
        'children': children
    }


def get_name(node):
    return node['name']


def get_meta(node):
    return node['meta']


def get_type(node):
    return node['type']


def is_leave(node):
    return get_type(node) == 'leave'


def is_node(node):
    return get_type(node) == 'node'


def get_children(node):
    if is_node(node):
        return node['children']
    else:
        return None


def get_deep(node, find_name):
    if get_name(node) == find_name:
        return 1
    if is_node(node):
        children = get_children(node)
        counts = list(map(children, lambda x: get_deep(x, find_name)))
        return 1 + sum(counts)
    else:
        return 0

    

