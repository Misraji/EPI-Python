"""Unit tests for EPI exercise 5.11."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_05_arrays.pg_052_next_permutation import next_permutation


@pytest.mark.parametrize(("arguments", "expected"), [(([],), []), (([1],), []), (([1, 2, 3],), [1, 3, 2]), (([3, 2, 1],), []), (([1, 1, 2],), [1, 2, 1])])
def test_cases(arguments, expected):
    assert next_permutation(*arguments) == expected


def test_textbook_next_permutation_is_in_place_and_matches_reference():
    from epi_python.chapter_05_arrays.pg_052_next_permutation import next_permutation, next_permutation_in_place
    import itertools
    for n in range(1, 6):
        permutations = list(itertools.permutations(range(n)))
        for idx, perm in enumerate(permutations):
            values = list(perm)
            identity = id(values)
            want = list(permutations[idx + 1]) if idx + 1 < len(permutations) else []
            assert next_permutation_in_place(values) == want
            assert next_permutation(list(perm)) == want
            assert id(values) == identity
