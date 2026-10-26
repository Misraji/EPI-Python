"""EPI exercise 7.13, printed page 96: Add list-based integers.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Add list-based integers.
Method/complexity: Single pass through both lists, O(max(n,m)) time and output storage.
For the book's original explanation and variants, see:
    pg_096_exercise_07_13_add_list_based_integers.md

Run: python -m epi_python.chapter_07_linked_lists.pg_096_add_list_based_integers
Test: python -m pytest tests/chapter_07_linked_lists/test_pg_096_add_list_based_integers.py -v
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


def add_two_numbers(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    """Add digits in least-significant-digit-first order, handling arbitrary length."""
    dummy = ListNode(0)
    tail = dummy
    carry = 0
    while a is not None or b is not None or carry:
        total = carry
        if a is not None:
            total += a.data
            a = a.next
        if b is not None:
            total += b.data
            b = b.next
        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next


def add_list_based_integers(a: list[int], b: list[int]) -> list[int]:
    return node_values(add_two_numbers(build_nodes(a), build_nodes(b)))


if __name__ == "__main__":
    print("reverse-digit sum:", add_list_based_integers([3, 1, 4], [7, 0, 9]))
    assert add_list_based_integers([3, 1, 4], [7, 0, 9]) == [0, 2, 3, 1]
