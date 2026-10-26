from epi_python.chapter_14_binary_search_trees.bst_nodes import BSTNode
from epi_python.chapter_14_binary_search_trees.pg_212_range_lookup_in_bst import range_lookup_in_bst


def test_range_lookup():
    root=BSTNode(10,BSTNode(5,BSTNode(2),BSTNode(7)),BSTNode(15,BSTNode(12),BSTNode(20)))
    for low,high,expected in [(0,30,[2,5,7,10,12,15,20]),(6,15,[7,10,12,15]),(11,11,[]),(0,2,[2]),(16,19,[])]:
        assert range_lookup_in_bst(root,low,high)==expected


def test_empty():
    assert range_lookup_in_bst(None,0,10)==[]
