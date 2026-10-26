"""EPI Python — Exercise 7.11: Test Whether a Singly Linked List Is Palindromic

Chapter 7: Linked Lists
Textbook: pages 94–95 (printed page numbers; problem, solution, program and
complexity on 94, variant on 95).

PROBLEM (from the textbook)
---------------------------
"It is straightforward to check whether the sequence stored in an array is
a palindrome. However, if this sequence is stored as a singly linked list,
the problem of detecting palindromicity becomes more challenging. See
Figure 7.1 on Page 82 for an example of a palindromic singly linked list."

"Write a program that tests whether a singly linked list is palindromic."

(Figure 7.1 shows L = 2 -> 3 -> 5 -> 3 -> 2.)

HINT (from the textbook)
------------------------
"It's easy if you can traverse the list forwards and backwards
simultaneously."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: compare the first and last nodes, then the second and
second-to-last, and so on. O(n^2) time for n nodes, O(1) space.

The O(n^2) cost comes from repeatedly walking the list to find the last,
second-to-last, ... node, while getting the first node is O(1). This
suggests paying a one-time O(n) cost to reverse the second half of the
list; then palindromicity reduces to checking that the first half and the
reversed second half are equal, node by node. This modifies the list that
was passed in, but the reversed part can be reversed again to restore the
original list.

The book's program finds the second half with a slow/fast iterator pair
(fast moves two nodes per step), reverses it with reverse_linked_list()
(the list-reversal routine from the variant of Exercise 7.2), and compares
the two halves.

Implementation in this file: is_linked_list_a_palindrome() is the textbook
algorithm, with its own nested reverse() helper and with the restoring
second reversal that the book mentions but does not code. build_nodes(),
node_values() and palindrome_values() are helpers added in this
repository (not in the book).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 2, 1]        -> True
    [1, 2, 3]        -> False
    [2, 3, 5, 3, 2]  -> True    (the list of Figure 7.1)
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


def is_linked_list_a_palindrome(head: ListNode | None) -> bool:
    """Compare first half to reversed second half; restore original links.

    This is the textbook's is_linked_list_a_palindrome(L) program
    (page 94), extended with the restoring reversal the book describes.
    """

    # Nested helper: reverse the chain starting at `node` in place and
    # return the new first node. (The book calls a separate
    # reverse_linked_list() function that it does not print here.)
    def reverse(node):
        previous = None
        while node is not None:

            # Multiple assignment: the right side (previous, node.next,
            # node) is evaluated first; then targets are assigned left to
            # right. So node.next is set (on the current node) before
            # `node` is moved on, and `previous` gets the old node.
            node.next, node, previous = previous, node.next, node
        return previous

    # Finds the second half of the list: when fast reaches the end, slow
    # is at the middle (for odd length, the exact middle node).
    slow = fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    # Compares the first half and the reversed second half. The first half
    # still links into the (now last) middle node, so the loop is driven by
    # `second`, which ends first.
    second_half = reverse(slow)
    first, second = head, second_half
    answer = True
    while second is not None:
        if first.data != second.data:
            answer = False

            # `break` leaves the loop at once; the list is still restored
            # below before returning.
            break
        first, second = first.next, second.next

    # Reverse the second half again so the caller's list is unchanged.
    reverse(second_half)
    return answer


def palindrome_values(values: list[int]) -> bool:
    """Helper added in this repository (not in the book).

    Builds a linked list from `values` and tests it for palindromicity.
    """
    return is_linked_list_a_palindrome(build_nodes(values))


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 94–95)
# -----------------------------------------------
# The time complexity is O(n). The space complexity is O(1).
#
# VARIANTS
# --------
# - Solve the same problem when the list is doubly linked and you have
#   pointers to the head and the tail.
#   (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Function name `is_linked_list_a_palindrome` matches; book parameter
#   `L`, file `head` with type hints.
# - Reversal: book calls an external `reverse_linked_list(slow)` (not
#   printed in this exercise); file defines a nested `reverse(node)`.
# - Midpoint loop: book `while fast and fast.next:` with tuple assignment
#   `fast, slow = fast.next.next, slow.next`; file uses `is not None`
#   tests and two separate statements.
# - Comparison: book loops `while second_half_iter and first_half_iter:`
#   and returns False immediately on a mismatch, returning True at the
#   end; file loops `while second is not None:`, sets `answer = False` and
#   `break`s, then reverses the second half again to restore the input
#   before returning `answer`. The book only mentions that restoring is
#   possible; it does not do it.
# - Names: book `first_half_iter`, `second_half_iter`; file `first`,
#   `second`, `second_half`.
# - Node class: file imports the @dataclass ListNode from
#   pg_084_merge_two_sorted_lists instead of the book's class (page 82).
# - build_nodes, node_values and palindrome_values are helpers not in the
#   book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Loop over a tuple of two example lists: a palindrome (prints True)
    # and a non-palindrome (prints False). This block prints results only;
    # it has no assert statements.
    for values in ([1, 2, 1], [1, 2, 3]):
        print("linked palindrome:", values, palindrome_values(values))
