from gendiff.formatters import stylish


def format_output(diff, format='stylish'):
    if format == 'stylish':
        return stylish.stylish(diff)
    else:
        return format
