"""EPI Python — Exercise 9.1: Test if a Binary Tree is Height-Balanced

Chapter 9: Binary Trees
Textbook: pages 114–116 (printed page numbers; problem on 114, solution on
115, complexity analysis and variants on 116).

PROBLEM (from the textbook)
---------------------------
"A binary tree is said to be height-balanced if for each node in the tree,
the difference in the height of its left and right subtrees is at most one.
A perfect binary tree is height-balanced, as is a complete binary tree. A
height-balanced binary tree does not have to be perfect or complete—see
Figure 9.2 on the next page for an example.

Write a program that takes as input the root of a binary tree and checks
whether the tree is height-balanced."

(Figure 9.2, "A height-balanced binary tree of height 4", shows a tree with
root A. A's left child B has children C and H; C has children D and G; D has
children E and F; H has children I and J. A's right child K has children L
and O; L has children M and N. The deepest path A-B-C-D-E has four edges,
and at every node the two subtree heights differ by at most one, even
though the tree is neither perfect nor complete.)

HINT (from the textbook)
------------------------
"Think of a classic binary tree algorithm."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: recursively compute the height of the subtree rooted at every
node, starting at the leaves and working upwards. At each node, check
whether the heights of its left and right children differ by more than
one. The heights can be kept in a hash table or in an extra field added to
each node. This uses O(n) storage and O(n) time, n being the number of
nodes.

Improvement: the heights of all nodes do not have to be stored at the same
time. Once a subtree has been fully processed, the only facts its parent
needs are (a) whether that subtree is height-balanced, and (b) if it is,
its height. Nothing about the subtree's descendants is needed afterwards.

The textbook's program therefore uses a recursive helper that returns a
pair (balanced, height), modelled as a collections.namedtuple called
BalancedStatusWithHeight:

1. An empty tree is balanced, with height -1 (the base case).
2. Recursively check the left subtree; if it is not balanced, immediately
   report "not balanced" (the height value is then irrelevant).
3. Otherwise recursively check the right subtree; if it is not balanced,
   immediately report "not balanced".
4. Otherwise the node is balanced exactly when the absolute difference of
   the two child heights is at most 1, and its height is one more than the
   larger child height.
5. The top-level function returns just the balanced field for the root.

This file implements the same postorder, early-exit idea, but encodes the
pair as a single integer (see TEXTBOOK CODE COMPARISON below):
`is_balanced_nodes` works on linked TreeNode objects, and
`is_balanced_binary_tree` is an adapter that first builds such nodes from
nested tuples.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
Trees are written as nested (value, left, right) tuples; None is empty.
    None                                     -> True  (empty tree)
    (1, None, None)                          -> True  (single node)
    (1, (2, (3, None, None), None), None)    -> False (left chain of 3:
                                                the root's subtrees have
                                                heights 2 and 0)
    (1, (2, None, None), (3, None, None))    -> True  (perfect tree)
"""

