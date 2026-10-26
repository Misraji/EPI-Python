"""EPI Python — Exercise 24.22: Merge Two BSTs

Chapter 24: Honors Class
Textbook: pages 379–380 (printed page numbers; problem and solution start
on 379).

PROBLEM (from the textbook)
---------------------------
"Design an algorithm that takes as input two BSTs and merges them to form a
balanced BST. For any node, you can update its left and right subtree
fields, but cannot change its key. See Figure 24.7 on the next page for an
example. Your solution can dynamically allocate no more than a few bytes."

The book notes first that simply building a BST holding the union of the
keys is easy: traverse one tree and insert its keys into the other.

Figure 24.7 (page 380): (a) two BSTs, one with root 17 (left child 5 with
children 2 and 11; right child 23) and one with root 13 (left child 7 with
left child 3; right child 19); (b) the merged balanced BST on the same nodes:
root 11; left child 5 (children 3, whose left child is 2, and 7); right
child 17 (children 13 and 23, whose left child is 19). Hex addresses show
that the nodes are reused.

HINT (from the textbook)
------------------------
"Can you relate this problem to Problems 24.21 on the facing page and 24.20
on Page 376?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: traverse one tree and insert its keys into the other. The cost
depends on how balanced the receiving tree is and how insertion is done. At
best, the receiving tree starts balanced and is kept balanced while adding,
giving O(n log n) for n total nodes. Reusing the existing nodes during the
walk is awkward with an inorder walk (the links change underneath it), but
easy with a post-order walk, because once a node is visited its original
left and right links are no longer needed.

The brute force ignores that both inputs are sorted. Ignoring the memory
limit, one could inorder-walk each tree into a sorted array, merge the two
arrays into a third sorted array, and build a balanced BST from it
recursively (e.g. Solution 14.8, page 210): O(n) time but O(n) extra space.

Within the memory limit:

1. View a list as a tree whose left children are all empty. Converting
   each BST into a sorted doubly linked list on its own nodes is
   straightforward (Solution 24.21, page 378).
2. Merge the two sorted lists into one sorted list on the same nodes
   (Solution 7.1, page 84). Viewed as a tree, this holds all keys, in O(n)
   time and O(h) space, h being the larger height of the two input trees.
3. That "tree" is completely unbalanced, so convert it to a height-balanced
   BST with Solution 24.20 (page 377).

The book's program is a short composition of those earlier functions
(bst_to_doubly_list, count_length, merge_two_sorted_lists,
build_bst_from_sorted_doubly_list). This file implements the same three
stages self-contained inside merge_two_bsts (see the code comparison).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    BST 2(1, 3) merged with BST 5(4, 6) -> balanced BST on keys 1..6
                                           (root 4 with this file's split)
"""


# Added helper class (the book prints no BST node class here).
class BSTNode:
    """Binary tree node; while in list form, left = previous, right = next.

    This class is an addition to the textbook listing.
    """

    # __init__ is the constructor Python calls for BSTNode(...). `data: int`
    # is a type hint (documentation only, not enforced). left/right default
    # to None so a leaf can be created as BSTNode(5).
    def __init__(self,data: int,left=None,right=None):

        # Tuple unpacking assigns all three attributes in one statement.
        self.data,self.left,self.right=data,left,right


