"""Independent tests for EPI 7.7.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_07_linked_lists.pg_090_remove_kth_last import remove_kth_last_values

@pytest.mark.parametrize(("args", "expected"), [
    (([1, 2, 3], 1), [1, 2]),
    (([1, 2, 3], 2), [1, 3]),
    (([1, 2, 3], 3), [2, 3]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert remove_kth_last_values(*copy.deepcopy(args)) == expected

def test_invalid_k():
    with pytest.raises((ValueError, IndexError)):
        remove_kth_last_values([1, 2], 0)
    with pytest.raises((ValueError, IndexError)):
        remove_kth_last_values([1, 2], 3)
