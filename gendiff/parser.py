from json import loads
from yaml import safe_load
from os.path import splitext


def get_format(source):
    file_ext = splitext(source)[1]
    return file_ext.lstrip('.')


def read_file(source):
    return source.readlines()


def parse(source, format):
    if format == 'json':
        return loads(''.join(source))
    elif format in ('yaml', 'yml'):
        return safe_load(''.join(source))
    else:
        print('Error file format')
        exit(0)
