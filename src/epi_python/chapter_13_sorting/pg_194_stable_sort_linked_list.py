"""EPI 13.10, printed page 194: Implement a fast sorting algorithm for lists.

Problem: Implement a fast sorting algorithm for lists. See pg_194_exercise_13_10_implement_a_fast_sorting_algorithm_for_lists.md for the full
original problem, hint, development, and variants from the PDF text layer.

Approach and complexity: O(n log n) stable merge sort; O(log n) recursion stack and O(1) extra list nodes per merge.

EDUCATIONAL RECONSTRUCTION: source and comments are not claimed verbatim.
Run directly: python -m epi_python.chapter_13_sorting.pg_194_stable_sort_linked_list
Test: python -m pytest tests/chapter_13_sorting/test_pg_194_stable_sort_linked_list.py -v
"""

# TEXTBOOK PROBLEM (exercise 13.10, printed page 194):
# Perform a stable, efficient sort of a singly linked list.
# HINT: Merge sort can splice linked nodes without array indexing.

# dataclass creates a compact singly-linked node type.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class ListNode:
    data: int
    next: 'ListNode | None' = None


def stable_sort_list(head: ListNode | None) -> ListNode | None:
    """Stable linked-list merge sort using tortoise/hare splitting."""
    if head is None or head.next is None:
        return head
    slow, fast = head, head.next
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    other = slow.next
    slow.next = None
    left = stable_sort_list(head)
    right = stable_sort_list(other)
    dummy = tail = ListNode(0)
    while left is not None and right is not None:
        if left.data <= right.data:
            tail.next, left = left, left.next
        else:
            tail.next, right = right, right.next
        tail = tail.next
    tail.next = left if left is not None else right
    return dummy.next


def to_linked(values: list[int]) -> ListNode | None:
    head = None
    for value in reversed(values):
        head = ListNode(value,head)
    return head


def to_list(head: ListNode | None) -> list[int]:
    result=[]
    while head is not None:
        result.append(head.data)
        head=head.next
    return result


if __name__ == '__main__':
    result = to_list(stable_sort_list(to_linked([4,1,3,1,2])))
    print('Sorted linked list:', result)
    assert result == [1,1,2,3,4]
