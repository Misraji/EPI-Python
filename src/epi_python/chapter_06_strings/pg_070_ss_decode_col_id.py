"""EPI 6.3: Compute the spreadsheet column encoding — printed page 70.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Compute the spreadsheet column encoding
Algorithm: Interpret spreadsheet column letters as base 26 with A=1 through Z=26.
Read the corresponding `pg_070_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_06_strings.pg_070_ss_decode_col_id
Test: python -m pytest tests/chapter_06_strings/test_pg_070_ss_decode_col_id.py -v
"""

def ss_decode_col_id(column: str) -> int:
    """Spreadsheet column label to 1-indexed column number."""
    result = 0
    for character in column:
        result = result * 26 + ord(character) - ord('A') + 1
    return result


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = ss_decode_col_id('A')
    print("ss_decode_col_id:", observed)
    assert observed == 1
    observed = ss_decode_col_id('Z')
    print("ss_decode_col_id:", observed)
    assert observed == 26
    observed = ss_decode_col_id('AA')
    print("ss_decode_col_id:", observed)
    assert observed == 27
    observed = ss_decode_col_id('AB')
    print("ss_decode_col_id:", observed)
    assert observed == 28
