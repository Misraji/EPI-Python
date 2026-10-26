"""EPI 14.2: Find the first key greater than a given value in a BST (printed page 201).

Problem: Find the first key greater than a given value in a BST. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(h) time and O(1) extra space, iterative BST search.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.2, printed page 201):
# Return the smallest key in a BST that is strictly greater than a given key.
# HINT: Keep the best candidate when descending to the left.

# Package-relative import gets the common BST node used in this chapter.
# Documentation: https://docs.python.org/3/reference/import.html#package-relative-imports
from .bst_nodes import BSTNode


def find_first_greater_than_k(tree: BSTNode | None, k: int) -> BSTNode | None:
    """Return the node with the smallest key strictly greater than k."""
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right
    return first_so_far


if __name__ == "__main__":
    root = BSTNode(10, BSTNode(5), BSTNode(15, BSTNode(12)))
    result = find_first_greater_than_k(root, 10)
    print("First key greater than 10:", result.data)
    assert result.data == 12
