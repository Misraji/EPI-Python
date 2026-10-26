"""EPI Python — Exercise 9.9: Compute the kth Node in an Inorder Traversal

Chapter 9: Binary Trees
Textbook: pages 122–123 (printed page numbers; problem, solution and
program on 122; the program's last line and the complexity on 123).

PROBLEM (from the textbook)
---------------------------
"It is trivial to find the kth node that appears in an inorder traversal
with O(n) time complexity, where n is the number of nodes. However, with
additional information on each node, you can do better.

Write a program that efficiently computes the kth node appearing in an
inorder traversal. Assume that each node stores the number of nodes in the
subtree rooted at that node."

HINT (from the textbook)
------------------------
"Use the divide and conquer principle."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: do an inorder walk, counting visited nodes, and stop at the
kth. This is O(n); e.g. in a left-skewed tree, finding the first node
(k = 1) already requires passing through every node.

The brute force ignores the size stored in each node. If k exceeds the
number of nodes in the left subtree, the kth node cannot be there. More
precisely, if the left subtree has L nodes, then the kth node of the whole
tree is the (k - L)th node once the left subtree is skipped (counting the
root as the first node after it). Conversely, if k <= L, the answer lies in
the left subtree. Book example (Figure 9.1, page 112): the root's left
subtree has seven nodes, so the tenth node is not in the left subtree; it
is the third node once the left subtree is skipped.

The book's program `find_kth_node_binary_tree(tree, k)` loops down the
tree:
  - If L + 1 < k: the node is in the right subtree; reduce k by L + 1 and
    go right.
  - If L == k - 1: the current node is the kth node; return it.
  - Otherwise: the node is in the left subtree; go left.
  - Falling out of the loop returns None, which the book notes is
    unreachable when 1 <= k <= tree size.

This file's `kth_node_inorder` implements the same three-way decision (in a
different order).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (2, (1, None, None), (3, None, None))
    kth_inorder_value(tree, 2) -> 2   (inorder sequence is 1, 2, 3)
"""

# Python standard library: automatically generated special methods for
# classes that mainly store data ("data classes").
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` generates __init__(data, left=None, right=None, size=1),
# __repr__ and __eq__ from the annotated attributes. The extra `size`
# field holds the number of nodes in the subtree rooted here (the extra
# information the problem assumes). Annotations are type hints only, not
# enforced; "SizeNode | None" is a quoted forward reference.
@dataclass
class SizeNode:
    data: int
    left: "SizeNode | None" = None
    right: "SizeNode | None" = None
    size: int = 1


def make_size_tree(tree) -> SizeNode | None:
    """Build SizeNodes from nested (value, left, right) tuples and fill in
    each subtree size. Helper added for testing; not in the textbook."""
    if tree is None:
        return None
    node = SizeNode(tree[0],make_size_tree(tree[1]),make_size_tree(tree[2]))

    # Size = 1 (this node) + sizes of existing children. Each
    # `X if cond else 0` is a conditional expression that substitutes 0 for
    # a missing (None, hence falsy) child.
    node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
    return node


# Type hints: `SizeNode | None` arguments/return (not enforced; `X | Y` in
# a signature needs Python 3.10+).
def kth_node_inorder(root: SizeNode | None, k: int) -> SizeNode | None:
    """Find kth node in inorder traversal (1-based) using subtree sizes.

    This file's version of the textbook's find_kth_node_binary_tree program
    (pages 122–123). Returns None if k is outside 1..tree size.
    """
    while root is not None:

        # L = number of nodes in the left subtree (0 if there is none).
        left_size = root.left.size if root.left else 0

        # Exactly L nodes come before this one, so it is the (L + 1)th.
        if k == left_size + 1:
            return root
        if k <= left_size:
            root = root.left
        else:

            # Skip the left subtree and this node: k drops by L + 1.
            k -= left_size + 1
            root = root.right
    return None


def kth_inorder_value(tree, k: int) -> int | None:
    """Convenience wrapper (not in the textbook): build the tree and
    return the kth inorder node's data, or None."""
    node = kth_node_inorder(make_size_tree(tree), k)
    return None if node is None else node.data


# TEXTBOOK POST-SOLUTION DISCUSSION (page 123)
# -------------------------------------------
# Each loop iteration moves one level down the tree, so the time complexity
# is O(h), h being the tree height. (The iterative loop uses O(1) extra
# space.)
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def find_kth_node_binary_tree(tree, k)`; file:
#   `kth_node_inorder(root: SizeNode | None, k: int) -> SizeNode | None`.
# - Book loops `while tree:` and tests in the order
#   `if left_size + 1 < k:` (go right, `k -= left_size + 1`),
#   `elif left_size == k - 1:` (return), `else:` (go left). File loops
#   `while root is not None:` and tests `if k == left_size + 1:` (return),
#   `if k <= left_size:` (go left), `else:` (go right). Same logic.
# - The book's comment that the final `return None` is unreachable for a
#   valid k is not in the file.
# - Not in the book: the `SizeNode` dataclass (book assumes nodes with a
#   `size` field), `make_size_tree`, `kth_inorder_value`. Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Root 2 with children 1 and 3: the inorder sequence is 1, 2, 3, so
    # the 2nd node is the root (its left subtree has exactly one node).
    tree=(2,(1,None,None),(3,None,None))
    print("2nd inorder:", kth_inorder_value(tree,2))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert kth_inorder_value(tree,2)==2
