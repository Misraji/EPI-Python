"""EPI 17.2: Schedule to minimize waiting time — printed page 261.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Schedule to minimize waiting time
Algorithm: Shortest-job-first minimizes total wait. Add prior job durations to the current total wait.
Read the corresponding `pg_261_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_17_greedy_algorithms_and_invariants.pg_261_minimum_waiting_time
Test: python -m pytest tests/chapter_17_greedy_algorithms_and_invariants/test_pg_261_minimum_waiting_time.py -v
"""

def minimum_waiting_time(service_times: list[int]) -> int:
    """Minimum total wait when one server handles jobs sequentially."""

    # sorted() leaves the caller's list unchanged.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    ordered=sorted(service_times)
    elapsed=0
    waiting=0
    for duration in ordered:
        waiting+=elapsed
        elapsed+=duration
    return waiting


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = minimum_waiting_time([])
    print("minimum_waiting_time:", observed)
    assert observed == 0
    observed = minimum_waiting_time([3])
    print("minimum_waiting_time:", observed)
    assert observed == 0
    observed = minimum_waiting_time([2, 5, 1])
    print("minimum_waiting_time:", observed)
    assert observed == 4
    observed = minimum_waiting_time([2, 2, 2])
    print("minimum_waiting_time:", observed)
    assert observed == 6
