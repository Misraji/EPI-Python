"""Unit tests for EPI exercise 16.1."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_236_num_combinations_for_final_score import num_combinations_for_final_score


@pytest.mark.parametrize(("arguments", "expected"), [((0, [2, 3]), 1), ((4, [2, 3]), 1), ((7, [2, 3, 7]), 2), ((1, [2, 3]), 0)])
def test_cases(arguments, expected):
    assert num_combinations_for_final_score(*arguments) == expected
