"""EPI Python — Exercise 7.12: Implement List Pivoting

Chapter 7: Linked Lists
Textbook: pages 95–96 (printed page numbers; problem, hint, solution and
start of the program on 95, end of the program and complexity on 96).

PROBLEM (from the textbook)
---------------------------
"For any integer k, the pivot of a list of integers with respect to k is
that list with its nodes reordered so that all nodes containing keys less
than k appear before nodes containing k, and all nodes containing keys
greater than k appear after the nodes containing k. See Figure 7.11 for an
example of pivoting."

"Implement a function which takes as input a singly linked list and an
integer k and performs a pivot of the list with respect to k. The relative
ordering of nodes that appear before k, and after k, must remain
unchanged; the same must hold for nodes holding keys equal to k."

Example (Figure 7.11): L = 3 -> 2 -> 2 -> 11 -> 7 -> 5 -> 11 pivoted with
k = 7 gives L = 3 -> 2 -> 2 -> 5 -> 7 -> 11 -> 11 (same node objects, per
the addresses in the figure).

HINT (from the textbook)
------------------------
"Form the three regions independently."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: iterate through the list, writing each value into one of
three new lists according to whether it is less than, equal to, or
greater than k. Then traverse the original list from the head and
overwrite its values with those of the less-than, then equal, then
greater-than lists. O(n) time and O(n) space for n nodes.

Key observation: no new nodes are needed for the three lists. Instead,
the original nodes are redistributed into three lists in one traversal of
the original list. Because the traversal is in order, each of the three
lists keeps its nodes' original relative order. The final step joins the
three lists. (The book's program uses a dummy head and an iterator for
each of the three lists.)

Implementation in this file: list_pivot() is the textbook algorithm,
written with lists of three dummy heads and three tails (see TEXTBOOK CODE
COMPARISON). build_nodes(), node_values() and list_pivot_values() are
helpers added in this repository (not in the book).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [3, 2, 2, 5, 1, 2], pivot 2 -> [1, 2, 2, 2, 3, 5]
    [3, 2, 2, 11, 7, 5, 11], pivot 7 -> [3, 2, 2, 5, 7, 11, 11]
        (the list of Figure 7.11)
"""

# Repository import (not the standard library): reuse the ListNode
# dataclass defined in this chapter's Exercise 7.1 module.
# Python import system: https://docs.python.org/3/reference/import.html
# `from ... import` statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_07_linked_lists.pg_084_merge_two_sorted_lists import ListNode


# Type hints such as `list[int]` and `ListNode | None` ("a node or None")
# document intended types; Python does not enforce them. The `|` form
# between types needs Python 3.10+.
def build_nodes(values: list[int]) -> ListNode | None:
    """Construct nodes in input order for the standalone examples and tests.

    Helper added in this repository (not in the book).
    """
    head = None

    # reversed(sequence) yields items from last to first without copying,
    # so prepending leaves `head` at values[0].
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


def list_pivot(head: ListNode | None, pivot: int) -> ListNode | None:
    """Stable three-way partition around pivot without allocating list nodes.

    This is the textbook's list_pivoting(L, x) program (pages 95–96). Only
    three placeholder (dummy) nodes are created; the data nodes are reused.
    """

    # Three dummy heads: index 0 for keys < pivot, 1 for keys == pivot,
    # 2 for keys > pivot. `dummy[:]` is a slice of the whole list, i.e. a
    # new list object holding the same three nodes, so `tail` can be
    # changed later without changing `dummy`.
    dummy = [ListNode(0), ListNode(0), ListNode(0)]
    tail = dummy[:]

    # Populates the three lists.
    while head is not None:

        # Save the successor, then detach the node so the last node of each
        # region never keeps a stale link into the old list.
        following = head.next
        head.next = None

        # Nested conditional expressions (`A if cond else B`) choose the
        # region index: 0 if less, otherwise 1 if equal, otherwise 2.
        index = 0 if head.data < pivot else (1 if head.data == pivot else 2)
        tail[index].next = head
        tail[index] = head
        head = following

    # Combines the three lists. The less-than region is followed by the
    # equal region if it has any node, otherwise directly by the
    # greater-than region. A node object is truthy and None is falsy, so
    # `if dummy[1].next` asks "is the equal region non-empty?".
    tail[0].next = dummy[1].next if dummy[1].next else dummy[2].next
    tail[1].next = dummy[2].next
    return dummy[0].next


def list_pivot_values(values: list[int], pivot: int) -> list[int]:
    """Helper added in this repository (not in the book).

    Builds a linked list from `values`, pivots it, and returns the result
    as a Python list.
    """
    return node_values(list_pivot(build_nodes(values), pivot))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 96)
# -------------------------------------------
# Building the three lists takes O(n) time and joining them takes O(1)
# time, so the overall time complexity is O(n). The space complexity is
# O(1).
#
# VARIANTS
# --------
# None printed for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Function: book `list_pivoting(L, x)`; file `list_pivot(head, pivot)`
#   with type hints.
# - Book uses six named variables, `less_head = less_iter = ListNode()`,
#   `equal_head = equal_iter = ListNode()`, `greater_head = greater_iter =
#   ListNode()`, and an if / elif / else chain appending to the matching
#   iterator. The file stores the three dummy heads in a list `dummy` and
#   the three tails in a list `tail`, and picks the index with a nested
#   conditional expression.
# - File detaches each node (`head.next = None`, saving `following`
#   first); the book does not detach and instead sets
#   `greater_iter.next = None` once at the end.
# - Joining: book `equal_iter.next = greater_head.next` then
#   `less_iter.next = equal_head.next` (works even when the equal list is
#   empty, because equal_iter is then the equal dummy head). File
#   `tail[0].next = dummy[1].next if dummy[1].next else dummy[2].next` and
#   `tail[1].next = dummy[2].next`.
# - Book `ListNode()` (data defaults to 0) is `ListNode(0)` in the file.
# - Node class: file imports the @dataclass ListNode from
#   pg_084_merge_two_sorted_lists instead of the book's class (page 82).
# - build_nodes, node_values and list_pivot_values are helpers not in the
#   book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Pivot around 2: the 1 comes first, then the three 2s in their
    # original order, then 3 and 5 in their original order. `assert`
    # raises AssertionError if the result is different from the expected
    # value.
    print("pivot:", list_pivot_values([3, 2, 2, 5, 1, 2], 2))
    assert list_pivot_values([3, 2, 2, 5, 1, 2], 2) == [1, 2, 2, 2, 3, 5]
