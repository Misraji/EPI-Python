"""Independent tests for EPI 12.9.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_12_hash_tables.pg_174_longest_contained_interval import longest_contained_range

@pytest.mark.parametrize(("args", "expected"), [
    (([3,-2,7,9,8,1,2,0,-1,5,8],), 6),
    (([], ), 0),
    (([1],), 1),
    (([10,11,10,12],), 3),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert longest_contained_range(*copy.deepcopy(args)) == expected

def test_random_sets_against_sorted_reference():
    import random
    rng=random.Random(7)
    for _ in range(100):
        data=[rng.randrange(-20,21) for _ in range(30)]
        ordered=sorted(set(data))
        longest=running=0
        for i,value in enumerate(ordered):
            running=running+1 if i and value==ordered[i-1]+1 else 1
            longest=max(longest,running)
        assert longest_contained_range(data)==longest
