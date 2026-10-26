"""EPI Python — Exercise 7.10: Implement Even-Odd Merge

Chapter 7: Linked Lists
Textbook: pages 93–94 (printed page numbers; problem, Figure 7.10, hint and
solution on 93, program and complexity on 94).

PROBLEM (from the textbook)
---------------------------
"Consider a singly linked list whose nodes are numbered starting at 0.
Define the even-odd merge of the list to be the list consisting of the
even-numbered nodes followed by the odd-numbered nodes. The even-odd merge
is illustrated in Figure 7.10."

"Write a program that computes the even-odd merge."

Example (Figure 7.10): L = l0 -> l1 -> l2 -> l3 -> l4 becomes
L = l0 -> l2 -> l4 -> l1 -> l3. The node addresses in the figure show that
no new nodes have been allocated.

HINT (from the textbook)
------------------------
"Use temporary additional storage."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: allocate new nodes to build two new lists, one with the
even-numbered nodes and one with the odd-numbered nodes, and concatenate
the first with the second. Time and space are both O(n).

The extra space can be avoided by reusing the existing nodes: iterate
through the list, appending even-numbered nodes to one list and
odd-numbered nodes to another, with an indicator variable saying which
list to append to next. Finally append the odd list to the end of the
even list. (The book's program uses two dummy heads and a two-element
list of tails indexed by the indicator.)

Implementation in this file: even_odd_merge() produces the same even-odd
merge in place with O(1) extra space, but by a different method from the
book's printed program (see TEXTBOOK CODE COMPARISON). build_nodes(),
node_values() and even_odd_merge_values() are helpers added in this
repository (not in the book).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [0, 1, 2, 3, 4]  -> [0, 2, 4, 1, 3]   (matches Figure 7.10's pattern)
    [0, 1, 2, 3]     -> [0, 2, 1, 3]
    [7]              -> [7]
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


def even_odd_merge(head: ListNode | None) -> ListNode | None:
    """Group nodes at positions 0,2,4,... before 1,3,5,... stably.

    Corresponds to the textbook's even_odd_merge(L) (page 94), but uses a
    different relinking method from the book's listing: two pointers that
    each skip over the other parity's node, instead of dummy heads and an
    alternating tails list.
    """
    if head is None:
        return None

    # Tuple assignment: `even` starts at node 0 and `odd` at node 1 (or
    # None for a one-node list). Remember the first odd node so the odd
    # chain can be attached after the last even node at the end.
    even, odd = head, head.next
    odd_head = odd

    # Each pass links the current even node to the next even node (the
    # node after `odd`) and the current odd node to the next odd node.
    # Stop when there is no further node to move.
    while odd is not None and odd.next is not None:
        even.next = odd.next
        even = even.next
        odd.next = even.next
        odd = odd.next

    # Append the odd chain after the last even node.
    even.next = odd_head
    return head


def even_odd_merge_values(values: list[int]) -> list[int]:
    """Helper added in this repository (not in the book).

    Builds a linked list from `values`, applies even_odd_merge(), and
    returns the result as a Python list.
    """
    return node_values(even_odd_merge(build_nodes(values)))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 94)
# -------------------------------------------
# The time complexity is O(n) and the space complexity is O(1).
#
# VARIANTS
# --------
# None printed for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Function name `even_odd_merge` matches; book parameter `L`, file
#   `head` with type hints.
# - Empty list: book `if not L: return L`; file `if head is None: return
#   None` (same result).
# - DIFFERENT METHOD: the book creates two dummy heads
#   (`even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)`), keeps
#   `tails = [even_dummy_head, odd_dummy_head]` and `turn = 0`, and for
#   each node appends it to `tails[turn]` and flips `turn ^= 1`
#   ("Alternate between even and odd"); it then sets `tails[1].next =
#   None`, `tails[0].next = odd_dummy_head.next` and returns
#   `even_dummy_head.next`. The file instead uses two pointers `even` and
#   `odd`, saves `odd_head`, relinks with `even.next = odd.next` /
#   `odd.next = even.next` while `odd` and `odd.next` exist, and finally
#   sets `even.next = odd_head`. No dummy nodes, tails list or XOR
#   indicator. Same output and same O(n) / O(1) bounds.
# - Node class: file imports the @dataclass ListNode from
#   pg_084_merge_two_sorted_lists instead of the book's class (page 82).
# - build_nodes, node_values and even_odd_merge_values are helpers not in
#   the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Positions 0, 2, 4 come first, then 1, 3 (as in Figure 7.10).
    # `assert` raises AssertionError if the result is different from the
    # expected value.
    print("even/odd merge:", even_odd_merge_values([0, 1, 2, 3, 4]))
    assert even_odd_merge_values([0, 1, 2, 3, 4]) == [0, 2, 4, 1, 3]
