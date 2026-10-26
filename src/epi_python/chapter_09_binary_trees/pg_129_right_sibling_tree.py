"""EPI Python — Exercise 9.16: Compute the Right Sibling Tree

Chapter 9: Binary Trees
Textbook: pages 129–131 (printed page numbers; problem starts at the foot
of 129, Figure 9.6, solution and program on 130, Figure 9.7, complexity and
variants on 131).

PROBLEM (from the textbook)
---------------------------
"For this problem, assume that each binary tree node has a extra field, call
it level-next, that holds a binary tree node (this field is distinct from
the fields for the left and right children). The level-next field will be
used to compute a map from nodes to their right siblings. The input is
assumed to be perfect binary tree. See Figure 9.6 for an example.

Write a program that takes a perfect binary tree, and sets each node's
level-next field to the node on its right, if one exists."

(Figure 9.6: a perfect binary tree with levels A; B, I; C, F, J, M;
D, E, G, H, K, L, N, O. Dashed arrows show the level-next values after the
update: B -> I; C -> F -> J -> M; D -> E -> G -> H -> K -> L -> N -> O. The
book notes that no arrow leaves A, I, M and O, the nodes on the path from
the root to the rightmost leaf, since they have no right siblings.)

HINT (from the textbook)
------------------------
"Think of an appropriate traversal order."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: compute every node's depth and store it in a hash table; order
the nodes of each depth by their inorder visit times; then set each node's
level-next field from that order. Time and space are both O(n), n being
the number of nodes.

Key insight for better space: use the structure of a perfect tree.
  - A node that is a left child has as its right sibling simply its
    parent's right child.
  - A node that is a right child has as its right sibling the left child
    of its parent's right sibling.
Book examples (Figure 9.6): C is B's left child, so C's right sibling is
B's right child, F. F is B's right child, so F's right sibling is the left
child of B's right sibling, i.e. J.

For this to work, nodes must be processed level by level, left to right.
Walking along a level whose level-next fields are already set is trivial
(just follow level-next). While walking a level, set the level-next fields
of the level below using the two rules above. To move on, remember the
first node of each level; when the level is finished, the next level starts
at that node's left child.

The book's program `construct_right_sibling(tree)` has a nested
`populate_children_next_field(start_node)` that walks one level and links
the children, and an outer loop that moves to the next level via `.left`.
This file's `construct_right_sibling` follows the same method with the
two loops inlined.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (1, (2, None, None), (3, None, None))
    level-order (node, right sibling): [(1, None), (2, 3), (3, None)]
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque

# Python standard library: automatically generated special methods for
# classes that mainly store data ("data classes").
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` generates __init__(data, left=None, right=None, next=None),
# __repr__ and __eq__ from the annotated attributes. The `next` field is
# the book's level-next field (the right sibling); naming an attribute
# `next` does not interfere with the built-in function next(). Annotations
# are type hints only (not enforced); "SiblingNode | None" is a quoted
# forward reference.
@dataclass
class SiblingNode:
    data: int
    left: "SiblingNode | None" = None
    right: "SiblingNode | None" = None
    next: "SiblingNode | None" = None


def make_sibling_tree(tree):
    """Build SiblingNodes (next = None) from nested (value, left, right)
    tuples. Helper added for testing; not in the textbook."""
    if tree is None:
        return None
    return SiblingNode(tree[0], make_sibling_tree(tree[1]), make_sibling_tree(tree[2]))


# Type hints: `SiblingNode | None` (not enforced; `X | Y` in a signature
# needs Python 3.10+).
def construct_right_sibling(root: SiblingNode | None) -> SiblingNode | None:
    """Link immediate neighbors at each depth in a perfect binary tree.

    This file's version of the textbook's construct_right_sibling program
    (page 130). Modifies the tree in place and also returns the root.
    Assumes a perfect binary tree (every non-leaf has two children), as the
    problem states.
    """

    # `level` is the first (left-most) node of the current level. Continue
    # while that level has children, i.e. it is not the leaf level.
    level = root
    while level is not None and level.left is not None:

        # Walk across the current level using the next fields already set
        # (the root level has only one node).
        current = level
        while current is not None:

            # A left child's right sibling is its parent's right child.
            current.left.next = current.right

            # A right child's right sibling is the left child of its
            # parent's right sibling, if the parent has one; otherwise the
            # right child is last in its level and keeps next = None.
            if current.next is not None:
                current.right.next = current.next.left
            current = current.next

        # The next level starts at the left child of this level's first node.
        level = level.left
    return root


# `list[tuple[int, int | None]]`: type hint for a list of 2-tuples whose
# second item is an int or None (not enforced).
def sibling_pairs(tree) -> list[tuple[int, int | None]]:
    """Testing helper (not in the textbook): build the tree, run
    construct_right_sibling, and list (data, right sibling's data or None)
    for every node in level order (breadth-first)."""
    root = construct_right_sibling(make_sibling_tree(tree))
    if root is None:
        return []

    # collections.deque is a double-ended queue: appending or popping at
    # either end is O(1) (popping from the front of a plain list is O(n)).
    # Used here as a FIFO queue for a breadth-first, level-order walk:
    # append() adds at the right end, popleft() removes from the left end.
    # deque([root]) creates a queue initially holding just the root.
    queue = deque([root])
    pairs = []

    # An empty deque is falsy, so the loop ends when the queue drains.
    while queue:
        node = queue.popleft()

        # Conditional expression: the sibling's data, or None if node.next
        # is None (falsy).
        pairs.append((node.data, node.next.data if node.next else None))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return pairs


# TEXTBOOK POST-SOLUTION DISCUSSION (page 131)
# -------------------------------------------
# Each node needs O(1) work, so the time complexity is O(n); the space
# complexity is O(1).
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Solve the same problem
# when there is no level-next field; the result should be stored in the
# right child field.
#
# Variant 2 (stated in the book; no solution given): Solve the same problem
# for a general binary tree. The book's Figure 9.7 example: root A with
# children B and D; B's left child C; D's children E and G; E's left child
# F; G's children H and I. After the update: B -> D; C -> E -> G;
# F -> H -> I.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def construct_right_sibling(tree)` with a nested helper
#   `populate_children_next_field(start_node)` and the outer loop
#   `while tree and tree.left: populate_children_next_field(tree);
#   tree = tree.left`; it returns nothing. File:
#   `construct_right_sibling(root: SiblingNode | None) -> SiblingNode |
#   None` inlines the helper as an inner `while current is not None:` loop
#   (variables `level`, `current`) and returns the root.
# - Book sets the right child unconditionally with
#   `start_node.right.next = start_node.next and start_node.next.left`
#   (evaluates to None when there is no next node); file uses
#   `if current.next is not None: current.right.next = current.next.left`.
#   Same effect, since next fields start as None.
# - Book's inner loop condition `while start_node and start_node.left:`;
#   file's inner loop only checks `current is not None` (the outer loop
#   already established that this level has children, valid for a
#   perfect tree).
# - Book's level-next field is called `next`; the file's SiblingNode
#   dataclass uses the same name.
# - Not in the book: `SiblingNode`, `make_sibling_tree`, `sibling_pairs`
#   (which imports collections.deque only for checking results). Type
#   hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # A perfect three-node tree: 2's right sibling is 3; the root and 3
    # have none. Pairs are listed in level order.
    tree=(1,(2,None,None),(3,None,None))
    print("right siblings:", sibling_pairs(tree))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert sibling_pairs(tree)==[(1,None),(2,3),(3,None)]
