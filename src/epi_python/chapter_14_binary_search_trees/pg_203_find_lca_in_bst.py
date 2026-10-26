"""EPI Python — Exercise 14.4: Compute the LCA in a BST

Chapter 14: Binary Search Trees
Textbook: pages 203–204 (printed page numbers; problem and solution start on 203).

PROBLEM (from the textbook)
---------------------------
"Since a BST is a specialized binary tree, the notion of lowest common
ancestor, as expressed in Problem 9.4 on Page 118, holds for BSTs too."

"In general, computing the LCA of two nodes in a BST is no easier than
computing the LCA in a binary tree, since structurally a binary tree can be
viewed as a BST where all the keys are equal. However, when the keys are
distinct, it is possible to improve on the LCA algorithms for binary
trees."

"Design an algorithm that takes as input a BST and two nodes, and returns
the LCA of the two nodes. For example, for the BST in Figure 14.1 on
Page 198, and nodes C and G, your algorithm should return B. Assume all keys
are distinct. Nodes do not have references to their parents."

Figure 14.1 (page 198), "An example of a BST" (node label = key):
    A=19 with left child B=7 and right child I=43
    B=7:  left C=3 (children D=2, E=5), right F=11
    F=11: right G=17, whose left child is H=13
    I=43: left J=23, right O=47
    J=23: right K=37 (children L=29, N=41); L=29 has right child M=31
    O=47: right P=53

HINT (from the textbook)
------------------------
"Take advantage of the BST property."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Solution 9.3 (page 117) solved this for general binary trees with a
postorder traversal: the LCA is the first node visited after both target
nodes have been visited. That costs O(n), n being the number of nodes.

With distinct BST keys we can do better. Example with Figure 14.1, nodes C
and G: both keys are smaller than A's key, so their LCA lies in A's left
subtree. At B, C's key is smaller than B's and B's key is smaller than G's,
so B must be the LCA of C and G.

In general, let s and b be the two nodes and assume, without loss of
generality, that s holds the smaller key (keys are distinct, so they cannot
be equal). Comparing with the key at the root, there are four cases:
- the root's key equals the key at s or at b: the root is the LCA;
- s's key is smaller than the root's and b's key is larger: the root is the
  LCA;
- both keys are smaller than the root's: the LCA is in the left subtree;
- both keys are larger than the root's: the LCA is in the right subtree.

The function below implements this case analysis (book name `find_LCA`).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    BST 10 with children 5 and 15; nodes 5 and 15 -> root (10)
"""

# Local project import (not the standard library): the chapter's shared BST
# node class, defined in bst_nodes.py in this same package. The leading dot
# makes this a package-relative import ("from the current package").
# BSTNode is a dataclass with fields `data`, `left` and `right`.
# Relative imports: https://docs.python.org/3/reference/import.html#package-relative-imports
# dataclasses (used by BSTNode): https://docs.python.org/3/library/dataclasses.html
from .bst_nodes import BSTNode


# Type hints: the tree (or None), two nodes, and a node-or-None result.
# Python does not enforce annotations at run time.
def find_lca_in_bst(tree: BSTNode | None, smaller: BSTNode, bigger: BSTNode) -> BSTNode | None:
    """Find where the two keys' search paths first diverge.

    This is the textbook's implementation (book name `find_LCA`),
    restructured as a single loop.
    """

    # sorted() returns a new ascending list of the two keys; unpacking it
    # into `low, high` means the caller may pass the nodes in either order
    # (the book requires s to hold the smaller key).
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    low, high = sorted((smaller.data, bigger.data))

    # A node is truthy and None is falsy: loop until we fall off the tree.
    while tree:
        if tree.data < low:

            # Both keys are larger: the LCA must be in the right subtree.
            tree = tree.right
        elif tree.data > high:

            # Both keys are smaller: the LCA must be in the left subtree.
            tree = tree.left
        else:

            # Now low <= tree.data <= high: the paths split here (or the
            # node is one of the targets), so this is the LCA.
            return tree

    # Added fallback (not in the book): reached only if the keys are not
    # both in the tree.
    return None


# TEXTBOOK POST-SOLUTION DISCUSSION (page 204)
# --------------------------------------------
# Each iteration descends one level, so the time complexity is O(h), where
# h is the height of the tree.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def find_LCA(tree, s, b):` preceded by the comment "Input nodes are
# nonempty and the key at s is less than or equal to that at b." An outer
# `while tree.data < s.data or tree.data > b.data:` loop ("Keep searching
# since tree is outside of [s, b].") contains two inner while loops that move
# right ("LCA must be in tree's right child.") or left ("LCA must be in
# tree's left child."); after it, "Now, s.data <= tree.data &&
# tree.data <= b.data." and `return tree`.
# File: renamed `find_lca_in_bst(tree, smaller, bigger)` with type hints;
# sorts the two keys so argument order does not matter; a single
# `while tree:` loop with if/elif/else replaces the nested loops; returns
# None if the search runs off the tree. Same result for valid inputs.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Because of the relative import above, run it as a module:
#   python -m epi_python.chapter_14_binary_search_trees.pg_203_find_lca_in_bst
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # An added example (not from the book): the LCA of a root's two
    # children is the root itself.
    left, right = BSTNode(5), BSTNode(15)
    root = BSTNode(10,left,right)
    print("Lowest common ancestor:", find_lca_in_bst(root,left,right).data)

    # `assert` stops the program with an AssertionError if the condition is
    # false. `is` checks that the very same node object is returned, not
    # merely an equal one. Full tests live in the tests/ folder.
    assert find_lca_in_bst(root,left,right) is root
