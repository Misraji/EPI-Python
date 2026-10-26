"""EPI 17.5: Find the majority element — printed page 266.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Find the majority element
Algorithm: Boyer–Moore candidate cancellation followed by a verifying pass.
Read the corresponding `pg_266_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_17_greedy_algorithms_and_invariants.pg_266_majority_search
Test: python -m pytest tests/chapter_17_greedy_algorithms_and_invariants/test_pg_266_majority_search.py -v
"""

def majority_search(values: list[str]) -> str | None:
    """Return a majority element appearing more than half the time, if any."""
    candidate=None
    count=0
    for value in values:
        if count == 0:
            candidate=value
            count=1
        elif value == candidate:
            count+=1
        else:
            count-=1
    if candidate is not None and values.count(candidate)>len(values)//2:
        return candidate
    return None


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = majority_search([])
    print("majority_search:", observed)
    assert observed == None
    observed = majority_search(['a', 'a', 'b'])
    print("majority_search:", observed)
    assert observed == 'a'
    observed = majority_search(['a', 'b'])
    print("majority_search:", observed)
    assert observed == None
    observed = majority_search(['z'])
    print("majority_search:", observed)
    assert observed == 'z'
