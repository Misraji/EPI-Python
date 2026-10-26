"""EPI exercise 7.12, printed page 95: Implement list pivoting.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement list pivoting.
Method/complexity: Three linked sublists with stable order; O(n) time and O(1) auxiliary space.
For the book's original explanation and variants, see:
    pg_095_exercise_07_12_implement_list_pivoting.md

Run: python -m epi_python.chapter_07_linked_lists.pg_095_list_pivot
Test: python -m pytest tests/chapter_07_linked_lists/test_pg_095_list_pivot.py -v
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


def list_pivot(head: ListNode | None, pivot: int) -> ListNode | None:
    """Stable three-way partition around pivot without allocating list nodes."""
    dummy = [ListNode(0), ListNode(0), ListNode(0)]
    tail = dummy[:]
    while head is not None:
        following = head.next
        head.next = None
        index = 0 if head.data < pivot else (1 if head.data == pivot else 2)
        tail[index].next = head
        tail[index] = head
        head = following
    tail[0].next = dummy[1].next if dummy[1].next else dummy[2].next
    tail[1].next = dummy[2].next
    return dummy[0].next


def list_pivot_values(values: list[int], pivot: int) -> list[int]:
    return node_values(list_pivot(build_nodes(values), pivot))


if __name__ == "__main__":
    print("pivot:", list_pivot_values([3, 2, 2, 5, 1, 2], 2))
    assert list_pivot_values([3, 2, 2, 5, 1, 2], 2) == [1, 2, 2, 2, 3, 5]
