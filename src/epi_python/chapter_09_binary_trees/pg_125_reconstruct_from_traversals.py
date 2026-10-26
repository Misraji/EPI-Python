"""EPI Python — Exercise 9.12: Reconstruct a Binary Tree from Traversal Data

Chapter 9: Binary Trees
Textbook: pages 125–127 (printed page numbers; problem on 125, solution and
program on 126, end of program, complexity and variants on 127).

PROBLEM (from the textbook)
---------------------------
"Many different binary trees yield the same sequence of keys in an inorder,
preorder, or postorder traversal. However, given an inorder traversal and
one of any two other traversal orders of a binary tree, there exists a
unique binary tree that yields those orders, assuming each node holds a
distinct key. For example, the unique binary tree whose inorder traversal
sequence is <F, B, A, E, H, C, D, I, G> and whose preorder traversal
sequence is <H, B, F, E, A, C, D, G, I> is given in Figure 9.5."

(Figure 9.5, "A binary tree—edges that do not terminate in nodes denote
empty subtrees": root H; H's left child B has left child F and right child
E; E's left child is A; H's right child C has right child D; D's right
child is G; G's left child is I.)

"Given an inorder traversal sequence and a preorder traversal sequence of a
binary tree write a program to reconstruct the tree. Assume each node has a
unique key."

HINT (from the textbook)
------------------------
"Focus on the root."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Truly brute force: enumerate every binary tree whose inorder sequence is
the given one and test whether its preorder sequence matches. The
complexity is enormous.

Insight 1: the first entry of the preorder sequence is the root's key.
Locating it in the inorder sequence splits the inorder sequence into the
left subtree's inorder sequence, then the root, then the right subtree's
inorder sequence.

Insight 2: the left subtree's preorder sequence can be cut out of the whole
preorder sequence. A preorder sequence is the root, followed by the left
subtree's preorder sequence, followed by the right subtree's. The root's
position in the inorder sequence tells us the number k of nodes in the left
subtree, so the k entries after the root in the preorder sequence are the
left subtree's preorder sequence (and the rest belong to the right
subtree).

Worked example from the book (Figure 9.5): the root is H, the first
preorder entry. In the inorder sequence, the root's left subtree is
<F, B, A, E>. So the four entries after H in the preorder sequence,
<B, F, E, A>, form the left subtree's preorder sequence. The right subtree
is handled the same way, and the construction continues recursively down to
the leaves.

Cost: done naively this is O(n^2), the worst case being a skewed tree,
because finding the root in an inorder sequence takes O(n). This improves
by first building a hash table from each key to its index in the inorder
sequence, which is the approach of the book's program
`binary_tree_from_preorder_inorder(preorder, inorder)`. Its helper builds
the subtree for preorder[preorder_start:preorder_end] and
inorder[inorder_start:inorder_end]: return None for an empty range; look up
the root's inorder index; compute the left subtree size; recursively build
the left and right subtrees from the corresponding sub-ranges.

This file's `reconstruct_from_preorder_inorder` uses the same hash-table
idea with a simplified recursion (see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    preorder [2, 1, 3], inorder [1, 2, 3]
        -> (2, (1, None, None), (3, None, None))
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


# `list[int]` is a type hint for "list of ints" (not enforced).
def reconstruct_from_preorder_inorder(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """Rebuild binary tree with distinct keys from matching preorder/inorder arrays.

    This file's version of the textbook's binary_tree_from_preorder_inorder
    program (pages 126–127). Adds input validation not in the book.
    """

    # Added check (not in the book). `len()` gives the length; `set(seq)`
    # builds a set of the distinct items (order and duplicates discarded),
    # so `set(a) != set(b)` is True when the two lists hold different keys.
    # `raise ValueError(...)` signals invalid input with the built-in
    # exception for "right type, bad value":
    # https://docs.python.org/3/library/exceptions.html#ValueError
    if len(preorder) != len(inorder) or set(preorder) != set(inorder):
        raise ValueError("Traversals must contain the same unique keys")

    # The book's hash table from key to inorder index, built with a
    # dictionary comprehension. Built-in `enumerate(inorder)` yields
    # (index, item) pairs: (0, inorder[0]), (1, inorder[1]), ...
    # https://docs.python.org/3/library/functions.html#enumerate
    # If a key repeats, a later index overwrites an earlier one, so the
    # dictionary ends up smaller than the list; the next check uses that.
    indices = {key: i for i,key in enumerate(inorder)}
    if len(indices) != len(inorder):
        raise ValueError("Distinct keys are needed for unambiguous reconstruction")

    # Index of the next unused preorder entry. Preorder lists each root
    # before its left subtree and then its right subtree, and construct()
    # builds in exactly that order, so the entries are consumed left to
    # right and no preorder range needs to be passed around.
    position = 0

    # Builds the subtree whose inorder sequence is inorder[lo:hi] (lo
    # inclusive, hi exclusive).
    def construct(lo, hi):

        # `nonlocal position` lets this nested function reassign the
        # enclosing function's variable `position` (without it,
        # `position += 1` would create a new local variable and fail).
        # https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement
        nonlocal position

        # Empty inorder range: empty subtree.
        if lo >= hi:
            return None

        # The next preorder entry is this subtree's root.
        key = preorder[position]
        position += 1

        # Root's position in the inorder sequence, found in O(1) via the
        # hash table: everything in [lo, mid) is the left subtree and
        # everything in [mid + 1, hi) the right subtree.
        mid = indices[key]
        node = TreeNode(key)

        # Order matters: the left subtree must be built first, because its
        # keys come first in the remaining preorder sequence.
        node.left = construct(lo, mid)
        node.right = construct(mid + 1, hi)
        return node
    return construct(0, len(inorder))


def reconstruct_tree(preorder: list[int], inorder: list[int]):
    """Convenience wrapper (not in the textbook): reconstruct, then return
    the tree as nested (value, left, right) tuples."""
    return nested_tree(reconstruct_from_preorder_inorder(preorder, inorder))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 127)
# -------------------------------------------
# Time: O(n). Building the hash table takes O(n), and the recursive
# reconstruction spends O(1) per node.
# Space: O(n + h) = O(n): the hash table plus the maximum depth of the
# function call stack.
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Solve the same problem
# with an inorder traversal sequence and a postorder traversal sequence.
#
# Variant 2 (stated in the book; no solution given): Let A be an array of n
# distinct integers and m the index of its maximum element. The max-tree on
# A is the binary tree on A's entries whose root holds the maximum element
# of A, whose left child is the max-tree on A[0, m - 1], and whose right
# child is the max-tree on A[m + 1, n - 1]. Design an O(n) algorithm for
# building the max-tree of A.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def binary_tree_from_preorder_inorder(preorder, inorder)`; file:
#   `reconstruct_from_preorder_inorder(preorder: list[int], inorder:
#   list[int]) -> TreeNode | None`.
# - Book's map is `node_to_inorder_idx = {data: i for i, data in
#   enumerate(inorder)}`; file's is `indices = {key: i for i,key in
#   enumerate(inorder)}` (same).
# - Book's helper `binary_tree_from_preorder_inorder_helper(preorder_start,
#   preorder_end, inorder_start, inorder_end)` passes both preorder and
#   inorder ranges, computes `left_subtree_size`, and returns
#   `BinaryTreeNode(preorder[preorder_start], <left>, <right>)` in one
#   expression. File's nested `construct(lo, hi)` passes only the inorder
#   range and instead consumes preorder entries with a shared counter
#   `position` updated via `nonlocal`; nodes are created first and children
#   assigned afterwards.
# - File adds input validation (length/key-set mismatch and duplicate keys
#   raise ValueError); the book has none.
# - Not in the book: `build_tree`, `nested_tree`, `reconstruct_tree`;
#   `TreeNode` imported from the 9.1 module instead of BinaryTreeNode.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Preorder [2, 1, 3] says the root is 2; inorder [1, 2, 3] puts 1 to
    # its left and 3 to its right. The result is shown as nested tuples.
    result=reconstruct_tree([2,1,3],[1,2,3])
    print("reconstructed:", result)

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert result==(2,(1,None,None),(3,None,None))
