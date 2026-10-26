"""EPI 9.1: Test if a binary tree is height-balanced, printed page 114.

Educational reconstruction, not a verbatim transcription. Algorithm: Bottom-up height computation propagates an imbalance sentinel to avoid repeated work.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_09_binary_trees.pg_114_is_balanced_binary_tree
Tests: python -m pytest tests/chapter_09_binary_trees/test_pg_114_is_balanced_binary_tree.py -v
"""

# dataclass defines a binary tree node and produces its initializer.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class TreeNode:
    data: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def is_balanced_nodes(root: TreeNode | None) -> bool:
    """Detect subtrees whose heights differ by more than one."""
    def height(node):
        if node is None:
            return 0
        left=height(node.left)
        if left < 0:
            return -1
        right=height(node.right)
        if right < 0 or abs(left-right)>1:
            return -1
        return max(left,right)+1
    return height(root)>=0


def is_balanced_binary_tree(tree: tuple | None) -> bool:
    """Adapter: nested (value,left,right) tuples specify small test trees."""
    def build(t):
        return None if t is None else TreeNode(t[0],build(t[1]),build(t[2]))
    return is_balanced_nodes(build(tree))

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=is_balanced_binary_tree(None)
    print('is_balanced_binary_tree', result)
    assert result == True
    result=is_balanced_binary_tree((1, None, None))
    print('is_balanced_binary_tree', result)
    assert result == True
    result=is_balanced_binary_tree((1, (2, (3, None, None), None), None))
    print('is_balanced_binary_tree', result)
    assert result == False
    result=is_balanced_binary_tree((1, (2, None, None), (3, None, None)))
    print('is_balanced_binary_tree', result)
    assert result == True
