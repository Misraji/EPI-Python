"""EPI Python — Exercise 9.2: Test if a Binary Tree is Symmetric

Chapter 9: Binary Trees
Textbook: pages 116–117 (printed page numbers; problem and solution start
on 116, the program and its complexity finish on 117).

PROBLEM (from the textbook)
---------------------------
"A binary tree is symmetric if you can draw a vertical line through the root
and then the left subtree is the mirror image of the right subtree."

The book illustrates this with Figure 9.3 (three trees, each with root A
holding 314 and children B and E both holding 6):
    (a) symmetric: B's right child C (2) has right child D (3); E's left
        child F (2) has left child G (3) — a mirror image in shape and keys.
    (b) "structurally symmetric, but not symmetric, because symmetry
        requires that corresponding nodes have the same keys; here C and F
        as well as D and G break symmetry" (C=561 vs F=2, D=3 vs G=1).
    (c) "asymmetric because there is no node corresponding to D" (C and F
        both hold 561, but only C has a child D).

"Write a program that checks whether a binary tree is symmetric."

HINT (from the textbook)
------------------------
"The definition of symmetry is recursive."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
First approach: build the mirror image of the tree and test whether it is
equal to the original. Mirroring is easy: swap the left and right subtrees
and continue recursively. Both time and space are O(n), n being the number
of nodes (the mirror copy takes O(n) space).

Better insight: the mirrored subtrees never need to be constructed. All
that matters is whether a given *pair* of subtrees are mirror images of each
other, and the check can short-circuit to False as soon as any pair fails.
The book's helper compares two subtrees:
  - both empty            -> True;
  - both non-empty        -> True exactly when their keys are equal, the
                             first's left mirrors the second's right, and
                             the first's right mirrors the second's left;
  - exactly one empty     -> False.
The whole tree is symmetric if it is empty or if its root's left and right
subtrees mirror each other.

This file implements that algorithm in `is_symmetric_nodes`;
`is_symmetric_binary_tree` is an added adapter that accepts nested tuples.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
Trees are written as nested (value, left, right) tuples; None is empty.
    None                                    -> True  (empty tree)
    (1, None, None)                         -> True  (single node)
    (1, (2, None, None), (2, None, None))   -> True  (equal mirrored keys)
    (1, (2, None, None), (3, None, None))   -> False (keys 2 and 3 differ)
"""

# Python standard library: automatically generated special methods for
# classes that mainly store data ("data classes").
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` is a class decorator: from the annotated class attributes
# (data, left, right) it generates __init__ (parameters in that order),
# __repr__ and __eq__, so TreeNode(1, None, None) works without a
# hand-written constructor.
#
# Annotations such as `data: int` are type hints: documentation for readers
# and tools, not enforced by Python at run time. "TreeNode | None" is a
# string (forward reference) because the class name does not exist yet
# while the class body runs; it means "a TreeNode or None". The `= None`
# defaults let TreeNode(5) create a leaf.
@dataclass
class TreeNode:
    data: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


# `root: TreeNode | None` and `-> bool` are type hints (not enforced). The
# `X | Y` union syntax evaluated in a signature requires Python 3.10+.
def is_symmetric_nodes(root: TreeNode | None) -> bool:
    """Compare mirror-image subtrees recursively.

    This file's version of the textbook's is_symmetric program (pages
    116–117), which never builds a mirrored copy of the tree.
    """

    # Nested helper corresponding to the book's check_symmetric: returns
    # True when the subtrees `left` and `right` are mirror images.
    def mirrored(left,right):

        # Handles the book's "both empty" and "exactly one empty" cases in
        # one step. `is` tests object identity. If at least one argument is
        # None, `left is right` is True only when both are None (both
        # subtrees empty) and False when just one is empty.
        if left is None or right is None:
            return left is right

        # Both subtrees exist. `and` short-circuits: evaluation stops at the
        # first False operand, so a key mismatch skips the recursive calls
        # and a failure in the first pair skips the second pair. Note the
        # crossed directions: left.left is paired with right.right, and
        # left.right with right.left.
        return (left.data==right.data and mirrored(left.left,right.right)
                and mirrored(left.right,right.left))

    # `or` short-circuits too: an empty tree is symmetric without further
    # work; otherwise compare the root's two subtrees.
    return root is None or mirrored(root.left,root.right)


def is_symmetric_binary_tree(tree: tuple | None) -> bool:
    """Adapter (not in the textbook): build TreeNodes from nested
    (value, left, right) tuples, then call is_symmetric_nodes."""

    # Recursive builder. `X if cond else Y` is a conditional expression:
    # None for an empty description, otherwise a new TreeNode whose children
    # are built from t[1] and t[2].
    def build(t):
        return None if t is None else TreeNode(t[0],build(t[1]),build(t[2]))
    return is_symmetric_nodes(build(tree))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 117)
# -------------------------------------------
# Time complexity O(n) and space complexity O(h), where n is the number of
# nodes and h is the height of the tree (the space is the recursion stack).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def is_symmetric(tree)` with nested
#   `check_symmetric(subtree_0, subtree_1)`; file: `is_symmetric_nodes(root:
#   TreeNode | None) -> bool` with nested `mirrored(left, right)`.
# - Book tests `if not subtree_0 and not subtree_1: return True`, then
#   `elif subtree_0 and subtree_1: return (...)`, then
#   `return False` (with comment "One subtree is empty, and the other is
#   not."). File merges the two empty cases into
#   `if left is None or right is None: return left is right` and then
#   returns the key/recursive comparison unconditionally. Same logic.
# - Book's final line `return not tree or check_symmetric(tree.left,
#   tree.right)`; file uses `root is None or mirrored(root.left,
#   root.right)`.
# - File adds `is_symmetric_binary_tree(tree: tuple | None)`, a
#   tuple-to-TreeNode adapter not in the book, and its own `TreeNode`
#   dataclass. Type hints are added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases; pytest has the full set.
    # They show an empty tree, a single node, a symmetric three-node tree,
    # and a structurally symmetric tree whose keys break symmetry (like
    # Figure 9.3(b)).
    #
    # `assert condition` raises AssertionError if the condition is false;
    # these are quick smoke checks only.
    result=is_symmetric_binary_tree(None)
    print('is_symmetric_binary_tree', result)
    assert result == True
    result=is_symmetric_binary_tree((1, None, None))
    print('is_symmetric_binary_tree', result)
    assert result == True
    result=is_symmetric_binary_tree((1, (2, None, None), (2, None, None)))
    print('is_symmetric_binary_tree', result)
    assert result == True
    result=is_symmetric_binary_tree((1, (2, None, None), (3, None, None)))
    print('is_symmetric_binary_tree', result)
    assert result == False
