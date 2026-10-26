"""EPI 6.9: Convert from Roman to decimal (printed page 76).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Convert from Roman to decimal
Method: Subtract the value of a symbol when a larger symbol immediately follows it. Assumes valid Roman input.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_076_exercise_06_09_convert_from_roman_to_decimal.md

Run independently:
    python -m epi_python.chapter_06_strings.pg_076_roman_to_integer
Run thorough tests:
    python -m pytest tests/chapter_06_strings/test_pg_076_roman_to_integer.py -v
"""

def roman_to_integer(roman: str) -> int:
    """Convert a valid Roman numeral to an integer."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for index, symbol in enumerate(roman):
        value = values[symbol]
        if index + 1 < len(roman) and value < values[roman[index + 1]]:
            result -= value
        else:
            result += value
    return result


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = roman_to_integer('I')
    print("roman_to_integer:", observed)
    assert observed == 1
    observed = roman_to_integer('IV')
    print("roman_to_integer:", observed)
    assert observed == 4
    observed = roman_to_integer('IX')
    print("roman_to_integer:", observed)
    assert observed == 9
    observed = roman_to_integer('XIV')
    print("roman_to_integer:", observed)
    assert observed == 14
    observed = roman_to_integer('MCMXCIV')
    print("roman_to_integer:", observed)
    assert observed == 1994
