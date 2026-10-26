"""EPI exercise 8.5, printed page 103: Compute buildings with a sunset view.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute buildings with a sunset view.
Method/complexity: Backward scan tracking the tallest building to east; O(n) time, O(n) output.
For the book's original explanation and variants, see:
    pg_103_exercise_08_05_compute_buildings_with_a_sunset_view.md

Run: python -m epi_python.chapter_08_stacks_and_queues.pg_103_sunset_view
Test: python -m pytest tests/chapter_08_stacks_and_queues/test_pg_103_sunset_view.py -v
"""

def examine_buildings_with_sunset(heights: list[int]) -> list[int]:
    """Return west-to-east indices of buildings visible toward the east."""
    # A building is visible exactly when every building to its right is shorter.
    visible = []
    highest_to_east = float('-inf')
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > highest_to_east:
            visible.append(i)
            highest_to_east = heights[i]
    return visible[::-1]


if __name__ == "__main__":
    print("sunset-visible indices:", examine_buildings_with_sunset([3,7,8,3,6,1]))
    assert examine_buildings_with_sunset([3,7,8,3,6,1]) == [2,4,5]
