from epi_python.chapter_14_binary_search_trees.bst_nodes import BSTNode
from epi_python.chapter_14_binary_search_trees.pg_201_find_first_greater_than_k import find_first_greater_than_k


def test_successor():
    root = BSTNode(10, BSTNode(5, BSTNode(2), BSTNode(7)), BSTNode(20, BSTNode(15), BSTNode(22)))
    for key, expected in [(-1,2),(2,5),(6,7),(7,10),(10,15),(19,20),(22,None)]:
        node = find_first_greater_than_k(root,key)
        assert (node.data if node else None)==expected


def test_empty():
    assert find_first_greater_than_k(None,3) is None