# Python standard library: automatically generated special methods for
# classes that mainly store data ("data classes").
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` is a class decorator: it reads the annotated class attributes
# below (data, left, right) and generates an __init__ method taking them as
# parameters (in that order), plus __repr__ and __eq__. So
# TreeNode(1, None, None) works without writing __init__ by hand.
#
# The annotations (`data: int`, etc.) are type hints: they document the
# intended types, but Python does not enforce them at run time. The string
# "TreeNode | None" is a forward reference (the class name is not defined
# yet while its body runs) meaning "a TreeNode or None". `= None` gives the
# children a default, so TreeNode(5) creates a leaf.
@dataclass
class TreeNode:
    data: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


# The annotation `root: TreeNode | None` says root is a node or None (empty
# tree); `-> bool` says the function returns True/False. The `X | Y` union
# syntax inside annotations is evaluated here, which requires Python 3.10+.
def is_balanced_nodes(root: TreeNode | None) -> bool:
    """Detect subtrees whose heights differ by more than one.

    This file's version of the textbook's is_balanced_binary_tree program
    (page 115): the same postorder traversal with early termination, but
    returning a single integer instead of a (balanced, height) namedtuple.
    """

    # Nested helper: returns the height of `node`'s subtree, or -1 as a
    # sentinel meaning "this subtree is not height-balanced".
    #
    # Height convention here: an empty subtree has height 0 and a leaf has
    # height 1 (the book uses -1 and 0; only differences matter, so the
    # test is unaffected). Because every real height is >= 0, the negative
    # value -1 can never be confused with a real height.
    def height(node):
        if node is None:
            return 0
        left=height(node.left)

        # Early termination, as in the book: if the left subtree is already
        # unbalanced, return immediately without visiting the right one.
        if left < 0:
            return -1
        right=height(node.right)

        # `abs()` is the built-in absolute value. The node is unbalanced if
        # its right subtree is unbalanced, or if the child heights differ by
        # more than one.
        if right < 0 or abs(left-right)>1:
            return -1

        # Built-in `max(a, b)` returns the larger argument; the node's
        # height is one more than its taller child.
        return max(left,right)+1

    # Any non-negative result means no unbalanced subtree was found.
    return height(root)>=0


def is_balanced_binary_tree(tree: tuple | None) -> bool:
    """Adapter: nested (value,left,right) tuples specify small test trees.

    Not in the textbook. It converts a tuple description into TreeNode
    objects and then calls is_balanced_nodes (the textbook algorithm).
    """

    # Recursive builder. `X if cond else Y` is a conditional expression: it
    # evaluates to None for an empty description, otherwise to a new
    # TreeNode whose children are built recursively. t[0], t[1], t[2] index
    # the tuple's value, left description and right description.
    def build(t):
        return None if t is None else TreeNode(t[0],build(t[1]),build(t[2]))
    return is_balanced_nodes(build(tree))


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 115–116)
# -------------------------------------------------
# The program is a postorder traversal, except that some recursive calls
# may be skipped because of early termination: whenever a left subtree is
# found not to be height-balanced, the matching right subtree need not be
# visited at all.
#
# Space: the call stack holds one frame per node on the path from the root
# to the node currently being processed, so its depth is bounded by the
# tree height h, giving O(h) space.
#
# Time: the same as a postorder traversal, O(n).
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Write a program that
# returns the size of the largest subtree that is complete.
#
# Variant 2 (stated in the book; no solution given): Call a node k-balanced
# if the number of nodes in its left subtree and the number of nodes in its
# right subtree differ by no more than k. Given a binary tree and a positive
# integer k, return a node that is not k-balanced but all of whose
# descendants are k-balanced. Example from the book: for the binary tree of
# Figure 9.1 (page 112) and k = 3, the answer is node J.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def is_balanced_binary_tree(tree)` with a nested
#   `check_balanced(tree)` that returns a
#   collections.namedtuple('BalancedStatusWithHeight', ('balanced',
#   'height')); empty tree -> (True, -1); unbalanced -> (False, 0).
# - File: the algorithm is in `is_balanced_nodes(root: TreeNode | None)`
#   with a nested `height(node)` that returns an int; -1 is the
#   "unbalanced" sentinel and an empty tree has height 0 (book: -1). No
#   collections/namedtuple import is used.
# - File: the book's early exit after an unbalanced left subtree is kept;
#   the right-subtree check and the height-difference check are merged into
#   one `if right < 0 or abs(left-right)>1` statement.
# - File: the name `is_balanced_binary_tree` is reused for a helper not in
#   the book that takes nested (value, left, right) tuples (parameter
#   `tree: tuple | None`) and builds TreeNode objects first.
# - File: defines its own `TreeNode` dataclass (data, left, right); the book
#   uses the BinaryTreeNode class from the chapter introduction. Type hints
#   are added throughout.


# Python executes this block only when this source file is run directly
# (for example `python -m epi_python.chapter_09_binary_trees.
# pg_114_is_balanced_binary_tree`). When pytest imports the file, this
# block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases; pytest has the full set.
    # The examples cover an empty tree, a single node, an unbalanced
    # left-leaning chain of three nodes, and a perfect three-node tree.
    #
    # `assert condition` stops the program with an AssertionError if the
    # condition is false; these are quick smoke checks only.
    result=is_balanced_binary_tree(None)
    print('is_balanced_binary_tree', result)
    assert result == True
    result=is_balanced_binary_tree((1, None, None))
    print('is_balanced_binary_tree', result)
    assert result == True
    result=is_balanced_binary_tree((1, (2, (3, None, None), None), None))
    print('is_balanced_binary_tree', result)
    assert result == False
    result=is_balanced_binary_tree((1, (2, None, None), (3, None, None)))
    print('is_balanced_binary_tree', result)
    assert result == True
