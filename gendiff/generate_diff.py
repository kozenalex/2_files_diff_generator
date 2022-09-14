from gendiff.formatter import format_output
from gendiff.diff_tree import gen_intern_diff
from gendiff.parser import parse, get_format, read_file


def generate_diff(source1, source2, format='stylish'):
    with open(source1) as input1:
        data1 = parse(read_file(input1), get_format(source1))
    with open(source2) as input2:
        data2 = parse(read_file(input2), get_format(source2))
    internal_diff = gen_intern_diff(data1, data2)
    return format_output(internal_diff, format)
