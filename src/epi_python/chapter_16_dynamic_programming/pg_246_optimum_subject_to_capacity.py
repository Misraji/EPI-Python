"""EPI 16.6: The knapsack problem, printed page 246.

Educational reconstruction, not a verbatim transcription. Algorithm: Descending-capacity DP ensures each item is used at most once, O(n*capacity) time.
The corresponding chapter's exercise Markdown retains the PDF text-layer
explanations, question and variants (with known OCR mistakes).

Run: python -m epi_python.chapter_16_dynamic_programming.pg_246_optimum_subject_to_capacity
Tests: python -m pytest tests/chapter_16_dynamic_programming/test_pg_246_optimum_subject_to_capacity.py -v
"""

def optimum_subject_to_capacity(items: list[tuple[int, int]], capacity: int) -> int:
    """Maximum value of 0/1 knapsack items (weight,value)."""
    best=[0]*(capacity+1)
    for weight,value in items:
        for limit in range(capacity,weight-1,-1):
            best[limit]=max(best[limit],best[limit-weight]+value)
    return best[capacity]

if __name__ == "__main__":
    # Executable demonstration cases; pytest has the full set.
    result=optimum_subject_to_capacity([], 10)
    print('optimum_subject_to_capacity', result)
    assert result == 0
    result=optimum_subject_to_capacity([(2, 3), (3, 4), (4, 5)], 5)
    print('optimum_subject_to_capacity', result)
    assert result == 7
    result=optimum_subject_to_capacity([(2, 10)], 1)
    print('optimum_subject_to_capacity', result)
    assert result == 0
    result=optimum_subject_to_capacity([(2, 10), (2, 20)], 4)
    print('optimum_subject_to_capacity', result)
    assert result == 30
