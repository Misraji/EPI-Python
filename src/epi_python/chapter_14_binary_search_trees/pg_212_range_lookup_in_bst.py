"""EPI Python — Exercise 14.10: The Range Lookup Problem

Chapter 14: Binary Search Trees
Textbook: pages 212–214 (printed page numbers; problem and solution start
on 212; the "Augmented BSTs" discussion that follows is on 214).

PROBLEM (from the textbook)
---------------------------
"Consider the problem of developing a web-service that takes a geographical
location, and returns the nearest restaurant. The service starts with a set
of restaurant locations—each location includes X and Y-coordinates. A query
consists of a location, and should return the nearest restaurant (ties can
be broken arbitrarily)."

"One approach is to build two BSTs on the restaurant locations: T_X sorted
on the X coordinates, and T_Y sorted on the Y coordinates. A query on
location (p,q) can be performed by finding all the restaurants whose X
coordinate is in the interval [p - D, p + D], and all the restaurants whose
Y coordinate is in the interval [q - D, q + D], taking the intersection of
these two sets, and finding the restaurant in the intersection which is
closest to (p,q). Heuristically, if D is chosen correctly, the subsets are
small and a brute-force search for the closest point is fast. One approach
is to start with a small value for D and keep doubling it until the final
intersection is nonempty."

"There are other data structures which are more robust, e.g., Quadtrees and
k-d trees, but the approach outlined above works well in practice."

"Write a program that takes as input a BST and an interval and returns the
BST keys that lie in the interval. For example, for the tree in Figure 14.1
on Page 198, and interval [16,31], you should return 17,19,23,29,31."

Figure 14.1 (page 198), "An example of a BST" (node label = key):
    A=19 with left child B=7 and right child I=43
    B=7:  left C=3 (children D=2, E=5), right F=11
    F=11: right G=17, whose left child is H=13
    I=43: left J=23, right O=47
    J=23: right K=37 (children L=29, N=41); L=29 has right child M=31
    O=47: right P=53

HINT (from the textbook)
------------------------
"How many edges are traversed when the successor function is repeatedly
called m times?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: traverse the BST (inorder, postorder or preorder) and record
the keys inside the interval. Time is that of the traversal, O(n) for n
nodes. It ignores the BST property and would work unchanged on any binary
tree.

Pruning with the BST property:
- if the root's key is less than the interval's left endpoint, no node of
  the left subtree can have a key in the interval;
- if the root's key is greater than the right endpoint, no node of the
  right subtree can;
- otherwise the root's key is inside the interval, and both subtrees may
  contain keys in the interval.

Worked example from the book, Figure 14.1 with interval [16,42]: start at A
(19). 19 lies in [16,42], so both children B and I are explored. At B, the
key 7 is less than 16, so nothing in B's left subtree can lie in [16,42].
Likewise at I, 43 > 42, so I's right subtree need not be explored.

The function below is the book's single implementation (inorder traversal
with pruning), taking the interval as two numbers instead of an Interval
namedtuple.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    BST 10 (left 5; right 15 with children 12, 20), [8,16] -> [10, 12, 15]
"""

# Local project import (not the standard library): the chapter's shared BST
# node class, defined in bst_nodes.py in this same package. The leading dot
# makes this a package-relative import ("from the current package").
# BSTNode is a dataclass with fields `data`, `left` and `right`.
# Relative imports: https://docs.python.org/3/reference/import.html#package-relative-imports
# dataclasses (used by BSTNode): https://docs.python.org/3/library/dataclasses.html
from .bst_nodes import BSTNode


