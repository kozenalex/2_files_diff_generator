from gendiff.formatters import stylish, plain


def format_output(diff, format='stylish'):
    if format == 'stylish':
        return stylish.stylish(diff)
    else:
        return plain.plain(diff)
