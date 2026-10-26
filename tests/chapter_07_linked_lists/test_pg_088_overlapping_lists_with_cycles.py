"""Independent tests for EPI 7.5.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_07_linked_lists.pg_088_overlapping_lists_with_cycles import overlapping_lists_with_cycles

@pytest.mark.parametrize(("args", "expected"), [
    ((None, None), None),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert overlapping_lists_with_cycles(*copy.deepcopy(args)) == expected

from epi_python.chapter_07_linked_lists.pg_088_overlapping_lists_with_cycles import ListNode


def test_shared_cycle_distinct_entries():
    a, b, c = ListNode(1), ListNode(2), ListNode(3)
    a.next, b.next, c.next = b, c, a
    assert overlapping_lists_with_cycles(a, b) in (a, b, c)


def test_disjoint_cycles():
    a, b = ListNode(1), ListNode(2)
    a.next, b.next = a, b
    assert overlapping_lists_with_cycles(a, b) is None


def test_shared_entry_with_shared_acyclic_stem():
    entry = ListNode(8)
    entry.next = entry
    stem = ListNode(7, entry)
    a, b = ListNode(1, stem), ListNode(2, stem)
    assert overlapping_lists_with_cycles(a, b) is stem
