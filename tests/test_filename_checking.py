# -*- coding: utf-8 -*-

import pytest

# args to only use checks that raise an 'N' prefixed error
extra_args = ['--select', 'N']

config = r"""
[flake8]
filename_check1 = filter_regex=test_.+
                  filename_regex=test_[\w-]+$
"""


def test_pass_filter_and_match_filename(flake8dir):
    """Verify that no violations are raised when a file passes the filter and matches the desired filename."""

    # Setup
    flake8dir.make_setup_cfg(config)
    flake8dir.make_file('test_File-10.py', 'import sys')

    # Test
    result = flake8dir.run_flake8(extra_args)
    assert result.out_lines == []


def test_fail_filter(flake8dir):
    """Verify that no violations are raised when a file fails the filter."""

    # Setup
    flake8dir.make_setup_cfg(config)
    flake8dir.make_file('regular_file.py', 'import sys')

    # Test
    result = flake8dir.run_flake8(extra_args)
    assert result.out_lines == []


def test_pass_filter_and_fail_match(flake8dir):
    """Verify that a violation is raised when a file passes the filter and fails to match the desired filename."""

    # Setup
    flake8dir.make_setup_cfg(config)
    flake8dir.make_file('test_not.allowed.py', 'import sys')

    expected = ["./test_not.allowed.py:0:1: N501 filename failed regex validation 'test_[\\w-]+$'"]

    # Test
    result = flake8dir.run_flake8(extra_args)
    observed = result.out_lines

    pytest.helpers.assert_lines(expected, observed)
