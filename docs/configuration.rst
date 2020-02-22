=============
Configuration
=============

Location
========
The flake8-filename plug-in loads its configuration options from the same source as standard flake8 configuration.
Flake8 supports storing its configuration in the following places:

Your top-level user directory. In your project in one of ``setup.cfg``, ``tox.ini``, or ``.flake8``. For more information
on configuration locations see:

Flake8_configuration_

Configuration
=============
You may configure up to 50 filename validators.

+---------------------+----------------------------------------------+-------------------------------------------------+
| Param Name          + Valid Argument                               + Explanation                                     +
+=====================+==============================================+=================================================+
| filter_regex        + any valid regex that does not contain spaces + A regex to filter on certain Python files       |
+---------------------+----------------------------------------------+-------------------------------------------------+
| filename_regex      + any valid regex that does not contain spaces | A regex to validate filtered Python filenames   |
+---------------------+----------------------------------------------+-------------------------------------------------+
| filter_with_ext     + A Boolean                                    | Whether to include the file extension when      |
|                     +                                              | filtering files. Default is to strip extension. |
+---------------------+----------------------------------------------+-------------------------------------------------+

**This plug-in will automatically strip the leading path for the Python files under evaluation, and extension, unless
`filter_with_ext` is set.**

Examples:
=========
All examples assume running against the following test file.


**test_example.py** : An example pytest::

    def test_thing():
        pass

**.flake8** : A simple configuration to validate that Python files that begin with "test\_" have "fun" in the name::

    [flake8]
    filename_check1 = filter_regex=test_.+
                      filename_regex=test_fun.*

**Shell Output** : evaluate if the filename contains "fun"::

    ./test_example.py:1:1: N501 filename failed regex validation 'test_fun.*'

.. _Flake8_configuration: http://flake8.pycqa.org/en/latest/user/configuration.html
