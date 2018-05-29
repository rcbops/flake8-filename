# -*- coding: utf-8 -*-

import pytest

# args to only use checks that raise an 'N' prefixed error
extra_args = ['--select', 'N']

config = """
[flake8]
filename_check1 = filter_regex=test_.+
                  filename_regex=test_file
filename_check2 = filter_regex=rest_.+
                  filename_regex=rest_file
filename_check3 = filter_regex=best_.+
                  filename_regex=best_file
filename_check4 = filter_regex=zest_.+
                  filename_regex=zest_file
"""


def test_pass_all_filters_and_filename_matches(flake8dir):
    """Verify that no violations are raised when a file passes all configured filters and matches all desired filename
    patterns.
    """

    # Setup
    flake8dir.make_setup_cfg(config)
    flake8dir.make_file('test_file.py', 'import sys')
    flake8dir.make_file('rest_file.py', 'import sys')
    flake8dir.make_file('best_file.py', 'import sys')
    flake8dir.make_file('zest_file.py', 'import sys')

    # Test
    result = flake8dir.run_flake8(extra_args)
    assert result.out_lines == []


def test_fail_all_filters(flake8dir):
    """Verify that no violations are raised when a file fails all configured filters.
    """

    # Setup
    flake8dir.make_setup_cfg(config)
    flake8dir.make_file('guest_file.py', 'import sys')
    flake8dir.make_file('blessed_file.py', 'import sys')
    flake8dir.make_file('chest_file.py', 'import sys')
    flake8dir.make_file('nest_file.py', 'import sys')

    # Test
    result = flake8dir.run_flake8(extra_args)
    assert result.out_lines == []


def test_pass_all_filters_and_fail_some_matches(flake8dir):
    """Verify violations are raised when a file passes all configured filters, but certain files fail desired filename
    patterns.
    """

    # Setup
    flake8dir.make_setup_cfg(config)
    flake8dir.make_file('test_file.py', 'import sys')
    flake8dir.make_file('rest_file.py', 'import sys')
    flake8dir.make_file('best_fail.py', 'import sys')
    flake8dir.make_file('zest_fail.py', 'import sys')

    expected = ["./best_fail.py:0:1: N503 filename failed regex validation 'best_file'",
                "./zest_fail.py:0:1: N504 filename failed regex validation 'zest_file'"]

    # Test
    result = flake8dir.run_flake8(extra_args)
    observed = result.out_lines

    pytest.helpers.assert_lines(expected, observed)
