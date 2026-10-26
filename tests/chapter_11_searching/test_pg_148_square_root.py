"""Unit tests for EPI exercise 11.4."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_11_searching.pg_148_square_root import square_root


@pytest.mark.parametrize(("arguments", "expected"), [((0,), 0), ((1,), 1), ((2,), 1), ((15,), 3), ((16,), 4), ((100,), 10)])
def test_cases(arguments, expected):
    assert square_root(*arguments) == expected
