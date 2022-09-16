from gendiff.consts import MARKS, NESTED, TAB_SPACE, ADDED, DELETD, UPDATED


# Функция формирует отступ для вывода, согласно
# глубине вложенности и ключу изменения параметра
def spacer(indent, mark=''):
    res_str = TAB_SPACE * indent
    pos = len(res_str) - 2
    if mark not in MARKS:
        return res_str
    else:
        return res_str[:pos] + mark + res_str[pos + 1:]


# Функция форматированного вывода словаря от глубины вложенности
def render_dict(d, deep=1):
    res = '{\n'
    for k, v in d.items():
        if isinstance(v, dict):
            res += TAB_SPACE * deep + k + ': '\
                + render_dict(v, deep + 1) + '\n'
        else:
            res += TAB_SPACE * deep + k + ': ' + str(v) + '\n'
    res += TAB_SPACE * (deep - 1) + '}'
    return res


# Функция выводит на печать свойство ключа, в зависимости от типа
def stringify_prop(prop, deep=1):
    if isinstance(prop, dict):
        return render_dict(prop, deep)
    return str(prop)


# Функция формирует строку вывода диффа в формате stylish
def stylish(diff, indent=0):
    res = '{\n'
    for key, val in diff.items():
        if val['state'] == NESTED:
            res += spacer(indent + 1)
            res += f'{key}: ' + stylish(val['prop'], indent + 1) + '\n'
        elif val['state'] == UPDATED:
            old_val, new_val = val['prop']
            res += spacer(indent + 1, DELETD)\
                + f'{key}: {stringify_prop(old_val, indent + 2)}\n'
            res += spacer(indent + 1, ADDED)\
                + f'{key}: {stringify_prop(new_val, indent + 2)}\n'
        else:
            new_val = val['prop']
            res += spacer(indent + 1, val['state'])\
                + f'{key}: {stringify_prop(new_val, indent + 2)}\n'
    res = res + spacer(indent) + '}'
    return res


def format(diff):
    return stylish(diff)
