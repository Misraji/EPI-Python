"""Parameterized checks of EPI 16.6 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_246_optimum_subject_to_capacity import optimum_subject_to_capacity


@pytest.mark.parametrize(("arguments", "expected"), [(([], 10), 0), (([(2, 3), (3, 4), (4, 5)], 5), 7), (([(2, 10)], 1), 0), (([(2, 10), (2, 20)], 4), 30)])
def test_examples(arguments, expected):
    assert optimum_subject_to_capacity(*arguments) == expected
