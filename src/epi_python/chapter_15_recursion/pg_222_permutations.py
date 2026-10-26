"""EPI 15.3: Generate permutations (printed page 222).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Generate permutations
Method: Backtracking with swap/restore explores every ordering; O(n·n!) time for output construction.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_222_exercise_15_03_generate_permutations.md

Run independently:
    python -m epi_python.chapter_15_recursion.pg_222_permutations
Run thorough tests:
    python -m pytest tests/chapter_15_recursion/test_pg_222_permutations.py -v
"""

def permutations(values: list[int]) -> list[list[int]]:
    """Enumerate all permutations by swapping one value into each position."""
    result: list[list[int]] = []
    remaining = values.copy()

    def visit(position: int) -> None:
        if position == len(remaining):
            result.append(remaining.copy())
            return
        for index in range(position, len(remaining)):
            remaining[position], remaining[index] = remaining[index], remaining[position]
            visit(position + 1)
            remaining[position], remaining[index] = remaining[index], remaining[position]

    visit(0)
    return result


if __name__ == "__main__":
    result = permutations([1, 2, 3])
    print("All permutations:", result)
    assert len(result) == 6
