"""EPI Python — Exercise 9.3: Compute the Lowest Common Ancestor in a Binary Tree

Chapter 9: Binary Trees
Textbook: pages 117–118 (printed page numbers; problem, solution and the
start of the program on 117; the rest of the program and the complexity
on 118).

PROBLEM (from the textbook)
---------------------------
"Any two nodes in a binary tree have a common ancestor, namely the root. The
lowest common ancestor (LCA) of any two nodes in a binary tree is the node
furthest from the root that is an ancestor of both nodes. For example, the
LCA of M and N in Figure 9.1 on Page 112 is K."

The book adds that computing the LCA has important applications, e.g. when
rendering web pages, to compute the Cascading Style Sheet (CSS) that
applies to a given Document Object Model (DOM) element.

"Design an algorithm for computing the LCA of two nodes in a binary tree in
which nodes do not have a parent field."

HINT (from the textbook)
------------------------
"When is the root the LCA?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: check whether the two nodes lie in different immediate
subtrees of the root, or whether one of them is the root; in either case
the root is the LCA. If instead both lie in the left subtree, or both in
the right subtree, recurse into that subtree. This takes O(n^2) time (n =
number of nodes); the worst case is a skewed tree with both nodes at the
bottom, because the "which subtree contains the node" searches are
repeated level after level.

Insight: multiple passes are unnecessary. When both nodes are found inside
a subtree, the recursion can compute the LCA right there, instead of just
returning a Boolean saying "both are in this subtree". The book's program
returns, for each subtree, an object with two fields (a
collections.namedtuple called Status):
  - num_target_nodes: how many of the two target nodes (0, 1 or 2) occur
    in the subtree;
  - ancestor: their LCA, set (non-null) only once both were found.
Steps of the book's helper for a subtree:
  1. Empty subtree -> Status(0, None).
  2. Recurse left; if the left result already has 2 targets, return it
     (both nodes found in the left subtree; its ancestor is the answer).
  3. Recurse right; likewise return it if it has 2 targets.
  4. Otherwise the count is left count + right count + 1 for each target
     that *is* the current node (tested by identity, `is`). If the count is
     2, the current node is the LCA; otherwise ancestor is None.
The top level returns the ancestor field for the root.

This file follows the same postorder structure, but identifies targets by
key value rather than by node identity (see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (4, (2, (1, None, None), (3, None, None)), (6, None, None))
    lca_value(tree, 1, 3) -> 2   (1 and 3 are the two children of 2)
"""

# Local project import (not the standard library): reuse the TreeNode
# dataclass (fields data, left, right; generated __init__) defined in this
# chapter's Exercise 9.1 module, so all files share one node type.
# Import system documentation: https://docs.python.org/3/reference/import.html
# `from ... import` statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_09_binary_trees.pg_114_is_balanced_binary_tree import TreeNode


# Type hints: `tree: tuple | None` means a nested tuple or None, and
# `-> TreeNode | None` the return type. Python does not enforce them; the
# `X | Y` syntax evaluated in a signature needs Python 3.10+.
def build_tree(tree: tuple | None) -> TreeNode | None:
    """Turn nested (value, left, right) tuples into binary tree nodes.

    Helper added for testing; not in the textbook.
    """
    if tree is None:
        return None
    return TreeNode(tree[0], build_tree(tree[1]), build_tree(tree[2]))


def nested_tree(root: TreeNode | None):
    """Inverse of build_tree: TreeNodes back to nested tuples.

    Helper added for testing; not in the textbook.
    """

    # `X if cond else Y` is a conditional expression: None for an empty
    # tree, otherwise a 3-tuple whose children are converted recursively.
    return None if root is None else (root.data, nested_tree(root.left), nested_tree(root.right))


def lowest_common_ancestor(root: TreeNode | None, a: int, b: int) -> TreeNode | None:
    """Find lowest node whose subtree contains two distinct target keys.

    This file's version of the textbook's lca(tree, node0, node1) program
    (pages 117–118). Unlike the book, the two targets are given as key
    values `a` and `b` and are matched by equality of node.data, not by node
    identity. Returns the LCA node, or None if fewer than two targets were
    found.
    """

    # Nested helper corresponding to the book's lca_helper. It returns a
    # plain 2-tuple (count, match) instead of the book's namedtuple
    # Status(num_target_nodes, ancestor).
    def descend(node):
        if node is None:
            return 0, None

        # Tuple unpacking: the returned pair is split into two variables.
        left_count, left_match = descend(node.left)

        # Both targets already found in the left subtree: its match is the
        # LCA, so pass it upward without visiting the right subtree.
        if left_count == 2:
            return left_count, left_match
        right_count, right_match = descend(node.right)
        if right_count == 2:
            return right_count, right_match

        # `node.data in (a, b)` is a bool; in arithmetic Python treats True
        # as 1 and False as 0 (bool is a subclass of int), so this adds 1
        # when the current node holds one of the target keys. Note it adds
        # at most 1 even if a == b.
        found = left_count + right_count + (node.data in (a, b))

        # Conditional expression: this node is the LCA exactly when the
        # count first reaches 2 here.
        return (found, node if found == 2 else None)

    # `[1]` selects the second element (the match) of the returned tuple.
    return descend(root)[1]


def lca_value(tree: tuple | None, a: int, b: int) -> int | None:
    """Convenience wrapper (not in the textbook): build the tree from
    tuples, run lowest_common_ancestor, and return the LCA's key or None."""
    match = lowest_common_ancestor(build_tree(tree), a, b)
    return None if match is None else match.data


# TEXTBOOK POST-SOLUTION DISCUSSION (page 118)
# -------------------------------------------
# The algorithm has the same structure as a recursive postorder traversal,
# and the same complexities: O(n) time and O(h) space, h being the height
# of the tree (the recursion stack).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def lca(tree, node0, node1)` takes two node references and
#   counts a target with `int(tree is node0) + int(tree is node1)` (object
#   identity). File: `lowest_common_ancestor(root: TreeNode | None, a: int,
#   b: int)` takes two key values and counts with
#   `(node.data in (a, b))` (value equality). Consequences: with duplicate
#   keys the file may match different nodes than intended, and when a == b
#   the file never counts 2 at one node (book: node0 is node1 counts 2).
#   The old summary docstring claimed node identity mattered; that was
#   inaccurate for this code.
# - Book's helper `lca_helper(tree, node0, node1)` returns
#   `collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))`;
#   file's nested `descend(node)` returns a plain tuple (count, match). No
#   collections import.
# - Early returns for a count of 2 in the left/right subtree match the book.
# - Helpers not in the book: `build_tree`, `nested_tree`, `lca_value`.
#   `TreeNode` is imported from the 9.1 module rather than the book's
#   BinaryTreeNode. Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # A small tree: 4 at the root, 2 (with children 1 and 3) on the left and
    # 6 on the right. The LCA of 1 and 3 is their parent, 2.
    tree = (4,(2,(1,None,None),(3,None,None)),(6,None,None))
    print("LCA(1,3):", lca_value(tree, 1, 3))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert lca_value(tree,1,3) == 2
