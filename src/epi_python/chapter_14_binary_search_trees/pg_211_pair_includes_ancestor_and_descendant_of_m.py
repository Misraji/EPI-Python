"""EPI 14.9: Test if three BST nodes are totally ordered (printed page 211).

Problem: Test if three BST nodes are totally ordered. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(h) worst-case for BST searches. The book further optimizes positive cases via interleaved searches.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.9, printed page 211):
# Check if one given node is an ancestor and the other a descendant of a middle node.
# HINT: Use the BST property to search along unique paths.

# Package-relative import gets the common BST node used in this chapter.
# Documentation: https://docs.python.org/3/reference/import.html#package-relative-imports
from .bst_nodes import BSTNode


def pair_includes_ancestor_and_descendant_of_m(
    possible_anc_or_desc_0: BSTNode,
    possible_anc_or_desc_1: BSTNode,
    middle: BSTNode,
) -> bool:
    """Check one candidate is a proper ancestor and other proper descendant."""
    def proper_ancestor(ancestor: BSTNode, descendant: BSTNode) -> bool:
        current = ancestor
        while current is not None and current is not descendant:
            current = current.left if descendant.data < current.data else current.right
        return current is descendant and ancestor is not descendant

    return (proper_ancestor(possible_anc_or_desc_0,middle)
            and proper_ancestor(middle,possible_anc_or_desc_1)) or (
            proper_ancestor(possible_anc_or_desc_1,middle)
            and proper_ancestor(middle,possible_anc_or_desc_0))


if __name__ == '__main__':
    leaf=BSTNode(1); mid=BSTNode(3,leaf); root=BSTNode(5,mid,BSTNode(8))
    print('Ordered ancestor/middle/descendant:',pair_includes_ancestor_and_descendant_of_m(root,leaf,mid))
    assert pair_includes_ancestor_and_descendant_of_m(root,leaf,mid)
