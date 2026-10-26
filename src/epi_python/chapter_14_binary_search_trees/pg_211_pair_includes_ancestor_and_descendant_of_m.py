"""EPI Python — Exercise 14.9: Test if Three BST Nodes Are Totally Ordered

Chapter 14: Binary Search Trees
Textbook: pages 211–212 (printed page numbers; problem and solution start on 211).

PROBLEM (from the textbook)
---------------------------
"Write a program which takes two nodes in a BST and a third node, the
"middle" node, and determines if one of the two nodes is a proper ancestor
and the other a proper descendant of the middle. (A proper ancestor of a
node is an ancestor that is not equal to the node; a proper descendant is
defined similarly.) For example, in Figure 14.1 on Page 198, if the middle
is Node J, your function should return true if the two nodes are {A, K} or
{I, M}. It should return false if the two nodes are {I, P} or {J, K}. You
can assume that all keys are unique. Nodes do not have pointers to their
parents"

Figure 14.1 (page 198), "An example of a BST" (node label = key):
    A=19 with left child B=7 and right child I=43
    B=7:  left C=3 (children D=2, E=5), right F=11
    F=11: right G=17, whose left child is H=13
    I=43: left J=23, right O=47
    J=23: right K=37 (children L=29, N=41); L=29 has right child M=31
    O=47: right P=53

HINT (from the textbook)
------------------------
"For what specific arrangements of the three nodes does the check pass?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: check whether the first node is a proper ancestor of the middle
and the second a proper descendant of it. If so, return true; otherwise
return the result of the same check with the roles of the first and second
nodes swapped. Example on Figure 14.1, nodes {L, I}, middle K: searching for
K from L fails, but searching for K from I succeeds; then searching for L
from K succeeds, so the answer is true.

Each search is O(h), h being the tree height, because the BST property
lets us discard one of the two children at every node. At most three
searches are performed, so the total is O(h).

Drawback of trying the two candidate ancestors one after another: even when
the three nodes are very close, e.g. nodes {A, J} with middle I, starting
the search for the middle from the lower node (J) costs the full O(h).

Improvement: search for the middle from both candidates in an INTERLEAVED
fashion. As soon as the middle is reached from one candidate, search for the
other candidate starting from the middle. This avoids running an unsuccessful
search over a large subtree. For {A, J} with middle I: search for I from both
A and J, stopping as soon as I is reached from A, thereby avoiding a wasteful
search from J. (A search for J from I is still needed to finish.)

In this file: `pair_includes_ancestor_and_descendant_of_m` implements the
book's BRUTE-FORCE approach (sequential searches, both orders). The book's
interleaved-search listing is not present.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    BST 5 (left 3 whose left child is 1; right 8);
    nodes {5, 1}, middle 3 -> True (5 is above 3, which is above 1)
"""

# Local project import (not the standard library): the chapter's shared BST
# node class, defined in bst_nodes.py in this same package. The leading dot
# makes this a package-relative import ("from the current package").
# BSTNode is a dataclass with fields `data`, `left` and `right`. It is
# declared with `eq=False`, so `==` between nodes means identity, as for
# ordinary objects.
# Relative imports: https://docs.python.org/3/reference/import.html#package-relative-imports
# dataclasses (used by BSTNode): https://docs.python.org/3/library/dataclasses.html
from .bst_nodes import BSTNode


# Type hints: three BSTNode objects in, a bool out. Python does not enforce
# annotations at run time.
def pair_includes_ancestor_and_descendant_of_m(
    possible_anc_or_desc_0: BSTNode,
    possible_anc_or_desc_1: BSTNode,
    middle: BSTNode,
) -> bool:
    """Check one candidate is a proper ancestor and other proper descendant.

    This follows the textbook's brute-force approach (two sequential
    searches, then the same check with the roles swapped), not the book's
    interleaved-search listing.
    """

    # Nested helper: is `ancestor` a PROPER ancestor of `descendant`?
    def proper_ancestor(ancestor: BSTNode, descendant: BSTNode) -> bool:
        current = ancestor

        # `is` / `is not` compare object identity: we are looking for that
        # very node, not merely a node with an equal key.
        while current is not None and current is not descendant:

            # BST search step written as a conditional expression
            # `X if cond else Y`: go left when the target key is smaller.
            current = current.left if descendant.data < current.data else current.right

        # Found it, and the two nodes are different ("proper").
        return current is descendant and ancestor is not descendant

    # Either node 0 is above the middle and node 1 below it, or vice versa.
    # `and` / `or` short-circuit, so later searches run only when needed.
    return (proper_ancestor(possible_anc_or_desc_0,middle)
            and proper_ancestor(middle,possible_anc_or_desc_1)) or (
            proper_ancestor(possible_anc_or_desc_1,middle)
            and proper_ancestor(middle,possible_anc_or_desc_0))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 212)
# --------------------------------------------
# For the interleaved version: when the middle node does have an ancestor and
# a descendant in the pair, the time is O(d), where d is the difference
# between the depths of the ancestor and the descendant. The interleaved
# search stops once the ancestor reaches the middle, after O(d) iterations,
# and the search from the middle down to the descendant then succeeds in
# O(d) steps. When the pair does not contain an ancestor and a descendant of
# the middle, the time is O(h), a worst-case BST search.
#
# (The brute-force version implemented in this file is O(h), as discussed
# in the development above.)
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0,
#   possible_anc_or_desc_1, middle)` performs INTERLEAVED searches
#   (`search_0`, `search_1` advanced together in one while loop; comment
#   "Perform interleaved searching from possible_anc_or_desc_0 and
#   possible_anc_or_desc_1 for middle."), returns False if neither search
#   reached the middle or one candidate reached the other first (comment
#   "If both searches were unsuccessful, or we got from ... without seeing
#   middle, middle cannot lie between ..."), and finally calls a nested
#   `search_target(source, target)` from the middle toward whichever
#   candidate did not reach it (comment "If we get here, we already know one
#   of ... has a path to middle. Check if middle has a path to ...").
# - File: same function name and parameter names, with type hints, but it
#   implements the book's brute-force idea instead: a nested
#   `proper_ancestor(ancestor, descendant)` search used for both orders.
#   The interleaved listing is NOT present. Results are the same; the
#   interleaved version's O(d) bound for the positive case is not obtained.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Because of the relative import above, run it as a module:
#   python -m epi_python.chapter_14_binary_search_trees.pg_211_pair_includes_ancestor_and_descendant_of_m
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example (not from the book). Semicolons put several simple
    # statements on one line: build 1 (leaf), 3 (its parent), and the root 5.
    leaf=BSTNode(1); mid=BSTNode(3,leaf); root=BSTNode(5,mid,BSTNode(8))
    print('Ordered ancestor/middle/descendant:',pair_includes_ancestor_and_descendant_of_m(root,leaf,mid))

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert pair_includes_ancestor_and_descendant_of_m(root,leaf,mid)
