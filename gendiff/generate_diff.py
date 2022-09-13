from gendiff.formatter import format_output
# from gendiff.internal_diff import gen_intern_diff
from gendiff.diff_tree import gen_intern_diff
from gendiff.load_data import get_data


def generate_diff(source1, source2, format='stylish'):
    internal_diff = gen_intern_diff(
        *get_data(source1, source2)
    )
    return format_output(internal_diff, format)
