"""Unit tests for EPI exercise 6.1."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_06_strings.pg_068_string_integer_interconversion import int_to_string


@pytest.mark.parametrize(("arguments", "expected"), [((0,), '0'), ((3,), '3'), ((-125,), '-125'), ((2001,), '2001')])
def test_cases(arguments, expected):
    assert int_to_string(*arguments) == expected


def test_reverse_conversion():
    from epi_python.chapter_06_strings.pg_068_string_integer_interconversion import string_to_int
    for value in (-124,0,100,23412):
        assert string_to_int(int_to_string(value)) == value
