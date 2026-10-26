"""Parameterized tests for EPI exercise 5.9.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_05_arrays.pg_049_generate_primes import generate_primes


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0,), []), ((1,), []), ((2,), [2]), ((10,), [2, 3, 5, 7]), ((20,), [2, 3, 5, 7, 11, 13, 17, 19])],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = generate_primes(*arguments)
    assert observed == expected


def test_prime_limit_inclusive():
    assert generate_primes(11)[-1] == 11
