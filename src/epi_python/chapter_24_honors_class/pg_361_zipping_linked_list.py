"""EPI Python — Exercise 24.9: Implement List Zipping

Chapter 24: Honors Class
Textbook: pages 361–362 (printed page numbers; problem, figure and the start
of the solution on 361, the program and analysis on 362).

PROBLEM (from the textbook)
---------------------------
Let L be a singly linked list. Assume its nodes are numbered starting at 0.
Define the zip of L to be the list consisting of the interleaving of the
nodes numbered 0, 1, 2, ... with the nodes numbered n - 1, n - 2, n - 3,
..., where n is the number of nodes in the list. The zipping function is
illustrated in Figure 24.2.

Figure 24.2 (described): (a) the list l0 -> l1 -> l2 -> l3 -> l4 before
zipping, with node addresses 0x1000, 0x1240, 0x1830, 0x2110, 0x2200;
(b) after zipping, l0 -> l4 -> l1 -> l3 -> l2, with the same addresses —
nodes are reused and no memory is allocated.

Implement the zip function.

HINT (from the textbook)
------------------------
Consider traversing the list in reverse order.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: repeatedly find the head and the tail, remove them from the
original list and append the pair to the result. Time is
O(n) + O(n - 2) + O(n - 4) + ... = O(n^2); space O(1).

The O(n^2) comes from traversing the list again and again to find the tail,
while getting the head of a singly linked list is O(1). This suggests paying
a one-time O(n) cost to reverse the second half of the list; then the
reversed second half only has to be interleaved with the first half.

Steps of the book's program `zipping_linked_list(L)`:
  1. Find the second half with a slow pointer (one step) and a fast pointer
     (two steps); when fast reaches the end, slow is at the middle.
  2. Split the list into two lists after slow.
  3. Reverse the second half (the book calls `reverse_linked_list`, a
     helper from the linked-lists chapter that is not reprinted here).
  4. Interleave the first half with the reversed second half.

This file implements `zipping_linked_list` plus the helpers it needs
(`ListNode`, `reverse_linked_list`) and a display helper `as_list`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    0 -> 1 -> 2 -> 3 -> 4   zips to   0 -> 4 -> 1 -> 3 -> 2
    1 -> 2 -> 3 -> 4        zips to   1 -> 4 -> 2 -> 3
"""


class ListNode:
    """Singly linked list node (helper; not printed in this exercise).

    The book uses a ListNode class with `data` and `next` fields defined in
    its linked-lists chapter.
    """

    # __init__ is the initializer called by ListNode(...). `next=None` is a
    # default argument, so a node created without a successor ends the list.
    #
    # Type hints: `data: int`. The hint for `next` is written as a STRING,
    # 'ListNode | None', because the class name ListNode is not yet defined
    # while its own body is being executed; a quoted annotation (a "forward
    # reference") is not evaluated. `X | None` means "an X or None".
    # Python does not enforce annotations at run time.
    # (Naming a parameter `next` hides the built-in next() inside __init__,
    # which is harmless here.)
    def __init__(self,data: int,next: 'ListNode | None'=None):
        self.data=data
        self.next=next


def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list in place (helper the book calls).

    The book uses `reverse_linked_list` from the linked-lists chapter but
    does not reprint it in this exercise; this is the file's own version.

    The unquoted hint `ListNode | None` works here because the class
    already exists; the `|` union syntax in annotations needs Python 3.10+.
    """
    prev=None

    # `while head:` loops until head is None (None is falsy; a node object
    # is truthy by default).
    while head:

        # Save the successor before overwriting head.next, otherwise the
        # rest of the list would be lost.
        nxt=head.next
        head.next=prev

        # Tuple assignment advances both pointers in one statement.
        prev,head=head,nxt
    return prev


def zipping_linked_list(head: ListNode | None) -> ListNode | None:
    """Textbook implementation: split at the middle, reverse, interleave."""

    # Lists with 0 or 1 nodes are already zipped.
    if not head or not head.next:
        return head

    # Finds the second half of L.
    # Chained assignment: slow and fast both start at head.
    slow=fast=head
    while fast and fast.next:
        slow,fast=slow.next,fast.next.next
    first_half_head=head
    second_half_head=slow.next

    # Splits the list into two lists.
    slow.next=None
    second_half_head=reverse_linked_list(second_half_head)

    # Interleave the first half and the reversed of the second half.
    first_iter,second_iter=first_half_head,second_half_head
    while second_iter:

        # Multiple assignment: ALL right-hand values (first_iter.next,
        # second_iter, second_iter.next) are evaluated before any target is
        # assigned, then the targets are assigned left to right. In effect:
        # the second-half node is spliced in after first_iter, it points to
        # first_iter's old successor, and second_iter advances to the next
        # node of the reversed half.
        second_iter.next,first_iter.next,second_iter=(first_iter.next,second_iter,second_iter.next)

        # Skip over the node just inserted to the next first-half node.
        first_iter=first_iter.next.next
    return first_half_head


def as_list(head: ListNode | None) -> list[int]:
    """Collect node values into a Python list (display helper; not in the book)."""
    out=[]
    while head:
        out.append(head.data)
        head=head.next
    return out


# TEXTBOOK POST-SOLUTION DISCUSSION (page 362)
# --------------------------------------------
# Time: O(n). Space: O(1) — nodes are relinked in place and no new nodes are
# allocated.
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def zipping_linked_list(L)`; iterators named `first_half_iter` /
#   `second_half_iter`; same slow/fast split, reverse call and interleaving
#   statements. ListNode and reverse_linked_list come from earlier chapters
#   and are not printed here.
# file: parameter renamed `head: ListNode | None` with return hint;
#   iterators renamed `first_iter` / `second_iter`; otherwise the same
#   statements. Helpers present in the file but not printed in this
#   exercise: class `ListNode`, `reverse_linked_list` (file's own iterative
#   version), and `as_list` (for display/tests).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Build 0 -> 1 -> 2 -> 3 -> 4 by nesting constructor calls (innermost
    # node first), zip it, and convert to a Python list for printing.
    # `assert` raises AssertionError if the order differs; the tests/ folder
    # holds the thorough pytest suite.
    h=ListNode(0,ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
    result=as_list(zipping_linked_list(h))
    print('Zipped:',result)
    assert result==[0,4,1,3,2]
