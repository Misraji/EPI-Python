"""Independent tests for EPI 10.6.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_10_heaps.pg_140_k_largest_in_binary_heap import k_largest_in_binary_heap

@pytest.mark.parametrize(("args", "expected"), [
    (([10,9,8,3,4,1,2], 3), [10,9,8]),
    (([5], 1), [5]),
    (([], 0), []),
    (([7,7,6], 2), [7,7]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert k_largest_in_binary_heap(*copy.deepcopy(args)) == expected

def test_against_full_sort():
    import random
    rng = random.Random(9)
    for n in range(1, 31):
        import heapq
        values = [rng.randrange(-50, 51) for _ in range(n)]
        heapq.heapify(values)
        maxheap = [-v for v in values]
        for k in (0, 1, n // 2, n):
            assert k_largest_in_binary_heap(maxheap, k) == sorted(maxheap, reverse=True)[:k]
