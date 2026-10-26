"""Independent tests for EPI 7.4.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_07_linked_lists.pg_087_overlapping_no_cycle_lists import overlapping_tail_first_value

@pytest.mark.parametrize(("args", "expected"), [
    (([1], [2, 3], [8, 9]), 8),
    (([], [], [5]), 5),
    (([1], [2], []), None),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert overlapping_tail_first_value(*copy.deepcopy(args)) == expected

from epi_python.chapter_07_linked_lists.pg_087_overlapping_no_cycle_lists import build_nodes, overlapping_no_cycle_lists, ListNode


def test_identity_not_equal_values():
    left = build_nodes([1, 2])
    right = build_nodes([1, 2])
    assert overlapping_no_cycle_lists(left, right) is None


def test_shared_tail_node_identity():
    shared = ListNode(42)
    left, right = ListNode(1, shared), ListNode(2, shared)
    assert overlapping_no_cycle_lists(left, right) is shared
