import pytest
from gendiff import generate_diff


def test_generate_diff():
    assert generate_diff(
        './gendiff/tests/fixtures/empty.json',
        './gendiff/tests/fixtures/empty.json'
    ) == '{\n}'
