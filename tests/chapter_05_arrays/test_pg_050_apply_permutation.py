"""Independent tests for EPI 5.10.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_050_apply_permutation import apply_permutation

@pytest.mark.parametrize(("args", "expected"), [
    (([2, 0, 1], ["a", "b", "c"]), ["b", "c", "a"]),
    (([0, 1], [7, 8]), [7, 8]),
    (([], []), []),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert apply_permutation(*copy.deepcopy(args)) == expected



def test_all_three_permutation_methods_and_input_restoration():
    """The two textbook implementations must restore the permutation list."""
    from random import Random
    from epi_python.chapter_05_arrays.pg_050_apply_permutation import (
        apply_permutation_without_sign_marking, apply_permutation_visited,
    )
    rng = Random(51010)
    for n in range(12):
        for _ in range(100):
            perm = list(range(n))
            rng.shuffle(perm)
            values = list(range(n))
            expected = [None] * n
            for i in range(n):
                expected[perm[i]] = values[i]
            for algorithm in (apply_permutation, apply_permutation_without_sign_marking,
                              apply_permutation_visited):
                copied_perm = perm.copy()
                copied_values = values.copy()
                assert algorithm(copied_perm, copied_values) == expected
                assert copied_perm == perm
