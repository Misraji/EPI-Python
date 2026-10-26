"""EPI 7.1: Merge two sorted lists, printed page 84.

Educational reconstruction, not a verbatim transcription. Algorithm: The real algorithm walks two ListNode chains and reuses nodes; an adapter handles examples as lists.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_07_linked_lists.pg_084_merge_two_sorted_lists
Tests: python -m pytest tests/chapter_07_linked_lists/test_pg_084_merge_two_sorted_lists.py -v
"""

# dataclass generates the initializer and representation for this node type.
# Documentation: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


@dataclass
class ListNode:
    data: int
    next: "ListNode | None" = None


def merge_sorted_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Merge two sorted singly linked lists by relinking existing nodes."""
    dummy = ListNode(0)
    tail = dummy
    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 if l1 is not None else l2
    return dummy.next


def merge_two_sorted_lists(a: list[int], b: list[int]) -> list[int]:
    """Convenient runnable demonstration of the linked-node algorithm."""
    def build(values):
        first = None
        for value in reversed(values):
            first = ListNode(value, first)
        return first
    current = merge_sorted_lists(build(a), build(b))
    result = []
    while current is not None:
        result.append(current.data)
        current = current.next
    return result

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=merge_two_sorted_lists([1, 3, 5], [2, 4, 6])
    print('merge_two_sorted_lists', result)
    assert result == [1, 2, 3, 4, 5, 6]
    result=merge_two_sorted_lists([], [1])
    print('merge_two_sorted_lists', result)
    assert result == [1]
    result=merge_two_sorted_lists([1, 1], [1, 2])
    print('merge_two_sorted_lists', result)
    assert result == [1, 1, 1, 2]
