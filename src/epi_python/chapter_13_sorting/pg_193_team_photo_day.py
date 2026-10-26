"""EPI 13.9, printed page 193: Team photo day - 1.

Problem: Team photo day - 1. See pg_193_exercise_13_09_team_photo_day_1.md for the full
original problem, hint, development, and variants from the PDF text layer.

Approach and complexity: O(n log n) sorting both teams; compare corresponding ranks.

EDUCATIONAL RECONSTRUCTION: source and comments are not claimed verbatim.
Run directly: python -m epi_python.chapter_13_sorting.pg_193_team_photo_day
Test: python -m pytest tests/chapter_13_sorting/test_pg_193_team_photo_day.py -v
"""

# TEXTBOOK PROBLEM (exercise 13.9, printed page 193):
# Determine whether all shorter members of one team can stand before members of another.
# HINT: Sort both teams by height and compare corresponding players.

def valid_placement_exists(team_a: list[int], team_b: list[int]) -> bool:
    """Return whether one team can stand strictly behind the other at all positions."""
    if len(team_a) != len(team_b):
        return False
    a, b = sorted(team_a), sorted(team_b)
    return all(x < y for x, y in zip(a,b)) or all(y < x for x, y in zip(a,b))


if __name__ == '__main__':
    a=[1,4,3]
    b=[2,6,5]
    print('Can photograph:', valid_placement_exists(a,b))
    assert valid_placement_exists(a,b)
