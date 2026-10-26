"""EPI Python 15.8, textbook printed page 229: Generate binary trees.

QUESTION: Return every distinct binary-tree shape containing exactly n nodes.

TEXTBOOK ALGORITHM: Split n-1 nodes across left and right subtrees; form their Cartesian product. Empty tree is None.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_15_recursion.pg_229_generate_all_binary_trees
Test: python -m pytest tests/chapter_15_recursion/test_pg_229_generate_all_binary_trees.py -v
"""

# dataclasses standard-library documentation: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class BinaryTreeNode:
    data: int
    left: 'BinaryTreeNode | None' = None
    right: 'BinaryTreeNode | None' = None


def generate_all_binary_trees(num_nodes: int) -> list[BinaryTreeNode | None]:
    if num_nodes == 0:
        return [None]
    result: list[BinaryTreeNode] = []
    for num_left_tree_nodes in range(num_nodes):
        num_right_tree_nodes = num_nodes - 1 - num_left_tree_nodes
        left_subtrees = generate_all_binary_trees(num_left_tree_nodes)
        right_subtrees = generate_all_binary_trees(num_right_tree_nodes)

        # The comprehension forms every possible left/right subtree pairing.
        result += [BinaryTreeNode(0, left, right)
                   for left in left_subtrees for right in right_subtrees]
    return result


if __name__ == '__main__':
    trees = generate_all_binary_trees(3)
    print('Distinct binary trees with three nodes:', len(trees))
    assert len(trees) == 5
