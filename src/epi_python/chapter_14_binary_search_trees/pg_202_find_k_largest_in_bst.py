"""EPI 14.3: Find the k largest elements in a BST (printed page 202).

Problem: Find the k largest elements in a BST. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(h+k) node visits and recursion depth O(h).

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.3, printed page 202):
# Find the k largest elements in a BST in decreasing order.
# HINT: Reverse inorder traversal visits large values first.

# Package-relative import gets the common BST node used in this chapter.
# Documentation: https://docs.python.org/3/reference/import.html#package-relative-imports
from .bst_nodes import BSTNode


def find_k_largest_in_bst(tree: BSTNode | None, k: int) -> list[int]:
    """Reverse inorder traversal, stopping after the requested k keys."""
    result: list[int] = []

    def helper(subtree: BSTNode | None) -> None:
        if subtree and len(result) < k:
            helper(subtree.right)
            if len(result) < k:
                result.append(subtree.data)
                helper(subtree.left)

    helper(tree)
    return result


if __name__ == "__main__":
    root = BSTNode(10, BSTNode(5), BSTNode(15, BSTNode(12), BSTNode(20)))
    print("Three largest keys:", find_k_largest_in_bst(root, 3))
    assert find_k_largest_in_bst(root, 3) == [20, 15, 12]
