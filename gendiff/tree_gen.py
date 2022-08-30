import gendiff.tree


def gegenerate_int_diff(name, dict1, dict2):
    children = []
    
    for key in dict1.keys():
        if key in dict2.keys():
            if dict1[key] == dict2[key]:
                children.append(gendiff.tree.make_leave(key, {' ': dict1[key]}))
            else:
                if type(dict1[key]) is dict and type(dict2[key]) is dict:
                    children.append(gegenerate_int_diff(key, dict1[key], dict2[key]))
                else:
                    children.append(gendiff.tree.make_leave(key, {
                        '-': dict1[key],
                        '+': dict2[key]
                    }))
        else:
            children.append(gendiff.tree.make_leave(key, {'-': dict1[key]}))
    for key in dict2.keys():
        if key not in dict1.keys():
            children.append(gendiff.tree.make_leave(key, {'+': dict2[key]}))
    diff_tree = gendiff.tree.make_node(name, children)
    return diff_tree
