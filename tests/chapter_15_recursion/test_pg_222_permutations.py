"""Parameterized tests for EPI exercise 15.3.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_15_recursion.pg_222_permutations import permutations


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(([],), [[]]), (([1],), [[1]]), (([1, 2],), [[1, 2], [2, 1]])],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = permutations(*arguments)
    assert observed == expected


def test_six_distinct_permutations():
    result = permutations([1, 2, 3])
    assert len(result) == len({tuple(x) for x in result}) == 6


def test_pdf_lexicographic_permutation_alternative():
    import itertools
    import random

    from epi_python.chapter_15_recursion.pg_222_permutations import (
        permutations_by_next_permutation,
    )

    generator = random.Random(15222)
    for n in range(7):
        values = generator.sample(range(-20, 20), n)
        expected = [list(p) for p in itertools.permutations(sorted(values))]
        assert permutations_by_next_permutation(values) == expected
        assert sorted(permutations(values)) == expected
