"""EPI Python — Exercise 15.8: Generate Binary Trees

Chapter 15: Recursion
Textbook: pages 229–230 (printed page numbers; problem and solution start on 229).

PROBLEM (from the textbook)
---------------------------
"Write a program which returns all distinct binary trees with a specified
number of nodes. For example, if the number of nodes is specified to be
three, return the trees in Figure 15.6 on the following page."
(Figure 15.6: "The five binary trees on three nodes.")

HINT (from the textbook)
------------------------
"Can two binary trees whose left subtrees differ in size be the same?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: generate all binary trees with n - 1 or fewer nodes, then form
every tree consisting of a root plus a left child and a right child taken
from those trees. All such trees are distinct (no two share both the same
left and right child), but many have fewer than n nodes and many have more,
so most of the work is wasted.

Directed search: if the left subtree has k nodes, the right subtree must
have n - 1 - k nodes for the whole tree to have n nodes. So, for each i from
0 to n - 1, take every left subtree on i nodes and every right subtree on
n - 1 - i nodes, and combine each pair under a new root.

Reading Figure 15.6 this way: the first two trees have a left subtree of
size 0 and a right subtree of size 2; the third is the only one with left
and right subtrees of size 1; the last two have a left subtree of size 2
and a right subtree of size 0. The two trees on two nodes are found
recursively the same way: there is one tree on one node, and it can hang
on either side of the root.

The book's program generate_all_binary_trees(num_nodes) returns [None] (the
empty tree) for zero nodes and otherwise builds the combinations with a
list comprehension. This file implements it with essentially the same code.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    generate_all_binary_trees(3) -> 5 trees (the five shapes of Figure 15.6)
"""

# Python standard library: dataclasses (automatically generated special
# methods such as __init__, __repr__ and __eq__ for classes that mainly
# store data).
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` is a class decorator. It reads the annotated class
# attributes below (data, left, right) and generates
#   __init__(self, data, left=None, right=None)
#   __repr__  (a readable printout such as BinaryTreeNode(data=0, ...))
#   __eq__    (field-by-field equality, so two trees with the same shape
#              and data compare equal)
# This replaces the separate BinaryTreeNode class that the book uses from
# its Chapter 9 (binary trees) code.
#
# Annotations such as `data: int` declare the fields; Python does not
# check their types. `'BinaryTreeNode | None'` is written as a STRING
# (a "forward reference") because the class name is not defined yet while
# its own body is executing. `X | None` means "an X or None".
# `= None` gives the field a default value, so left/right are optional
# arguments.
@dataclass
class BinaryTreeNode:
    data: int
    left: 'BinaryTreeNode | None' = None
    right: 'BinaryTreeNode | None' = None


def generate_all_binary_trees(num_nodes: int) -> list[BinaryTreeNode | None]:
    """Return every distinct binary tree with num_nodes nodes (textbook version).

    Every node stores data 0; only the shapes differ. Zero nodes gives
    [None], one (empty) tree. Subtrees are shared between results, not
    copied, as in the book.
    """

    # Return type hint: a list whose items are BinaryTreeNode objects or
    # None. The `X | None` union syntax in an evaluated annotation needs
    # Python 3.10 or newer. Hints are not enforced at run time.
    #
    # Empty tree, added as a None (the book's comment). Returning [None]
    # rather than [] is essential: it gives exactly ONE choice of empty
    # subtree, so the pairing loop below still produces trees.
    if num_nodes == 0:
        return [None]
    result: list[BinaryTreeNode] = []

    # One node is the root; split the remaining num_nodes - 1 nodes between
    # the left subtree (num_left_tree_nodes) and the right subtree.
    for num_left_tree_nodes in range(num_nodes):
        num_right_tree_nodes = num_nodes - 1 - num_left_tree_nodes
        left_subtrees = generate_all_binary_trees(num_left_tree_nodes)
        right_subtrees = generate_all_binary_trees(num_right_tree_nodes)

        # The comprehension forms every possible left/right subtree pairing
        # (the book: "Generates all combinations of left_subtrees and
        # right_subtrees."). Two `for` clauses work like nested loops: for
        # each left, for each right, build a new root BinaryTreeNode(0, left,
        # right). `result += [...]` extends the list in place.
        result += [BinaryTreeNode(0, left, right)
                   for left in left_subtrees for right in right_subtrees]
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 230)
# --------------------------------------------
# The number of calls C(n) satisfies C(n) = sum over i = 1 .. n of
# C(n - i) * C(i - 1). C(n) is the nth Catalan number, known to equal
# (2n)! / (n! (n + 1)!). Solution 15.6 (matched parens, page 227) is very
# similar; Catalan numbers appear in many kinds of combinatorial problems.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * The function body matches the book's listing (same names, same loop and
#   list comprehension). The file adds type hints (`num_nodes: int`,
#   `-> list[BinaryTreeNode | None]`, `result: list[BinaryTreeNode]`).
# * The book uses a BinaryTreeNode class defined elsewhere (Chapter 9);
#   the file defines its own `BinaryTreeNode` as a @dataclass with fields
#   data, left, right (a helper not printed in this exercise), which adds
#   generated __init__/__repr__/__eq__ and requires the dataclasses import.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # The book's example: there are exactly five binary trees on three
    # nodes (Figure 15.6), the Catalan number C(3) = 6!/(3! 4!) = 5.
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, the pytest suite is thorough.
    trees = generate_all_binary_trees(3)
    print('Distinct binary trees with three nodes:', len(trees))
    assert len(trees) == 5
