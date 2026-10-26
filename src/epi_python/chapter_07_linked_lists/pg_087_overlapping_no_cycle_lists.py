"""EPI Python — Exercise 7.4: Test for Overlapping Lists—Lists Are Cycle-Free

Chapter 7: Linked Lists
Textbook: pages 87–88 (printed page numbers; problem and start of the
solution on 87, Figure 7.6, program and complexity on 88).

PROBLEM (from the textbook)
---------------------------
"Given two singly linked lists there may be list nodes that are common to
both. (This may not be a bug—it may be desirable from the perspective of
reducing memory footprint, as in the flyweight pattern, or maintaining a
canonical form.) For example, the lists in Figure 7.6 on the following
page overlap at Node I."

"Write a program that takes two cycle-free singly linked lists, and
determines if there exists a node that is common to both lists."

Figure 7.6: L1 has two nodes of its own and L2 has one; L1's second node
links into L2's second node, I, after which the two lists share I and the
remaining nodes through the common tail.

HINT (from the textbook)
------------------------
"Solve the simple cases first."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force with a hash table: put every node of one list in a hash table,
then walk the other list and test each node for membership. O(n) time and
O(n) space, n being the total number of nodes.

Without extra space: two nested loops, the outer one going through the
first list and the inner one searching the second list for the current
node. This takes O(n^2) time.

Key observation: the lists overlap if and only if they end at the same
tail node, because once two lists meet at a node they cannot separate
again later (each node has only one next field). So merely deciding
whether there is overlap reduces to finding each list's tail.

To return the first overlapping node: compute both lengths, advance in the
longer list by the difference in lengths, then advance through both lists
in step, stopping at the first node they have in common. Reaching the end
of a list without finding a common node means no overlap.

Implementation in this file: overlapping_no_cycle_lists() is the
textbook algorithm. build_nodes(), node_values() and
overlapping_tail_first_value() are helpers added in this repository (not
in the book) for building examples and tests.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    prefixes [1, 2] and [3], shared tail [7, 8]
        L1: 1 -> 2 -> 7 -> 8      L2: 3 -> 7 -> 8
        first common node holds 7 (the same node object in both lists)

"Common" means the very same node object (identity), not merely a node
holding an equal value.
"""

# Repository import (not the standard library): reuse the ListNode
# dataclass defined in this chapter's Exercise 7.1 module, so these lists
# are made of the same kind of node as the other exercises.
# Python import system: https://docs.python.org/3/reference/import.html
# `from ... import` statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_07_linked_lists.pg_084_merge_two_sorted_lists import ListNode


# Type hints such as `list[int]` ("list of ints") and `ListNode | None`
# ("a node or None") document intended types; Python does not enforce
# them. The `|` form between types needs Python 3.10+.
def build_nodes(values: list[int]) -> ListNode | None:
    """Construct nodes in input order for the standalone examples and tests.

    Helper added in this repository (not in the book).
    """
    head = None

    # reversed(sequence) yields items from last to first without copying.
    # Prepending in that order leaves `head` at values[0].
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def node_values(head: ListNode | None) -> list[int]:
    """Read an acyclic chain into a convenient Python list.

    Helper added in this repository (not in the book).
    """
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result


def overlapping_no_cycle_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    """Find the first shared node by object identity in two acyclic lists.

    This is the textbook's overlapping_no_cycle_lists(L1, L2) program
    (page 88). Returns None when the lists do not overlap.
    """

    # Nested helper (as in the book): count nodes until the end. `while
    # head:` relies on truthiness: None is falsy, and a ListNode object is
    # truthy because it defines neither __bool__ nor __len__.
    def length(head):
        result = 0
        while head:
            result += 1
            head = head.next
        return result

    # Tuple assignment computes both lengths in one statement.
    length_a, length_b = length(a), length(b)

    # Swap so that `b` is the longer list. `a, b = b, a` exchanges two
    # names without a temporary: the right side is built first.
    if length_a > length_b:
        a, b = b, a
        length_a, length_b = length_b, length_a

    # Advances the longer list to get equal-length remainders.
    for _ in range(length_b - length_a):
        b = b.next

    # `is not` compares identity. Because the remaining lengths are now
    # equal, the two pointers either meet at the first shared node or both
    # become None together (meaning no overlap; None is returned).
    while a is not b:
        a = a.next
        b = b.next
    return a


def overlapping_tail_first_value(a: list[int], b: list[int], tail: list[int]) -> int | None:
    """Build two lists with a physically shared tail for demonstration.

    Helper added in this repository (not in the book). Returns the data in
    the first overlapping node, or None. `int | None` means "an int or
    None".
    """
    common = build_nodes(tail)

    # Nested function: it can read `common` from the enclosing function
    # (a closure). It appends the shared tail after the given prefix.
    def with_tail(prefix):
        if not prefix:
            return common
        head = build_nodes(prefix)
        node = head
        while node.next:
            node = node.next
        node.next = common
        return head
    match = overlapping_no_cycle_lists(with_tail(a), with_tail(b))

    # Conditional expression `A if condition else B`.
    return None if match is None else match.data


# TEXTBOOK POST-SOLUTION DISCUSSION (page 88)
# -------------------------------------------
# Time complexity O(n) (each list is walked a constant number of times),
# and space complexity O(1).
#
# VARIANTS
# --------
# None printed for this exercise. (Exercise 7.5, which follows, extends the
# problem to lists that may have cycles.)


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Node class: book uses the chapter's `class ListNode` (page 82); file
#   imports the @dataclass ListNode from pg_084_merge_two_sorted_lists.
# - Function: book `overlapping_no_cycle_lists(L1, L2)`; file same name,
#   parameters renamed `a`, `b`, with type hints. Nested length(L) helper
#   matches (parameter `head`, counter `result` instead of `length`).
#   Book lengths are `L1_len, L2_len`; file `length_a, length_b`.
# - Swap: book swaps only the lists (`L1, L2 = L2, L1`) and then advances
#   `abs(L1_len - L2_len)` steps; file swaps the lists AND the lengths and
#   advances `length_b - length_a` steps (no abs()).
# - Final loop: book `while L1 and L2 and L1 is not L2:` with tuple
#   assignment `L1, L2 = L1.next, L2.next`; file `while a is not b:` with
#   two separate assignments (equivalent here because the remainders have
#   equal length, so both reach None together).
# - build_nodes, node_values and overlapping_tail_first_value are helpers
#   not in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Lists 1 -> 2 -> 7 -> 8 and 3 -> 7 -> 8 share the tail nodes 7 -> 8,
    # so the first common node holds 7. `assert` raises AssertionError if
    # the result is different from the expected value.
    match = overlapping_tail_first_value([1, 2], [3], [7, 8])
    print("first overlapping value:", match)
    assert match == 7
