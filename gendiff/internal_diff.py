from math import inf
from gendiff.consts import NESTED, DELETD, ADDED, UPDATED_NEW, UPDATED_OLD


# Функция проверки,что оба занчения - словари
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
                DELETD + key: dict1[key]
            })
        elif (dict1.get(key, inf) == dict2.get(key, inf)):
            res.update({
                NESTED + key: dict1[key]
            })
        elif key in dict2.keys() and key not in dict1.keys():
            res.update({
                ADDED + key: dict2[key]
            })
        else:
            res.update(
                {
                    key: gen_intern_diff(dict1[key], dict2[key])
                } if is_both_dict(dict1[key], dict2[key]) else {
                    UPDATED_OLD + key: dict1[key],
                    UPDATED_NEW + key: dict2[key]
                }
            )
    return res
