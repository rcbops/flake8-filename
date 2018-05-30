# -*- coding: utf-8 -*-
import pytest
from flake8_filename import FilenameChecker

pytest_plugins = ['helpers_namespace']


# noinspection PyUnresolvedReferences
@pytest.helpers.register
def assert_lines(expected, observed):
    """A helper to assert that the contents of two arrays are the same

    Args:
        expected (list): The expected list of strings.
        observed (list): The observed list of strings.
    """
    e = [str(string) for string in expected]
    o = [str(string) for string in observed]
    e.sort()
    o.sort()
    assert e == o


@pytest.yield_fixture(autouse=True)
def run_around_tests():
    """A fixture to execute code before and after every test
    Code before the yield will run before each test.
    Code after the yield will run after each test.
    """
    FilenameChecker.filename_checks = dict.fromkeys(["filename_check{}".format(x) for x in range(1, 50)], {})
    yield
