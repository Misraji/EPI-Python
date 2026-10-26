"""EPI Python — Exercise 13.10: Implement a Fast Sorting Algorithm for Lists

Chapter 13: Sorting
Textbook: pages 194–195 (printed page numbers; problem and solution start on 194).

PROBLEM (from the textbook)
---------------------------
"Implement a routine which sorts lists efficiently. It should be a stable
sort, i.e., the relative positions of equal elements must remain
unchanged."

HINT (from the textbook)
------------------------
"In what respects are lists superior to arrays?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: repeatedly delete the smallest element of the list and append
it to a new list: O(n^2) time and O(n) additional space, n being the number
of nodes.

Refinement to O(1) space: reorder the existing nodes instead of creating new
ones. The book's `insertion_sort(L)` keeps a dummy head in front of the list
and maintains the invariant that the nodes up to and including the current
node are sorted in increasing order. When the next node is smaller than the
current one, it is unlinked and spliced in after the last predecessor
smaller than it (found by walking from the dummy head); otherwise the
current position simply advances. Its time is O(n^2), the worst case being
a list that starts out reverse-sorted; its space is O(1).

Faster: take intuition from arrays. Quicksort is the best all-round array
sort (O(n log n), in place) but is not stable. Mergesort on arrays is stable
and O(n log n) but not in place, since two sorted halves of an array cannot
be merged in place in linear time. Lists, unlike arrays, CAN be merged in
place, conceptually because inserting into the middle of a list is O(1).

So implement mergesort on lists:
1. Split the list into two equal-sized sublists around its middle node. Find
   the middle by advancing two iterators, one twice as fast as the other;
   when the fast one reaches the end, the slow one is at the middle.
2. Recursively sort both sublists.
3. Combine them with the merge of two sorted lists (Solution 7.1, page 84).

This file implements the mergesort as `stable_sort_list` (with the merge
written inline). The book's `insertion_sort` listing is not present.
`to_linked` and `to_list` are conversion helpers added in this file.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    4 -> 1 -> 3 -> 1 -> 2   sorts to   1 -> 1 -> 2 -> 3 -> 4
"""

# Python standard library: automatic generation of special methods for
# simple record-like classes.
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` generates `__init__` from the annotated fields, so
# `ListNode(5)` or `ListNode(5, other_node)` work (`next` defaults to None),
# plus a `__repr__` and an all-field `__eq__`.
# The annotation `'ListNode | None'` is written as a string because the
# class name is not yet defined while its own body runs; it means "a ListNode
# or None". Annotations are not enforced at run time.
@dataclass
class ListNode:
    data: int
    next: 'ListNode | None' = None


# Type hints: takes and returns the head of a list, or None for an empty
# list (`X | None` is union syntax, Python 3.10+).
def stable_sort_list(head: ListNode | None) -> ListNode | None:
    """Stable linked-list merge sort using tortoise/hare splitting.

    This is the textbook's mergesort implementation, with the merge step
    (Solution 7.1 in the book) written inline.
    """

    # Base cases: an empty list or a single node is already sorted.
    if head is None or head.next is None:
        return head

    # Find the midpoint with a slow and a fast pointer. Starting `fast` one
    # node ahead makes `slow` stop at the LAST node of the left half, so the
    # list can be cut right after it. The tuple assignment advances both
    # pointers in one statement (right side evaluated first).
    slow, fast = head, head.next
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next

    # Cut the list into two halves: [head .. slow] and [other .. end].
    other = slow.next
    slow.next = None

    # Recursively sort both halves.
    left = stable_sort_list(head)
    right = stable_sort_list(other)

    # Merge (the book calls merge_two_sorted_lists). `dummy = tail =
    # ListNode(0)` binds both names to one placeholder node; `tail` tracks
    # the end of the merged list and `dummy.next` will be its head.
    dummy = tail = ListNode(0)
    while left is not None and right is not None:

        # `<=` takes from the LEFT half on ties, so equal elements keep
        # their original relative order: this is what makes the sort stable.
        # Each tuple assignment links the chosen node and advances past it.
        if left.data <= right.data:
            tail.next, left = left, left.next
        else:
            tail.next, right = right, right.next
        tail = tail.next

    # Conditional expression `X if cond else Y`: attach whichever half still
    # has nodes (they are already sorted).
    tail.next = left if left is not None else right
    return dummy.next


def to_linked(values: list[int]) -> ListNode | None:
    # Helper added in this file (not in the textbook): build a linked list
    # from a Python list. reversed(values) iterates from the last item to the
    # first without copying, so prepending each value yields the original
    # order.
    # Documentation: https://docs.python.org/3/library/functions.html#reversed
    head = None
    for value in reversed(values):
        head = ListNode(value,head)
    return head


def to_list(head: ListNode | None) -> list[int]:
    # Helper added in this file (not in the textbook): collect node values
    # into a Python list, for printing and comparison.
    result=[]
    while head is not None:
        result.append(head.data)
        head=head.next
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 195)
# --------------------------------------------
# Time is the same as mergesort, O(n log n). No memory is explicitly
# allocated, but space is O(log n): the maximum depth of the call stack,
# since each recursive call receives a list half as long.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book `insertion_sort(L)` (O(n^2), O(1) space, using `ListNode(0, L)` as a
#   dummy head): NOT present in this file.
# - Book: `def stable_sort_list(L):` (comment "Base cases: L is empty or a
#   single node, nothing to do.") finds the midpoint with
#   `pre_slow, slow, fast = None, L, L`, advancing `pre_slow = slow` and
#   `fast, slow = fast.next.next, slow.next`, then `pre_slow.next = None`
#   ("Splits the list into two equal-sized lists.") and returns
#   `merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))`.
# - File: parameter `head: ListNode | None` with return hint; base case uses
#   `is None` tests; midpoint found with `slow, fast = head, head.next`
#   (no `pre_slow`), the cut is made after `slow`, and the merge of Solution
#   7.1 is written inline (dummy/tail loop) rather than calling a separate
#   function. The file defines its own `ListNode` dataclass.
# - Helpers `to_linked` and `to_list` are added (not in the book).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example (not from the book) with a duplicated value 1.
    # Convert a Python list to a linked list, sort it, and convert back.
    result = to_list(stable_sort_list(to_linked([4,1,3,1,2])))
    print('Sorted linked list:', result)

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert result == [1,1,2,3,4]
