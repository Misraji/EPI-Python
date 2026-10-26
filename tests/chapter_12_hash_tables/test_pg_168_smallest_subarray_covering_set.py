"""Independent tests for EPI 12.6.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_12_hash_tables.pg_168_smallest_subarray_covering_set import smallest_subarray_covering_set

@pytest.mark.parametrize(("args", "expected"), [
    ((["a","x","b","a","c","b"], {"a","b","c"}), (2,4)),
    ((["a","a","a"], {"b"}), None),
    ((["x"], set()), (0,-1)),
    (([], {"a"}), None),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert smallest_subarray_covering_set(*copy.deepcopy(args)) == expected

def test_against_bruteforce_windows():
    words = ["a","b","c","b","a","c","a"]
    for needed in ({"a"},{"a","b"},{"a","c"},{"a","b","c"}):
        result = smallest_subarray_covering_set(words, needed)
        valid = [(i,j) for i in range(len(words)) for j in range(i,len(words)) if needed <= set(words[i:j+1])]
        assert result in valid
        assert result[1]-result[0] == min(j-i for i,j in valid)
