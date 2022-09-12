from gendiff import generate_diff
import pytest
RES_FIXTURES = (
    './tests/fixtures/test1.txt',
    './tests/fixtures/test2.txt',
    './tests/fixtures/test3.txt',
    './tests/fixtures/test_plain.txt',
    './tests/fixtures/test4.txt'
)

input1 = (
    './tests/fixtures/test11.json',
    './tests/fixtures/test21.json',
    './tests/fixtures/test11.yaml',
    './tests/fixtures/file1.json',
    './tests/fixtures/file1.yaml'
)


input2 = (
    './tests/fixtures/test12.json',
    './tests/fixtures/test22.json',
    './tests/fixtures/test12.yaml',
    './tests/fixtures/file2.json',
    './tests/fixtures/file2.yaml'
)


def res_load(file):
    with open(file) as test_res:
        res_str = ''
        for line in test_res:
            res_str += line
    return res_str


test_data = [
    (input1[0], input2[0], 'stylish', res_load(RES_FIXTURES[0])),
    (input1[1], input2[1], 'stylish', res_load(RES_FIXTURES[1])),
    (input1[2], input2[2], 'stylish', res_load(RES_FIXTURES[0])),
    (input1[3], input2[3], 'stylish', res_load(RES_FIXTURES[2])),
    (input1[4], input2[4], 'stylish', res_load(RES_FIXTURES[2])),
    (input1[3], input2[3], 'plain', res_load(RES_FIXTURES[3])),
    (input1[3], input2[3], 'json', res_load(RES_FIXTURES[4]))
]


@pytest.mark.parametrize("input1, input2, format, expected", test_data)
def test_generate_diff(input1, input2, format, expected):
    assert generate_diff(input1, input2, format) == expected
