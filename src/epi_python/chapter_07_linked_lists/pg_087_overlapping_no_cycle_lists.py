"""EPI exercise 7.4, printed page 87: Test for overlapping lists - lists are cycle-free.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Test for overlapping lists - lists are cycle-free.
Method/complexity: Align lengths and walk both lists; O(n+m) time and O(1) auxiliary space.
For the book's original explanation and variants, see:
    pg_087_exercise_07_04_test_for_overlapping_lists_lists_are_cycle_free.md

Run: python -m epi_python.chapter_07_linked_lists.pg_087_overlapping_no_cycle_lists
Test: python -m pytest tests/chapter_07_linked_lists/test_pg_087_overlapping_no_cycle_lists.py -v
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


def overlapping_no_cycle_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    """Find the first shared node by object identity in two acyclic lists."""
    def length(head):
        result = 0
        while head:
            result += 1
            head = head.next
        return result
    length_a, length_b = length(a), length(b)
    if length_a > length_b:
        a, b = b, a
        length_a, length_b = length_b, length_a
    for _ in range(length_b - length_a):
        b = b.next
    while a is not b:
        a = a.next
        b = b.next
    return a


def overlapping_tail_first_value(a: list[int], b: list[int], tail: list[int]) -> int | None:
    """Build two lists with a physically shared tail for demonstration."""
    common = build_nodes(tail)
    def with_tail(prefix):
        if not prefix:
            return common
        head = build_nodes(prefix)
        node = head
        while node.next:
            node = node.next
        node.next = common
        return head
    match = overlapping_no_cycle_lists(with_tail(a), with_tail(b))
    return None if match is None else match.data


if __name__ == "__main__":
    match = overlapping_tail_first_value([1, 2], [3], [7, 8])
    print("first overlapping value:", match)
    assert match == 7
