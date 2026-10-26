"""EPI 6.1: Interconvert strings and integers — printed page 68.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Interconvert strings and integers
Algorithm: Use character codes and repeated base-10 arithmetic to interconvert int and str.
Read the corresponding `pg_068_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_06_strings.pg_068_string_integer_interconversion
Test: python -m pytest tests/chapter_06_strings/test_pg_068_string_integer_interconversion.py -v
"""

def int_to_string(x: int) -> str:
    """Convert an integer to decimal characters without calling str(x)."""
    if x == 0:
        return '0'
    negative = x < 0
    x = abs(x)
    digits = []
    while x:
        digits.append(chr(ord('0') + x % 10))
        x //= 10
    if negative:
        digits.append('-')
    return ''.join(reversed(digits))


def string_to_int(text: str) -> int:
    """Convert an optional leading minus and decimal digits to an integer."""
    negative = text.startswith('-')
    result = 0
    for digit in text[int(negative):]:
        result = result * 10 + ord(digit) - ord('0')
    return -result if negative else result


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = int_to_string(0)
    print("int_to_string:", observed)
    assert observed == '0'
    observed = int_to_string(3)
    print("int_to_string:", observed)
    assert observed == '3'
    observed = int_to_string(-125)
    print("int_to_string:", observed)
    assert observed == '-125'
    observed = int_to_string(2001)
    print("int_to_string:", observed)
    assert observed == '2001'
