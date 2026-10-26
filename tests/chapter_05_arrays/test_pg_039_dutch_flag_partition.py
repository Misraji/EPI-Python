"""Independent tests for EPI 5.1.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_05_arrays.pg_039_dutch_flag_partition import dutch_flag_partition

@pytest.mark.parametrize(("args", "expected"), [
    ((1, [3, 1, 2, 1, 3]), [1, 1, 2, 3, 3]),
    ((0, [1, 1, 1]), [1, 1, 1]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert dutch_flag_partition(*copy.deepcopy(args)) == expected

def test_partition_properties():
    for values in ([4, 1, 3, 4, 2, 4, 0], [3, 3], [1]):
        pivot = values[0]
        original = sorted(values)
        result = dutch_flag_partition(0, values[:])
        assert sorted(result) == original
        stage = 0
        for item in result:
            category = (item > pivot) + (item >= pivot)
            assert category >= stage
            stage = category


def test_three_textbook_partition_algorithms():
    """Cross-check all three implementations on numerous array shapes."""
    from random import Random
    from epi_python.chapter_05_arrays.pg_039_dutch_flag_partition import (
        dutch_flag_partition_quadratic,
        dutch_flag_partition_two_pass,
    )

    algorithms = (dutch_flag_partition_quadratic, dutch_flag_partition_two_pass,
                  dutch_flag_partition)
    rng = Random(5101)
    for _ in range(900):
        original = [rng.randint(-3, 3) for _ in range(rng.randrange(1, 15))]
        index = rng.randrange(len(original))
        pivot = original[index]
        for algorithm in algorithms:
            result = algorithm(index, original.copy())
            categories = [(v > pivot) + (v >= pivot) for v in result]
            assert categories == sorted(categories), (algorithm.__name__, original, result)
            assert sorted(result) == sorted(original)
