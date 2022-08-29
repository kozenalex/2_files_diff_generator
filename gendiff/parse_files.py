import json
import yaml


def generate_diff(file1, file2):
    with open(file1) as f1:
        with open(file2) as f2:
            if file1.endswith('.json'):
                dict1 = json.load(f1)
            elif file1.endswith('.yml') or file1.endswith('.yaml'):
                dict1 = yaml.safe_load(f1)
            else:
                print('usupported file format!')
                return
            if file2.endswith('.json'):
                dict2 = json.load(f2)
            elif file2.endswith('.yml') or file2.endswith('.yaml'):
                dict2 = yaml.safe_load(f2)
            else:
                print('usupported file format!')
                return
            res = []
            if dict1 is None:
                dict1 = {}
            if dict2 is None:
                dict2 = {}
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
