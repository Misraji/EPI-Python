"""EPI 15.5: Generate all subsets of size k — printed page 226.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Generate all subsets of size k
Algorithm: Backtracking enumerates increasing combinations and backtracks after each choice.
Read the corresponding `pg_226_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_15_recursion.pg_226_combinations
Test: python -m pytest tests/chapter_15_recursion/test_pg_226_combinations.py -v
"""

def combinations(n: int, k: int) -> list[list[int]]:
    """All k-element subsets chosen from {1, ..., n}."""
    result=[]
    def visit(next_value: int, partial: list[int]) -> None:
        if len(partial) == k:
            result.append(partial.copy())
            return
        for value in range(next_value,n+1):
            partial.append(value)
            visit(value+1,partial)
            partial.pop()
    visit(1,[])
    return result


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = combinations(0, 0)
    print("combinations:", observed)
    assert observed == [[]]
    observed = combinations(3, 0)
    print("combinations:", observed)
    assert observed == [[]]
    observed = combinations(3, 2)
    print("combinations:", observed)
    assert observed == [[1, 2], [1, 3], [2, 3]]
    observed = combinations(2, 3)
    print("combinations:", observed)
    assert observed == []
