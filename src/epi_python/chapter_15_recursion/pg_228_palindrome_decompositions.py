"""EPI Python 15.7, textbook printed page 228: Generate palindromic decompositions.

QUESTION: Enumerate every way to partition a string into palindromic substrings.

TEXTBOOK ALGORITHM: Try palindromic prefixes, recursively extend the rest of the input; the printed book also supplies a Pythonic recursive variant.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_15_recursion.pg_228_palindrome_decompositions
Test: python -m pytest tests/chapter_15_recursion/test_pg_228_palindrome_decompositions.py -v
"""

def palindrome_decompositions(text: str) -> list[list[str]]:
    """Backtracking implementation from the PDF solution."""
    result: list[list[str]] = []

    def directed_palindrome_decompositions(offset: int, partial_partition: list[str]) -> None:
        if offset == len(text):
            result.append(list(partial_partition))
            return
        for i in range(offset + 1, len(text) + 1):
            prefix = text[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_decompositions(i, partial_partition + [prefix])

    directed_palindrome_decompositions(0, [])
    return result


def palindrome_decompositions_pythonic(text: str) -> list[list[str]]:
    """The second, concise implementation printed below the first."""
    return ([[text[:i]] + right
             for i in range(1, len(text) + 1)
             if text[:i] == text[:i][::-1]
             for right in palindrome_decompositions_pythonic(text[i:])]
            or [[]])


if __name__ == '__main__':
    for function in (palindrome_decompositions, palindrome_decompositions_pythonic):
        result = function('aab')
        print(function.__name__, result)
        assert sorted(result) == [['a', 'a', 'b'], ['aa', 'b']]
