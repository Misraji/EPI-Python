"""Unit tests for EPI exercise 24.2."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_352_first_missing_positive import first_missing_positive


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 1), (([1, 2, 3],), 4), (([3, 4, -1, 1],), 2), (([1, 1],), 2)])
def test_cases(arguments, expected):
    assert first_missing_positive(*arguments) == expected
