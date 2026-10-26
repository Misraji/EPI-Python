"""Unit tests for EPI exercise 12.8."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_12_hash_tables.pg_173_longest_subarray_with_distinct_entries import longest_subarray_with_distinct_entries


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 0), (([1, 2, 3],), 3), (([1, 2, 1, 3, 4],), 4), (([1, 1, 1],), 1)])
def test_cases(arguments, expected):
    assert longest_subarray_with_distinct_entries(*arguments) == expected
