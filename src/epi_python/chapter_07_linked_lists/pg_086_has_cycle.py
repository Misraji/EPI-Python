"""EPI Python — Exercise 7.3: Test for Cyclicity

Chapter 7: Linked Lists
Textbook: pages 86–87 (printed page numbers; problem and solution start on
86, program continues and complexity and variant on 87). The ListNode
prototype used by the whole chapter is printed on page 82.

PROBLEM (from the textbook)
---------------------------
"Although a linked list is supposed to be a sequence of nodes ending in
null, it is possible to create a cycle in a linked list by making the next
field of an element reference to one of the earlier nodes."

"Write a program that takes the head of a singly linked list and returns
null if there does not exist a cycle, and the node at the start of the
cycle, if a cycle is present. (You do not know the length of the list in
advance.)"

HINT (from the textbook)
------------------------
"Consider using two iterators, one fast and one slow."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The book notes there are several solutions.

1. Hash table (if space is no concern): follow next fields from the head,
   recording every visited node in a hash table. A cycle exists exactly
   when a node already in the table is reached again; without a cycle the
   walk ends at the tail, whose next field is null. Needs O(n) space for
   n nodes.

2. Brute force with no extra storage and no modification of the list: an
   outer loop visits nodes one by one; for each, an inner loop walks from
   the head as many nodes as the outer loop has covered. If the outer
   loop's current node is met twice, there is a loop. If the outer loop
   reaches the end of the list, there is no cycle. O(n^2) time.

3. Linear time: use a slow iterator advancing one node per step and a fast
   iterator advancing two. There is a cycle exactly when they meet. The
   reasoning: if the fast iterator ever jumps over the slow one, the two
   will be equal on the following step.

Finding where the cycle starts, once a meeting shows a cycle exists:
first compute the cycle length C, which is easy because we already hold a
node on the cycle (walk around until returning to it). Then take two
iterators starting at the head, put one C nodes ahead of the other, and
advance them together; the node where they meet is the first node of the
cycle.

Implementations in this file:
  - has_cycle_nodes_via_cycle_length(): the book's main program (cycle
    length, then two aligned iterators).
  - has_cycle_nodes(): the shorter program that the book prints as a
    variant question (reset one pointer to the head after the meeting and
    advance both one step at a time). The book asks whether that program
    is correct and does not answer in this exercise.
  - has_cycle(): helper added in this repository (not in the book) that
    builds a chain from a Python list, optionally links the tail back to
    position cycle_start, and returns True/False.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []                       -> False  (empty list)
    [1, 2, 3]                -> False  (tail's next is None)
    [1, 2, 3], cycle_start=0 -> True   (tail links back to the head)
    [1, 2, 3], cycle_start=2 -> True   (tail links to itself)
    1 -> 2 -> 3 -> back to 2 : both node functions return the node 2
"""

