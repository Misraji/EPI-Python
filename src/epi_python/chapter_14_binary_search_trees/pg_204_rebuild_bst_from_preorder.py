"""EPI Python — Exercise 14.5: Reconstruct a BST from Traversal Data

Chapter 14: Binary Search Trees
Textbook: pages 204–206 (printed page numbers; problem on 204, solution
starts on 205).

PROBLEM (from the textbook)
---------------------------
"As discussed in Problem 9.12 on Page 125 there are many different binary
trees that yield the same sequence of visited nodes in an inorder traversal.
This is also true for preorder and postorder traversals. Given the sequence
of nodes that an inorder traversal sequence visits and either of the other
two traversal sequences, there exists a unique binary tree that yields
those sequences. Here we study if it is possible to reconstruct the tree
with less traversal information when the tree is known to be a BST."

"It is critical that the elements stored in the tree be unique. If the root
contains key v and the tree contains more occurrences of v, we cannot always
identify from the sequence whether the subsequent vs are in the left subtree
or the right subtree. For example, for the tree rooted at G in Figure 14.2
on Page 202 the preorder traversal sequence is 285,243,285,401. The same
preorder traversal sequence is seen if 285 appears in the left subtree as
the right child of the node with key 243 and 401 is at the root's right
child."

"Suppose you are given the sequence in which keys are visited in an inorder
traversal of a BST, and all keys are distinct. Can you reconstruct the BST
from the sequence? If so, write a program to do so. Solve the same problem
for preorder and postorder traversal sequences."

Figure 14.1 (page 198), "An example of a BST" (node label = key):
    A=19 with left child B=7 and right child I=43
    B=7:  left C=3 (children D=2, E=5), right F=11
    F=11: right G=17, whose left child is H=13
    I=43: left J=23, right O=47
    J=23: right K=37 (children L=29, N=41); L=29 has right child M=31
    O=47: right P=53

HINT (from the textbook)
------------------------
"Draw the five BSTs on the keys 1,2,3, and the corresponding traversal
orders."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Inorder is not enough: experimenting shows that an inorder sequence does not
determine the tree. The sequence <1,2,3> fits five distinct BSTs
(Figure 14.3, "Five distinct BSTs for the traversal sequence <1,2,3>"):
    1 -> right 2 -> right 3;   1 -> right 3 -> left 2;
    2 with children 1 and 3;   3 -> left 1 -> right 2;
    3 -> left 2 -> left 1.

Preorder is different. Example: preorder <43,23,37,29,31,41,47,53>. The root
holds 43 because it is visited first. The left subtree holds the keys less
than 43 (23,37,29,31,41) and the right subtree the keys greater than 43
(47,53). Moreover <23,37,29,31,41> is exactly the preorder sequence of the
left subtree and <47,53> that of the right subtree. Recursively, 23 and 47
are the roots of those subtrees, and so on; the result is exactly the
subtree rooted at node I in Figure 14.1.

Generalizing: in any preorder sequence the first key is the root; the
subsequence from the second element through the last key smaller than the
root is the preorder sequence of the left subtree; the remaining keys,
greater than the root, form the preorder sequence of the right subtree.
Rebuild both subtrees recursively from these subsequences and attach them to
the root. (The book's first program does exactly this, finding the
transition point with `next` over a generator and slicing.)

Its cost: the worst-case input is the preorder sequence of a left-skewed
tree, with W(n) = W(n - 1) + O(n), i.e. O(n^2). The best case is a
right-skewed tree, O(n). For a balanced BST, B(n) = 2B(n/2) + O(n), i.e.
O(n log n).

Improvement: that program may iterate over nodes several times. Instead,
build the left subtree in the same pass that identifies its nodes. Rather
than scanning from the entry after the root to the last entry smaller than
the root, and then partly repeating this for the left subtree, pass along
the RANGE of keys the subtree being built may contain. For
<43,23,37,29,31,41,47,53>, instead of recursing on <23,37,29,31,41> (which
requires a scan to find where it ends), recurse directly on
<23,37,29,31,41,47,53> with the constraint that the subtree being built
holds keys less than 43. A shared index advances through the sequence as
nodes are created.

This file implements the second (range-based) program. The first
(slicing) program is not present.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    preorder [10,5,2,7,15,12,20] -> root 10; left 5 (children 2, 7);
                                    right 15 (children 12, 20)
"""

