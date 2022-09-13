from json import load
from yaml import safe_load


def get_format(source):
    return 'json' if source.endswith('json') else 'yaml'


def read_file(source):
    return open(source)


def parse(source, format):
    if format == 'json':
        return load(source)
    else:
        return safe_load(source)
