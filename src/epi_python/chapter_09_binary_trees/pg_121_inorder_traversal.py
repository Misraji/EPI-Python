"""EPI 9.7: Implement an inorder traversal without recursion, printed page 121.

Educational reconstruction, not a verbatim transcription. Algorithm: Emulate recursive left-root-right traversal with an explicit stack of ancestors.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_09_binary_trees.pg_121_inorder_traversal
Tests: python -m pytest tests/chapter_09_binary_trees/test_pg_121_inorder_traversal.py -v
"""

# Standard-library dataclass decorator: ordinary tree node records.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class TreeNode:
    data: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def inorder_nodes(root: TreeNode | None) -> list[int]:
    """Inorder tree traversal using an explicit stack, not recursion."""
    result=[]
    stack=[]
    current=root
    while stack or current is not None:
        if current is not None:
            stack.append(current)
            current=current.left
        else:
            current=stack.pop()
            result.append(current.data)
            current=current.right
    return result


def inorder_traversal(tree: tuple | None) -> list[int]:
    def build(t):
        return None if t is None else TreeNode(t[0],build(t[1]),build(t[2]))
    return inorder_nodes(build(tree))

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=inorder_traversal(None)
    print('inorder_traversal', result)
    assert result == []
    result=inorder_traversal((1, None, None))
    print('inorder_traversal', result)
    assert result == [1]
    result=inorder_traversal((2, (1, None, None), (3, None, None)))
    print('inorder_traversal', result)
    assert result == [1, 2, 3]
