"""EPI 16.1: Count the number of score combinations — printed page 236.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Count the number of score combinations
Algorithm: Unbounded coin-change dynamic programming over score, iterating each play value in the outer loop.
Read the corresponding `pg_236_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_16_dynamic_programming.pg_236_num_combinations_for_final_score
Test: python -m pytest tests/chapter_16_dynamic_programming/test_pg_236_num_combinations_for_final_score.py -v
"""

def num_combinations_for_final_score(score: int, scores: list[int]) -> int:
    """Number of unordered combinations that sum to the target score."""
    ways=[0]*(score+1)
    ways[0]=1
    for play in scores:
        for total in range(play,score+1):
            ways[total] += ways[total-play]
    return ways[score]


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = num_combinations_for_final_score(0, [2, 3])
    print("num_combinations_for_final_score:", observed)
    assert observed == 1
    observed = num_combinations_for_final_score(4, [2, 3])
    print("num_combinations_for_final_score:", observed)
    assert observed == 1
    observed = num_combinations_for_final_score(7, [2, 3, 7])
    print("num_combinations_for_final_score:", observed)
    assert observed == 2
    observed = num_combinations_for_final_score(1, [2, 3])
    print("num_combinations_for_final_score:", observed)
    assert observed == 0
