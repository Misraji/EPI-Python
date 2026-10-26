"""EPI exercise 12.4, printed page 166: Compute the LCA, optimizing for close ancestors.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the LCA, optimizing for close ancestors.
Method/complexity: Interleaved ancestor walk O(h) worst-case time/space, early termination when ancestors are close.
For the book's original explanation and variants, see:
    pg_166_exercise_12_04_compute_the_lca_optimizing_for_close_ancestors.md

Run: python -m epi_python.chapter_12_hash_tables.pg_166_lca_close_ancestors
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_166_lca_close_ancestors.py -v
"""

# Reuse parent-aware binary tree from chapter 9.
from epi_python.chapter_09_binary_trees.pg_118_lca_with_parent import ParentNode, build_parent_tree, find_node


def lca_close_ancestors(a: ParentNode | None, b: ParentNode | None) -> ParentNode | None:
    """Walk both parent chains alternately; stop at first common ancestor."""
    visited: set[int] = set()
    while a is not None or b is not None:
        if a is not None:
            if id(a) in visited:
                return a
            visited.add(id(a))
            a = a.parent
        if b is not None:
            if id(b) in visited:
                return b
            visited.add(id(b))
            b = b.parent
    return None


def lca_close_value(tree, a: int, b: int) -> int | None:
    root = build_parent_tree(tree)
    node_a, node_b = find_node(root, a), find_node(root, b)
    node = lca_close_ancestors(node_a, node_b)
    return None if node is None else node.data


if __name__ == "__main__":
    tree=(4,(2,(1,None,None),(3,None,None)),(6,None,None))
    print("close-ancestor LCA:", lca_close_value(tree,1,3))
    assert lca_close_value(tree,1,3) == 2
