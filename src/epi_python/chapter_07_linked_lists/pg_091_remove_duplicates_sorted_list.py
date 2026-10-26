"""EPI Python — Exercise 7.8: Remove Duplicates from a Sorted List

Chapter 7: Linked Lists
Textbook: pages 91–92 (printed page numbers; problem, hint and start of the
solution on 91, program, complexity and variant on 92). The ListNode
prototype used by the whole chapter is printed on page 82.

PROBLEM (from the textbook)
---------------------------
"This problem is concerned with removing duplicates from a sorted list of
integers. See Figure 7.8 for an example."

"Write a program that takes as input a singly linked list of integers in
sorted order, and removes duplicates from it. The list should be sorted."

Example (Figure 7.8): L = 2 -> 2 -> 3 -> 5 -> 7 -> 11 -> 11 becomes
L = 2 -> 3 -> 5 -> 7 -> 11. The node addresses in the figure show that the
surviving nodes are the original first node of each value.

HINT (from the textbook)
------------------------
"Focus on the successor fields which have to be updated."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: build a new list, using a hash table to check whether a value
has already been added. Alternatively, search the new list itself for the
candidate value. For a list of length n, the first needs O(n) extra space
for the hash table and the second O(n^2) time for the lookups; both
allocate n nodes for the new list.

Better: use the fact that the list is sorted, so equal values are next to
each other. While traversing, remove all following nodes whose value
equals the current node's value, by pointing the current node directly at
the next node with a different value.

Implementation in this file: remove_duplicates_nodes() is the textbook
program. remove_duplicates_sorted_list() is a helper added in this
repository (not in the book) that converts a Python list to nodes and
back.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []               -> []
    [1, 1, 2, 2, 3]  -> [1, 2, 3]
    [1, 2, 3]        -> [1, 2, 3]   (no duplicates)
    [4, 4, 4]        -> [4]         (all equal)
"""

# Python standard library: automatic generation of special methods for
# classes that mainly store data.
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` is a decorator that generates __init__(self, data, next=None),
# a readable __repr__ and a field-by-field __eq__ from the annotated
# attributes. It replaces the book's hand-written ListNode (page 82:
# __init__(self, data=0, next_node=None)).
#
# Annotations like `data: int` document types and are not enforced. The
# `next` annotation is a string because ListNode is not yet defined while
# its body runs; `X | None` means "an X or None" (None ends the list).
@dataclass
class ListNode:
    data: int
    next: "ListNode | None" = None


# `ListNode | None` in the signature (evaluated at definition time; the `|`
# form needs Python 3.10+) says the list may be empty.
def remove_duplicates_nodes(head: ListNode | None) -> ListNode | None:
    """Drop duplicate nodes from a sorted linked list.

    This is the textbook's remove_duplicates(L) program (page 92). The
    list is changed in place and its head is returned.
    """
    current=head
    while current is not None:

        # Uses next_distinct to find the next distinct value. The `and`
        # operator short-circuits: when next_distinct is None, the right
        # side (next_distinct.data) is never evaluated, so no error occurs.
        next_distinct=current.next
        while next_distinct is not None and next_distinct.data == current.data:
            next_distinct=next_distinct.next

        # Skip all the duplicates at once, then move to the next value.
        current.next=next_distinct
        current=next_distinct
    return head


def remove_duplicates_sorted_list(values: list[int]) -> list[int]:
    """Run node-based duplicate removal on a list of test values.

    Helper added in this repository (not in the book). `list[int]` is a
    type hint meaning "a list of ints" (not enforced).
    """
    head=None

    # reversed(sequence) yields items from last to first without copying,
    # so prepending leaves `head` at values[0].
    for value in reversed(values):
        head=ListNode(value,head)
    head=remove_duplicates_nodes(head)
    result=[]
    while head is not None:
        result.append(head.data)
        head=head.next
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 92)
# -------------------------------------------
# The time bound needs a little amortized analysis: a single node can take
# more than O(1) time to process when it is followed by many nodes with the
# same value. A clearer argument is that each link is traversed once, so the
# total time is O(n). The space complexity is O(1).
#
# VARIANTS
# --------
# - Let m be a positive integer and L a sorted singly linked list of
#   integers. For each integer k, if k appears more than m times in L,
#   remove all nodes from L containing k.
#   (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Node class: book (page 82) `class ListNode` with
#   `__init__(self, data=0, next_node=None)`; file uses a @dataclass with
#   fields `data: int` and `next: "ListNode | None" = None`.
# - Function: book `remove_duplicates(L)`; file
#   `remove_duplicates_nodes(head)` with type hints.
# - Iterator: book `it`; file `current`. Book tests truthiness
#   (`while it:`, `while next_distinct and ...`); file uses explicit
#   `is not None` tests. Otherwise the statements match.
# - Helper remove_duplicates_sorted_list is not in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases; pytest has the full set.
    # They cover an empty list, runs of duplicates, no duplicates, and all
    # values equal. `assert` raises AssertionError if a result is
    # different from the expected value.
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
