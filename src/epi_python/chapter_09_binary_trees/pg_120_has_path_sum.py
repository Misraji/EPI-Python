"""EPI Python — Exercise 9.6: Find a Root to Leaf Path with Specified Sum

Chapter 9: Binary Trees
Textbook: page 120 (printed page number; problem, solution, complexity and
variant are all on page 120).

PROBLEM (from the textbook)
---------------------------
"You are given a binary tree where each node is labeled with an integer. The
path weight of a node in such a tree is the sum of the integers on the
unique path from the root to that node. For the example shown in Figure 9.1
on Page 112, the path weight of E is 591.

Write a program which takes as input an integer and a binary tree with
integer node weights, and checks if there exists a leaf whose path weight
equals the given integer."

HINT (from the textbook)
------------------------
"What do you need to know about the rest of the tree when checking a
specific subtree?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: the brute-force method of Solution 9.5 (record parents in a
hash table, then walk up from every leaf summing as you go) applies
directly. Its cost is the same: O(Lh) time, L being the number of
root-to-leaf paths (= number of leaves) and h the height, and O(n) space
dominated by the hash table, n being the number of nodes.

Why it is wasteful: paths overlap, and the brute force recomputes the sums
along the shared portions instead of sharing them.

Better: traverse the tree while tracking the *remaining weight*, i.e. the
target minus the sum of the root-to-node path so far. As soon as a leaf is
reached whose weight equals the remaining weight, return True. Because the
two recursive checks are combined with a short-circuiting `or`, once a
matching leaf has been found no further leaves are processed. That is all a
subtree needs to know about the rest of the tree: how much weight is still
required.

The book's program is `has_path_sum(tree, remaining_weight)`; this file's
`has_path_sum` follows it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (5, (2, None, None), (3, None, None))
    target 8 -> True (path 5 -> 3); target 7 -> True (5 -> 2);
    target 5 -> False (the root alone is not a leaf).
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


def has_path_sum(root: TreeNode | None, target: int) -> bool:
    """Check for a complete root-to-leaf path whose values sum to target.

    This file's version of the textbook's has_path_sum(tree,
    remaining_weight) program (page 120); `target` plays the role of the
    book's remaining weight.
    """

    # An empty subtree contains no leaf, so it cannot complete a path.
    if root is None:
        return False

    # Weight still required below this node once its own value is used.
    remainder = target - root.data

    # Leaf: the path matches exactly when nothing remains (equivalent to
    # the book's test "remaining weight == leaf's weight").
    if root.left is None and root.right is None:
        return remainder == 0

    # `or` short-circuits: if the left subtree has a matching leaf, the
    # right subtree is never searched.
    return has_path_sum(root.left, remainder) or has_path_sum(root.right, remainder)


def has_path_sum_values(tree, target: int) -> bool:
    """Convenience wrapper (not in the textbook): build the tree from
    nested tuples and call has_path_sum."""
    return has_path_sum(build_tree(tree), target)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 120)
# -------------------------------------------
# Time complexity O(n) and space complexity O(h) (recursion stack), n being
# the number of nodes and h the height.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): with the same inputs as
# Problem 9.6, return all the paths to leaves whose weight equals s. Book
# example: for s = 619 (tree of Figure 9.1) return
# <<A, B, C, D>, <A, I, O, P>>.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def has_path_sum(tree, remaining_weight)`; file:
#   `has_path_sum(root: TreeNode | None, target: int) -> bool` (parameters
#   renamed, type hints added).
# - Book's leaf test returns `remaining_weight == tree.data` and recurses
#   with `remaining_weight - tree.data` written twice. File computes
#   `remainder = target - root.data` once, before the leaf test, and the
#   leaf returns `remainder == 0`. Same results.
# - Book tests a leaf with `not tree.left and not tree.right`; file uses
#   `is None` comparisons.
# - Not in the book: `build_tree`, `nested_tree`, `has_path_sum_values`;
#   `TreeNode` imported from the 9.1 module.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Root 5 with leaves 2 and 3: the path 5 -> 3 has weight 8.
    tree=(5,(2,None,None),(3,None,None))
    print("has root-leaf path sum 8:", has_path_sum_values(tree, 8))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert has_path_sum_values(tree, 8)
