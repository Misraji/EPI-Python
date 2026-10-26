"""EPI 17.4: The 3-sum problem (printed page 264).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: The 3-sum problem
Method: For each candidate, use a two-pointer two-sum search in the sorted input. Repetitions are allowed by this EPI exercise.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_264_exercise_17_04_the_3_sum_problem.md

Run independently:
    python -m epi_python.chapter_17_greedy_algorithms_and_invariants.pg_264_has_three_sum
Run thorough tests:
    python -m pytest tests/chapter_17_greedy_algorithms_and_invariants/test_pg_264_has_three_sum.py -v
"""

def has_three_sum(values: list[int], target: int) -> bool:
    """Check whether three values (repetitions allowed) sum to target."""

    # sorted(iterable) creates a NEW sorted list without modifying the input.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    ordered = sorted(values)
    for candidate in ordered:
        left, right = 0, len(ordered) - 1
        while left <= right:
            total = candidate + ordered[left] + ordered[right]
            if total == target:
                return True
            if total < target:
                left += 1
            else:
                right -= 1
    return False


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = has_three_sum([], 0)
    print("has_three_sum:", observed)
    assert observed == False
    observed = has_three_sum([1, 2, 3], 6)
    print("has_three_sum:", observed)
    assert observed == True
    observed = has_three_sum([1, 2, 3], 9)
    print("has_three_sum:", observed)
    assert observed == True
    observed = has_three_sum([1, 2, 3], 0)
    print("has_three_sum:", observed)
    assert observed == False
    observed = has_three_sum([0], 0)
    print("has_three_sum:", observed)
    assert observed == True
