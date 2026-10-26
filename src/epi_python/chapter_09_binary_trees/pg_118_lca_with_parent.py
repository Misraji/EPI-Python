"""EPI Python — Exercise 9.4: Compute the LCA When Nodes Have Parent Pointers

Chapter 9: Binary Trees
Textbook: pages 118–119 (printed page numbers; problem, solution and the
start of the program on 118; end of the program and complexity on 119).

PROBLEM (from the textbook)
---------------------------
"Given two nodes in a binary tree, design an algorithm that computes their
LCA. Assume that each node has a parent pointer."

HINT (from the textbook)
------------------------
"The problem is easy if both nodes are the same distance from the root."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: put every node on the search path from the root to one of the
nodes into a hash table (easy to collect by following parent fields up
from that node). Then climb from the second node, stopping at the first
node that is in the hash table; that node is the LCA. Time and space are
both O(h), h being the tree height.

Better: the two nodes always share an ancestor (the root). If they were at
the same depth, we could climb from both in tandem and stop at the first
node they have in common, which is the LCA. When the depths differ, the
brute force needed the set of visited nodes to recognise the first common
node; that storage can be avoided by first climbing from the deeper node
until it is at the same depth as the shallower one, and only then climbing
in tandem.

Worked example from the book (Figure 9.1, page 112): nodes M and P have
depths 5 and 3. Their search paths are <A, I, J, K, L, M> and
<A, I, O, P>. Climbing from M up to depth 3 reaches K. Climbing from K and
P together, the first common node is I, which is the LCA of M and P.

Depths are simple to compute by following parent fields: O(h) time and
O(1) space. With the depths known, the tandem climb produces the LCA.

The book's program `lca(node_0, node_1)`:
  1. A nested get_depth(node) counts steps up the parent chain.
  2. Swap the nodes if necessary so that node_0 is the deeper one.
  3. Climb from node_0 by the depth difference.
  4. Climb both nodes together while they are different objects; return
     the node where they meet.
This file's `lca_with_parent` implements those steps.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (4, (2, (1, None, None), (3, None, None)), (6, None, None))
    lca_parent_value(tree, 1, 3) -> 2   (1 and 3 are both children of 2)
"""

# Python standard library: automatically generated special methods for
# classes that mainly store data ("data classes").
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` generates __init__(data, left=None, right=None, parent=None),
# __repr__ and __eq__ from the annotated attributes below. Annotations are
# type hints only (not enforced at run time); the quoted "ParentNode | None"
# is a forward reference, since the class is not yet defined while its body
# runs.
#
# Edge case: the generated __eq__ compares all fields, and here children
# point to parents and parents to children. The algorithm therefore compares
# nodes with `is` (identity), never with `==`.
@dataclass
class ParentNode:
    data: int
    left: "ParentNode | None" = None
    right: "ParentNode | None" = None
    parent: "ParentNode | None" = None


def build_parent_tree(tree, parent=None):
    """Build a binary tree with reciprocal child/parent links.

    Helper added for testing (not in the textbook): converts nested
    (value, left, right) tuples into ParentNode objects.
    """
    if tree is None:
        return None

    # `parent=parent` is a keyword argument: it sets the `parent` field
    # while leaving left and right at their default None. The children are
    # then built with this node as their parent.
    node = ParentNode(tree[0], parent=parent)
    node.left = build_parent_tree(tree[1], node)
    node.right = build_parent_tree(tree[2], node)
    return node


def find_node(root, key):
    """Return a node holding `key` (preorder search), or None.

    Helper added for testing; not in the textbook.
    """
    if root is None or root.data == key:
        return root

    # `x or y` returns x if x is truthy, otherwise y. A found node is
    # truthy and None is falsy, so the right subtree is searched only when
    # the left search found nothing.
    return find_node(root.left, key) or find_node(root.right, key)


# Type hints: two ParentNode arguments; returns a ParentNode or None (not
# enforced; `X | Y` in a signature needs Python 3.10+).
def lca_with_parent(a: ParentNode, b: ParentNode) -> ParentNode | None:
    """Align ancestor depths, then walk upwards together.

    This file's version of the textbook's lca(node_0, node_1) program
    (pages 118–119).
    """

    # Nested helper (book: get_depth): count nodes on the parent chain up
    # to and including the root. The root gets depth 1 here; only the
    # difference between the two depths is used.
    def depth(node):
        d = 0
        while node is not None:
            d += 1
            node = node.parent
        return d

    # Tuple assignment: both depths are computed, then assigned.
    depth_a, depth_b = depth(a), depth(b)

    # Make `a` the deeper node. `a, b = b, a` swaps two variables in one
    # statement: the right-hand tuple is built first, then unpacked.
    if depth_a < depth_b:
        a, b = b, a
        depth_a, depth_b = depth_b, depth_a

    # Climb from the deeper node by the depth difference. `range(k)` yields
    # k values; `_` is the conventional name for a loop variable that is
    # not used.
    for _ in range(depth_a - depth_b):
        a = a.parent

    # Now both are at the same depth: climb in tandem until they are the
    # same object (`is not` tests identity). They meet at the LCA at the
    # latest at the root.
    while a is not b:
        a, b = a.parent, b.parent
    return a


def lca_parent_value(tree, a: int, b: int) -> int | None:
    """Convenience wrapper (not in the textbook): build the tree, look up
    the nodes holding keys a and b, and return their LCA's key (None if a
    key is absent)."""
    root = build_parent_tree(tree)
    left, right = find_node(root, a), find_node(root, b)
    if left is None or right is None:
        return None
    node = lca_with_parent(left, right)
    return None if node is None else node.data


# TEXTBOOK POST-SOLUTION DISCUSSION (page 119)
# -------------------------------------------
# Time and space complexity are those of computing the depths: O(h) time
# and O(1) space.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def lca(node_0, node_1)` with nested `get_depth(node)` using
#   `while node:`; file: `lca_with_parent(a: ParentNode, b: ParentNode) ->
#   ParentNode | None` with nested `depth(node)` using
#   `while node is not None:`.
# - Book swaps only the nodes (`if depth_1 > depth_0: node_0, node_1 =
#   node_1, node_0`) and then uses `depth_diff = abs(depth_0 - depth_1)`
#   with a `while depth_diff:` loop that decrements it. File swaps both
#   the nodes and the depths, and climbs with
#   `for _ in range(depth_a - depth_b)`.
# - The final tandem loop `while ... is not ...` matches the book.
# - Not in the book: the `ParentNode` dataclass (book uses nodes with a
#   parent field from the chapter introduction), `build_parent_tree`,
#   `find_node`, `lca_parent_value`. Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # A small tree: 4 at the root, 2 (children 1 and 3) on the left, 6 on
    # the right. The nodes holding 1 and 3 have the same depth, so the
    # tandem climb meets immediately at their parent, 2.
    tree=(4,(2,(1,None,None),(3,None,None)),(6,None,None))
    print("parent LCA:", lca_parent_value(tree, 1, 3))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert lca_parent_value(tree, 1, 3) == 2
