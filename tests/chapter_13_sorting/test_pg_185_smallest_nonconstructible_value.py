"""Unit tests for EPI exercise 13.4."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_13_sorting.pg_185_smallest_nonconstructible_value import smallest_nonconstructible_value


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 1), (([1, 1, 3, 4],), 10), (([1, 2, 2],), 6), (([2, 3],), 1)])
def test_cases(arguments, expected):
    assert smallest_nonconstructible_value(*arguments) == expected
