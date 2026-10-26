"""Unit tests for EPI exercise 16.1."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_236_num_combinations_for_final_score import num_combinations_for_final_score


@pytest.mark.parametrize(("arguments", "expected"), [((0, [2, 3]), 1), ((4, [2, 3]), 1), ((7, [2, 3, 7]), 2), ((1, [2, 3]), 0)])
def test_cases(arguments, expected):
    assert num_combinations_for_final_score(*arguments) == expected


def test_pdf_two_dimensional_score_dp():
    from epi_python.chapter_16_dynamic_programming.pg_236_num_combinations_for_final_score import (
        num_combinations_for_final_score_table,
    )
    for score in range(35):
        for plays in ([], [2], [2, 3], [2, 3, 7], [3, 5, 8]):
            assert num_combinations_for_final_score_table(score, plays) == num_combinations_for_final_score(score, plays)
