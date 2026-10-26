"""EPI 14.8: Build a minimum height BST from a sorted array (printed page 210).

Problem: Build a minimum height BST from a sorted array. The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(n) construction time; O(log n) depth for distinct sorted keys.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.8, printed page 210):
# Build a minimum-height BST from a sorted array.
# HINT: Choose the middle element as root and recurse.

# Package-relative import gets the common BST node used in this chapter.
# Documentation: https://docs.python.org/3/reference/import.html#package-relative-imports
from .bst_nodes import BSTNode


def build_min_height_bst_from_sorted_array(values: list[int]) -> BSTNode | None:
    """Choose each subarray's midpoint as the root for a balanced BST."""
    def build(start: int,end: int) -> BSTNode | None:
        if start >= end:
            return None
        middle=(start+end)//2
        return BSTNode(values[middle],build(start,middle),build(middle+1,end))
    return build(0,len(values))


if __name__ == '__main__':
    result=build_min_height_bst_from_sorted_array([1,2,3,4,5,6,7])
    print('Root of minimum-height BST:',result.data)
    assert result.data==4
