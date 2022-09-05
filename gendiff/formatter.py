from gendiff.formatters import stylish, plain, json


# Функция "очищает" форматированный вывод, приводя к требуемому
def output_clean(str_):
    str_ = str_.replace('None', 'null')
    str_ = str_.replace('True', 'true').replace('False', 'false')
    return str_.rstrip('\n')


# Функция формирует вывод диффа, используя требуемый
# форматтер согласно переданному параметру
def format_output(diff, format='stylish'):
    if format == 'json':
        return json.json_format(diff)
    elif format == 'stylish':
        out_str = stylish.stylish(diff)
    elif format == 'plain':
        out_str = plain.plain(diff)
    return output_clean(out_str)
