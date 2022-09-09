from gendiff.formatters import stylish, plain, json, finish_format


# Функция формирует вывод диффа, используя требуемый
# форматтер согласно переданному параметру
def format_output(diff, format='stylish'):
    if format == 'json':
        return json.json_format(diff)
    elif format == 'stylish':
        out_str = stylish.stylish(diff)
    elif format == 'plain':
        out_str = plain.plain(diff)
    return finish_format.output_strip_lower(out_str)
