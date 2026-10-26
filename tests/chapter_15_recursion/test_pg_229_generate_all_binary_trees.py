# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_15_recursion.pg_229_generate_all_binary_trees import generate_all_binary_trees


def size(tree):
    return 0 if tree is None else 1 + size(tree.left) + size(tree.right)


def shape(tree):
    return None if tree is None else (shape(tree.left), shape(tree.right))


@pytest.mark.parametrize(('n', 'catalan'), [(0,1),(1,1),(2,2),(3,5),(4,14)])
def test_shapes(n, catalan):
    trees = generate_all_binary_trees(n)
    assert len(trees) == catalan
    assert all(size(t) == n for t in trees)
    assert len({str(shape(t)) for t in trees}) == catalan
