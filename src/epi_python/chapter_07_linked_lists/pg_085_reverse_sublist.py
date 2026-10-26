"""EPI Python — Exercise 7.2: Reverse a Single Sublist

Chapter 7: Linked Lists
Textbook: pages 85–86 (printed page numbers; problem, solution and first
variant on 85, second variant and Figure 7.5 on 86). The ListNode prototype
used by the whole chapter is printed on page 82.

PROBLEM (from the textbook)
---------------------------
"This problem is concerned with reversing a sublist within a list."

"Write a program which takes a singly linked list L and two integers s and
f as arguments, and reverses the order of the nodes from the sth node to
fth node, inclusive. The numbering begins at 1, i.e., the head node is the
first node. Do not allocate additional nodes."

Example (Figure 7.4, applied to the list of Figure 7.5): starting from
M = 11 -> 7 -> 5 -> 3 -> 2, reversing the second through fourth nodes
gives 11 -> 3 -> 5 -> 7 -> 2. The node addresses printed in the figures
show that the same node objects are reused.

HINT (from the textbook)
------------------------
"Focus on the successor fields which have to be updated."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Direct approach: cut out the sublist, reverse it, and splice it back into
place. Its drawback is that it passes over the sublist twice.

Single-pass approach: combine finding the sublist with reversing it.

1. Iterate from the head to reach the sth node, keeping its predecessor
   (the node just before the sublist).
2. From the sth node onward, reverse while continuing to count.
3. On reaching the fth node, stop reversing and connect the reversed part
   with the parts before and after it that were not reversed.

The book's program starts from a placeholder (dummy head) node pointing at
L, so that reversal starting at the very first node needs no special case.
In each of the f - s steps, the node immediately after the current first
node of the sublist is unlinked and reinserted directly after the
predecessor, i.e. at the front of the sublist.

Implementation in this file: reverse_sublist_nodes() is the textbook
algorithm on linked nodes. reverse_sublist() is a helper added in this
repository (not in the book) that converts a Python list to nodes, checks
the bounds, calls the algorithm, and converts back.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 2, 3, 4], s=2, f=3   -> [1, 3, 2, 4]
    [1, 2, 3],    s=1, f=3   -> [3, 2, 1]   (whole list reversed)
    [1],          s=1, f=1   -> [1]         (one-node sublist)
"""

