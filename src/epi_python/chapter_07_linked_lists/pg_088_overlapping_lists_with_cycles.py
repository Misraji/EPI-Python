"""EPI exercise 7.5, printed page 88: Test for overlapping lists - lists may have cycles.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Test for overlapping lists - lists may have cycles.
Method/complexity: Cycle detection and identity comparisons, O(n+m) time and O(1) auxiliary space.
For the book's original explanation and variants, see:
    pg_088_exercise_07_05_test_for_overlapping_lists_lists_may_have_cycles.md

Run: python -m epi_python.chapter_07_linked_lists.pg_088_overlapping_lists_with_cycles
Test: python -m pytest tests/chapter_07_linked_lists/test_pg_088_overlapping_lists_with_cycles.py -v
"""

# Reuse this chapter's singly linked ListNode, rather than a list-backed mock.
from epi_python.chapter_07_linked_lists.pg_084_merge_two_sorted_lists import ListNode


def build_nodes(values: list[int]) -> ListNode | None:
    """Construct nodes in input order for the standalone examples and tests."""
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def node_values(head: ListNode | None) -> list[int]:
    """Read an acyclic chain into a convenient Python list."""
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result

# Reuse Floyd's cycle-entry detection (O(1) additional memory).
from epi_python.chapter_07_linked_lists.pg_086_has_cycle import has_cycle_nodes

# Reuse the acyclic overlap algorithm for the zero-cycle case.
from epi_python.chapter_07_linked_lists.pg_087_overlapping_no_cycle_lists import overlapping_no_cycle_lists


def overlapping_lists_with_cycles(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    """Return shared node, or any node on common cycle when ambiguity exists."""
    entry_a, entry_b = has_cycle_nodes(a), has_cycle_nodes(b)
    if entry_a is None and entry_b is None:
        return overlapping_no_cycle_lists(a, b)
    if (entry_a is None) != (entry_b is None):
        return None
    if entry_a is entry_b:
        def distance(head, stop):
            length = 0
            while head is not stop:
                length += 1
                head = head.next
            return length
        na, nb = distance(a, entry_a), distance(b, entry_b)
        if na > nb:
            a, b = b, a
            na, nb = nb, na
        for _ in range(nb - na):
            b = b.next
        while a is not b and a is not entry_a and b is not entry_b:
            a, b = a.next, b.next
        return a if a is b else entry_a
    cursor = entry_a.next
    while cursor is not entry_a and cursor is not entry_b:
        cursor = cursor.next
    return entry_a if cursor is entry_b else None


if __name__ == "__main__":
    cycle_a = ListNode(1)
    cycle_b = ListNode(2, cycle_a)
    cycle_a.next = cycle_b
    print("overlap (cycles):", overlapping_lists_with_cycles(cycle_a, cycle_b).data)
    assert overlapping_lists_with_cycles(cycle_a, cycle_b) is cycle_a
