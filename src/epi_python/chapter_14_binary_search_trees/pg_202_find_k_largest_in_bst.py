"""EPI Python — Exercise 14.3: Find the k Largest Elements in a BST

Chapter 14: Binary Search Trees
Textbook: pages 202–203 (printed page numbers; problem and solution start on 202).

PROBLEM (from the textbook)
---------------------------
"A BST is a sorted data structure, which suggests that it should be possible
to find the k largest keys easily."

"Write a program that takes as input a BST and an integer k, and returns the
k largest elements in the BST in decreasing order. For example, if the input
is the BST in Figure 14.1 on Page 198 and k = 3, your program should return
<53,47,43>."

Figure 14.1 (page 198), "An example of a BST" (node label = key):
    A=19 with left child B=7 and right child I=43
    B=7:  left C=3 (children D=2, E=5), right F=11
    F=11: right G=17, whose left child is H=13
    I=43: left J=23, right O=47
    J=23: right K=37 (children L=29, N=41); L=29 has right child M=31
    O=47: right P=53

HINT (from the textbook)
------------------------
"What does an inorder traversal yield?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: an inorder traversal lists keys in ascending order; return the
last k visited. A queue suits storing them, since it easily evicts nodes
visited more than k steps earlier. Drawback: it may process many nodes that
cannot be in the result, e.g. when k is small and the left subtree is large.

Better: start with the desired nodes and work backwards, recursing on the
right subtree first and then the left: a reverse-inorder traversal. For
Figure 14.1 the reverse-inorder visit order is
<P,O,I,N,K,M,L,J,A,G,H,F,B,E,C,D>.

Stop as soon as k nodes have been visited. The code stores the keys in a
dynamic array and returns once it holds k elements; newer keys go at the end,
so the array is in decreasing order as the problem requires.

Worked example from the book, the five largest keys in Figure 14.1: recurse
on A, I, O, P in that order; returning from the recursive calls, visit P, O,
I in that order, adding their keys. Then recurse on J, K, N in that order.
Finally visit N and then K, adding their keys. Stop: the array holds five
keys.

The function below is the book's single implementation.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    BST 10 (left 5; right 15 with children 12, 20), k=3 -> [20, 15, 12]
"""

# Local project import (not the standard library): the chapter's shared BST
# node class, defined in bst_nodes.py in this same package. The leading dot
# makes this a package-relative import ("from the current package").
# BSTNode is a dataclass with fields `data`, `left` and `right`.
# Relative imports: https://docs.python.org/3/reference/import.html#package-relative-imports
# dataclasses (used by BSTNode): https://docs.python.org/3/library/dataclasses.html
from .bst_nodes import BSTNode


# Type hints: a tree (or None) and an int in, a list of ints out. Python
# does not enforce annotations at run time.
def find_k_largest_in_bst(tree: BSTNode | None, k: int) -> list[int]:
    """Reverse inorder traversal, stopping after the requested k keys.

    This is the textbook's implementation.
    """

    # A variable annotation documenting the result type (not enforced).
    result: list[int] = []

    # Nested function: `helper` can read the enclosing `result` and `k`.
    # It never rebinds `result` (it only calls `result.append`), so no
    # `nonlocal` declaration is needed.
    def helper(subtree: BSTNode | None) -> None:

        # Perform reverse inorder traversal (right, node, left), but only
        # while the subtree exists and fewer than k keys have been found.
        if subtree and len(result) < k:
            helper(subtree.right)

            # Re-check: the right-subtree call may have filled the result.
            if len(result) < k:
                result.append(subtree.data)
                helper(subtree.left)

    helper(tree)
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 203)
# --------------------------------------------
# Time O(h + k), which can be much better than a conventional inorder walk,
# e.g. for a balanced tree and small k. The bound holds because the number
# of times the program descends the tree is at most h more than the number
# of times it ascends, and each ascent happens after a node is added to the
# result; after k nodes have been added, the program stops.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def find_k_largest_in_bst(tree, k):` with a nested
# `find_k_largest_in_bst_helper(tree)` (comment "Perform reverse inorder
# traversal.") and the list named `k_largest_elements`, created after the
# helper's definition. File: helper renamed `helper(subtree)`, list renamed
# `result` and created before the helper, type hints added. The traversal
# statements are otherwise the same.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Because of the relative import above, run it as a module:
#   python -m epi_python.chapter_14_binary_search_trees.pg_202_find_k_largest_in_bst
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # An added example (not from the book): keys 5, 10, 12, 15, 20.
    root = BSTNode(10, BSTNode(5), BSTNode(15, BSTNode(12), BSTNode(20)))
    print("Three largest keys:", find_k_largest_in_bst(root, 3))

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert find_k_largest_in_bst(root, 3) == [20, 15, 12]
