"""EPI 16.10: Count the number of moves to climb stairs — printed page 253.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Count the number of moves to climb stairs
Algorithm: Sum the number of ways to arrive from each legal preceding step size.
Read the corresponding `pg_253_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_16_dynamic_programming.pg_253_number_of_ways_to_top
Test: python -m pytest tests/chapter_16_dynamic_programming/test_pg_253_number_of_ways_to_top.py -v
"""

def number_of_ways_to_top(top: int, max_step: int) -> int:
    """Number of ordered ways to climb top stairs with steps up to max_step."""
    ways=[0]*(top+1)
    ways[0]=1
    for height in range(1,top+1):
        ways[height]=sum(ways[height-step] for step in range(1,min(max_step,height)+1))
    return ways[top]


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = number_of_ways_to_top(0, 2)
    print("number_of_ways_to_top:", observed)
    assert observed == 1
    observed = number_of_ways_to_top(1, 2)
    print("number_of_ways_to_top:", observed)
    assert observed == 1
    observed = number_of_ways_to_top(2, 2)
    print("number_of_ways_to_top:", observed)
    assert observed == 2
    observed = number_of_ways_to_top(3, 2)
    print("number_of_ways_to_top:", observed)
    assert observed == 3
