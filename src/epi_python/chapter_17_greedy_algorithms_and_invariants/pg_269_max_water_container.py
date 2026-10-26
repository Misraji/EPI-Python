"""EPI 17.7: Compute the maximum water trapped by a pair of vertical lines — printed page 269.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Compute the maximum water trapped by a pair of vertical lines
Algorithm: Two pointers start at both ends; advance the limiting (shorter) wall each iteration.
Read the corresponding `pg_269_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_17_greedy_algorithms_and_invariants.pg_269_max_water_container
Test: python -m pytest tests/chapter_17_greedy_algorithms_and_invariants/test_pg_269_max_water_container.py -v
"""

def max_water_container(heights: list[int]) -> int:
    """Maximum area between two vertical height lines."""
    left,right=0,len(heights)-1
    best=0
    while left<right:
        best=max(best,(right-left)*min(heights[left],heights[right]))
        if heights[left]<heights[right]:
            left+=1
        else:
            right-=1
    return best


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = max_water_container([])
    print("max_water_container:", observed)
    assert observed == 0
    observed = max_water_container([1])
    print("max_water_container:", observed)
    assert observed == 0
    observed = max_water_container([1, 1])
    print("max_water_container:", observed)
    assert observed == 1
    observed = max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print("max_water_container:", observed)
    assert observed == 49
