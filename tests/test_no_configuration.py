# -*- coding: utf-8 -*-
import pytest

# args to only use checks that raise an 'N' prefixed error
extra_args = ['--select', 'N']


def test_no_configuration(flake8dir):
    """Verify that a violation is raised when the plug-in is loaded without a configuration."""

    # Setup
    flake8dir.make_file('test_file.py', 'import sys')
    result = flake8dir.run_flake8(extra_args)

    # Test
    expected = ['./test_file.py:0:1: N401 no configuration found for flake8-filename, please provide filename configuration in a flake8 config']  # noqa: E501
    observed = result.out_lines

    pytest.helpers.assert_lines(expected, observed)
