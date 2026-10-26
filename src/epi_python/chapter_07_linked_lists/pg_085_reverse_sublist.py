"""EPI 7.2: Reverse a single sublist, printed page 85.

Educational reconstruction, not a verbatim transcription. Algorithm: Repeatedly take the node following the sublist head and splice it at the beginning of the sublist.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_07_linked_lists.pg_085_reverse_sublist
Tests: python -m pytest tests/chapter_07_linked_lists/test_pg_085_reverse_sublist.py -v
"""

# Dataclasses are lightweight ways to declare linked-list record types.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class ListNode:
    data: int
    next: "ListNode | None" = None


def reverse_sublist_nodes(head: ListNode | None, start: int, finish: int) -> ListNode | None:
    """Reverse the 1-indexed inclusive sublist of an existing linked chain."""
    dummy = ListNode(0, head)
    predecessor = dummy
    for _ in range(1, start):
        predecessor = predecessor.next
    front = predecessor.next
    for _ in range(finish - start):
        moving = front.next
        front.next = moving.next
        moving.next = predecessor.next
        predecessor.next = moving
    return dummy.next


def reverse_sublist(values: list[int], start: int, finish: int) -> list[int]:
    """Build nodes, apply the relinking algorithm, return values for display."""
    if not 1 <= start <= finish <= len(values):
        raise ValueError('invalid 1-indexed sublist bounds')
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    head = reverse_sublist_nodes(head, start, finish)
    result=[]
    while head is not None:
        result.append(head.data)
        head=head.next
    return result

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=reverse_sublist([1, 2, 3, 4], 2, 3)
    print('reverse_sublist', result)
    assert result == [1, 3, 2, 4]
    result=reverse_sublist([1, 2, 3], 1, 3)
    print('reverse_sublist', result)
    assert result == [3, 2, 1]
    result=reverse_sublist([1], 1, 1)
    print('reverse_sublist', result)
    assert result == [1]
