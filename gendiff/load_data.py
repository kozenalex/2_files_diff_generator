from json import load
from yaml import safe_load


def get_data(source1, source2):
    with open(source1) as s1:
        with open(source2) as s2:
            if source1.endswith('.json'):
                data1 = load(s1)
            elif source1.endswith('.yml') or source1.endswith('.yaml'):
                data1 = safe_load(s1)
            else:
                print('usupported file format!')
                return
            if source2.endswith('.json'):
                data2 = load(s2)
            elif source2.endswith('.yml') or source2.endswith('.yaml'):
                data2 = safe_load(s2)
            else:
                print('usupported file format!')
                return
    return data1, data2
