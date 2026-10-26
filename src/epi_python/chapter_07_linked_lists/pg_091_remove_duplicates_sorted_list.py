"""EPI 7.8: Remove duplicates from a sorted list, printed page 91.

Educational reconstruction, not a verbatim transcription. Algorithm: Skip maximal runs of duplicate nodes by relinking the first node of each run.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_07_linked_lists.pg_091_remove_duplicates_sorted_list
Tests: python -m pytest tests/chapter_07_linked_lists/test_pg_091_remove_duplicates_sorted_list.py -v
"""

# dataclass produces a compact node with `data` and `next` attributes.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class ListNode:
    data: int
    next: "ListNode | None" = None


def remove_duplicates_nodes(head: ListNode | None) -> ListNode | None:
    """Drop duplicate nodes from a sorted linked list."""
    current=head
    while current is not None:
        next_distinct=current.next
        while next_distinct is not None and next_distinct.data == current.data:
            next_distinct=next_distinct.next
        current.next=next_distinct
        current=next_distinct
    return head


def remove_duplicates_sorted_list(values: list[int]) -> list[int]:
    """Run node-based duplicate removal on a list of test values."""
    head=None
    for value in reversed(values):
        head=ListNode(value,head)
    head=remove_duplicates_nodes(head)
    result=[]
    while head is not None:
        result.append(head.data)
        head=head.next
    return result

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=remove_duplicates_sorted_list([])
    print('remove_duplicates_sorted_list', result)
    assert result == []
    result=remove_duplicates_sorted_list([1, 1, 2, 2, 3])
    print('remove_duplicates_sorted_list', result)
    assert result == [1, 2, 3]
    result=remove_duplicates_sorted_list([1, 2, 3])
    print('remove_duplicates_sorted_list', result)
    assert result == [1, 2, 3]
    result=remove_duplicates_sorted_list([4, 4, 4])
    print('remove_duplicates_sorted_list', result)
    assert result == [4]
