from gendiff import generate_diff


def test_generate_diff():
    test_res = open('./gendiff/tests/fixtures/test1.txt')
    test_str = ''
    for line in test_res:
        test_str += line
    assert generate_diff(
        './gendiff/tests/fixtures/test11.json',
        './gendiff/tests/fixtures/test12.json'
    ) == test_str
