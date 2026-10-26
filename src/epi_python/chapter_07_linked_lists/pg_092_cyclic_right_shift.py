"""EPI exercise 7.9, printed page 92: Implement cyclic right shift for singly linked lists.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement cyclic right shift for singly linked lists.
Method/complexity: One traversal to find length, another to break ring; O(n) time, O(1) space.
For the book's original explanation and variants, see:
    pg_092_exercise_07_09_implement_cyclic_right_shift_for_singly_linked_lists.md

Run: python -m epi_python.chapter_07_linked_lists.pg_092_cyclic_right_shift
Test: python -m pytest tests/chapter_07_linked_lists/test_pg_092_cyclic_right_shift.py -v
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


def cyclic_right_shift(head: ListNode | None, k: int) -> ListNode | None:
    """Rotate nodes k steps toward the head by relinking the last k nodes."""
    if k < 0:
        raise ValueError("Shift must be nonnegative")
    if head is None:
        return None
    tail, length = head, 1
    while tail.next:
        tail = tail.next
        length += 1
    k %= length
    if not k:
        return head
    tail.next = head
    steps = length - k
    new_tail = tail
    for _ in range(steps):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head


def cyclic_shift_values(values: list[int], k: int) -> list[int]:
    return node_values(cyclic_right_shift(build_nodes(values), k))


if __name__ == "__main__":
    print("cyclic shift:", cyclic_shift_values([1, 2, 3, 4], 1))
    assert cyclic_shift_values([1, 2, 3, 4], 1) == [4, 1, 2, 3]
