# Функция "очищает" форматированный вывод, приводя к требуемому
def output_strip_lower(str_):
    str_ = str_.replace('None', 'null')
    str_ = str_.replace('True', 'true').replace('False', 'false')
    return str_.rstrip('\n')
