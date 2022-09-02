from gendiff import generate_diff


def test_generate_diff():
    test1_res = open('./tests/fixtures/test1.txt')
    test2_res = open('./tests/fixtures/test2.txt')
    test3_res = open('./tests/fixtures/test3.txt')
    test4_res = open('./tests/fixtures/test_plain.txt')
    test1_str = ''
    test2_str = ''
    test3_str = ''
    test_plain = ''
    for line in test1_res:
        test1_str += line
    for line in test2_res:
        test2_str += line
    for line in test3_res:
        test3_str += line
    for line in test4_res:
        test_plain += line
    
    assert generate_diff(
        './tests/fixtures/test11.json',
        './tests/fixtures/test12.json'
    ) == test1_str
    assert generate_diff(
        './tests/fixtures/test21.json',
        './tests/fixtures/test22.json'
    ) == test2_str
    assert generate_diff(
        './tests/fixtures/test11.yaml',
        './tests/fixtures/test12.yaml'
    ) == test1_str
    assert generate_diff(
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json'
    ) == test3_str
    assert generate_diff(
        './tests/fixtures/file1.yaml',
        './tests/fixtures/file2.yaml'
    ) == test3_str
    assert generate_diff(
        './tests/fixtures/file1.yaml',
        './tests/fixtures/file2.yaml',
        'plain'
    ) == test_plain
