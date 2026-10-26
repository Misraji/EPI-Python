"""EPI Python — Exercise 14.8: Build a Minimum Height BST from a Sorted Array

Chapter 14: Binary Search Trees
Textbook: page 210 (printed page number; problem and solution on 210).

PROBLEM (from the textbook)
---------------------------
"Given a sorted array, the number of BSTs that can be built on the entries
in the array grows enormously with its size. Some of these trees are skewed,
and are closer to lists; others are more balanced. See Figure 14.3 on
Page 205 for an example."

"How would you build a BST of minimum possible height from a sorted array?"

HINT (from the textbook)
------------------------
"Which element should be the root?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force does not help much: enumerating every BST on the array to find
one of minimum height needs a nontrivial recursion and takes an enormous
amount of time.

Intuition: the subtrees should be as balanced as possible. Nothing is gained
by making one subtree shorter than the other, because the height is set by
the taller one. More formally, balance is achieved by keeping the numbers of
nodes in the two subtrees as close as possible.

With n the array length, make the middle element (the floor(n/2)-th entry)
the root, and recursively build minimum-height BSTs from the subarrays on
either side of it.

Worked example from the book: for <2,3,5,7,11,13,17,19,23> the root is the
middle element, 11. The left subtree is built from <2,3,5,7> and the right
subtree from <13,17,19,23>, each by calling the procedure recursively so
that both have minimum height.

The function below is the book's single implementation.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1,2,3,4,5,6,7] -> balanced BST rooted at 4 (children 2 and 6)
"""

# Local project import (not the standard library): the chapter's shared BST
# node class, defined in bst_nodes.py in this same package. The leading dot
# makes this a package-relative import ("from the current package").
# BSTNode is a dataclass with fields `data`, `left` and `right`, so
# `BSTNode(key, left, right)` builds a node.
# Relative imports: https://docs.python.org/3/reference/import.html#package-relative-imports
# dataclasses (used by BSTNode): https://docs.python.org/3/library/dataclasses.html
from .bst_nodes import BSTNode


# Type hints: a sorted list of ints in, the root (or None if empty) out.
# Python does not enforce annotations at run time.
def build_min_height_bst_from_sorted_array(values: list[int]) -> BSTNode | None:
    """Choose each subarray's midpoint as the root for a balanced BST.

    This is the textbook's implementation.
    """

    # Nested helper working on the half-open index range [start, end): it
    # includes `start` and excludes `end`, so no subarray copies are made.
    def build(start: int,end: int) -> BSTNode | None:

        # An empty range produces an empty subtree.
        if start >= end:
            return None

        # `//` is floor division: it divides and rounds down to an int,
        # giving a valid middle index.
        middle=(start+end)//2

        # The middle element is the root; the elements to its left form the
        # left subtree and those to its right the right subtree.
        return BSTNode(values[middle],build(start,middle),build(middle+1,end))
    return build(0,len(values))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 210)
# --------------------------------------------
# The time T(n) satisfies T(n) = 2T(n/2) + O(1), which solves to O(n).
# Equivalently, the recursive function is called exactly n times [as stated
# in the book] and does O(1) work per call.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def build_min_height_bst_from_sorted_array(A):` with nested
# `build_min_height_bst_from_sorted_subarray(start, end)` and variable
# `mid`. File: parameter renamed `values: list[int]`, helper renamed
# `build`, `mid` renamed `middle`, type hints added. Logic identical.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Because of the relative import above, run it as a module:
#   python -m epi_python.chapter_14_binary_search_trees.pg_210_build_min_height_bst_from_sorted_array
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example (not from the book): seven sorted keys; the middle
    # one, 4, becomes the root.
    result=build_min_height_bst_from_sorted_array([1,2,3,4,5,6,7])
    print('Root of minimum-height BST:',result.data)

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert result.data==4
