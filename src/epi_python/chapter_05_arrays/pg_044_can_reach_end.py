"""EPI 5.4: Advancing through an array (printed page 44).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Advancing through an array
Method: Maintain the furthest reachable index; never explore positions beyond it. Time O(n), space O(1).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_044_exercise_05_04_advancing_through_an_array.md

Run independently:
    python -m epi_python.chapter_05_arrays.pg_044_can_reach_end
Run thorough tests:
    python -m pytest tests/chapter_05_arrays/test_pg_044_can_reach_end.py -v
"""

def can_reach_end(max_steps: list[int]) -> bool:
    """Check whether jumps from index zero can reach the final index."""
    farthest = 0
    last = len(max_steps) - 1
    for index, steps in enumerate(max_steps):
        if index > farthest:
            break
        farthest = max(farthest, index + steps)
        if farthest >= last:
            return True
    return last < 0


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = can_reach_end([3, 3, 1, 0, 2, 0, 1])
    print("can_reach_end:", observed)
    assert observed == True
    observed = can_reach_end([3, 2, 0, 0, 2, 0, 1])
    print("can_reach_end:", observed)
    assert observed == False
    observed = can_reach_end([0])
    print("can_reach_end:", observed)
    assert observed == True
    observed = can_reach_end([])
    print("can_reach_end:", observed)
    assert observed == True
    observed = can_reach_end([0, 1])
    print("can_reach_end:", observed)
    assert observed == False
