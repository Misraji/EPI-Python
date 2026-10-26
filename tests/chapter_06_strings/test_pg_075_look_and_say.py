"""Unit tests for EPI exercise 6.8."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_06_strings.pg_075_look_and_say import look_and_say


@pytest.mark.parametrize(("arguments", "expected"), [((1,), '1'), ((2,), '11'), ((3,), '21'), ((4,), '1211'), ((5,), '111221')])
def test_cases(arguments, expected):
    assert look_and_say(*arguments) == expected
