"""EPI Python — Exercise 7.9: Implement Cyclic Right Shift for Singly Linked Lists

Chapter 7: Linked Lists
Textbook: pages 92–93 (printed page numbers; problem, hint, solution and
start of the program on 92, rest of the program and complexity on 93).

PROBLEM (from the textbook)
---------------------------
"This problem is concerned with performing a cyclic right shift on a
list."

"Write a program that takes as input a singly linked list and a
nonnegative integer k, and returns the list cyclically shifted to the
right by k. See Figure 7.9 for an example of a cyclic right shift."

Example (Figure 7.9): applying a right cyclic shift by 3 to the list of
Figure 7.1, L = 2 -> 3 -> 5 -> 3 -> 2, gives L = 5 -> 3 -> 2 -> 2 -> 3.
The caption notes that no new nodes have been allocated.

HINT (from the textbook)
------------------------
"How does this problem differ from rotating an array?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: shift right by one node, k times. Each single shift finds the
tail and its predecessor, moves the tail in front of the current head, and
sets the predecessor's next to null so it becomes the new tail. That takes
O(kn) time and O(1) space for n nodes.

Improvement: k may exceed n; shifting by k is then the same as shifting by
k mod n, so assume k < n. Linked lists can be cut and reassembled cheaply:

1. Find the tail node t (counting n along the way).
2. Since the tail's successor should be the original head, set t's next
   field to the head; the list is temporarily a ring.
3. The original head is to become the kth node from the start of the new
   list; the book concludes that the new head is the (n - k)th node of the
   original list. The program walks n - k steps starting from the old
   tail to reach the new tail; the node after it is the new head.
4. Break the ring after the new tail.

Implementation in this file: cyclic_right_shift() is the textbook program
(with an argument check added). build_nodes(), node_values() and
cyclic_shift_values() are helpers added in this repository (not in the
book).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 2, 3, 4], k=1   -> [4, 1, 2, 3]
    [1, 2, 3, 4], k=4   -> [1, 2, 3, 4]   (k mod n == 0: unchanged)
    [1, 2, 3, 4], k=5   -> [4, 1, 2, 3]   (same as k=1)
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


def cyclic_right_shift(head: ListNode | None, k: int) -> ListNode | None:
    """Rotate nodes k steps toward the head by relinking the last k nodes.

    In other words: the last k nodes (k taken mod n) move, in order, to the
    front of the list. This is the textbook's
    cyclically_right_shift_list(L, k) program (pages 92–93). It raises
    ValueError for negative k (a check the book does not have).
    """
    if k < 0:
        raise ValueError("Shift must be nonnegative")
    if head is None:
        return None

    # Computes the length of the list and its tail. Tuple assignment sets
    # both names at once.
    tail, length = head, 1
    while tail.next:
        tail = tail.next
        length += 1

    # `k %= length` is short for `k = k % length`. For a positive length,
    # Python's % gives a result in range(0, length), so a shift by k equals
    # a shift by k mod n.
    k %= length

    # `not k` is True when k == 0 (zero is falsy): nothing to shift.
    if not k:
        return head

    # Makes a cycle by connecting the tail to the head.
    tail.next = head

    # Walk n - k steps from the old tail to reach the new tail.
    steps = length - k
    new_tail = tail
    for _ in range(steps):
        new_tail = new_tail.next

    # The node after the new tail is the new head; break the ring.
    new_head = new_tail.next
    new_tail.next = None
    return new_head


def cyclic_shift_values(values: list[int], k: int) -> list[int]:
    """Helper added in this repository (not in the book).

    Builds a linked list from `values`, shifts it right by k, and returns
    the result as a Python list.
    """
    return node_values(cyclic_right_shift(build_nodes(values), k))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 93)
# -------------------------------------------
# The time complexity is O(n), and the space complexity is O(1).
#
# VARIANTS
# --------
# None printed for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Function: book `cyclically_right_shift_list(L, k)`; file
#   `cyclic_right_shift(head, k)` with type hints.
# - File adds a ValueError for k < 0 (the book's problem states k is
#   nonnegative and has no check).
# - Empty list: book `if not L: return L`; file
#   `if head is None: return None` (same result).
# - Length: book names it `n`; file `length`. Book increments before
#   moving (`n += 1` then `tail = tail.next`); file moves first (same
#   result).
# - Zero shift: book `if k == 0`; file `if not k`.
# - Walk to new tail: book uses tuple assignment
#   `steps_to_new_head, new_tail = n - k, tail` and a
#   `while steps_to_new_head:` countdown; file uses `steps = length - k`,
#   `new_tail = tail`, and `for _ in range(steps)`.
# - Node class: file imports the @dataclass ListNode from
#   pg_084_merge_two_sorted_lists instead of the book's class (page 82).
# - build_nodes, node_values and cyclic_shift_values are helpers not in
#   the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Shift 1 -> 2 -> 3 -> 4 right by one: the last node moves to the
    # front. `assert` raises AssertionError if the result is different
    # from the expected value.
    print("cyclic shift:", cyclic_shift_values([1, 2, 3, 4], 1))
    assert cyclic_shift_values([1, 2, 3, 4], 1) == [4, 1, 2, 3]
