"""Unit tests for EPI exercise 5.8."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_05_arrays.pg_048_rearrange_alternation import rearrange_alternation


@pytest.mark.parametrize(("arguments", "expected"), [(([],), []), (([3, 2],), [2, 3]), (([1, 2, 3, 4],), [1, 3, 2, 4]), (([4, 3, 2, 1],), [3, 4, 1, 2])])
def test_cases(arguments, expected):
    assert rearrange_alternation(*arguments) == expected


def test_textbook_mutates_original_alternation():
    from epi_python.chapter_05_arrays.pg_048_rearrange_alternation import rearrange_alternation_in_place
    import random
    rng = random.Random(5108)
    for size in range(25):
        for _ in range(20):
            data = [rng.randrange(0,10) for _ in range(size)]
            before, identity = sorted(data), id(data)
            assert rearrange_alternation_in_place(data) is None
            assert id(data) == identity and sorted(data) == before
            assert all((data[i] <= data[i+1] if i%2==0 else data[i] >= data[i+1]) for i in range(len(data)-1))
