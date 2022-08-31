from gendiff.tree import make_leave, make_node


def is_both_dict(a, b):
    return isinstance(a, dict) and isinstance(b, dict)


def generate_int_diff(name, dict1, dict2):
    children = []
    keys = sorted(set(
        list(dict1.keys()) + list(dict2.keys())))
    for key in keys:
        if key in dict1.keys() and key not in dict2.keys():
            children.append(make_leave(key, {'-': dict1[key]}))
        elif key in dict2.keys() and key in dict1.keys() and dict2[key] == dict1[key]:
            children.append(make_leave(key, {' ': dict1[key]}))
        elif key in dict2.keys() and key not in dict1.keys():
            children.append(make_leave(key, {'+': dict2[key]}))
        else:
            children.extend(
                [
                    generate_int_diff(key, dict1[key], dict2[key])
                    ] if is_both_dict(dict1[key], dict2[key])
                else [
                    make_leave(key, {'-': dict1[key]}),
                    make_leave(key, {'+': dict2[key]})
                    ]
            )    
    diff_tree = make_node(name, children)
    return diff_tree
