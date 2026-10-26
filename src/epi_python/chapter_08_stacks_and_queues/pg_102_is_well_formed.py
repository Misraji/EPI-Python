"""EPI 8.3: Test a string for well-formedness — printed page 102.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Test a string for well-formedness
Algorithm: A stack records unmatched opening delimiters; a closing one must match the most recent opening one.
Read the corresponding `pg_102_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_08_stacks_and_queues.pg_102_is_well_formed
Test: python -m pytest tests/chapter_08_stacks_and_queues/test_pg_102_is_well_formed.py -v
"""

def is_well_formed(brackets: str) -> bool:
    """Return whether (), [], and {} brackets are correctly nested."""
    matching = {')': '(', ']':'[', '}':'{'}
    stack = []
    for character in brackets:
        if character in '([{':
            stack.append(character)
        elif character in matching:
            if not stack or stack.pop() != matching[character]:
                return False
    return not stack


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = is_well_formed('')
    print("is_well_formed:", observed)
    assert observed == True
    observed = is_well_formed('()[]{}')
    print("is_well_formed:", observed)
    assert observed == True
    observed = is_well_formed('([{}])')
    print("is_well_formed:", observed)
    assert observed == True
    observed = is_well_formed('([)]')
    print("is_well_formed:", observed)
    assert observed == False
