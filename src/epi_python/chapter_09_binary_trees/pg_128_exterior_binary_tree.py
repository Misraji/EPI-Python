"""EPI Python — Exercise 9.15: Compute the Exterior of a Binary Tree

Chapter 9: Binary Trees
Textbook: pages 128–129 (printed page numbers; problem and start of the
solution on 128; rest of the solution, program and complexity on 129).

PROBLEM (from the textbook)
---------------------------
"The exterior of a binary tree is the following sequence of nodes: the nodes
from the root to the leftmost leaf, followed by the leaves in left-to-right
order, followed by the nodes from the rightmost leaf to the root. (By
leftmost (rightmost) leaf, we mean the leaf that appears first (last) in an
inorder traversal.) For example, the exterior of the binary tree in Figure
9.1 on Page 112 is <A, B, C, D, E, H, M, N, P, O, I>.

Write a program that computes the exterior of a binary tree."

HINT (from the textbook)
------------------------
"Handle the root's left child and right child in mirror fashion."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force by case analysis: three sequences are needed, the nodes on the
path from the root to the leftmost leaf, the nodes on the path from the
root to the rightmost leaf, and the leaves in left-to-right order.
  - The leaves in order are computed as in Solution 9.14.
  - The path to the leftmost leaf: from each node go left if there is a
    left child, otherwise go right; the leaf where this stops is the
    leftmost leaf. The rightmost path is computed symmetrically.
  - Time: O(h + n + h) = O(n), n nodes and height h.
The implementation is a little tricky because some nodes appear in more
than one sequence. Book example (Figure 9.1): the root-to-leftmost-leaf
path is <A, B, C, D>, the leaves in order are <D, E, H, M, N, P>, and the
root-to-rightmost-leaf path is <A, I, O, P>; the leftmost leaf D, the
rightmost leaf P and the root A each appear in two sequences.

Simplification used by the book's program: compute the left boundary
(root-to-leftmost-leaf path) together with the leaves of the left subtree
in one traversal; then, in a second traversal, compute the leaves of the
right subtree followed by the right boundary from the rightmost leaf back
up to the root. For Figure 9.1, the first traversal returns
<B, C, D, E, H> and the second returns <M, N, P, O, I>; the answer is <A>
followed by the first and then the second sequence.

The book's program `exterior_binary_tree(tree)` has helpers `is_leaf`,
`left_boundary_and_leaves(subtree, is_boundary)` (a node is included if it
is on the boundary or is a leaf; its right child stays on the boundary only
when it has no left child) and the mirror-image
`right_boundary_and_leaves(subtree, is_boundary)`.

This file's `exterior_binary_tree` produces the same sequence using a
different structure (see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (1, (2, (4, None, None), None), (3, None, (5, None, None)))
        -> [1, 2, 4, 5, 3]   (root, left boundary 2, leaves 4 and 5,
                              right boundary 3 on the way back up)
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


# `-> list[int]`: type hint for "list of ints" (not enforced).
def exterior_binary_tree(root: TreeNode | None) -> list[int]:
    """Return root, left boundary, leaves and reversed right boundary without duplicates.

    This file's version of the textbook's exterior_binary_tree program
    (page 129). It returns node data values (the book returns nodes) and
    computes the boundaries with loops instead of the book's two recursive
    helpers.
    """
    if root is None:
        return []

    # A single-node tree: the root is also the only leaf; list it once.
    if root.left is None and root.right is None:
        return [root.data]
    exterior = [root.data]

    # Left boundary (root's left subtree down to the leftmost leaf): go
    # left when possible, otherwise right. Only non-leaf nodes are added
    # here; the leftmost leaf is added later with the other leaves, which
    # avoids listing it twice.
    node = root.left
    while node is not None:
        if node.left is not None or node.right is not None:
            exterior.append(node.data)

        # Conditional expression choosing the next node on the boundary.
        node = node.left if node.left is not None else node.right

    # Nested recursive helper that appends every leaf of a subtree, left
    # subtree before right, so leaves come out in left-to-right order.
    # (It mutates the enclosing list with append(), which needs no
    # `nonlocal` because the name `exterior` is never reassigned.)
    def leaves(node):
        if node is None:
            return
        if node.left is None and node.right is None:
            exterior.append(node.data)
            return
        leaves(node.left)
        leaves(node.right)
    leaves(root.left)
    leaves(root.right)

    # Right boundary, collected top-down (mirror image: go right when
    # possible, otherwise left), again skipping the rightmost leaf.
    right_boundary = []
    node = root.right
    while node is not None:
        if node.left is not None or node.right is not None:
            right_boundary.append(node.data)
        node = node.right if node.right is not None else node.left

    # The exterior lists the right boundary bottom-up. Built-in
    # `reversed(seq)` returns an iterator over the items in reverse order
    # (it does not copy or modify the list), and `list.extend(iterable)`
    # appends each of those items.
    # https://docs.python.org/3/library/functions.html#reversed
    # https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    exterior.extend(reversed(right_boundary))
    return exterior


def exterior_values(tree) -> list[int]:
    """Convenience wrapper (not in the textbook): build the tree from
    nested tuples and call exterior_binary_tree."""
    return exterior_binary_tree(build_tree(tree))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 129)
# -------------------------------------------
# The time complexity is O(n).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def exterior_binary_tree(tree)` with nested `is_leaf(node)`,
#   `left_boundary_and_leaves(subtree, is_boundary)` and
#   `right_boundary_and_leaves(subtree, is_boundary)`, each a single
#   recursive expression built by list concatenation; final
#   `return ([tree] + left_boundary_and_leaves(tree.left,
#   is_boundary=True) + right_boundary_and_leaves(tree.right,
#   is_boundary=True) if tree else [])`. It returns tree *nodes*.
# - File: `exterior_binary_tree(root: TreeNode | None) -> list[int]`
#   returns node *data*; it special-cases a single-node tree, walks each
#   boundary with a `while` loop (adding only non-leaf boundary nodes),
#   gathers all leaves with a separate nested `leaves` helper over the left
#   then right subtree, and appends the right boundary with
#   `exterior.extend(reversed(right_boundary))`. No `is_leaf` or
#   `is_boundary` parameters. The book does left boundary + left leaves in
#   one pass and right leaves + right boundary in another; the file uses
#   four separate steps.
# - Not in the book: `build_tree`, `nested_tree`, `exterior_values`;
#   `TreeNode` imported from the 9.1 module. Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Root 1; left boundary 2 -> leaf 4; right boundary 3 -> leaf 5. The
    # exterior is root, left boundary, leaves, right boundary reversed.
    tree=(1,(2,(4,None,None),None),(3,None,(5,None,None)))
    print("exterior:", exterior_values(tree))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert exterior_values(tree)==[1,2,4,5,3]
