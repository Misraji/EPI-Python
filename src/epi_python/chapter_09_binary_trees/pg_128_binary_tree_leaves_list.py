"""EPI Python — Exercise 9.14: Form a Linked List from the Leaves of a Binary Tree

Chapter 9: Binary Trees
Textbook: page 128 (printed page number; problem, solution, program and
complexity are all on page 128).

PROBLEM (from the textbook)
---------------------------
"In some applications of a binary tree, only the leaf nodes contain actual
information. For example, the outcomes of matches in a tennis tournament
can be represented by a binary tree where leaves are players. The internal
nodes correspond to matches, with a single winner advancing. For such a
tree, we can link the leaves to get a list of participants.

Given a binary tree, compute a linked list from the leaves of the binary
tree. The leaves should appear in left-to-right order. For example, when
applied to the binary tree in Figure 9.1 on Page 112, your function should
return <D, E, H, M, N, P>."

HINT (from the textbook)
------------------------
"Build the list incrementally—it's easy if the partial list is a global."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
A fairly direct approach uses two passes: the first finds the leaves, the
second assigns them ranks, with the left-most leaf getting the lowest
rank. The answer is the leaves sorted by ascending rank.

Two passes are unnecessary: if the tree is processed from left to right,
the leaves are met in exactly the required order, so each can be added to
the result as soon as it is found.

The book's program `create_list_of_leaves(tree)` does this recursively: an
empty tree gives an empty list, a leaf gives a one-element list holding
that leaf, and any other node gives the left subtree's list followed by the
right subtree's list (left subtree first, then right).

This file's `create_list_of_leaves` also walks left before right, but
appends each leaf to a singly linked list as it goes (closer to the hint's
"partial list as a global"); see TEXTBOOK CODE COMPARISON.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (2, (1, None, None), (3, None, None)) -> leaves [1, 3]
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

# Local project import (not the standard library), placed here in the
# middle of the module: an import may appear anywhere and runs when that
# line executes. It reuses the singly linked list node from Chapter 7
# (Exercise 7.1): a dataclass ListNode with fields `data` and `next`
# (default None), constructed as ListNode(value).
# Import system documentation: https://docs.python.org/3/reference/import.html
# `from ... import` statement: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
from epi_python.chapter_07_linked_lists.pg_084_merge_two_sorted_lists import ListNode


def create_list_of_leaves(root: TreeNode | None) -> ListNode | None:
    """Build a linked chain of leaf nodes, ordered left-to-right.

    This file's version of the textbook's create_list_of_leaves program
    (page 128). It returns the head of a new singly linked list of
    ListNodes holding the leaves' data (None if there are no leaves),
    whereas the book returns a Python list of the leaf tree nodes.
    """

    # Dummy (sentinel) head: a placeholder node whose `next` will be the
    # real first leaf, so appending never needs a special "empty list"
    # case. `tail` always points to the last node of the list built so far.
    dummy = ListNode(0)
    tail = dummy
    def visit(node):

        # `nonlocal tail` lets this nested function reassign the enclosing
        # function's `tail` variable; without it, `tail = tail.next` would
        # make `tail` a new local name. This shared tail plays the role of
        # the hint's "global" partial list.
        # https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement
        nonlocal tail
        if node is None:
            return

        # Leaf: append a new list node holding its data and advance tail.
        if node.left is None and node.right is None:
            tail.next = ListNode(node.data)
            tail = tail.next
            return

        # First the left subtree, then the right: leaves come out in
        # left-to-right order.
        visit(node.left)
        visit(node.right)
    visit(root)

    # Skip the dummy node; its successor is the first leaf (or None).
    return dummy.next


def leaf_values(tree) -> list[int]:
    """Convenience wrapper (not in the textbook): build the tree, create
    the leaf list, and copy its data into a Python list."""
    current = create_list_of_leaves(build_tree(tree))
    result = []

    # A ListNode object is truthy and None is falsy, so the loop walks the
    # list until it runs off the end.
    while current:
        result.append(current.data)
        current = current.next
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 128)
# -------------------------------------------
# The time complexity is O(n), n being the number of nodes.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def create_list_of_leaves(tree)` returns a Python list of the
#   leaf *tree nodes*: `[]` for an empty tree, `[tree]` for a leaf, else
#   `create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)`
#   (list concatenation). File: `create_list_of_leaves(root: TreeNode |
#   None) -> ListNode | None` returns a singly linked list of new ListNode
#   objects holding the leaves' *data*, built with a dummy head, a nested
#   `visit` function and a `nonlocal tail`.
# - File imports `ListNode` from Chapter 7 (pg_084_merge_two_sorted_lists);
#   the book uses no linked-list class here. This import sits in the middle
#   of the module rather than at the top.
# - Not in the book: `build_tree`, `nested_tree`, `leaf_values`; `TreeNode`
#   imported from the 9.1 module. Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Root 2 with leaves 1 and 3: the leaves, left to right, are 1 then 3.
    tree=(2,(1,None,None),(3,None,None))
    print("leaf list:", leaf_values(tree))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert leaf_values(tree)==[1,3]
