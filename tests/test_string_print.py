"""Simple test for hello"""
from python_starter_project.string_print import string_print


def test_hello():
    """Test of happy path with string"""
    assert string_print("hello") == "hello"


def test_hello_int():
    """Test of value with integer 5"""
    value = 5
    assert string_print(value) == 5
