"""EPI 14.10: The range lookup problem (printed page 212).

Problem: The range lookup problem. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(h+m) output-sensitive on a balanced BST, m keys in the range.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.10, printed page 212):
# Return all BST keys lying in a given inclusive value interval.
# HINT: Prune subtrees that cannot contain a key in the range.

# Package-relative import gets the common BST node used in this chapter.
# Documentation: https://docs.python.org/3/reference/import.html#package-relative-imports
from .bst_nodes import BSTNode


def range_lookup_in_bst(tree: BSTNode | None, low: int, high: int) -> list[int]:
    """Return all BST keys within the inclusive [low, high] interval."""
    result: list[int] = []

    def helper(node: BSTNode | None) -> None:
        if node is None:
            return
        if low <= node.data <= high:
            helper(node.left)
            result.append(node.data)
            helper(node.right)
        elif node.data < low:
            helper(node.right)
        else:
            helper(node.left)

    helper(tree)
    return result


if __name__ == '__main__':
    root=BSTNode(10,BSTNode(5),BSTNode(15,BSTNode(12),BSTNode(20)))
    print('Keys between 8 and 16:',range_lookup_in_bst(root,8,16))
    assert range_lookup_in_bst(root,8,16)==[10,12,15]
