"""Parameterized tests for EPI exercise 13.1.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_13_sorting.pg_182_intersect_two_sorted_arrays import intersect_two_sorted_arrays


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(([], []), []), (([1, 2, 2, 3], [2, 2, 3, 4]), [2, 3]), (([1, 3], [2, 4]), []), (([1, 1], [1]), [1])],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = intersect_two_sorted_arrays(*arguments)
    assert observed == expected


def test_binary_search_vs_two_pointer_intersection():
    from epi_python.chapter_13_sorting.pg_182_intersect_two_sorted_arrays import intersect_two_sorted_arrays,intersect_two_sorted_arrays_bisect
    import random
    rng=random.Random(1301)
    for _ in range(1200):
        a=sorted(rng.choices(range(-10,11),k=rng.randrange(30)))
        b=sorted(rng.choices(range(-10,11),k=rng.randrange(30)))
        want=sorted(set(a)&set(b))
        assert intersect_two_sorted_arrays(a,b)==want
        assert intersect_two_sorted_arrays_bisect(a,b)==want
