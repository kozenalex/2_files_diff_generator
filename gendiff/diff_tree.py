from math import inf
from gendiff.consts import NESTED, DELETD, ADDED, EQUAL, UPDATED


# Функция проверки,что оба занчения - словари
def is_both_dict(a, b):
    return isinstance(a, dict) and isinstance(b, dict)


def is_nested(node):
    return node['state'] == NESTED


def is_updated(node):
    return node['state'] == UPDATED


# Функция формирует внутренне представление диффа
def gen_intern_diff(dict1, dict2):
    res = {}
    keys = sorted(set(
        list(dict1.keys()) + list(dict2.keys())))
    for key in keys:
        if key in dict1.keys() and key not in dict2.keys():
            res.update({
                key: {
                    'state': DELETD,
                    'prop': dict1[key]
                }
            })
        elif (dict1.get(key, inf) == dict2.get(key, inf)):
            res.update({
                key: {
                    'state': EQUAL,
                    'prop': dict1[key]
                }
            })
        elif key in dict2.keys() and key not in dict1.keys():
            res.update({
                key: {
                    'state': ADDED,
                    'prop': dict2[key]
                }
            })
        else:
            res.update(
                {
                    key: {
                        'state': NESTED,
                        'prop': gen_intern_diff(dict1[key], dict2[key])
                    }
                } if is_both_dict(dict1[key], dict2[key]) else {
                    key: {
                        'state': UPDATED,
                        'prop': (dict1[key], dict2[key])
                    }
                }
            )
    return res
