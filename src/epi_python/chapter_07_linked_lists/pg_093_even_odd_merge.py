"""EPI exercise 7.10, printed page 93: Implement even-odd merge.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement even-odd merge.
Method/complexity: Rewire even and odd chains; O(n) time, O(1) space.
For the book's original explanation and variants, see:
    pg_093_exercise_07_10_implement_even_odd_merge.md

Run: python -m epi_python.chapter_07_linked_lists.pg_093_even_odd_merge
Test: python -m pytest tests/chapter_07_linked_lists/test_pg_093_even_odd_merge.py -v
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


def even_odd_merge(head: ListNode | None) -> ListNode | None:
    """Group nodes at positions 0,2,4,... before 1,3,5,... stably."""
    if head is None:
        return None
    even, odd = head, head.next
    odd_head = odd
    while odd is not None and odd.next is not None:
        even.next = odd.next
        even = even.next
        odd.next = even.next
        odd = odd.next
    even.next = odd_head
    return head


def even_odd_merge_values(values: list[int]) -> list[int]:
    return node_values(even_odd_merge(build_nodes(values)))


if __name__ == "__main__":
    print("even/odd merge:", even_odd_merge_values([0, 1, 2, 3, 4]))
    assert even_odd_merge_values([0, 1, 2, 3, 4]) == [0, 2, 4, 1, 3]
