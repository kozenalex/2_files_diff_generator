from math import inf


# Функция проверки,что оа занчения - словари
def is_both_dict(a, b):
    return isinstance(a, dict) and isinstance(b, dict)


# Функция формирует внутренне представление диффа
def gen_intern_diff(dict1, dict2):
    res = {}
    keys = sorted(set(
        list(dict1.keys()) + list(dict2.keys())))
    for key in keys:
        if key in dict1.keys() and key not in dict2.keys():
            res.update({
                '--' + key: dict1[key]
            })
        elif (dict1.get(key, inf) == dict2.get(key, inf)):
            res.update({
                '  ' + key: dict1[key]
            })
        elif key in dict2.keys() and key not in dict1.keys():
            res.update({
                '++' + key: dict2[key]
            })
        else:
            res.update(
                {
                    key: gen_intern_diff(dict1[key], dict2[key])
                } if is_both_dict(dict1[key], dict2[key]) else {
                    '-+' + key: dict1[key],
                    '+-' + key: dict2[key]
                }
            )
    return res
