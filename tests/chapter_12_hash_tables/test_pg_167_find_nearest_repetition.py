"""Unit tests for EPI exercise 12.5."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_12_hash_tables.pg_167_find_nearest_repetition import find_nearest_repetition


@pytest.mark.parametrize(("arguments", "expected"), [(([],), -1), ((['a', 'b', 'a'],), 2), ((['a', 'a', 'b'],), 1), ((['a', 'b'],), -1)])
def test_cases(arguments, expected):
    assert find_nearest_repetition(*arguments) == expected
