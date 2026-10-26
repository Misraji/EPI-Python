"""EPI 6.8: The look-and-say problem — printed page 75.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: The look-and-say problem
Algorithm: Iteratively describe maximal adjacent runs: “one 1” becomes 11, then “two 1s” becomes 21.
Read the corresponding `pg_075_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_06_strings.pg_075_look_and_say
Test: python -m pytest tests/chapter_06_strings/test_pg_075_look_and_say.py -v
"""

def look_and_say(n: int) -> str:
    """Return the nth look-and-say sequence term, beginning with '1'."""
    term = '1'
    for _ in range(1,n):
        chunks = []
        i = 0
        while i < len(term):
            j = i + 1
            while j < len(term) and term[j] == term[i]:
                j += 1
            chunks.append(str(j - i) + term[i])
            i = j
        term = ''.join(chunks)
    return term


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = look_and_say(1)
    print("look_and_say:", observed)
    assert observed == '1'
    observed = look_and_say(2)
    print("look_and_say:", observed)
    assert observed == '11'
    observed = look_and_say(3)
    print("look_and_say:", observed)
    assert observed == '21'
    observed = look_and_say(4)
    print("look_and_say:", observed)
    assert observed == '1211'
