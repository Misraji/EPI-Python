"""EPI Python — Exercise 9.13: Reconstruct a Binary Tree from a Preorder Traversal with Markers

Chapter 9: Binary Trees
Textbook: pages 127–128 (printed page numbers; problem, solution and
program on 127; complexity and variant on 128).

PROBLEM (from the textbook)
---------------------------
"Many different binary trees have the same preorder traversal sequence.

In this problem, the preorder traversal computation is modified to mark
where a left or right child is empty. For example, the binary tree in
Figure 9.5 on Page 125 yields the following preorder traversal sequence:

    <H, B, F, null, null, E, A, null, null, null, C, null, D, null, G, I,
     null, null, null>

Design an algorithm for reconstructing a binary tree from a preorder
traversal visit sequence that uses null to mark empty children."

(Figure 9.5: root H; H's left child B has children F and E; E's left child
is A; H's right child C has right child D; D's right child G has left
child I.)

HINT (from the textbook)
------------------------
"It's difficult to solve this problem by examining the preorder traversal
visit sequence from left-to-right."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: enumerate all binary trees and compare each one's preorder
sequence with the given sequence; the time complexity is unacceptable.

Intuition for a better algorithm: the first entry of the sequence is the
root, and the root's left subtree sequence appears before every node of the
root's right subtree. Where the left subtree's portion ends is not obvious
by inspection. But solved recursively, we may assume the recursive call
correctly builds the left subtree, and in doing so it also reveals where the
right subtree begins (the right subtree starts with whatever the left call
did not consume).

The book's program `reconstruct_preorder(preorder)` passes a single
iterator over the sequence to a recursive helper:
  1. Take the next key from the iterator; if it is null (None), return an
     empty subtree.
  2. Otherwise build the left subtree, then the right subtree, each by a
     recursive call on the same iterator. The book stresses that the order
     of these two calls is critical, because each call advances the shared
     iterator.
  3. Return a node with that key and those two subtrees.

This file's `reconstruct_preorder_with_null` follows the same design and
adds input validation.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 2, None, None, 3, None, None] -> (1, (2, None, None), (3, None, None))
    [None]                            -> None (empty tree)
    [1, None]                         -> ValueError (truncated sequence)
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


# `list[int | None]`: type hint for a list whose items are ints or None
# (None is the "null" marker). Not enforced at run time.
def reconstruct_preorder_with_null(preorder: list[int | None]) -> TreeNode | None:
    """Deserialize preorder sequence where None represents each empty child.

    This file's version of the textbook's reconstruct_preorder program
    (page 127), with added checks for truncated or over-long input.
    """

    # Built-in `iter(iterable)` returns an iterator: an object that hands
    # out the items one at a time and remembers its position. Every call
    # below shares this one iterator, so each entry is consumed exactly once.
    # https://docs.python.org/3/library/functions.html#iter
    cursor = iter(preorder)

    # Recursive helper (book: reconstruct_preorder_helper).
    def read():

        # Built-in `next(iterator)` returns the next item; when none are
        # left it raises StopIteration. That would mean the sequence ended
        # in the middle of a subtree, so it is reported as a ValueError.
        # `try`/`except` catches the exception; `raise ... from None`
        # raises the new exception while hiding the original StopIteration
        # from the traceback (exception chaining suppressed).
        # https://docs.python.org/3/library/functions.html#next
        # https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
        try:
            value = next(cursor)
        except StopIteration:
            raise ValueError("Truncated preorder sequence") from None

        # A marker means an empty child.
        if value is None:
            return None
        node = TreeNode(value)

        # The order of these two calls is critical: each advances the shared
        # iterator, and in preorder the left subtree's entries come first.
        node.left = read()
        node.right = read()
        return node
    root = read()

    # Added check (not in the book): `next(iterator, default)` returns the
    # default (here None) instead of raising when the iterator is
    # exhausted. A non-None leftover means extra keys after a complete tree.
    # Edge case: a leftover None marker returns None and is not reported.
    if next(cursor, None) is not None:
        raise ValueError("Extraneous trailing values")
    return root


def reconstruct_marked_tree(preorder: list[int | None]):
    """Convenience wrapper (not in the textbook): reconstruct, then return
    the tree as nested (value, left, right) tuples."""
    return nested_tree(reconstruct_preorder_with_null(preorder))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 128)
# -------------------------------------------
# The time complexity is O(n), n being the number of nodes in the tree.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Solve the same problem
# when the sequence corresponds to a postorder traversal sequence. Is this
# problem solvable when the sequence corresponds to an inorder traversal
# sequence?


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def reconstruct_preorder(preorder)` with nested
#   `reconstruct_preorder_helper(preorder_iter)` that receives the iterator
#   as a parameter, and a final `return reconstruct_preorder_helper(
#   iter(preorder))`. File: `reconstruct_preorder_with_null(preorder:
#   list[int | None]) -> TreeNode | None` stores the iterator in `cursor`
#   and the nested `read()` takes no parameters (it uses the enclosing
#   variable).
# - Book: `subtree_key = next(preorder_iter)` with no error handling; file
#   wraps `next` in try/except and raises ValueError("Truncated preorder
#   sequence"). File also raises ValueError for trailing non-None values;
#   neither check is in the book.
# - Book builds `BinaryTreeNode(subtree_key, left_subtree, right_subtree)`
#   after both calls; file creates `TreeNode(value)` first and assigns
#   `node.left` / `node.right` afterwards (same call order).
# - Not in the book: `build_tree`, `nested_tree`,
#   `reconstruct_marked_tree`; `TreeNode` imported from the 9.1 module.
#   Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Root 1, left leaf 2, right leaf 3: each leaf is followed by two None
    # markers for its empty children.
    example=[1,2,None,None,3,None,None]
    print("preorder with null markers:", reconstruct_marked_tree(example))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert reconstruct_marked_tree(example) == (1,(2,None,None),(3,None,None))
