"""Unit tests for EPI exercise 17.5."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_17_greedy_algorithms_and_invariants.pg_266_majority_search import majority_search


@pytest.mark.parametrize(("arguments", "expected"), [(([],), None), ((['a', 'a', 'b'],), 'a'), ((['a', 'b'],), None), ((['z'],), 'z')])
def test_cases(arguments, expected):
    assert majority_search(*arguments) == expected