# Type hints: a tree (or None) and the two interval endpoints in, a list of
# keys out. Python does not enforce annotations at run time.
def range_lookup_in_bst(tree: BSTNode | None, low: int, high: int) -> list[int]:
    """Return all BST keys within the inclusive [low, high] interval.

    This is the textbook's implementation (pruned inorder traversal).
    """

    # A variable annotation documenting the result type (not enforced).
    result: list[int] = []

    # Nested helper: it reads `low`, `high` and appends to `result` from the
    # enclosing function (no rebinding, so no `nonlocal` needed).
    def helper(node: BSTNode | None) -> None:
        if node is None:
            return

        # Chained comparison: low <= key and key <= high.
        if low <= node.data <= high:

            # node.data lies in the interval: visit left, record, visit right
            # (inorder), so keys come out in ascending order.
            helper(node.left)
            result.append(node.data)
            helper(node.right)
        elif node.data < low:

            # Key too small: the whole left subtree is too small; go right.
            helper(node.right)
        else:

            # Key too large (high < node.data): only the left subtree can
            # contain keys in the interval.
            helper(node.left)

    helper(tree)
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 213–214)
# -------------------------------------------------
# The time complexity is tricky to analyze; reason in terms of m, the number
# of keys in the interval. Split nodes into those the program recurses on and
# those it does not. In the [16,42] example it recurses on A, B, F, G, H, I,
# J, K, L, M, N. Not all of these have keys in the interval, but no node
# outside this set can. The recursed-on nodes fall into three groups: nodes
# on the search path to 16, nodes on the search path to 42, and the rest.
# Every node in the third group is in the result; nodes of the first two
# groups may or may not be. Visiting the first two groups costs O(h); the
# third costs O(m), since each edge is traversed twice (down and up). The
# total is O(m + h), much better than the O(n) brute force when the tree is
# balanced and few keys lie in the range.
#
# Augmented BSTs (page 214). So far nodes hold a key, children and possibly
# a parent; adding fields can speed up some queries. Example: a structure
# supporting efficient insertion, deletion, lookup of integer keys and range
# COUNT queries (how many keys lie in an interval).
# - A plain BST can count keys in [U, V] by finding the first node with key
#   >= U and calling successor (9.10, page 123) until a key exceeds V (or
#   nodes run out): O(h + m), slow when m is large.
# - Better: give each node a size field, the number of nodes in the subtree
#   rooted there.
# - Counting keys less than a value v: start with count = 0. Since keys may
#   repeat, search for the first occurrence of v in inorder order using
#   Solution 14.2 (page 201), stopping once v is known to be absent. Taking a
#   left child leaves count unchanged; taking a right child adds one plus the
#   size of the corresponding left child. If v is present, on reaching its
#   first occurrence add the size of its left child. The same approach
#   counts entries greater than v, at most v, or at least v.
# - Book example, keys less than 40 in Figure 14.1: A's key 19 < 40, so
#   count = 7 + 1 = 8 (7 from the left child's size, 1 for A) and continue
#   at I. 43 > 40, so move to I's left child J. 23 < 40: count = 8 + 1 = 9,
#   continue at K. 37 < 40: count = 9 + 2 + 1 = 12, continue at N. 41 > 40:
#   move to N's left child, which is empty. Return 12. The left subtrees of
#   A and K were never explored.
# - These computations take O(h) since the search only descends; when m is
#   large (e.g. comparable to n) this is much faster than repeated successor
#   calls.
# - Keys in [L, U]: compute the count of keys less than L and the count of
#   keys greater than U, and subtract both from the total (the root's size).
# - The size field can be maintained on insert and delete without changing
#   their O(h) time: only nodes on the search path to the inserted/deleted
#   node change size, and each needs a constant number of extra checks.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `Interval = collections.namedtuple('Interval', ('left', 'right'))`
# and `def range_lookup_in_bst(tree, interval):` with nested
# `range_lookup_in_bst_helper(tree)` (comments "tree.data lies in the
# interval." and "interval.right > tree.data" on the else branch, the
# latter as printed), testing `interval.left <= tree.data <=
# interval.right` and `interval.left > tree.data`; `result = []` is created
# after the helper. File: no Interval namedtuple; the interval is passed as
# two parameters `low`, `high`; helper renamed `helper(node)`; the second
# test is written `node.data < low`; `result` created first; type hints
# added. Same behaviour.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Because of the relative import above, run it as a module:
#   python -m epi_python.chapter_14_binary_search_trees.pg_212_range_lookup_in_bst
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example (not from the book): keys 5, 10, 12, 15, 20; those in
    # [8, 16] are 10, 12, 15 (5 and 20 lie outside).
    root=BSTNode(10,BSTNode(5),BSTNode(15,BSTNode(12),BSTNode(20)))
    print('Keys between 8 and 16:',range_lookup_in_bst(root,8,16))

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert range_lookup_in_bst(root,8,16)==[10,12,15]
