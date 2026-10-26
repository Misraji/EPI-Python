"""Independent tests for EPI 7.6.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_07_linked_lists.pg_090_delete_node import delete_at_index

@pytest.mark.parametrize(("args", "expected"), [
    (([1, 2, 3], 1), [1, 3]),
    (([1, 2], 0), [2]),
    (([1, 2, 3], 0), [2, 3]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert delete_at_index(*copy.deepcopy(args)) == expected

from epi_python.chapter_07_linked_lists.pg_090_delete_node import ListNode, delete_node


def test_tail_cannot_be_deleted():
    with pytest.raises(ValueError):
        delete_node(ListNode(1))
