"""EPI Python — Exercise 9.11: Implement an Inorder Traversal with O(1) Space

Chapter 9: Binary Trees
Textbook: pages 124–125 (printed page numbers; problem, solution and the
start of the program on 124; end of the program, complexity, alternative
and variant on 125).

IMPORTANT: the code in this file is NOT the textbook's algorithm. The book
uses parent fields; this file implements a different technique (Morris
traversal, which temporarily rewires right pointers). See TEXTBOOK CODE
COMPARISON below. The notes that follow describe the book's solution.

PROBLEM (from the textbook)
---------------------------
"The direct implementation of an inorder traversal using recursion has O(h)
space complexity, where h is the height of the tree. Recursion can be
removed with an explicit stack, but the space complexity remains O(h).

Write a nonrecursive program for computing the inorder traversal sequence
for a binary tree. Assume nodes have parent fields."

HINT (from the textbook)
------------------------
"How can you tell whether a node is a left child or right child of its
parent?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Inorder traversal is: traverse left, visit root, traverse right. After
finishing a subtree we must return to its parent, and what happens next
depends on which side we came from: returning from the parent's left
subtree, we visit the parent and then its right subtree; returning from the
right subtree, we are done with the parent and return from it too.

One non-recursive approach records, in a hash table, the parent of every
node from which a traversal is started. That costs O(n) time and O(n) space
for the table (n nodes, h the height); evicting a node from the table once
its subtree is finished reduces the space to O(h).

Here every node already stores its parent, so no hash table is needed and
the extra space drops to O(1).

What remains is to recognise, on returning to a parent, whether the
subtree just completed was its left child (then visit the parent and go to
its right subtree) or its right subtree (then the parent is finished). The
book does this by remembering the root of the subtree just left before
moving to the parent, and comparing it with the parent's left child.
Book example (Figure 9.1, page 112): after finishing the subtree rooted at
C we return to B, having recorded C; since C is B's left child, B's right
child still has to be traversed. When we later return from F to B we have
recorded F; F is not B's left child, so it must be B's right child, and B
is finished.

The book's program `inorder_traversal(tree)` keeps `prev` (the node we
came from) and, in each iteration, picks `next`:
  - came down from the parent (prev is tree.parent): go left if possible;
    otherwise record the node and go right if non-empty, else up;
  - came up from the left child (tree.left is prev): record the node, then
    go right if non-empty, else up;
  - otherwise (came up from the right child): go up.

[The file does not contain this program; its `inorder_constant_space`
function uses Morris traversal on nodes without parent fields.]

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    tree = (2, (1, None, None), (3, None, None))  -> [1, 2, 3]
"""

# Local project import (not the standard library): reuse the TreeNode
# dataclass (fields data, left, right; generated __init__; no parent field)
# defined in this chapter's Exercise 9.1 module.
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
    """Inverse of build_tree (helper added for testing; not in the book).
    Useful to confirm the tree is unchanged after a Morris traversal."""

    # Conditional expression `X if cond else Y`: None for an empty tree,
    # otherwise a (data, left, right) tuple built recursively.
    return None if root is None else (root.data, nested_tree(root.left), nested_tree(root.right))


# `-> list[int]`: type hint for "list of ints" (not enforced).
def inorder_constant_space(root: TreeNode | None) -> list[int]:
    """Morris traversal: temporary predecessor threads avoid an explicit stack.

    NOT the textbook's program (the book's version, inorder_traversal on
    page 124, relies on parent fields and does not modify the tree). This
    technique needs no parent fields but temporarily changes right pointers
    of some nodes; every change is undone before the function returns.
    Uses O(1) extra space besides the result list.
    """
    result = []
    current = root
    while current is not None:

        # No left subtree: visit this node now, then continue to the right.
        # (The "right" may be a temporary thread back to an ancestor.)
        if current.left is None:
            result.append(current.data)
            current = current.right
        else:

            # Find current's inorder predecessor: the right-most node of
            # its left subtree. Stop early if we meet the thread we planted
            # earlier (a right pointer that already leads back to current).
            # `is` / `is not` compare object identity.
            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right

            # First arrival: plant a thread predecessor -> current, so we
            # can climb back after the left subtree, then descend left.
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:

                # Second arrival (via the thread): the left subtree is done.
                # Remove the thread to restore the tree, visit current, and
                # go right.
                predecessor.right = None
                result.append(current.data)
                current = current.right
    return result


def morris_values(tree) -> list[int]:
    """Convenience wrapper (not in the textbook): build the tree from
    nested tuples and call inorder_constant_space."""
    return inorder_constant_space(build_tree(tree))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 125)
# -------------------------------------------
# The book's parent-field program runs in O(n) time with O(1) additional
# space.
#
# Alternative noted by the book: because a node's successor is the node
# that follows it in inorder, one could start at the left-most node and
# repeatedly call the successor function, reusing Solution 9.10 (page 123).
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): How would you perform
# preorder and postorder traversals iteratively using O(1) additional
# space? Your algorithm cannot modify the tree. Nodes have an explicit
# parent field.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - DIFFERENT ALGORITHM. Book: `def inorder_traversal(tree)` on nodes WITH
#   parent fields, tracking `prev, result = None, []` and choosing `next`
#   from three cases (`prev is tree.parent`, `tree.left is prev`, else),
#   ending each iteration with `prev, tree = tree, next`; it never modifies
#   the tree. File: `inorder_constant_space(root: TreeNode | None) ->
#   list[int]` implements Morris traversal on nodes WITHOUT parent fields,
#   temporarily setting `predecessor.right = current` and later restoring
#   it to None. The book does not describe Morris traversal, and the book's
#   implementation is missing from the file.
# - The file name `pg_124_morris_inorder.py` also refers to Morris
#   traversal rather than the book's program name `inorder_traversal`.
# - Not in the book: `build_tree`, `nested_tree`, `morris_values`;
#   `TreeNode` imported from the 9.1 module. Type hints added.
# - The previous module docstring stated a hint ("Temporarily connect a
#   node's inorder predecessor back to it") and a variant wording that do
#   not match the book; both have been replaced with the book's text.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Root 2 with children 1 and 3: the inorder sequence is 1, 2, 3.
    tree=(2,(1,None,None),(3,None,None))
    print("Morris inorder:", morris_values(tree))

    # `assert` raises AssertionError if the condition is false; a quick
    # smoke check (pytest has the thorough tests).
    assert morris_values(tree)==[1,2,3]
