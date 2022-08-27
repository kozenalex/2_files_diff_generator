import json


def generate_diff(file1, file2):
    with open(file1) as f1:
        with open(file2) as f2:
            dict1 = json.load(f1)
            dict2 = json.load(f2)
            res = []
            res.extend(
                [
                    f'   {key}: {dict1[key]}' for key in dict1.keys()
                    if dict1[key] == dict2.get(key, '')
                ]
            )
            res.extend(
                [
                    f' + {key}: {dict2[key]}' for key in dict2.keys()
                    if key not in dict1.keys()
                ]
            )
            res.extend(
                [
                    f' - {key}: {dict1[key]}' for key in dict1.keys()
                    if key not in dict2.keys()
                ]
            )
            res.extend(
                [
                    f' + {key}: {dict2[key]}\n - {key}: {dict1[key]}'
                    for key in dict1.keys()
                    if dict1[key] != dict2.get(key, dict1[key])
                ]
            )
            print_str = '{\n'
            for elem in res:
                print_str += elem + '\n'
    return print_str + '}'
