"""EPI Python — Exercise 14.2: Find the First Key Greater Than a Given Value in a BST

Chapter 14: Binary Search Trees
Textbook: pages 201–202 (printed page numbers; problem and solution start on 201).

PROBLEM (from the textbook)
---------------------------
"Write a program that takes as input a BST and a value, and returns the
first key that would appear in an inorder traversal which is greater than
the input value. For example, when applied to the BST in Figure 14.1 on
Page 198 you should return 29 for input 23."

Figure 14.1 (page 198), "An example of a BST" (node label = key):
    A=19 with left child B=7 and right child I=43
    B=7:  left C=3 (children D=2, E=5), right F=11
    F=11: right G=17, whose left child is H=13
    I=43: left J=23, right O=47
    J=23: right K=37 (children L=29, N=41); L=29 has right child M=31
    O=47: right P=53

HINT (from the textbook)
------------------------
"Perform binary search, keeping some additional state."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
An inorder walk finds the desired node in O(n) time, n being the number of
nodes, but it ignores the BST property.

Better: use the BST search idiom. Keep the best candidate found so far and
update it while iteratively descending the tree, eliminating subtrees by
comparing node keys with the input value:
- if the current subtree's root holds a key <= the input value, search the
  right subtree (the root and its whole left subtree are too small);
- if the root's key is greater than the input value, record the root as the
  candidate and search the left subtree for something smaller that still
  qualifies.
Correctness: whenever the candidate is first set to a node, the answer must
lie within the subtree rooted at that node.

Worked example from the book: searching for the first key greater than 23
in Figure 14.1 visits A, I, J, K, L. L has no left child, so its key, 29,
is the result.

The function below is the book's single implementation.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    BST 10 (left 5, right 15 with left child 12), k=10 -> node with key 12
"""

# Local project import (not the standard library): the chapter's shared BST
# node class, defined in bst_nodes.py in this same package. The leading dot
# makes this a package-relative import ("from the current package").
# BSTNode is a dataclass with fields `data`, `left` and `right`, so
# `BSTNode(10, BSTNode(5), BSTNode(15))` builds a small tree.
# Relative imports: https://docs.python.org/3/reference/import.html#package-relative-imports
# dataclasses (used by BSTNode): https://docs.python.org/3/library/dataclasses.html
from .bst_nodes import BSTNode


# Type hints: `BSTNode | None` means a node or None (an empty tree / no
# answer). Python does not enforce annotations at run time.
def find_first_greater_than_k(tree: BSTNode | None, k: int) -> BSTNode | None:
    """Return the node with the smallest key strictly greater than k.

    This is the textbook's implementation (iterative BST search keeping the
    best candidate). Returns None if no key exceeds k.
    """

    # Tuple assignment: start at the root with no candidate yet.
    subtree, first_so_far = tree, None

    # A node object is truthy and None is falsy, so this loops until the
    # search falls off the bottom of the tree.
    while subtree:
        if subtree.data > k:

            # This node qualifies; remember it and look left for a smaller
            # qualifying key.
            first_so_far, subtree = subtree, subtree.left
        else:

            # Root and all keys in its left subtree are <= k, so skip them
            # (the book's own comment on this branch).
            subtree = subtree.right
    return first_so_far


# TEXTBOOK POST-SOLUTION DISCUSSION (page 202)
# --------------------------------------------
# Time O(h), where h is the height of the tree. Space O(1).
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Write a program that
# takes as input a BST and a value, and returns the node whose key equals the
# input value and appears first in an inorder traversal of the BST. For
# example, when applied to the BST in Figure 14.2, your program should return
# Node B for 108, Node G for 285, and null for 143.
#
# Figure 14.2 (page 202), "A BST with duplicate keys":
#     A=108 with left child B=108 and right child G=285
#     B=108: left C=-10 (children D=-14, E=2), right F=108
#     G=285: left H=243, right I=285; I has right child J=401


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def find_first_greater_than_k(tree, k):` with the same body.
# File: identical statements, plus type hints `tree: BSTNode | None`,
# `k: int`, `-> BSTNode | None`. The book's comment on the else branch is
# kept above that branch. The code matches the book's listing otherwise.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Because of the relative import above, run it as a module:
#   python -m epi_python.chapter_14_binary_search_trees.pg_201_find_first_greater_than_k
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # An added example (not from the book): keys 5, 10, 12, 15; the first
    # key greater than 10 is 12 (left child of 15).
    root = BSTNode(10, BSTNode(5), BSTNode(15, BSTNode(12)))
    result = find_first_greater_than_k(root, 10)
    print("First key greater than 10:", result.data)

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert result.data == 12
