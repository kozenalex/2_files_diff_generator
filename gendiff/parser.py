from json import loads
from yaml import safe_load
from os.path import splitext


def get_format(source):
    file_ext = splitext(source)[1]
    return file_ext.lstrip('.')


def read_file(source):
    loaded_input = ''
    for line in source:
        loaded_input += line
    return loaded_input


def parse(source, format):
    if format == 'json':
        return loads(source)
    elif format in ('yaml', 'yml'):
        return safe_load(source)
    else:
        print('Error file format')
        exit(0)
