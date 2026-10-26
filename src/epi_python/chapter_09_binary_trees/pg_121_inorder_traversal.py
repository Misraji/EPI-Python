"""EPI Python — Exercise 9.7: Implement an Inorder Traversal Without Recursion

Chapter 9: Binary Trees
Textbook: page 121 (printed page number; problem, solution, program and
complexity are all on page 121).

PROBLEM (from the textbook)
---------------------------
"This problem is concerned with traversing nodes in a binary tree in an
inorder fashion. See Page 113 for details and examples of these traversals.
Generally speaking, a traversal computation is easy to implement if
recursion is allowed.

Write a program which takes as input a binary tree and performs an inorder
traversal of the tree. Do not use recursion. Nodes do not contain parent
references."

HINT (from the textbook)
------------------------
"Simulate the function call stack."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The recursive solution is trivial: traverse the left subtree, visit the
root, then traverse the right subtree. It can be turned into an iterative
algorithm by managing an explicit stack in place of the call stack.

Many iterative versions are possible. The book's program is notable for
two reasons: it pushes the *current node* (not its right child), and it
needs no "visited" field. Its loop runs while the stack is non-empty or
there is a current node:
  - If there is a current node: push it and go left.
  - Otherwise: go up by popping a node from the stack, record its data,
    and go right.

Worked example from the book (tree of Figure 9.1, page 112): the first
few stack states are <A>, <A, B>, <A, B, C>, <A, B, C, D>, <A, B, C>,
<A, B, D>, <A, B>, <A>, <A, F>.

This file's `inorder_nodes` implements the same loop.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
Trees are nested (value, left, right) tuples; None is empty.
    None                                    -> []
    (1, None, None)                         -> [1]
    (2, (1, None, None), (3, None, None))   -> [1, 2, 3]
"""

# Python standard library: automatically generated special methods for
# classes that mainly store data ("data classes").
# Module documentation: https://docs.python.org/3/library/dataclasses.html
# dataclass decorator: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
from dataclasses import dataclass


# `@dataclass` generates __init__(data, left=None, right=None), __repr__
# and __eq__ from the annotated attributes. Annotations such as
# `data: int` are type hints, not enforced at run time; the quoted
# "TreeNode | None" is a forward reference to the class being defined.
@dataclass
class TreeNode:
    data: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


# `-> list[int]` is a type hint meaning "a list of ints" (built-in generic
# syntax, Python 3.9+); `TreeNode | None` in a signature needs 3.10+. Hints
# are not enforced.
def inorder_nodes(root: TreeNode | None) -> list[int]:
    """Inorder tree traversal using an explicit stack, not recursion.

    This file's version of the textbook's inorder_traversal program
    (page 121).
    """
    result=[]

    # A Python list used as a stack: append() pushes onto the end and pop()
    # with no argument removes and returns the last item (LIFO), both O(1).
    # https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
    stack=[]
    current=root

    # An empty list is falsy, so `stack` is True while it holds nodes.
    # Continue while there are pending ancestors or a subtree to descend.
    while stack or current is not None:
        if current is not None:

            # Going left: remember this node (to visit after its left
            # subtree) and descend.
            stack.append(current)
            current=current.left
        else:

            # Going up: the left subtree of the most recently pushed node
            # is finished, so visit that node, then go right.
            current=stack.pop()
            result.append(current.data)
            current=current.right
    return result


def inorder_traversal(tree: tuple | None) -> list[int]:
    """Adapter (not in the textbook): build TreeNodes from nested
    (value, left, right) tuples, then call inorder_nodes."""

    # Conditional expression `X if cond else Y`: None for an empty
    # description, otherwise a TreeNode with recursively built children.
    def build(t):
        return None if t is None else TreeNode(t[0],build(t[1]),build(t[2]))
    return inorder_nodes(build(tree))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 121)
# -------------------------------------------
# Time: O(n), because each node is handled in O(1) total time (pushed once,
# popped once).
# Space: O(h), h being the tree height. This storage is allocated
# dynamically; it corresponds to the maximum depth the function call stack
# would reach in the recursive implementation. (Tree height is defined on
# page 113.)
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def inorder_traversal(tree)` with `s, result = [], []` and loop
#   `while s or tree:` that reuses `tree` as the moving pointer. File:
#   `inorder_nodes(root: TreeNode | None) -> list[int]` with separate
#   variables `result`, `stack`, `current`, and the condition
#   `while stack or current is not None:` (book: `if tree:`, file:
#   `if current is not None:`). The loop body is otherwise the same.
# - The name `inorder_traversal` is reused in the file for an adapter that
#   takes nested tuples (not in the book).
# - File defines its own `TreeNode` dataclass. Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Executable demonstration cases; pytest has the full set.
    # They show an empty tree, a single node, and a three-node tree whose
    # inorder visit order (left, root, right) is 1, 2, 3.
    #
    # `assert` raises AssertionError if the condition is false; these are
    # quick smoke checks only.
    result=inorder_traversal(None)
    print('inorder_traversal', result)
    assert result == []
    result=inorder_traversal((1, None, None))
    print('inorder_traversal', result)
    assert result == [1]
    result=inorder_traversal((2, (1, None, None), (3, None, None)))
    print('inorder_traversal', result)
    assert result == [1, 2, 3]
