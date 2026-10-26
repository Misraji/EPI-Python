"""EPI exercise 6.2, printed page 69: Base conversion.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Base conversion.
Method/complexity: Parse positional notation, then repeated quotient/remainder extraction; O(digits²) with arbitrary-precision big integers.
For the book's original explanation and variants, see:
    pg_069_exercise_06_02_base_conversion.md

Run: python -m epi_python.chapter_06_strings.pg_069_convert_base
Test: python -m pytest tests/chapter_06_strings/test_pg_069_convert_base.py -v
"""

DIGITS = "0123456789ABCDEF"


def convert_base(number: str, source_base: int, target_base: int) -> str:
    """Convert a signed integer string between bases 2 through 16."""
    if not 2 <= source_base <= 16 or not 2 <= target_base <= 16:
        raise ValueError("Only bases 2 through 16 are supported")
    if not number or number == '-':
        raise ValueError("Missing digits")
    sign = -1 if number[0] == '-' else 1
    abs_text = number.lstrip('-').upper()
    decimal_value = 0
    for digit in abs_text:
        value = DIGITS.find(digit)
        if not 0 <= value < source_base:
            raise ValueError("Digit is not valid in source base")
        decimal_value = decimal_value * source_base + value
    if decimal_value == 0:
        return "0"
    symbols = []
    while decimal_value:
        decimal_value, remainder = divmod(decimal_value, target_base)
        symbols.append(DIGITS[remainder])
    return ('-' if sign < 0 else '') + ''.join(reversed(symbols))


if __name__ == "__main__":
    for text, b1, b2 in [("FF", 16, 10), ("101", 2, 10)]:
        print(f"{text} (base {b1}) -> {convert_base(text, b1, b2)} (base {b2})")
    assert convert_base("FF", 16, 10) == "255"
