"""EPI Python — Exercise 9.8: Implement a Preorder Traversal Without Recursion

Chapter 9: Binary Trees
Textbook: pages 121–122 (printed page numbers; problem and start of the
solution on 121, stack example, program and complexity on 122).

PROBLEM (from the textbook)
---------------------------
"This problem is concerned with traversing nodes in a binary tree in
preorder fashion. See Page 113 for details and examples of these
traversals. Generally speaking, a traversal computation is easy to
implement if recursion is allowed.

Write a program which takes as input a binary tree and performs a preorder
traversal of the tree. Do not use recursion. Nodes do not contain parent
references."

(The book prints no hint for this exercise.)

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Intuition: a preorder traversal visits nodes in last-in, first-out order,
which suggests a stack of tree nodes.
  1. Initialise the stack with the root.
  2. Visit a node by popping it, then push first its right child and then
     its left child. The left child goes on last because it must be
     processed next (it ends up on top of the stack).

Worked example from the book (tree of Figure 9.1, page 112; the top of the
stack is the rightmost entry): the first few stack states are <A>, <I, B>,
<I, F, C>, <I, F, E, D>, <I, F, E>, <I, F>, <I, G>, <I, H>, and <I>.

This file's `preorder_traversal` implements the same idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (2, (1, None, None), (3, None, None))  -> [2, 1, 3]
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
def preorder_traversal(root: TreeNode | None) -> list[int]:
    """Visit root, left, right by pushing right before left onto a stack.

    This file's version of the textbook's preorder_traversal program
    (page 122).
    """
    if root is None:
        return []

    # A Python list used as a stack: append() pushes onto the end, pop()
    # with no argument removes and returns the last item (LIFO), O(1).
    # https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
    stack = [root]
    result = []

    # A non-empty list is truthy; loop until the stack is empty.
    while stack:
        node = stack.pop()
        result.append(node.data)

        # Push right first, then left, so the left child is on top and is
        # visited next. Unlike the book, empty children are never pushed.
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result


def preorder_values(tree) -> list[int]:
    """Convenience wrapper (not in the textbook): build the tree from
    nested tuples and call preorder_traversal."""
    return preorder_traversal(build_tree(tree))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 122)
# -------------------------------------------
# Time: O(n), n being the number of nodes, since each node is pushed and
# popped exactly once.
# Space: O(h), h being the tree height, because apart from possibly the
# top of the stack, the nodes on the stack are the right children of nodes
# on a path that starts at the root.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def preorder_traversal(tree)` with `path, result = [tree], []`;
#   every popped item is tested with `if curr:` and both children are
#   pushed unconditionally with `path += [curr.right, curr.left]` (so None
#   entries go onto the stack and are skipped when popped).
# - File: `preorder_traversal(root: TreeNode | None) -> list[int]` returns
#   `[]` up front for an empty tree, names the stack `stack`, and pushes
#   each child only if it is not None, with two separate `append` calls.
#   Same visit order.
# - Not in the book: `build_tree`, `nested_tree`, `preorder_values`;
#   `TreeNode` imported from the 9.1 module. Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Root 2 with children 1 and 3: preorder visits root, left, right.
    tree=(2,(1,None,None),(3,None,None))
    print("preorder:", preorder_values(tree))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert preorder_values(tree)==[2,1,3]
