"""EPI exercise 5.10, printed page 50: Permute the elements of an array.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Permute the elements of an array.
Method/complexity: Follow permutation cycles; O(n) time, O(n) visited array in this readable version.
For the book's original explanation and variants, see:
    pg_050_exercise_05_10_permute_the_elements_of_an_array.md

Run: python -m epi_python.chapter_05_arrays.pg_050_apply_permutation
Test: python -m pytest tests/chapter_05_arrays/test_pg_050_apply_permutation.py -v
"""

def apply_permutation(perm: list[int], values: list[int]) -> list[int]:
    """Move old entry i to destination perm[i], mutating the given list."""
    if len(values) != len(perm) or sorted(perm) != list(range(len(perm))):
        raise ValueError("Expected a permutation of all indices")
    # Follow disjoint cycles: the visited array prevents moving entries twice.
    visited = [False] * len(values)
    for start in range(len(values)):
        if visited[start]:
            continue
        position, carried = start, values[start]
        while not visited[position]:
            visited[position] = True
            next_position = perm[position]
            values[next_position], carried = carried, values[next_position]
            position = next_position
    return values


if __name__ == "__main__":
    values = ["a", "b", "c"]
    print("permuted:", apply_permutation([2, 0, 1], values))
    assert values == ["b", "c", "a"]
