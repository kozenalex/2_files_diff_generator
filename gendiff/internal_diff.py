def is_both_dict(a, b):
    return isinstance(a, dict) and isinstance(b, dict)


def gen_intern_diff(dict1, dict2):
    res = {}
    keys = sorted(set(
        list(dict1.keys()) + list(dict2.keys())))
    for key in keys:
        if key in dict1.keys() and key not in dict2.keys():
            res.update({
                '-' + key: dict1[key]
            })
        elif key in dict2.keys() and key in dict1.keys() and dict2[key] == dict1[key]:
            res.update({
                '=' + key: dict1[key]
            })
        elif key in dict2.keys() and key not in dict1.keys():
            res.update({
                '+' + key: dict2[key]
            })
        else:
            res.update(
                {
                    key: gen_intern_diff(dict1[key], dict2[key])
                } if is_both_dict(dict1[key], dict2[key]) else {
                    '-' + key: dict1[key],
                    '+' + key: dict2[key]
                }
            )
    return res