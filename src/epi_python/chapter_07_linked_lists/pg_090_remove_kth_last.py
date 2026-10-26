"""EPI Python — Exercise 7.7: Remove the kth Last Element from a List

Chapter 7: Linked Lists
Textbook: pages 90–91 (printed page numbers; problem on 90, hint,
solution, program and complexity on 91).

PROBLEM (from the textbook)
---------------------------
"Without knowing the length of a linked list, it is not trivial to delete
the kth last element in a singly linked list."

"Given a singly linked list and an integer k, write a program to remove
the kth last element from the list. Your algorithm cannot use more than a
few words of storage, regardless of the length of the list. In particular,
you cannot assume that it is possible to record the length of the list."

HINT (from the textbook)
------------------------
"If you know the length of the list, can you find the kth last node using
two iterators?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: one pass to compute the length, then a second pass to reach
and delete the right node. Its drawback is the two passes over the data,
which is slow when, for example, traversing the list involves disc
accesses.

Two-iterator approach: advance the first iterator k steps, then move both
iterators together. When the first iterator reaches the tail, the second
one is at the (k + 1)th last node, so the kth last node (its successor)
can be removed by changing one next field. A placeholder (dummy head) in
front of the list lets the same code remove the head itself.

Implementation in this file: remove_kth_last() is the textbook algorithm
(with argument checks added). build_nodes(), node_values() and
remove_kth_last_values() are helpers added in this repository (not in the
book).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 2, 3], k=2  -> [1, 3]   (the 2nd last element, 2, is removed)
    [1, 2, 3], k=3  -> [2, 3]   (the head is removed; dummy node helps)
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


def remove_kth_last(head: ListNode | None, k: int) -> ListNode | None:
    """Remove kth-to-last node using two pointers k steps apart (k starts at 1).

    This is the textbook's remove_kth_last(L, k) program (page 91). The
    book assumes L has at least k nodes; this version raises an exception
    instead when the assumption fails.
    """

    # `raise` stops the function with an exception. ValueError signals an
    # invalid argument value; IndexError (below) signals a position past
    # the end of a sequence.
    if k <= 0:
        raise ValueError("k must be positive")

    # Placeholder in front of the head, so removing the head itself (the
    # kth last when k equals the length) needs no special case.
    dummy = ListNode(0, head)
    lead = dummy

    # Move the leading iterator k nodes ahead of `follow`.
    for _ in range(k):
        lead = lead.next
        if lead is None:
            raise IndexError("k exceeds list length")
    follow = dummy

    # Advance both in tandem until `lead` is the tail. `follow` then
    # points to the (k + 1)th last node.
    while lead.next is not None:
        lead = lead.next
        follow = follow.next

    # Deletes the successor of `follow`, i.e. the kth last node.
    follow.next = follow.next.next
    return dummy.next


def remove_kth_last_values(values: list[int], k: int) -> list[int]:
    """Helper added in this repository (not in the book).

    Builds a linked list from `values`, removes the kth last node, and
    returns the remaining values as a Python list.
    """
    return node_values(remove_kth_last(build_nodes(values), k))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 91)
# -------------------------------------------
# The time is that of one list traversal, O(n) for a list of length n.
# The space is O(1), since only two iterators are used.
#
# Compared with the brute-force two-pass method: if k is small enough that
# the nodes between the two iterators can be kept in memory, while the
# whole list is too large to fit, the two-iterator approach halves the
# number of disc accesses.
#
# VARIANTS
# --------
# None printed for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Function: book `remove_kth_last(L, k)`; file same name with parameter
#   `head` and type hints.
# - File adds checks: ValueError when k <= 0 and IndexError when the list
#   has fewer than k nodes (book: comment "Assumes L has at least k
#   nodes").
# - Iterator names: book `first` / `second`; file `lead` / `follow`. Book
#   starts `first = dummy_head.next` and loops `while first:` (until first
#   is None); file starts `lead = dummy` and loops
#   `while lead.next is not None:`. Both loops run the same number of
#   times, leaving the trailing iterator at the (k + 1)th last node.
# - Book advances with tuple assignment `first, second = first.next,
#   second.next`; file uses two statements. Book's `dummy_head` is
#   `dummy` here.
# - Node class: file imports the @dataclass ListNode from
#   pg_084_merge_two_sorted_lists instead of the book's class (page 82).
# - build_nodes, node_values and remove_kth_last_values are helpers not
#   in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Remove the second-to-last element of 1 -> 2 -> 3. `assert` raises
    # AssertionError if the result is different from the expected value.
    print("remove second-to-last:", remove_kth_last_values([1, 2, 3], 2))
    assert remove_kth_last_values([1, 2, 3], 2) == [1, 3]
