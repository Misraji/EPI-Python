"""Unit tests for EPI exercise 16.4."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_244_compute_binomial_coefficients import compute_binomial_coefficients


@pytest.mark.parametrize(("arguments", "expected"), [((0, 0), 1), ((5, 2), 10), ((4, 4), 1), ((4, 5), 0)])
def test_cases(arguments, expected):
    assert compute_binomial_coefficients(*arguments) == expected
