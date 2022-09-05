from gendiff.formatters import stylish, plain


def output_clean(str_):
    str_ = str_.replace('None', 'null')
    str_ = str_.replace('True', 'true').replace('False', 'false')
    return str_.rstrip('\n')


def format_output(diff, format='stylish'):
    if format == 'stylish':
        out_str = stylish.stylish(diff)
    else:
        out_str = plain.plain(diff)
    return output_clean(out_str)
