"""EPI Python — Exercise 9.10: Compute the Successor

Chapter 9: Binary Trees
Textbook: pages 123–124 (printed page numbers; problem, solution and
program on 123; the program's last line and the complexity on 124).

PROBLEM (from the textbook)
---------------------------
"The successor of a node in a binary tree is the node that appears
immediately after the given node in an inorder traversal. For example, in
Figure 9.1 on Page 112, the successor of G is A, and the successor of A is
J.

Design an algorithm that computes the successor of a node in a binary tree.
Assume that each node stores its parent."

HINT (from the textbook)
------------------------
"Study the node's right subtree. What if the node does not have a right
subtree?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: run an inorder walk and stop at the first node visited after
the given one; O(n) time for n nodes.

Case 1 — the node has a nonempty right subtree. Then its successor lies in
that subtree and nothing else in the tree matters. Book examples (Figure
9.1): whatever A's left subtree looks like, A's successor must be in the
subtree rooted at I; likewise B's successor is in the subtree rooted at F.
The successor is the first node an inorder traversal of that right subtree
visits, i.e. its "left-most" node, found by following left children until
there is no left child.

Case 2 — the node has no right subtree (e.g. H in Figure 9.1).
  - If it is its parent's left child, the parent is visited next and is
    the successor (G is H's successor).
  - If it is its parent's right child (e.g. G), the parent has already
    been visited. So keep following parent links, stopping when the move
    up is made from a left child. From G we go to F, then B, then A; we
    stop at A because B is A's left child, so A is G's successor.
  - The climb may reach the root without ever moving up from a left
    child. That happens exactly when the node is the last in inorder, so it
    has no successor; node P in Figure 9.1 is such a case.

The book's program `find_successor(node)` implements both cases; this
file's `inorder_successor` follows it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (2, (1, None, None), (3, None, None))
    successor of 1 -> 2 (1 is a left child with no right subtree)
    successor of 2 -> 3 (left-most node of 2's right subtree)
    successor of 3 -> None (last node in inorder)
"""

# Local project import (not the standard library): reuse, from this
# chapter's Exercise 9.4 module, the ParentNode dataclass (data, left,
# right, parent), build_parent_tree (nested tuples -> linked ParentNodes
# with parent links set) and find_node (search for a node by key).
# Import system documentation: https://docs.python.org/3/reference/import.html
# `from ... import` statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_09_binary_trees.pg_118_lca_with_parent import ParentNode, build_parent_tree, find_node


# Type hints: argument and result are a ParentNode or None (not enforced;
# `X | Y` in a signature needs Python 3.10+).
def inorder_successor(node: ParentNode | None) -> ParentNode | None:
    """Find next node of inorder traversal without inspecting node keys.

    This file's version of the textbook's find_successor program
    (pages 123–124). Returns None if the node is the rightmost node (no
    successor), or if `node` itself is None (an addition not in the book).
    """
    if node is None:
        return None

    # Case 1: the successor is the left-most node in the right subtree.
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        return node

    # Case 2: find the closest ancestor whose left subtree contains node.
    # Climb while we are the right child of our parent; `is` compares
    # object identity, which is exactly "this very node is that child".
    # `and` short-circuits, so node.parent.right is never evaluated when
    # node.parent is None.
    while node.parent is not None and node.parent.right is node:
        node = node.parent

    # Either the parent reached from a left child (the successor) or None
    # when we climbed past the root (node was the last in inorder).
    return node.parent


def inorder_successor_value(tree, key: int) -> int | None:
    """Convenience wrapper (not in the textbook): build the tree, find the
    node with `key`, and return its successor's data or None."""
    root = build_parent_tree(tree)
    candidate = inorder_successor(find_node(root,key))
    return None if candidate is None else candidate.data


# TEXTBOOK POST-SOLUTION DISCUSSION (page 124)
# -------------------------------------------
# The number of edges followed can never exceed the tree height, so the
# time complexity is O(h), h being the height. (Extra space is O(1).)
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def find_successor(node)`; file:
#   `inorder_successor(node: ParentNode | None) -> ParentNode | None`.
# - File adds an initial `if node is None: return None` guard not in the
#   book.
# - Book uses truthiness tests (`if node.right:`, `while node.left:`,
#   `while node.parent and node.parent.right is node:`); file uses explicit
#   `is not None` comparisons. Same logic and same `return node.parent`.
# - The book's comments (left-most element of right subtree; closest
#   ancestor whose left subtree contains node; None means rightmost node)
#   are paraphrased in the file's comments.
# - Not in the book: `inorder_successor_value`; `ParentNode`,
#   `build_parent_tree` and `find_node` are imported from the 9.4 module.
#   Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Root 2 with children 1 and 3: node 1 has no right subtree and is a
    # left child, so its successor is its parent, 2.
    tree=(2,(1,None,None),(3,None,None))
    print("successor of 1:", inorder_successor_value(tree,1))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert inorder_successor_value(tree,1) == 2
