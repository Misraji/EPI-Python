"""EPI Python — Exercise 24.10: Copy a Postings List

Chapter 24: Honors Class
Textbook: pages 362–364 (printed page numbers; problem and brute force on
362, the improved method, Figure 24.4 and most of the program on 363, the
end of the program and the analysis on 364).

PROBLEM (from the textbook)
---------------------------
A postings list is a singly linked list with an additional "jump" field at
each node. The jump field points to any other node. Figure 24.3 illustrates
a postings list with four nodes.

Implement a function which takes a postings list and returns a copy of it.
You can modify the original list, but must restore it to its initial state
before returning.

Figure 24.3 (described): a list L of four nodes a -> b -> c -> d, each with
a next field and a jump field drawn as curved arrows to other nodes (a jump
may point to the node itself).

HINT (from the textbook)
------------------------
Copy the jump field and then copy the next field.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force:
  1. Copy the postings list without assigning the jump fields.
  2. Use a hash table to map each node of the original list to its copy.
  3. Walk the original and new lists in tandem, using the mapping to set
     each copied jump field.
Time and space are both O(n), where n is the number of nodes.

Improving the space: use each original node's next field to record the
mapping from that node to its copy. To keep the structure of the original
list recoverable, each copied node's next field points to the successor of
its original node. The list becomes a, a', b, b', c, c', ... (Figure
24.4(b), "copy with cross-referencing").

Then proceed like the brute force: set the jump field of each copy using
the next field of the original list to find the corresponding copied node
(Figure 24.4(c), "assign jump field"): copy-of-x.jump = (x.jump).next.

Finally, undo the changes to the original list and set the next fields of
the copied list (Figure 24.4(d), "undo changes").

Figure 24.4 (described): (a) the initial list; (b) original nodes a..d each
followed by their copies a'..d', with copies' jump fields still empty;
(c) copies' jump fields assigned to the copies of their originals' jump
targets; (d) two separate lists L and L' with identical structure.

The book prints one program, `copy_postings_list(L)`, in three commented
stages; this file implements the same three stages.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    nodes a(1) -> b(2), a.jump = b, b.jump = a
    copy: a'(1) -> b'(2), a'.jump is b', b'.jump is a'; original unchanged
"""


class PostingListNode:
    """Postings-list node with `order`, `next` and `jump` fields.

    Helper class; the book uses PostingListNode(order, next, jump) but does
    not print its definition in this exercise.
    """

    # __init__ runs when PostingListNode(...) is called. The default `None`
    # values mean "no successor" / "no jump target".
    # The hints are quoted strings ('PostingListNode | None') because the
    # class name does not exist yet while its body runs; quoted annotations
    # (forward references) are not evaluated. `X | None` means "an X or
    # None". Python does not enforce type hints.
    def __init__(self,order: int,next: 'PostingListNode | None'=None,jump: 'PostingListNode | None'=None):
        self.order=order
        self.next=next
        self.jump=jump


def copy_postings_list(head: PostingListNode | None) -> PostingListNode | None:
    """Textbook implementation: interleave copies, set jumps, then separate.

    Uses O(1) extra space besides the copied nodes, and restores the
    original list before returning.
    """

    # `is None` tests identity with the None object, the recommended way to
    # test for "no list".
    if head is None:
        return None

    # Stage 1: Makes a copy of the original list without assigning the jump
    # field, and creates the mapping for each node in the original list to
    # the copied list (the copy is inserted right after its original).
    it=head
    while it:
        copy=PostingListNode(it.order,it.next,None)
        it.next=copy
        it=copy.next

    # Stage 2: Assigns the jump field in the copied list.
    # it.next is the copy of `it`; it.jump.next is the copy of it's jump
    # target. `if it.jump:` skips nodes whose jump is None.
    # Advancing by `it.next.next` steps over the copy to the next original.
    it=head
    while it:
        if it.jump:
            it.next.jump=it.jump.next
        it=it.next.next

    # Stage 3: Reverts the original list, and assigns the next field of the
    # copied list.
    it=head
    new_head=head.next
    while it:
        copy=it.next

        # Restore the original's next to the following original node.
        it.next=copy.next

        # Conditional expression `X if cond else Y`: the copy's next becomes
        # the following original's copy, or None at the end of the list.
        copy.next=it.next.next if it.next else None
        it=it.next
    return new_head


# TEXTBOOK POST-SOLUTION DISCUSSION (page 364)
# --------------------------------------------
# Time: O(n). Space: O(1) beyond the n new nodes of the copy itself
# (the brute-force hash-table version needed O(n) extra space).
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def copy_postings_list(L)` with `if not L: return None`; Stage 1
#   variable named `new_node`; Stage 2 identical; Stage 3 is `it = L`,
#   `new_list_head = it.next`, then `while it.next: it.next, it =
#   it.next.next, it.next` (one loop that walks every node, original and
#   copy alternately, relinking each to the node two ahead).
# file: parameter `head` with hints `PostingListNode | None`; test written
#   `if head is None`; Stage 1 variable named `copy`; Stage 3 rewritten as a
#   loop over original nodes only, with a separate `copy` variable and the
#   conditional `copy.next = it.next.next if it.next else None`; result
#   variable renamed `new_head`. The `PostingListNode` class is defined in
#   the file (the book does not print it here). Same results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Two nodes whose jumps point at each other.
    # `;` separates several simple statements on one line.
    a,b=PostingListNode(1),PostingListNode(2)
    a.next=b;a.jump=b;b.jump=a
    cloned=copy_postings_list(a)
    print('Copied postings:',cloned.order,cloned.jump.order)

    # `is` / `is not` compare object identity: the copy must be a new node,
    # its jump must point to the COPIED second node (cloned.next), and the
    # original list must be restored (a.next is b again).
    # `assert` raises AssertionError if any check fails; the tests/ folder
    # holds the thorough pytest suite.
    assert cloned is not a and cloned.jump is cloned.next and a.next is b
