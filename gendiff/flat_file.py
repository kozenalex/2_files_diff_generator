import json


def generate_diff(file1, file2):
    with open(file1) as f1:
        with open(file2) as f2:
            dict1 = json.load(f1)
            dict2 = json.load(f2)
            keys = set(list(dict1.keys()) + list(dict2.keys()))
            res = '{\n'
            for key in keys:
                if key in dict1.keys() and key in dict2.keys():
                    if dict1[key] == dict2[key]:
                        res += ' '*3 + key + ': ' + str(dict1[key]) + '\n'
                    if dict1[key] != dict2[key]:
                        res += ' - ' + key + ': ' + str(dict1[key]) + '\n'
                        res += ' + ' + key + ': ' + str(dict2[key]) + '\n'
                elif key in dict1.keys() and key not in dict2.keys():
                    res += ' - ' + key + ': ' + str(dict1[key]) + '\n'
                else:
                    res += ' + ' + key + ': ' + str(dict2[key]) + '\n'
    res += '}'
    return res