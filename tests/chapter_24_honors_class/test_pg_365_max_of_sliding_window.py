"""Unit tests for EPI exercise 24.12."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_365_max_of_sliding_window import max_of_sliding_window


@pytest.mark.parametrize(("arguments", "expected"), [(([], 1), []), (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]), (([2, 1], 1), [2, 1]), (([2, 1], 2), [2])])
def test_cases(arguments, expected):
    assert max_of_sliding_window(*arguments) == expected
