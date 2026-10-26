"""EPI Python — Exercise 24.20: Convert a Sorted Doubly Linked List into a BST

Chapter 24: Honors Class
Textbook: pages 376–378 (printed page numbers; problem on 376, solution
starts on 377).

PROBLEM (from the textbook)
---------------------------
"Write a program that takes as input a doubly linked list of sorted numbers
and builds a height-balanced BST on the entries in the list. Reuse the nodes
of the list for the BST, using the previous and next fields for the left and
right children, respectively."

The book introduces this by observing that lists and BSTs are both "linked"
structures, and that doubly linked list nodes and BST nodes both have a key
and two references. Figure 24.6 (page 377) shows (a) a BST on five nodes with
keys 2, 3, 5, 7, 11 (root 7; 3 has children 2 and 5; 11 has no children),
each node labelled with a hex memory address, and (b) the sorted doubly
linked list 2 <-> 3 <-> 5 <-> 7 <-> 11 built from the very same nodes
(same addresses).

HINT (from the textbook)
------------------------
"Update reference fields, not node contents."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Array approach: if the list nodes were stored in an array, the midpoint could
be found by indexing, giving the recurrence T(n) = O(1) + 2T(n/2), which
solves to O(n). This is the method of Solution 14.8 (page 210). Nodes can be
recycled, but the array itself costs O(n) extra space.

Direct midpoint approach: without allocating anything, find the list's
midpoint, make it the root, and recurse on the two halves. Finding the
midpoint requires a traversal (including computing the length), so
T(n) = O(n) + 2T(n/2), i.e. O(n log n). The extra log factor comes purely from
not being able to reach a list's midpoint in O(1) time.

Key insight: since O(n) time is spent walking to the midpoint anyway, do
useful work during that walk:

1. Build a balanced BST on the first floor(n/2) nodes.
2. The node that comes next, number floor(n/2) + 1, becomes the root of the
   final BST; its left child is the BST from step 1.
3. Because the list links are being rewritten, keep a reference to the head
   of the not-yet-processed part of the list and advance it inside the
   recursive calls. This way the root is found as a by-product of building
   the left subtree.
4. Finally build a balanced BST on the remaining n - floor(n/2) - 1 nodes and
   make it the root's right child.

The book prints one program implementing this; it corresponds to
build_bst_from_sorted_doubly_list below (the inner helper is named `build`
in this file).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    list 1 <-> 2 <-> 3, n = 3  -> root is node 2, left child node 1,
                                  right child node 3 (same node objects)
"""


# Added helper class (the book does not print a node class here; it relies
# on list nodes that have data, prev and next fields).
class DoublyNode:
    """Doubly linked list node; also serves as a BST node.

    `prev` plays the role of the BST left child and `next` the right child
    after conversion. This class is an addition to the textbook listing.
    """

    # __init__ is the constructor method that Python calls when you write
    # DoublyNode(...). `data: int` is a type hint (documentation only; Python
    # does not enforce it). `prev=None, next=None` are default argument
    # values, so DoublyNode(5) creates an unlinked node. (Naming a parameter
    # `next` shadows the built-in next() function inside this method only.)
    def __init__(self,data: int,prev=None,next=None):

        # Tuple unpacking assigns all three attributes in one statement.
        self.data,self.prev,self.next=data,prev,next


# Type hints: `DoublyNode | None` (Python 3.10+ union syntax) means "a
# DoublyNode or None"; `n: int` is the list length; the return value is the
# BST root or None for an empty list. Annotations are not enforced at run
# time.
def build_bst_from_sorted_doubly_list(head: DoublyNode | None,n: int) -> DoublyNode | None:
    """Return the root of a height-balanced BST built from the list's nodes.

    This is the textbook's single implementation (build the left subtree,
    take the next list node as the root, then build the right subtree).
    `prev` and `next` of each node become its left and right child. The
    length n of the list is given, as in the book.
    """

    # A one-element list used as a mutable "cursor" shared with the nested
    # function: build() can change current[0] (an item of the list) without
    # rebinding the name `current`. The book uses the same trick
    # (`head = [L]`). An alternative in modern Python would be the
    # `nonlocal` statement, but the list keeps the textbook's style.
    current=[head]

    # Nested function (defined inside another function). It can read the
    # enclosing variable `current`. It builds a BST from list positions
    # start .. end - 1 (the book's comment: "from the (start + 1)-th to the
    # end-th node, inclusive") and returns the root.
    def build(start: int,end: int) -> DoublyNode | None:

        # Empty range: no nodes, so an empty subtree.
        if start>=end:return None

        # `//` is floor (integer) division, so mid is an int index.
        mid=(start+end)//2

        # Recursively build the left half first; this consumes exactly the
        # nodes start .. mid - 1 and advances the cursor past them.
        left=build(start,mid)

        # The book's comment here: the last call moved the cursor to the
        # successor of the maximum node in the tree rooted at `left`, so the
        # cursor now points at this subtree's root.
        root=current[0]

        # Added safety check (not in the book): if the list has fewer nodes
        # than n says, the cursor runs out. `raise` stops normal execution
        # with a ValueError exception carrying the given message.
        if root is None:raise ValueError('List shorter than indicated length')

        # Advance the cursor before root.next is overwritten below; the old
        # root.next is the next unprocessed list node.
        current[0]=root.next

        # Reuse the reference fields: prev becomes the left child and next
        # becomes the right child.
        root.prev=left
        root.next=build(mid+1,end)
        return root
    return build(0,n)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 378)
# --------------------------------------------
# The algorithm does O(1) work per node, so the time complexity is O(n).
# No dynamic memory allocation is needed: the list nodes themselves become
# the tree nodes. The deepest chain of recursive calls is ceil(log n) frames,
# so the space complexity (call stack) is O(log n).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Node class: the book prints no node class; the file adds `DoublyNode`
#   with fields data, prev, next.
# * Signature: book `def build_bst_from_sorted_doubly_list(L, n)`; file
#   renames the list parameter to `head` and adds type hints
#   (`DoublyNode | None`, `int`, return `DoublyNode | None`).
# * Helper: book's nested `build_bst_from_sorted_doubly_list_helper(start,
#   end)`; file's nested helper is named `build` with int type hints.
# * Cursor: book `head = [L]` defined just before the final return; file
#   `current=[head]` defined before the helper.
# * Root step: book uses one statement
#   `curr, head[0] = head[0], head[0].next` then `curr.prev = left`,
#   `curr.next = ...`; file splits this into `root=current[0]`, an added
#   `if root is None: raise ValueError(...)` check, and
#   `current[0]=root.next`, using the name `root` instead of `curr`.
# * The recursion order, midpoint formula and returned value match the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: build the sorted list 1 <-> 2 <-> 3 by hand. Tuple
    # unpacking creates three nodes in one statement; `;` separates several
    # simple statements on one line (legal, though usually discouraged).
    a,b,c=DoublyNode(1),DoublyNode(2),DoublyNode(3)
    a.next=b;b.prev=a;b.next=c;c.prev=b
    tree=build_bst_from_sorted_doubly_list(a,3)
    print('BST root:',tree.data)

    # `assert` stops the program with an AssertionError if the condition is
    # false. `is` checks object identity, confirming that the original list
    # nodes were reused (node 2 is the root, 1 its left, 3 its right child).
    # pytest provides the more thorough verification.
    assert tree is b and tree.prev is a and tree.next is c
