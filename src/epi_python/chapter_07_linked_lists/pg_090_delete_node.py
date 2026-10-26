"""EPI exercise 7.6, printed page 90: Delete a node from a singly linked list.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Delete a node from a singly linked list.
Method/complexity: Copy successor data and bypass it; O(1) time, O(1) space.
For the book's original explanation and variants, see:
    pg_090_exercise_07_06_delete_a_node_from_a_singly_linked_list.md

Run: python -m epi_python.chapter_07_linked_lists.pg_090_delete_node
Test: python -m pytest tests/chapter_07_linked_lists/test_pg_090_delete_node.py -v
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


def delete_node(node: ListNode) -> None:
    """Delete a non-tail node given only its pointer, by copying its successor."""
    if node.next is None:
        raise ValueError("Cannot delete a tail node this way")
    node.data = node.next.data
    node.next = node.next.next


def delete_at_index(values: list[int], index: int) -> list[int]:
    """Adapter: delete a non-tail node and return the resulting linked-list data."""
    if not 0 <= index < len(values) - 1:
        raise ValueError("Index must refer to a non-tail node")
    head = build_nodes(values)
    node = head
    for _ in range(index):
        node = node.next
    delete_node(node)
    return node_values(head)


if __name__ == "__main__":
    print("delete node:", delete_at_index([1, 2, 3], 1))
    assert delete_at_index([1, 2, 3], 1) == [1, 3]
