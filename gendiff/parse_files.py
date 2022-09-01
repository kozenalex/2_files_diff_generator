import json
import yaml


from gendiff.formatter import format_output
from gendiff.internal_diff import gen_intern_diff


def generate_diff(file1, file2, format='stylish'):
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
            internal_diff = gen_intern_diff(dict1, dict2)
    return format_output(internal_diff, format)