# Python standard library: automatic generation of special methods for
# classes that mainly store data.
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` is a decorator: it takes the class just defined and adds an
# __init__(self, data, next=None), a readable __repr__, and a field-by-field
# __eq__, all generated from the annotated attributes below. It replaces the
# book's hand-written ListNode (page 82: __init__(self, data=0,
# next_node=None)).
#
# Annotations like `data: int` document intended types; Python does not
# enforce them. The annotation for `next` is a string because ListNode is
# not yet defined while its class body runs. `X | None` means "an X or
# None"; None marks the end of the list.
@dataclass
class ListNode:
    data: int
    next: "ListNode | None" = None


# `ListNode | None` in the signature (evaluated at definition time; the `|`
# form needs Python 3.10+) says the list may be empty.
def reverse_sublist_nodes(head: ListNode | None, start: int, finish: int) -> ListNode | None:
    """Reverse the 1-indexed inclusive sublist of an existing linked chain.

    This is the textbook's reverse_sublist(L, start, finish) program
    (page 85). Only `next` fields change; no data nodes are allocated.
    """

    # Placeholder node in front of the real head (book: dummy_head), so the
    # node before position `start` always exists, even when start == 1.
    dummy = ListNode(0, head)
    predecessor = dummy

    # range(1, start) yields start - 1 values, so this loop advances
    # start - 1 times and stops on the node just before the sublist.
    # `_` is the conventional name for a loop variable that is not used.
    for _ in range(1, start):
        predecessor = predecessor.next

    # Reverses sublist. `front` is the original sth node; it stays in place
    # in memory and drifts to the end of the reversed segment as nodes
    # behind it are moved to the front.
    front = predecessor.next
    for _ in range(finish - start):

        # Unlink the node after `front` and reinsert it right after
        # `predecessor`. The order of these three assignments matters: each
        # one reads a link before a later statement overwrites it.
        moving = front.next
        front.next = moving.next
        moving.next = predecessor.next
        predecessor.next = moving
    return dummy.next


def reverse_sublist(values: list[int], start: int, finish: int) -> list[int]:
    """Build nodes, apply the relinking algorithm, return values for display.

    Helper added in this repository (not in the book). It rejects bounds
    outside 1 <= start <= finish <= len(values).
    """

    # Chained comparison: `a <= b <= c <= d` means a <= b and b <= c and
    # c <= d, each middle value being evaluated only once.
    #
    # `raise ValueError(...)` stops the function with an exception; the
    # caller can catch it with try/except. ValueError is the standard
    # exception for an argument of the right type but an invalid value.
    if not 1 <= start <= finish <= len(values):
        raise ValueError('invalid 1-indexed sublist bounds')
    head = None

    # reversed(sequence) yields items from last to first without copying.
    # Prepending in that order leaves `head` at the first value.
    for value in reversed(values):
        head = ListNode(value, head)
    head = reverse_sublist_nodes(head, start, finish)
    result=[]
    while head is not None:
        result.append(head.data)
        head=head.next
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 85–86)
# -----------------------------------------------
# The running time is dominated by the walk to the fth node: O(f).
# No additional nodes are allocated, so the extra space is O(1).
#
# VARIANTS
# --------
# - Write a function that reverses a singly linked list. It should use no
#   more than constant storage beyond that needed for the list itself.
#   Figure 7.5 shows the result: the list of Figure 7.3(b),
#   2 -> 3 -> 5 -> 7 -> 11, becomes 11 -> 7 -> 5 -> 3 -> 2 with no new
#   nodes allocated. (stated in the book; no solution given)
# - Write a program which takes as input a singly linked list L and a
#   nonnegative integer k, and reverses the list k nodes at a time. If the
#   number of nodes n is not a multiple of k, leave the last n mod k nodes
#   unchanged. Do not change the data stored within a node.
#   (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Node class: book (page 82) `class ListNode` with
#   `__init__(self, data=0, next_node=None)`; file uses a @dataclass with
#   fields `data: int` and `next: "ListNode | None" = None`.
# - Function name: book `reverse_sublist(L, start, finish)`; file
#   `reverse_sublist_nodes(head, start, finish)` with type hints. The name
#   reverse_sublist is reused in the file for an added helper that takes
#   and returns Python lists and raises ValueError on bad bounds.
# - Variable names: book `dummy_head`, `sublist_head`, `sublist_iter`,
#   `temp`; file `dummy`, `predecessor`, `front`, `moving`.
# - Book initializes with chained assignment
#   `dummy_head = sublist_head = ListNode(0, L)`; file uses two statements.
# - The book's single tuple assignment
#   `sublist_iter.next, temp.next, sublist_head.next = (temp.next,
#   sublist_head.next, temp)` is split into three ordinary assignments in
#   the file; the resulting links are the same.
# - Helper reverse_sublist (list conversion and bounds check) is not in
#   the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases; pytest has the full set.
    # The examples reverse a middle segment, the whole list, and a
    # one-node segment. `assert` raises AssertionError if a result is
    # different from the expected value (a quick smoke check).
    result=reverse_sublist([1, 2, 3, 4], 2, 3)
    print('reverse_sublist', result)
    assert result == [1, 3, 2, 4]
    result=reverse_sublist([1, 2, 3], 1, 3)
    print('reverse_sublist', result)
    assert result == [3, 2, 1]
    result=reverse_sublist([1], 1, 1)
    print('reverse_sublist', result)
    assert result == [1]
