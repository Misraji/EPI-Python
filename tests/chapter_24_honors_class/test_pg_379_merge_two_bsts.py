# pytest documentation: https://docs.pytest.org/en/stable/
from epi_python.chapter_24_honors_class.pg_379_merge_two_bsts import BSTNode,merge_two_bsts


def inorder(tree):
    return [] if tree is None else inorder(tree.left)+[tree.data]+inorder(tree.right)


def height(tree):
    return 0 if tree is None else 1+max(height(tree.left),height(tree.right))


def test_merge():
    a=BSTNode(2,BSTNode(1),BSTNode(3))
    b=BSTNode(5,BSTNode(4),BSTNode(6))
    tree=merge_two_bsts(a,b)
    assert inorder(tree)==[1,2,3,4,5,6]
    assert height(tree)<=3


def test_empty():
    assert merge_two_bsts(None,None) is None
