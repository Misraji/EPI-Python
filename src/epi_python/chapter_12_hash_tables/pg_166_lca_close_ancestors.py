"""EPI Python — Exercise 12.4: Compute the LCA, Optimizing for Close Ancestors

Chapter 12: Hash Tables
Textbook: pages 166–167 (printed page numbers; problem, solution and the
start of the program on 166, rest of program and complexity on 167).

PROBLEM (from the textbook)
---------------------------
"Problem 9.4 on Page 118 is concerned with computing the LCA in a binary
tree with parent pointers in time proportional to the height of the tree.
The algorithm presented in Solution 9.4 on Page 118 entails traversing all
the way to the root even if the nodes whose LCA is being computed are very
close to their LCA.

Design an algorithm for computing the LCA of two nodes in a binary tree.
The algorithm's time complexity should depend only on the distance from the
nodes to the LCA."

HINT (from the textbook)
------------------------
"Focus on the extreme case described in the problem introduction."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: walk upwards from one node to the root, recording every node on
that path; then walk upwards from the other node and stop at the first node
that is on the recorded path. The trouble is that when both nodes are far
from the root, the first walk still goes all the way to the root, even if
the LCA is just their parent (i.e., they are siblings) -- the book points to
nodes L and N in Figure 9.1 on page 112 as an illustration.

The brute force is suboptimal because it may process many nodes well above
the LCA. To avoid that, move upwards from the two nodes ALTERNATELY, one
step at a time, storing every visited node in a hash table. Each time a node
is visited, check whether it has been visited before; the first node seen a
second time is the LCA.

The implementation below, lca_close_ancestors, follows this idea.
lca_close_value is a convenience wrapper added in this repository.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
Tree written as nested (value, left, right) tuples:
            4
           / \\
          2   6
         / \\
        1   3
    LCA of 1 and 3 -> 2
"""

# Reuse parent-aware binary tree from chapter 9.
#
# Local project import (this repository's own code, not the standard
# library): the Chapter 9 exercise module for Problem 9.4 defines
#   * ParentNode -- a dataclass node with data, left, right and parent;
#   * build_parent_tree -- builds ParentNode objects from nested
#     (value, left, right) tuples (a testing helper);
#   * find_node -- returns the node holding a given key, or None.
# `from package.module import a, b, c` imports just those names.
# Import system documentation: https://docs.python.org/3/reference/import.html
# The import statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_09_binary_trees.pg_118_lca_with_parent import ParentNode, build_parent_tree, find_node


def lca_close_ancestors(a: ParentNode | None, b: ParentNode | None) -> ParentNode | None:
    """Walk both parent chains alternately; stop at first common ancestor.

    This is the textbook's lca(node_0, node_1) for this exercise, storing
    node identities (id()) in the set instead of the nodes themselves, and
    returning None instead of raising when the nodes share no ancestor.

    Type hints: `ParentNode | None` means "a ParentNode or None" (the `|`
    union syntax in annotations needs Python 3.10+). Python does not enforce
    annotations.
    """

    # set() creates an empty hash set, giving O(1) expected `in` checks and
    # add() calls -- the book's hash table of visited nodes.
    #
    # It stores id(node) values rather than nodes: ParentNode is a
    # @dataclass that generates __eq__, which makes instances unhashable
    # (they cannot go in a set). id(obj) returns an int that is unique to
    # that object while it is alive, so it identifies each node exactly.
    # `visited: set[int]` is an annotated assignment documenting the type.
    # set: https://docs.python.org/3/library/stdtypes.html#set
    # id: https://docs.python.org/3/library/functions.html#id
    visited: set[int] = set()

    # Book's comment: ascend the tree in tandem for these two nodes. The
    # loop continues while at least one pointer has not yet passed the root.
    # `is not None` tests identity with the None object.
    while a is not None or b is not None:
        if a is not None:

            # a was already reached from b's side: it is the LCA.
            if id(a) in visited:
                return a
            visited.add(id(a))
            a = a.parent
        if b is not None:
            if id(b) in visited:
                return b
            visited.add(id(b))
            b = b.parent

    # Both walks passed their roots without meeting: the nodes are not in
    # the same tree (the book raises ValueError here instead).
    return None


def lca_close_value(tree, a: int, b: int) -> int | None:
    """Build the tree, find the nodes holding keys a and b, return the LCA's key.

    Convenience wrapper added in this repository; not in the textbook.
    `tree` is a nested (value, left, right) tuple. `-> int | None` means an
    int, or None if no LCA is found.
    """
    root = build_parent_tree(tree)
    node_a, node_b = find_node(root, a), find_node(root, b)
    node = lca_close_ancestors(node_a, node_b)

    # Conditional expression `X if condition else Y`: return None when there
    # is no LCA, otherwise the LCA node's stored value.
    return None if node is None else node.data


# TEXTBOOK POST-SOLUTION DISCUSSION (page 167)
# --------------------------------------------
# This trades space for time. Solution 9.4 (page 118) used O(1) space and
# O(h) time. The algorithm here uses O(D0 + D1) space and time, where D0 is
# the distance from the LCA to the first node and D1 the distance from the
# LCA to the second node. In the worst case the nodes are leaves whose LCA
# is the root, and the cost becomes O(h) space and time, where h is the
# height of the tree.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def lca(node_0, node_1):` with `iter_0, iter_1 = node_0, node_1`,
#   `nodes_on_path_to_root = set()`, `while iter_0 or iter_1:` (comment
#   "Ascend tree in tandem for these two nodes."), truthiness tests
#   `if iter_0:` / `if iter_1:`, storing the node objects themselves in the
#   set, and finally `raise ValueError('node_0 and node_1 are not in the
#   same tree')`.
# File: function renamed `lca_close_ancestors`; parameters `a`, `b` with
#   `ParentNode | None` hints and a return hint; the parameters are advanced
#   directly instead of copying into iter_0/iter_1; the set is named
#   `visited` and holds `id(node)` integers instead of nodes (needed because
#   the repository's dataclass ParentNode is unhashable); explicit
#   `is not None` tests replace truthiness tests; returns None instead of
#   raising ValueError when no common ancestor exists. The node class and
#   tree builders are imported from the Chapter 9 module. Extra wrapper
#   `lca_close_value` is not in the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The nested tuple encodes the tree drawn in the module docstring:
    # root 4 with children 2 and 6; 2 has children 1 and 3. The LCA of
    # leaves 1 and 3 is their parent, 2 -- the "close ancestor" case this
    # algorithm is designed for.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, while pytest provides the more
    # thorough automated verification.
    tree=(4,(2,(1,None,None),(3,None,None)),(6,None,None))
    print("close-ancestor LCA:", lca_close_value(tree,1,3))
    assert lca_close_value(tree,1,3) == 2
