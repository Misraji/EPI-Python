"""EPI Python — Exercise 8.6: Compute Binary Tree Nodes in Order of Increasing Depth

Chapter 8: Stacks and Queues
Textbook: pages 106–107 (printed page numbers; problem, solution and program
on page 106, complexity and variants at the top of page 107).

PROBLEM (from the textbook)
---------------------------
"Binary trees are formally defined in Chapter 9. In particular, each node in
a binary tree has a depth, which is its distance from the root.

Given a binary tree, return an array consisting of the keys at the same
level. Keys should appear in the order of the corresponding nodes' depths,
breaking ties from left to right. For example, you should return
<<314>, <6, 6>, <271, 561, 2, 271>, <28, 0, 3, 1, 28>, <17, 401, 257>, <641>>
for the binary tree in Figure 9.1 on Page 112."

HINT (from the textbook)
------------------------
"First think about solving this problem with a pair of queues."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: write every node into an array together with its depth,
computed during a preorder traversal. Because preorder visits a node's left
child before its right child, nodes of equal depth appear in left-to-right
order. Then sort the array with a stable sort keyed on depth (stability
keeps the left-to-right order among equal depths). Sorting dominates:
O(n log n) time, plus O(n) space to store the depths.

Improvement: the tree already arranges the nodes in a partially ordered way,
so a full sort should be avoidable, lowering the time. And if nodes are
processed depth by depth, no node needs an explicit depth label.

Approach: keep one queue holding the nodes at depth i and another for the
nodes at depth i + 1. Once every depth-i node has been processed, that queue
is finished; the depth-(i + 1) queue is processed next, while depth-(i + 2)
nodes go into a fresh queue. The book's program `binary_tree_depth_order`
realises this with Python lists: each iteration records the keys of the
current level and builds the next level's list of children.

This file's `binary_tree_depth_order` instead uses a single
`collections.deque` and processes exactly one level's worth of nodes per
outer iteration (see the code comparison at the end).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    depth_order_values((1, (2, None, None), (3, None, None))) -> [[1], [2, 3]]
    depth_order_values(None) -> []
Trees for `depth_order_values` are nested tuples (key, left, right), with
None for a missing child.
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
#
# `from module import name` binds just that name, so it is used as `deque`
# rather than `collections.deque`.
from collections import deque

# Local project import: the binary-tree node class defined in the repository's
# Chapter 9 exercise file (fields `data`, `left`, `right`), reused here so the
# examples have real tree nodes. This is an absolute import through the
# installed `epi_python` package.
# Import system documentation: https://docs.python.org/3/reference/import.html
# The import statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_09_binary_trees.pg_114_is_balanced_binary_tree import TreeNode


# Type hints (not enforced by Python):
# * `TreeNode | None` (Python 3.10+ union syntax) means "a TreeNode, or None
#   for an empty tree".
# * `list[list[int]]` means a list whose items are lists of ints, one inner
#   list per depth.
def binary_tree_depth_order(root: TreeNode | None) -> list[list[int]]:
    """Return level-order lists using breadth-first traversal.

    Implements the textbook's `binary_tree_depth_order` idea (page 106)
    with one deque instead of the book's per-level lists.
    """
    if root is None:
        return []

    # collections.deque(iterable) creates a double-ended queue initialised
    # with the iterable's items, here a one-element list holding the root.
    # A deque supports O(1) append() at the right end and O(1) popleft() at
    # the left end, which is exactly first-in, first-out queue behaviour.
    # (A plain list's pop(0) would shift every remaining element: O(n).)
    # popleft() on an empty deque raises IndexError.
    # Documentation: https://docs.python.org/3/library/collections.html#collections.deque
    queue = deque([root])
    result: list[list[int]] = []

    # An empty deque is falsy, so the loop stops when no nodes remain.
    while queue:
        level = []

        # At the start of each outer iteration the deque contains exactly the
        # nodes of one depth. len(queue) is captured once by range(), so the
        # inner loop handles just those nodes; children appended meanwhile
        # wait for the next outer iteration. `_` is the conventional name
        # for a loop variable whose value is not used.
        for _ in range(len(queue)):

            # deque.popleft() removes and returns the leftmost (oldest) node.
            # Documentation: https://docs.python.org/3/library/collections.html#collections.deque.popleft
            node = queue.popleft()
            level.append(node.data)

            # Left child before right child keeps each level in left-to-right
            # order. A node object is truthy; None is falsy.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def depth_order_values(tree: tuple | None) -> list[list[int]]:
    """Build TreeNodes from nested (key, left, right) tuples, then run
    `binary_tree_depth_order`.

    Repository helper added for testing/learning; not in the textbook.
    """

    # A nested (inner) function that is visible only inside this function.
    # It calls itself recursively to convert each subtree tuple, using a
    # conditional expression `A if condition else B`: None stays None,
    # otherwise t[0] is the key and t[1], t[2] are the subtrees.
    def build(t):
        return None if t is None else TreeNode(t[0], build(t[1]), build(t[2]))
    return binary_tree_depth_order(build(tree))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 107)
# --------------------------------------------
# Every node is enqueued once and dequeued once, so the time complexity is
# O(n). The space complexity is O(m), where m is the largest number of nodes
# found at any single depth.
#
# VARIANTS (all stated in the book; no solutions given)
# 1. Given a binary tree, return its keys top down, level by level,
#    alternating left-to-right and right-to-left, beginning left-to-right.
#    For the tree of Figure 9.1 (page 112) the expected answer is
#    <<314>, <6, 6>, <271, 561, 2, 271>, <28, 1, 3, 0, 28>, <17, 401, 257>,
#    <641>>.
# 2. Given a binary tree, return its keys bottom up, each level
#    left-to-right. For Figure 9.1 the expected answer is
#    <<641>, <17, 401, 257>, <28, 0, 3, 1, 28>, <271, 561, 2, 271>, <6, 6>,
#    <314>>.
# 3. Given a binary tree with integer keys, return the average of the keys
#    at each level. For Figure 9.1 the expected answer is
#    <314, 6, 276.25, 12, 225, 641>.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def binary_tree_depth_order(tree)` with `result = []`, returning it
# immediately when `not tree`; `curr_depth_nodes = [tree]` is a plain list;
# each `while` iteration appends `[curr.data for curr in curr_depth_nodes]`
# and replaces `curr_depth_nodes` with a list comprehension of all non-None
# children `for curr in curr_depth_nodes for child in (curr.left,
# curr.right) if child`. No import is needed.
# File: parameter renamed `root: TreeNode | None` with `-> list[list[int]]`;
# tests `root is None`; uses one `collections.deque` (extra import) with
# popleft/append and a `for _ in range(len(queue))` inner loop instead of
# rebuilding per-level lists with comprehensions. Same output.
# Not in the book: the `TreeNode` import from the Chapter 9 file and the
# helper `depth_order_values` (with nested `build`).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # A three-node tree: root 1 with left child 2 and right child 3,
    # written as nested (key, left, right) tuples. Depth 0 holds [1] and
    # depth 1 holds [2, 3] in left-to-right order.
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, pytest does the thorough testing.
    tree = (1, (2, None, None), (3, None, None))
    print("tree levels:", depth_order_values(tree))
    assert depth_order_values(tree) == [[1], [2, 3]]
