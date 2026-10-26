"""EPI 6.12: Implement run-length encoding (printed page 79).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Implement run-length encoding
Method: Encode repeated adjacent characters as count plus value; decode using digit parsing. The two functions are tested separately.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_079_exercise_06_12_implement_run_length_encoding.md

Run independently:
    python -m epi_python.chapter_06_strings.pg_079_run_length_encoding
Run thorough tests:
    python -m pytest tests/chapter_06_strings/test_pg_079_run_length_encoding.py -v
"""

def encoding(text: str) -> str:
    """Run-length encode a text string as count + symbol segments."""
    parts: list[str] = []
    index = 0
    while index < len(text):
        end = index + 1
        while end < len(text) and text[end] == text[index]:
            end += 1
        parts.append(str(end - index) + text[index])
        index = end

    # str.join() assembles a list of strings with no separator here.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#str.join
    return "".join(parts)


def decoding(text: str) -> str:
    """Decode count + symbol segments (assumes symbol is not a digit)."""
    pieces: list[str] = []
    count = 0
    for symbol in text:
        if symbol.isdigit():
            count = count * 10 + int(symbol)
        else:
            pieces.append(symbol * count)
            count = 0
    return "".join(pieces)


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = encoding('')
    print("encoding:", observed)
    assert observed == ''
    observed = encoding('a')
    print("encoding:", observed)
    assert observed == '1a'
    observed = encoding('aaaabcccaa')
    print("encoding:", observed)
    assert observed == '4a1b3c2a'
    observed = encoding('ab')
    print("encoding:", observed)
    assert observed == '1a1b'
