from gendiff.tests.fixtures.testres import TEST1
from gendiff import generate_diff


def test_generate_diff():
    assert generate_diff(
        './gendiff/tests/fixtures/test11.json',
        './gendiff/tests/fixtures/test12.json'
    ) == TEST1
