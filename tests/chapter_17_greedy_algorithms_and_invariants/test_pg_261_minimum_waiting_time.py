"""Unit tests for EPI exercise 17.2."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_17_greedy_algorithms_and_invariants.pg_261_minimum_waiting_time import minimum_waiting_time


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 0), (([3],), 0), (([2, 5, 1],), 4), (([2, 2, 2],), 6)])
def test_cases(arguments, expected):
    assert minimum_waiting_time(*arguments) == expected
