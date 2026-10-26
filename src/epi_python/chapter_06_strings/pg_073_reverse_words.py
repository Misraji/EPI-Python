"""EPI 6.6: Reverse all the words in a sentence — printed page 73.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Reverse all the words in a sentence
Algorithm: Split sentence into words, then join them in opposite order. In-place char-buffer version is also discussed in EPI.
Read the corresponding `pg_073_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_06_strings.pg_073_reverse_words
Test: python -m pytest tests/chapter_06_strings/test_pg_073_reverse_words.py -v
"""

def reverse_words(sentence: str) -> str:
    """Reverse the order of words separated by single ASCII spaces."""

    # str.split(sep) divides a string into a list at each separator.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#str.split
    words = sentence.split(' ')

    # reversed(sequence) yields elements in reverse order without sorting.
    # Documentation: https://docs.python.org/3/library/functions.html#reversed
    return ' '.join(reversed(words))


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = reverse_words('Alice likes Bob')
    print("reverse_words:", observed)
    assert observed == 'Bob likes Alice'
    observed = reverse_words('a')
    print("reverse_words:", observed)
    assert observed == 'a'
    observed = reverse_words('')
    print("reverse_words:", observed)
    assert observed == ''
    observed = reverse_words('one two')
    print("reverse_words:", observed)
    assert observed == 'two one'
