"""Parameterized tests for EPI exercise 5.2.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_05_arrays.pg_043_plus_one import plus_one


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(([1, 2, 9],), [1, 3, 0]), (([9, 9],), [1, 0, 0]), (([0],), [1]), (([2, 3],), [2, 4])],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = plus_one(*arguments)
    assert observed == expected


def test_carry_modifies_same_list_as_in_textbook():
    digits = [9, 9]
    assert plus_one(digits) is digits
    assert digits == [1, 0, 0]


def test_empty_representation_is_invalid():
    with pytest.raises(ValueError):
        plus_one([])
