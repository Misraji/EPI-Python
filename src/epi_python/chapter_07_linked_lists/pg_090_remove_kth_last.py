"""EPI exercise 7.7, printed page 90: Remove the kth last element from a list.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Remove the kth last element from a list.
Method/complexity: Advance fast pointer k nodes, then move both to end; O(n) time, O(1) space.
For the book's original explanation and variants, see:
    pg_090_exercise_07_07_remove_the_kth_last_element_from_a_list.md

Run: python -m epi_python.chapter_07_linked_lists.pg_090_remove_kth_last
Test: python -m pytest tests/chapter_07_linked_lists/test_pg_090_remove_kth_last.py -v
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


def remove_kth_last(head: ListNode | None, k: int) -> ListNode | None:
    """Remove kth-to-last node using two pointers k steps apart (k starts at 1)."""
    if k <= 0:
        raise ValueError("k must be positive")
    dummy = ListNode(0, head)
    lead = dummy
    for _ in range(k):
        lead = lead.next
        if lead is None:
            raise IndexError("k exceeds list length")
    follow = dummy
    while lead.next is not None:
        lead = lead.next
        follow = follow.next
    follow.next = follow.next.next
    return dummy.next


def remove_kth_last_values(values: list[int], k: int) -> list[int]:
    return node_values(remove_kth_last(build_nodes(values), k))


if __name__ == "__main__":
    print("remove second-to-last:", remove_kth_last_values([1, 2, 3], 2))
    assert remove_kth_last_values([1, 2, 3], 2) == [1, 3]
