"""EPI 7.3: Test for cyclicity, printed page 86.

Educational reconstruction, not a verbatim transcription. Algorithm: Floyd tortoise-and-hare fast/slow pointers detect cycles; reset one pointer to find the entry.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_07_linked_lists.pg_086_has_cycle
Tests: python -m pytest tests/chapter_07_linked_lists/test_pg_086_has_cycle.py -v
"""

# The dataclass decorator automatically builds the list node initializer.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class ListNode:
    data: int
    next: "ListNode | None" = None


def has_cycle_nodes(head: ListNode | None) -> ListNode | None:
    """Return a cycle-entry node, or None, using Floyd's two-pointer method."""
    slow=fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow is fast:
            finder=head
            while finder is not slow:
                finder=finder.next
                slow=slow.next
            return finder
    return None


def has_cycle(values: list[int], cycle_start: int | None = None) -> bool:
    """Build an example chain with an optional backward pointer at its tail."""
    nodes=[ListNode(value) for value in values]
    for first, second in zip(nodes,nodes[1:]):
        first.next=second
    if nodes and cycle_start is not None:
        nodes[-1].next=nodes[cycle_start]
    return has_cycle_nodes(nodes[0] if nodes else None) is not None

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=has_cycle([])
    print('has_cycle', result)
    assert result == False
    result=has_cycle([1, 2, 3])
    print('has_cycle', result)
    assert result == False
    result=has_cycle([1, 2, 3], 0)
    print('has_cycle', result)
    assert result == True
    result=has_cycle([1, 2, 3], 2)
    print('has_cycle', result)
    assert result == True
