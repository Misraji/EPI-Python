"""EPI Python — Exercise 9.5: Sum the Root-to-Leaf Paths in a Binary Tree

Chapter 9: Binary Trees
Textbook: pages 119–120 (printed page numbers; problem and solution start
on 119, program and complexity on 120).

PROBLEM (from the textbook)
---------------------------
"Consider a binary tree in which each node contains a binary digit. A
root-to-leaf path can be associated with a binary number—the MSB is at the
root. As an example, the binary tree in Figure 9.4 represents the numbers
(1000)_2, (1001)_2, (10110)_2, (110011)_2, (11000)_2, and (1100)_2."

(Figure 9.4, "Binary tree encoding integers": root A=1; A's children
B=0 and I=1; B's children C=0 and F=1; C's children D=0 and E=1; F's right
child G=1, whose left child is H=0; I's children J=0 and O=0; J's right
child K=0, with children L=1 and N=0; L's right child M=1; O's right child
P=0.)

"Design an algorithm to compute the sum of the binary numbers represented
by the root-to-leaf paths."

HINT (from the textbook)
------------------------
"Think of an appropriate way of traversing the tree."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: find the leaves, and record each node's parent in a hash table
(child -> parent), e.g. during an inorder walk. Then, from every leaf,
follow the parent map up to the root; each such leaf-to-root walk gives a
binary integer whose least significant bit is the leaf's bit. Add up these
integers. Time is O(Lh), where L is the number of root-to-leaf paths (equal
to the number of leaves) and h the tree height; the hash table dominates
the space, O(n) for n nodes.

Insight: paths share nodes, so the work on shared prefixes need not be
repeated. The integer for the path from the root to a node equals twice the
integer for the path to its parent, plus the node's own bit. Book example
(Figure 9.4): the path from A to L encodes 2 x (1100)_2 + 1 = (11001)_2.

Hence the sum over all root-to-leaf paths can be computed by a single
traversal: at each visited node, compute its path integer from the
parent's value; at a leaf return that integer; at a non-leaf return the sum
of the results for the left and right children. The book's program is
`sum_root_to_leaf(tree, partial_path_sum=0)`; this file's
`sum_root_to_leaf` follows it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (1, (0, None, None), (1, None, None))
    Paths 1->0 = (10)_2 = 2 and 1->1 = (11)_2 = 3, so the sum is 5.
"""

# Local project import (not the standard library): reuse the TreeNode
# dataclass (fields data, left, right; generated __init__) defined in this
# chapter's Exercise 9.1 module, so all files share one node type.
# Import system documentation: https://docs.python.org/3/reference/import.html
# `from ... import` statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_09_binary_trees.pg_114_is_balanced_binary_tree import TreeNode


# Type hints (`tuple | None`, `-> TreeNode | None`) document intended types;
# Python does not enforce them. The `X | Y` form evaluated in a signature
# requires Python 3.10+.
def build_tree(tree: tuple | None) -> TreeNode | None:
    """Turn nested (value, left, right) tuples into binary tree nodes.

    Helper added for testing; not in the textbook.
    """
    if tree is None:
        return None
    return TreeNode(tree[0], build_tree(tree[1]), build_tree(tree[2]))


def nested_tree(root: TreeNode | None):
    """Inverse of build_tree (helper added for testing; not in the book)."""

    # Conditional expression `X if cond else Y`: None for an empty tree,
    # otherwise a (data, left, right) tuple built recursively.
    return None if root is None else (root.data, nested_tree(root.left), nested_tree(root.right))


# `partial: int = 0` is a parameter with a default value, so callers pass
# only the root; recursive calls pass the running path value.
def sum_root_to_leaf(root: TreeNode | None, partial: int = 0) -> int:
    """Interpret each path of binary digits as a base-2 integer, sum paths.

    This file's version of the textbook's sum_root_to_leaf program
    (page 120). It adds a validation check not present in the book.
    """
    if root is None:
        return 0

    # Added check (not in the book): `raise` signals an error by creating
    # and throwing a ValueError exception, ending this call immediately.
    # ValueError is the built-in exception for "right type, bad value":
    # https://docs.python.org/3/library/exceptions.html#ValueError
    if root.data not in (0, 1):
        raise ValueError("Binary paths require node values 0 or 1")

    # Extend the parent's path value by one bit. `partial << 1` is a left
    # shift: it moves all bits one place left, i.e. multiplies by 2
    # (Python ints are unbounded, so this never overflows). `| root.data`
    # is bitwise OR: since the new lowest bit is 0 after the shift, OR-ing
    # with 0 or 1 sets that bit, which equals adding the bit. This is the
    # book's `partial_path_sum * 2 + tree.data` written with bit operators.
    partial = (partial << 1) | root.data

    # Leaf: both children absent; its path integer is the contribution.
    if root.left is None and root.right is None:
        return partial

    # Non-leaf: sum the results from both subtrees. A missing child
    # contributes 0 through the `root is None` case above.
    return sum_root_to_leaf(root.left, partial) + sum_root_to_leaf(root.right, partial)


def sum_root_to_leaf_paths(tree) -> int:
    """Convenience wrapper (not in the textbook): build the tree from
    nested tuples and return sum_root_to_leaf of it."""
    return sum_root_to_leaf(build_tree(tree))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 120)
# -------------------------------------------
# Time complexity O(n) and space complexity O(h) (the recursion stack),
# n being the number of nodes and h the height.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def sum_root_to_leaf(tree, partial_path_sum=0)`; file:
#   `sum_root_to_leaf(root: TreeNode | None, partial: int = 0) -> int`
#   (parameters renamed, type hints added).
# - Book: `partial_path_sum = partial_path_sum * 2 + tree.data`; file:
#   `partial = (partial << 1) | root.data` (same value for bits 0/1).
# - File adds a check not in the book: it raises ValueError if a node's
#   value is not 0 or 1.
# - Book tests a leaf with `if not tree.left and not tree.right`; file uses
#   `is None` comparisons. The recursive sum is the same.
# - Not in the book: `build_tree`, `nested_tree`, `sum_root_to_leaf_paths`;
#   `TreeNode` imported from the 9.1 module.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Root 1 with leaves 0 and 1: paths (10)_2 = 2 and (11)_2 = 3, sum 5.
    tree=(1,(0,None,None),(1,None,None))
    print("sum of binary paths:", sum_root_to_leaf_paths(tree))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert sum_root_to_leaf_paths(tree) == 5