# Local project import (not the standard library): the chapter's shared BST
# node class, defined in bst_nodes.py in this same package. The leading dot
# makes this a package-relative import ("from the current package").
# BSTNode is a dataclass with fields `data`, `left` and `right`, so
# `BSTNode(key, left, right)` builds a node.
# Relative imports: https://docs.python.org/3/reference/import.html#package-relative-imports
# dataclasses (used by BSTNode): https://docs.python.org/3/library/dataclasses.html
from .bst_nodes import BSTNode


# Type hints: a list of ints in, the root node (or None if empty) out.
# Python does not enforce annotations at run time.
def rebuild_bst_from_preorder(preorder: list[int]) -> BSTNode | None:
    """Consume preorder values only when they fall in the subtree's key range.

    This is the textbook's second, O(n) implementation (range-constrained
    recursion with a shared index).
    """

    # A one-element list used as a mutable shared counter (the book's
    # "Tracks current subtree."). The nested function changes
    # `root_idx[0]` in place, which works without a `nonlocal` declaration
    # because the name `root_idx` itself is never rebound.
    root_idx = [0]

    # Nested function: builds the subtree whose keys lie strictly between
    # `lower` and `upper`, starting at preorder[root_idx[0]].
    def within_range(lower: float, upper: float) -> BSTNode | None:

        # All keys consumed: nothing left to build.
        if root_idx[0] == len(preorder):
            return None
        key = preorder[root_idx[0]]

        # Chained comparison `lower < key < upper`. A key outside the range
        # belongs to some ancestor's other subtree, so it is left unconsumed.
        if not lower < key < upper:
            return None
        root_idx[0] += 1

        # Note that within_range updates root_idx[0], so the order of the
        # following two calls is critical: the left subtree's keys come
        # first in preorder.
        left = within_range(lower, key)
        right = within_range(key, upper)
        return BSTNode(key, left, right)

    # float('-inf') / float('inf') are infinities that compare below / above
    # every number, so the root's range is unbounded.
    # Documentation: https://docs.python.org/3/library/functions.html#float
    return within_range(float('-inf'), float('inf'))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 206)
# --------------------------------------------
# The range-based program's worst-case time is O(n), since it does a constant
# amount of work per node. The book notes its similarity to Solution 24.20
# (page 377).
#
# A postorder traversal sequence also uniquely specifies the BST, and the
# reconstruction algorithm is very similar to the preorder case.
#
# (The inorder question from the problem is answered in the development
# above: an inorder sequence alone does not determine the BST.)
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book's first listing `rebuild_bst_from_preorder(preorder_sequence)`
#   (O(n^2) worst case, finds `transition_point` with `next(...)` over an
#   enumerate generator and recurses on slices): NOT present in this file.
# - Book's second listing: outer `rebuild_bst_from_preorder(
#   preorder_sequence)` with nested
#   `rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound)`,
#   variables `root`, `left_subtree`, `right_subtree`, and the range test
#   `if not lower_bound <= root <= upper_bound:` (inclusive). Its
#   `root_idx = [0]` is assigned after the nested function is defined.
#   File: parameter `preorder: list[int]`, nested `within_range(lower,
#   upper)`, variables `key`, `left`, `right`, type hints, `root_idx`
#   assigned first, and a STRICT test `not lower < key < upper`. With the
#   distinct keys the problem assumes, the results are the same.
# - The book's comments ("Note that ... updates root_idx[0]. So the order of
#   following two calls are critical." and "Tracks current subtree.") are
#   reflected in the comments above.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Because of the relative import above, run it as a module:
#   python -m epi_python.chapter_14_binary_search_trees.pg_204_rebuild_bst_from_preorder
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # An added example (not from the book): a balanced seven-node BST.
    root=rebuild_bst_from_preorder([10,5,2,7,15,12,20])
    print("Reconstructed root:",root.data)

    # `assert` stops the program with an AssertionError if the condition is
    # false. 7 must be the right child of 5 (the left child of the root).
    # Full tests live in the tests/ folder.
    assert root.left.right.data == 7
