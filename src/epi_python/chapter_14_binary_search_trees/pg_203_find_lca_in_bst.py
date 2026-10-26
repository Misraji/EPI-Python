"""EPI 14.4: Compute the LCA in a BST (printed page 203).

Problem: Compute the LCA in a BST. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(h) time and O(1) space for distinct BST keys.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.4, printed page 203):
# Find the lowest common ancestor of two nodes in a BST with distinct keys.
# HINT: The split point of their search paths is their LCA.

# Package-relative import gets the common BST node used in this chapter.
# Documentation: https://docs.python.org/3/reference/import.html#package-relative-imports
from .bst_nodes import BSTNode


def find_lca_in_bst(tree: BSTNode | None, smaller: BSTNode, bigger: BSTNode) -> BSTNode | None:
    """Find where the two keys' search paths first diverge."""
    low, high = sorted((smaller.data, bigger.data))
    while tree:
        if tree.data < low:
            tree = tree.right
        elif tree.data > high:
            tree = tree.left
        else:
            return tree
    return None


if __name__ == "__main__":
    left, right = BSTNode(5), BSTNode(15)
    root = BSTNode(10,left,right)
    print("Lowest common ancestor:", find_lca_in_bst(root,left,right).data)
    assert find_lca_in_bst(root,left,right) is root