# Type hints: `BSTNode | None` (Python 3.10+ union syntax) means "a BSTNode
# or None". Annotations are documentation only and not enforced.
def merge_two_bsts(a: BSTNode | None,b: BSTNode | None) -> BSTNode | None:
    """Merge two BSTs into one height-balanced BST reusing their nodes.

    Implements the textbook's approach (BST -> list, merge lists,
    list -> balanced BST) with all three stages written inline rather
    than calling the earlier solutions' functions as the book does.
    """

    # Stage 1 (Solution 24.21): convert a BST into a sorted doubly linked
    # list in place, returning the 2-tuple (head, tail). Empty trees give
    # (None, None). `if not tree:` is true when tree is None.
    def to_list(tree):
        if not tree:return None,None
        lh,lt=to_list(tree.left)
        rh,rt=to_list(tree.right)

        # Attach the root after the left list's tail, then the right list
        # after the root. `if lt:` means "if that list is nonempty", since
        # None is falsy and node objects are truthy.
        tree.left=lt
        if lt:lt.right=tree
        tree.right=rh
        if rh:rh.left=tree

        # `x or y` gives x when x is truthy, otherwise y: the head is the
        # left list's head unless that list is empty, then the root itself.
        return lh or tree,rt or tree

    # Only the heads are needed; `_` is the conventional name for a value
    # that is deliberately ignored (here, the tails).
    a_head,_=to_list(a)
    b_head,_=to_list(b)

    # Stage 2 (Solution 7.1): merge the two sorted lists by relinking nodes.
    # Chained assignment sets both names to None. n counts the nodes, which
    # the book instead obtains with count_length().
    merged_head=merged_tail=None
    n=0
    while a_head or b_head:

        # Take from list a when b is exhausted, or when a's key is <= b's
        # (taking a on ties keeps the merge stable). `a_head is not None`
        # guards the attribute access when list a is exhausted.
        if not b_head or (a_head is not None and a_head.data<=b_head.data):

            # `;` separates two simple statements on one line.
            node=a_head;a_head=a_head.right
        else:
            node=b_head;b_head=b_head.right

        # Append node to the merged list (left = previous, right = next).
        node.left=merged_tail
        if merged_tail:merged_tail.right=node
        else:merged_head=node
        merged_tail=node
        n+=1

    # Terminate the merged list so its last node has no stale successor.
    if merged_tail:merged_tail.right=None

    # Stage 3 (Solution 24.20): build a height-balanced BST from the sorted
    # list. `cursor` is a one-element list used as a shared mutable cursor:
    # the nested build() can change cursor[0] without rebinding a name.
    cursor=[merged_head]

    # build(size) consumes the next `size` list nodes and returns the root
    # of a balanced BST on them: first the left subtree of size // 2 (floor
    # division), then the next node as root, then the remaining
    # size - size//2 - 1 nodes as the right subtree.
    def build(size):
        if size==0:return None
        left=build(size//2)
        root=cursor[0]

        # Advance the cursor before root.right is overwritten.
        cursor[0]=root.right
        root.left=left
        root.right=build(size-size//2-1)
        return root
    return build(n)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 380)
# --------------------------------------------
# Each stage (tree to list, list merge, list to balanced tree) runs in O(n)
# time. Because the nodes are recycled, the extra space is dominated by the
# BST-to-list conversion, which is O(h) (its recursion depth). (The book's
# sentence says "dominated by the time to convert"; from context it means
# the space used by that conversion.)
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Book program (in full, by composition):
#   `def merge_two_bsts(A, B):` converts with `bst_to_doubly_list(A)` and
#   `bst_to_doubly_list(B)`, computes `A_length, B_length` with
#   `count_length`, and returns `build_bst_from_sorted_doubly_list(
#   merge_two_sorted_lists(A, B), A_length + B_length)`.
# * File: parameters renamed `a`, `b` with type hints `BSTNode | None`;
#   adds a `BSTNode` class; none of the helper functions the book calls
#   are imported. Instead the file writes three nested pieces inline:
#   `to_list` (like Solution 24.21's helper, returning plain tuples), a
#   `while` loop that merges the lists and counts `n` (replacing
#   `merge_two_sorted_lists` and `count_length`), and `build(size)`
#   (a size-based variant of Solution 24.20's `(start, end)` helper).
# * Midpoint choice: Solution 24.20 uses `mid = (start + end) // 2`;
#   `build(size)` puts size // 2 nodes on the left. Both are balanced but
#   may pick a different root for even sizes.
# * The book's `count_length` and `merge_two_sorted_lists` work on
#   singly linked lists via `.next`; the file's list uses `.left`/`.right`
#   of BST nodes, as Solution 24.21 produces.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: two three-node BSTs, keys 1..3 and 4..6. `;` puts two
    # statements on one line.
    a=BSTNode(2,BSTNode(1),BSTNode(3));b=BSTNode(5,BSTNode(4),BSTNode(6))
    merged=merge_two_bsts(a,b)
    print('Merged BST root:',merged.data)

    # `assert` stops with an AssertionError if the condition is false. For
    # six keys either middle key is a valid balanced root, so the check
    # accepts 3 or 4 (`in` tests tuple membership). pytest provides the
    # more thorough verification.
    assert merged.data in (3,4)
