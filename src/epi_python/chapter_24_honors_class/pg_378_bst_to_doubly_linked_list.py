"""EPI Python — Exercise 24.21: Convert a BST to a Sorted Doubly Linked List

Chapter 24: Honors Class
Textbook: pages 378–379 (printed page numbers; problem and solution start
on 378).

PROBLEM (from the textbook)
---------------------------
"Design an algorithm that takes as input a BST and returns a sorted doubly
linked list on the same elements. Your algorithm should not do any dynamic
allocation. The original BST does not have to be preserved; use its nodes as
the nodes of the resulting list, as shown in Figure 24.6 on the preceding
page."

Context given by the book: a BST node has two references (left, right) and a
doubly linked list node has two (previous, next). Reading left as previous and
right as next, a BST node can serve as a list node; and an inorder traversal
of a BST is an ordered sequence just like a sorted list. So the question is
whether the tree's reference fields can be rewritten so that the nodes form a
list in inorder sequence. (Figure 24.6, page 377: the BST with keys 2, 3, 5,
7, 11 and the list 2 <-> 3 <-> 5 <-> 7 <-> 11 made of the same nodes.)

HINT (from the textbook)
------------------------
"The tricky part is attaching the root to its subtrees."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Without the no-allocation rule, an inorder traversal could write the nodes
into a dynamic array and then link them; that is O(n) time for n nodes but
also O(n) extra space.

The key property used instead: lists are easy to concatenate. Given the
lists already built from the left and right subtrees, the root can be
spliced between them in O(1) time, as long as each recursive call reports
both the head and the tail of its list:

1. An empty subtree yields an empty list (no head, no tail).
2. Recursively convert the left subtree and the right subtree.
3. Append the root after the left list's tail (link both directions).
4. Append the right list's head after the root (link both directions).
5. The combined list's head is the left list's head, or the root if the
   left list is empty; its tail is the right list's tail, or the root if
   the right list is empty.

The book prints one program; bst_to_doubly_linked_list below follows it
(using plain tuples instead of the book's HeadAndTail named tuple).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    BST 2 with children 1 and 3  ->  1 <-> 2 <-> 3
"""


# Added helper class (the book prints no BST node class here).
class BSTNode:
    """Binary tree node. After conversion, left means previous and right next.

    This class is an addition to the textbook listing.
    """

    # __init__ is the constructor Python calls for BSTNode(...). `data: int`
    # is a type hint (documentation only, not enforced). left/right default
    # to None so a leaf can be created as BSTNode(5).
    def __init__(self,data: int,left=None,right=None):

        # Tuple unpacking assigns all three attributes in one statement.
        self.data,self.left,self.right=data,left,right


# Type hints: `BSTNode | None` (Python 3.10+ union syntax) means "a BSTNode
# or None". The return value is the head of the list (None for an empty
# tree). Annotations are not enforced at run time.
def bst_to_doubly_linked_list(tree: BSTNode | None) -> BSTNode | None:
    """Rewrite the BST's links in place and return the list's head.

    This is the textbook's single implementation (recursive conversion
    returning head and tail of each subtree's list).
    """

    # Nested helper: converts the subtree at `root` in place and returns a
    # 2-tuple (head, tail) of the resulting list. The book returns a
    # HeadAndTail named tuple instead of a plain tuple.
    def helper(root):

        # Empty subtree: empty list. `return a, b` returns the tuple (a, b).
        if root is None:return None,None

        # Recursively build the lists for the left and right subtrees. Tuple
        # unpacking splits each returned (head, tail) pair into two names.
        left_head,left_tail=helper(root.left)
        right_head,right_tail=helper(root.right)

        # Append root to the list from the left subtree. `if left_tail:`
        # relies on truthiness: None is false and a node object is true, so
        # this means "if the left list is not empty".
        root.left=left_tail
        if left_tail:left_tail.right=root

        # Append the list from the right subtree after root.
        root.right=right_head
        if right_head:right_head.left=root

        # `x or y` evaluates to x if x is truthy, otherwise to y. So the head
        # is left_head when the left list is nonempty, else root; similarly
        # the tail is right_tail or root.
        return left_head or root,right_tail or root

    # helper(tree) returns (head, tail); `[0]` selects the head.
    return helper(tree)[0]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 379)
# --------------------------------------------
# Each node receives a constant amount of work, so the time complexity is
# O(n). The space complexity is the maximum depth of the call stack, O(h),
# where h is the height of the BST. The worst case is a skewed tree, for
# which n activation records are on the stack at once.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Node class: the book prints none; the file adds `BSTNode`.
# * Signature: book `def bst_to_doubly_linked_list(tree)`; file adds type
#   hints `BSTNode | None` for the parameter and the return value.
# * Return type of the helper: the book defines
#   `HeadAndTail = collections.namedtuple('HeadAndTail', ('head', 'tail'))`
#   and returns `HeadAndTail(...)` objects, accessed as `left.tail`,
#   `right.head`; the file returns plain tuples and unpacks them into
#   `left_head, left_tail, right_head, right_tail`. Consequently the file
#   needs no `collections` import.
# * Helper name/parameter: book `bst_to_doubly_linked_list_helper(tree)`
#   with `if not tree:`; file `helper(root)` with `if root is None:`.
# * Order of the two link updates: the book does `if left.tail:
#   left.tail.right = tree` before `tree.left = left.tail`; the file sets
#   `root.left=left_tail` first. Same effect.
# * Final line: book `...helper(tree).head`; file `helper(tree)[0]`.
# * The book's comments ("Empty subtree", "Recursively builds the list from
#   left and right subtrees", "Appends tree to the list from left subtree",
#   "Appends the list from right subtree to tree") are reflected in the
#   comments above.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: the BST 2 with children 1 and 3.
    root=BSTNode(2,BSTNode(1),BSTNode(3))
    head=bst_to_doubly_linked_list(root)

    # Walk forward through the list via the `right` (next) references.
    print('Inorder linked:',head.data,head.right.data,head.right.right.data)

    # `assert` stops with an AssertionError if the condition is false. It
    # checks the head is 1 and that the backward (`left`) link from 3 leads
    # to 2. pytest provides the more thorough verification.
    assert head.data==1 and head.right.right.left.data==2