# Python standard library: automatic generation of special methods for
# classes that mainly store data.
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` is a decorator that generates __init__(self, data, next=None),
# __repr__ and a field-by-field __eq__ from the annotated attributes. It
# replaces the book's hand-written ListNode (page 82: __init__(self,
# data=0, next_node=None)).
#
# Note: because the generated __eq__ compares fields, `==` between nodes
# compares their contents; that is why this file uses `is` (same object)
# when comparing iterators. With a cycle, __repr__ of a node would also
# recurse forever, so avoid printing nodes that are on a cycle.
#
# Annotations like `data: int` document types and are not enforced. The
# `next` annotation is a string because ListNode is not yet defined while
# its body runs; `X | None` means "an X or None".
@dataclass
class ListNode:
    data: int
    next: "ListNode | None" = None


# `ListNode | None` in the signature (evaluated at definition time; the `|`
# form needs Python 3.10+) documents "a node or None".
def has_cycle_nodes(head: ListNode | None) -> ListNode | None:
    """Return a cycle-entry node, or None, using Floyd's two-pointer method.

    This is the shorter program the book prints in the VARIANT of this
    exercise (page 87, also named has_cycle in the book), which the book
    presents as a question ("Is the program correct?").
    """

    # Chained assignment: both names refer to the same head node.
    slow=fast=head

    # Stop when fast reaches the end: then there is no cycle. Testing
    # `fast.next` too is needed because fast moves two nodes at a time.
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next

        # `is` tests object identity (the very same node), not equal data.
        # A meeting means there is a cycle.
        if slow is fast:

            # Tries to find the start of the cycle: one pointer restarts at
            # the head and both advance one step at a time until they meet.
            finder=head
            while finder is not slow:
                finder=finder.next
                slow=slow.next
            return finder
    return None


def has_cycle(values: list[int], cycle_start: int | None = None) -> bool:
    """Build an example chain with an optional backward pointer at its tail.

    Helper added in this repository (not in the book). `cycle_start` is a
    0-based index into `values`; None (the default) means no cycle. Returns
    True when has_cycle_nodes() finds a cycle. `int | None = None` is a
    type hint ("an int or None") with default None; hints are not enforced.
    """

    # List comprehension: creates one ListNode per value, in order.
    nodes=[ListNode(value) for value in values]

    # zip(a, b) yields pairs (a[0], b[0]), (a[1], b[1]), ... and stops at
    # the shorter input. Pairing `nodes` with the slice `nodes[1:]` (a copy
    # without the first element) gives every adjacent pair (node, successor),
    # which is linked here. With 0 or 1 nodes there are no pairs.
    for first, second in zip(nodes,nodes[1:]):
        first.next=second

    # nodes[-1] is the last element (negative indices count from the end).
    # An empty list is falsy, so `nodes and ...` skips the empty case.
    if nodes and cycle_start is not None:
        nodes[-1].next=nodes[cycle_start]

    # `A if condition else B` is a conditional expression; it passes None
    # (an empty list) when there are no nodes.
    return has_cycle_nodes(nodes[0] if nodes else None) is not None


def has_cycle_nodes_via_cycle_length(head: ListNode | None) -> ListNode | None:
    """First PDF listing: detect collision, compute cycle length, align pointers.

    This is the textbook's main has_cycle(head) program (pages 86–87). The
    book's nested helper cycle_len(end) is written inline here.
    """
    slow=fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow is fast:

            # Counts the cycle length C: walk from slow around the cycle
            # until arriving back at slow (book: nested cycle_len(end)).
            cycle_size=1
            current=slow.next
            while current is not slow:
                cycle_size+=1
                current=current.next

            # Finds the start of the cycle: move one iterator C nodes ahead
            # of the head (book: cycle_len_advanced_iter).
            advanced=head
            for _ in range(cycle_size):
                advanced=advanced.next

            # Both iterators advance in tandem; where they meet is the
            # start of the cycle (book: `it`).
            iterator=head
            while iterator is not advanced:
                iterator=iterator.next
                advanced=advanced.next
            return iterator

    # No cycle.
    return None


# TEXTBOOK POST-SOLUTION DISCUSSION (page 87)
# -------------------------------------------
# Let F be the number of nodes before the start of the cycle, C the number
# of nodes on the cycle, and n the total number of nodes. The time is
# O(F) + O(C) = O(n): O(F) for both pointers to reach the cycle, and O(C)
# for them to overlap once the slower one has entered the cycle.
# (Extra space is a constant number of iterators.)
#
# VARIANTS
# --------
# - The book prints a shorter program that claims to find the start of the
#   cycle without computing the cycle's length, and asks: is the program
#   correct? (The program: run slow/fast until they meet; then set slow to
#   the head and advance slow and fast one step at a time until they meet;
#   return slow.) It is implemented in this file as has_cycle_nodes().
#   (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Node class: book (page 82) `class ListNode` with
#   `__init__(self, data=0, next_node=None)`; file uses a @dataclass with
#   fields `data: int` and `next: "ListNode | None" = None`.
# - Main listing: book `has_cycle(head)` with a nested `cycle_len(end)`
#   function; file `has_cycle_nodes_via_cycle_length(head)` with the cycle
#   length loop written inline (counter `cycle_size`, iterator `current`).
#   Book names `cycle_len_advanced_iter` and `it` become `advanced` and
#   `iterator`.
# - Loop condition: book `while fast and fast.next and fast.next.next:`;
#   file `while fast is not None and fast.next is not None:` (one check
#   fewer). Book uses tuple assignment `slow, fast = slow.next,
#   fast.next.next`; file uses two separate statements.
# - Variant listing: book also names it `has_cycle(head)`; file
#   `has_cycle_nodes(head)`. Book reuses `slow = head` and advances
#   `slow, fast` together; file introduces a new `finder` at the head and
#   advances `finder` and `slow` (slow equals fast at that moment). Same
#   loop condition difference as above.
# - The file's `has_cycle(values, cycle_start=None)` is an added helper
#   returning bool; it is not the book's has_cycle (which returns a node).
# - Type hints added throughout.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases; pytest has the full set.
    # The first four calls cover an empty list, a list without a cycle, a
    # cycle back to the head, and a tail pointing at itself. `assert`
    # raises AssertionError if a result is not the expected value.
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

    # Build 1 -> 2 -> 3 -> back to 2 by hand with tuple assignment, then
    # check with `is` that both textbook programs return the node 2 itself.
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next, node2.next, node3.next = node2, node3, node2
    assert has_cycle_nodes_via_cycle_length(node1) is node2
    assert has_cycle_nodes(node1) is node2
