"""EPI 14.1: Test if a binary tree satisfies the BST property, printed page 199.

Educational reconstruction, not a verbatim transcription. Algorithm: Propagate key bounds from all ancestors rather than checking only immediate children. Allows duplicates.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_14_binary_search_trees.pg_199_is_binary_tree_bst
Tests: python -m pytest tests/chapter_14_binary_search_trees/test_pg_199_is_binary_tree_bst.py -v
"""

# dataclass produces a simple binary-search-tree node data type.
# Documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class TreeNode:
    data: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def is_bst_nodes(root: TreeNode | None) -> bool:
    """Check every node against the full valid ancestor key range."""
    def valid(node,lower,upper):
        if node is None:
            return True
        if not lower <= node.data <= upper:
            return False
        return valid(node.left,lower,node.data) and valid(node.right,node.data,upper)
    return valid(root,float('-inf'),float('inf'))


def is_binary_tree_bst(tree: tuple | None) -> bool:
    def build(t):
        return None if t is None else TreeNode(t[0],build(t[1]),build(t[2]))
    return is_bst_nodes(build(tree))

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=is_binary_tree_bst(None)
    print('is_binary_tree_bst', result)
    assert result == True
    result=is_binary_tree_bst((2, (1, None, None), (3, None, None)))
    print('is_binary_tree_bst', result)
    assert result == True
    result=is_binary_tree_bst((2, (3, None, None), (1, None, None)))
    print('is_binary_tree_bst', result)
    assert result == False
    result=is_binary_tree_bst((10, (5, None, (12, None, None)), (15, None, None)))
    print('is_binary_tree_bst', result)
    assert result == False
