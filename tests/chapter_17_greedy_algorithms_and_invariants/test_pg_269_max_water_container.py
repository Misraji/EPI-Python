"""Unit tests for EPI exercise 17.7."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_17_greedy_algorithms_and_invariants.pg_269_max_water_container import max_water_container


@pytest.mark.parametrize(("arguments", "expected"), [(([],), 0), (([1],), 0), (([1, 1],), 1), (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49)])
def test_cases(arguments, expected):
    assert max_water_container(*arguments) == expected
