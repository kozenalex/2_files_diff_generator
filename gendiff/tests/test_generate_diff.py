from gendiff import generate_diff


def test_generate_diff():
    test1_res = open('./gendiff/tests/fixtures/test1.txt')
    test2_res = open('./gendiff/tests/fixtures/test2.txt')
    test1_str = ''
    test2_str = ''
    for line in test1_res:
        test1_str += line
    for line in test2_res:
        test2_str += line
    assert generate_diff(
        './gendiff/tests/fixtures/test11.json',
        './gendiff/tests/fixtures/test12.json'
    ) == test1_str
    assert generate_diff(
        './gendiff/tests/fixtures/test21.json',
        './gendiff/tests/fixtures/test22.json'
    ) == test2_str
    assert generate_diff(
        './gendiff/tests/fixtures/test11.yaml',
        './gendiff/tests/fixtures/test12.yaml'
    ) == test1_str
