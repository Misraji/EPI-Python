"""EPI Python — Exercise 7.13: Add List-Based Integers

Chapter 7: Linked Lists
Textbook: page 96 (printed page number; problem, solution, program,
complexity and variant all on 96).

PROBLEM (from the textbook)
---------------------------
"A singly linked list whose nodes contain digits can be viewed as an
integer, with the least significant digit coming first. Such a
representation can be used to represent unbounded integers. This problem
is concerned with adding integers represented in this fashion. See Figure
7.12 for an example."

"Write a program which takes two singly linked lists of digits, and
returns the list corresponding to the sum of the integers they represent.
The least significant digit comes first."

Example (Figure 7.12, "List-based interpretation of 413 + 907 = 1320"):
L1 = 3 -> 1 -> 4 and L2 = 7 -> 0 -> 9 give the sum L = 0 -> 2 -> 3 -> 1.

HINT (from the textbook)
------------------------
"First, solve the problem assuming no pair of corresponding digits sum to
more than 9."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Converting the lists to integers is not an option in general, because a
machine integer has a fixed word length while the lists can be arbitrarily
long.

Instead, imitate grade-school addition: add the digits in corresponding
nodes of the two lists, digit position by digit position. The subtle part
is the carry-out from each position. The algorithm keeps going until both
lists are used up AND no carry remains (so a final carry produces one more
digit, as in 413 + 907 = 1320).

Implementation in this file: add_two_numbers() is the textbook program.
build_nodes(), node_values() and add_list_based_integers() are helpers
added in this repository (not in the book).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [3, 1, 4] + [7, 0, 9]  -> [0, 2, 3, 1]   (Figure 7.12: 413 + 907)
    [9, 9]    + [1]        -> [0, 0, 1]      (99 + 1 = 100; final carry)
    []        + [5]        -> [5]            (empty list stands for 0)
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


def add_two_numbers(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    """Add digits in least-significant-digit-first order, handling arbitrary length.

    This is the textbook's add_two_numbers(L1, L2) program (page 96). The
    input lists are not modified; new nodes are created for the result.
    """

    # Placeholder head for the result (book: dummy_head); `tail` is the
    # last result node so far (book: place_iter).
    dummy = ListNode(0)
    tail = dummy
    carry = 0

    # Continue while either list has digits left or a carry remains.
    # `carry` alone in the condition is truthy when nonzero.
    while a is not None or b is not None or carry:

        # An exhausted list contributes 0 for this digit position.
        total = carry
        if a is not None:
            total += a.data
            a = a.next
        if b is not None:
            total += b.data
            b = b.next

        # divmod(x, y) returns the pair (x // y, x % y) in one call. Here,
        # total // 10 is the carry into the next position (0 or 1) and
        # total % 10 is the digit written at this position.
        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next


def add_list_based_integers(a: list[int], b: list[int]) -> list[int]:
    """Helper added in this repository (not in the book).

    Builds linked lists from two digit lists (least significant digit
    first), adds them, and returns the sum's digits as a Python list.
    """
    return node_values(add_two_numbers(build_nodes(a), build_nodes(b)))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 96)
# -------------------------------------------
# The time complexity is O(n + m) and the space complexity is
# O(max(n, m)), where n and m are the lengths of the two lists (the result
# list has at most max(n, m) + 1 nodes).
#
# VARIANTS
# --------
# - Solve the same problem when integers are represented as lists of
#   digits with the most significant digit coming first.
#   (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Function name `add_two_numbers` matches; book parameters `L1, L2`,
#   file `a, b` with type hints.
# - Book: `place_iter = dummy_head = ListNode()`; file: `dummy =
#   ListNode(0)` and `tail = dummy` (separate statements, new names).
# - Loop condition: book `while L1 or L2 or carry:`; file uses
#   `is not None` tests for the lists.
# - Digit sum: book computes `val = carry + (L1.data if L1 else 0) +
#   (L2.data if L2 else 0)` with conditional expressions and advances with
#   `L1 = L1.next if L1 else None`; file uses `total` and two if-blocks.
# - Book appends `ListNode(val % 10)` and then
#   `carry, place_iter = val // 10, place_iter.next`; file computes
#   `carry, digit = divmod(total, 10)` and advances `tail` separately.
# - Node class: file imports the @dataclass ListNode from
#   pg_084_merge_two_sorted_lists instead of the book's class (page 82).
# - build_nodes, node_values and add_list_based_integers are helpers not
#   in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The book's Figure 7.12 example: 413 + 907 = 1320, written least
    # significant digit first. `assert` raises AssertionError if the
    # result is different from the expected value.
    print("reverse-digit sum:", add_list_based_integers([3, 1, 4], [7, 0, 9]))
    assert add_list_based_integers([3, 1, 4], [7, 0, 9]) == [0, 2, 3, 1]
