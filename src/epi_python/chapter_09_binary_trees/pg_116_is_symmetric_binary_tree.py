"""EPI 9.2: Test if a binary tree is symmetric, printed page 116.

Educational reconstruction, not a verbatim transcription. Algorithm: Recursively compare left child of one side to right child of its mirror.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_09_binary_trees.pg_116_is_symmetric_binary_tree
Tests: python -m pytest tests/chapter_09_binary_trees/test_pg_116_is_symmetric_binary_tree.py -v
"""

# dataclass creates the ordinary mutable binary-tree node record.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class TreeNode:
    data: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def is_symmetric_nodes(root: TreeNode | None) -> bool:
    """Compare mirror-image subtrees recursively."""
    def mirrored(left,right):
        if left is None or right is None:
            return left is right
        return (left.data==right.data and mirrored(left.left,right.right)
                and mirrored(left.right,right.left))
    return root is None or mirrored(root.left,root.right)


def is_symmetric_binary_tree(tree: tuple | None) -> bool:
    def build(t):
        return None if t is None else TreeNode(t[0],build(t[1]),build(t[2]))
    return is_symmetric_nodes(build(tree))

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=is_symmetric_binary_tree(None)
    print('is_symmetric_binary_tree', result)
    assert result == True
    result=is_symmetric_binary_tree((1, None, None))
    print('is_symmetric_binary_tree', result)
    assert result == True
    result=is_symmetric_binary_tree((1, (2, None, None), (2, None, None)))
    print('is_symmetric_binary_tree', result)
    assert result == True
    result=is_symmetric_binary_tree((1, (2, None, None), (3, None, None)))
    print('is_symmetric_binary_tree', result)
    assert result == False
