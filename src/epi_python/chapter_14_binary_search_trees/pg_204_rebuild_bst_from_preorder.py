"""EPI 14.5: Reconstruct a BST from traversal data (printed page 204).

Problem: Reconstruct a BST from traversal data. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(n) time; each preorder value is consumed once.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.5, printed page 204):
# Reconstruct a BST from its preorder traversal.
# HINT: Use the known BST key ranges to consume the preorder sequence once.

# Package-relative import gets the common BST node used in this chapter.
# Documentation: https://docs.python.org/3/reference/import.html#package-relative-imports
from .bst_nodes import BSTNode


def rebuild_bst_from_preorder(preorder: list[int]) -> BSTNode | None:
    """Consume preorder values only when they fall in the subtree's key range."""
    root_idx = [0]

    def within_range(lower: float, upper: float) -> BSTNode | None:
        if root_idx[0] == len(preorder):
            return None
        key = preorder[root_idx[0]]
        if not lower < key < upper:
            return None
        root_idx[0] += 1
        left = within_range(lower, key)
        right = within_range(key, upper)
        return BSTNode(key, left, right)

    return within_range(float('-inf'), float('inf'))


if __name__ == "__main__":
    root=rebuild_bst_from_preorder([10,5,2,7,15,12,20])
    print("Reconstructed root:",root.data)
    assert root.left.right.data == 7
