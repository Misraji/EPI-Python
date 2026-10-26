"""EPI Python — Exercise 7.1: Merge Two Sorted Lists

Chapter 7: Linked Lists
Textbook: pages 84–85 (printed page numbers; problem and solution start on
84, complexity analysis and variant on 85). The ListNode prototype used by
the whole chapter is printed on page 82.

PROBLEM (from the textbook)
---------------------------
"Consider two singly linked lists in which each node holds a number. Assume
the lists are sorted, i.e., numbers in the lists appear in ascending order
within each list. The merge of the two lists is a list consisting of the
nodes of the two lists in which numbers appear in ascending order."

"Write a program that takes two lists, assumed to be sorted, and returns
their merge. The only field your program can change in a node is its next
field."

Example (Figure 7.3): L1 = 2 -> 5 -> 7 and L2 = 3 -> 11 merge into
R = 2 -> 3 -> 5 -> 7 -> 11. The figure prints a memory address under each
node (for example 0x1000 for the node holding 2) to show that the merged
list R is made of the very same node objects as L1 and L2, just relinked.

HINT (from the textbook)
------------------------
"Two sorted arrays can be merged using two indices. For lists, take care
when one iterator reaches the end."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Naive approach: join the two lists end to end and then sort the combined
list. This ignores the fact that each input is already sorted, so its cost
is the cost of sorting, O((n + m) log(n + m)), where n and m are the two
list lengths.

Better approach: walk both lists at once. At each step compare the nodes
at the front of the two remaining lists, attach the one with the smaller
key to the end of the result, and advance in the list it came from. When
one list is used up, the rest of the other list is already sorted and is
attached in a single step.

The book's program uses a placeholder ("dummy head") node so that the
first attachment needs no special case; the answer is the node after the
placeholder. (The chapter's Table 7.1 recommends exactly this trick.)

Implementation in this file: merge_sorted_lists() is the textbook
algorithm. merge_two_sorted_lists() is a helper added in this repository
(not in the book) that converts Python lists to linked nodes, merges, and
converts back, so the algorithm is easy to call from tests and examples.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 3, 5] and [2, 4, 6]  -> [1, 2, 3, 4, 5, 6]
    []        and [1]        -> [1]           (one list empty)
    [1, 1]    and [1, 2]     -> [1, 1, 1, 2]  (duplicate keys kept)
"""

# Python standard library: automatic generation of special methods for
# classes that mainly store data.
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` is a decorator: it receives the class just defined and adds
# methods to it. From the annotated class attributes below it writes an
# __init__(self, data, next=None), a readable __repr__, and an __eq__ that
# compares fields. This replaces the book's hand-written ListNode class
# (page 82), whose initializer is __init__(self, data=0, next_node=None).
#
# Annotations such as `data: int` declare field types for readers and
# tools; Python does NOT check them at run time. The annotation of `next`
# is written as a string ("ListNode | None") because the name ListNode does
# not exist yet while its own class body is being executed. `X | None`
# means "an X or None"; None marks the end of a list.
@dataclass
class ListNode:
    data: int
    next: "ListNode | None" = None


# The annotations `ListNode | None` in this signature are evaluated when the
# function is defined; the `|` syntax between types needs Python 3.10+.
# They document that either argument may be None (an empty list).
def merge_sorted_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """Merge two sorted singly linked lists by relinking existing nodes.

    This is the textbook's merge_two_sorted_lists(L1, L2) program
    (page 84). No new data nodes are created; only `next` fields change.
    """

    # Placeholder node for the result (the book's "dummy head"). `tail`
    # always points at the last node of the merged prefix built so far.
    dummy = ListNode(0)
    tail = dummy
    while l1 is not None and l2 is not None:

        # Tuple assignment: the right-hand side (l1, l1.next) is evaluated
        # completely before anything is assigned, so tail.next receives the
        # current front node and l1 then advances to that node's successor.
        # Using `<=` takes the l1 node first on equal keys.
        if l1.data <= l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next

    # Appends the remaining nodes of l1 or l2 (at most one is non-empty).
    # `A if condition else B` is a conditional expression: it evaluates to
    # A when the condition is true, otherwise to B.
    tail.next = l1 if l1 is not None else l2
    return dummy.next


def merge_two_sorted_lists(a: list[int], b: list[int]) -> list[int]:
    """Convenient runnable demonstration of the linked-node algorithm.

    Helper added in this repository (not in the book): builds linked lists
    from Python lists, calls merge_sorted_lists(), and returns the merged
    keys as a Python list. `list[int]` is a type hint meaning "a list of
    ints" (not enforced at run time).
    """

    # A nested function: build() is defined inside this function and is
    # visible only here.
    def build(values):
        first = None

        # reversed(sequence) yields the items from last to first without
        # copying the list. Building from the back lets each new node point
        # at the previously built one, so the final `first` is the head.
        for value in reversed(values):
            first = ListNode(value, first)
        return first
    current = merge_sorted_lists(build(a), build(b))
    result = []
    while current is not None:
        result.append(current.data)
        current = current.next
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 85)
# -------------------------------------------
# The worst case for running time is when the two lists have comparable
# lengths, giving O(n + m) time. In the best case one list is much shorter
# than the other and all its entries come at the start of the merged list,
# so the loop stops early and the rest is attached in one step.
#
# Because the existing nodes are reused, the extra space is O(1).
#
# VARIANTS
# --------
# - Solve the same problem when the lists are doubly linked.
#   (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Node class: book (page 82) defines `class ListNode` with an explicit
#   `__init__(self, data=0, next_node=None)`; file uses a @dataclass with
#   fields `data: int` (no default) and `next: "ListNode | None" = None`.
#   Consequently the book's `ListNode()` call becomes `ListNode(0)` here.
# - Function name: book `merge_two_sorted_lists(L1, L2)`; file
#   `merge_sorted_lists(l1, l2)` with lower-case parameter names and type
#   hints added. The name merge_two_sorted_lists is used in the file for a
#   different, added helper that takes and returns Python lists.
# - Book names the placeholder `dummy_head` and initializes with chained
#   assignment `dummy_head = tail = ListNode()`; file uses `dummy` and two
#   separate statements.
# - Loop condition: book `while L1 and L2:`; file `while l1 is not None and
#   l2 is not None:` (same effect for node objects).
# - Comparison: book `if L1.data < L2.data:` (ties taken from L2); file
#   `if l1.data <= l2.data:` (ties taken from l1). The merged keys are the
#   same, but the order of equal-keyed nodes differs.
# - Remainder: book `tail.next = L1 or L2`; file uses the conditional
#   expression `l1 if l1 is not None else l2`.
# - Helper merge_two_sorted_lists (with nested build) is not in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases; pytest has the full set.
    # The examples show interleaved lists, an empty input list, and
    # duplicate keys. `assert` stops the program with an AssertionError if
    # a result differs from the expected value (a quick smoke check).
    result=merge_two_sorted_lists([1, 3, 5], [2, 4, 6])
    print('merge_two_sorted_lists', result)
    assert result == [1, 2, 3, 4, 5, 6]
    result=merge_two_sorted_lists([], [1])
    print('merge_two_sorted_lists', result)
    assert result == [1]
    result=merge_two_sorted_lists([1, 1], [1, 2])
    print('merge_two_sorted_lists', result)
    assert result == [1, 1, 1, 2]
