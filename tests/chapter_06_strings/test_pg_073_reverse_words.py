"""Unit tests for EPI exercise 6.6."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_06_strings.pg_073_reverse_words import reverse_words


@pytest.mark.parametrize(("arguments", "expected"), [(('Alice likes Bob',), 'Bob likes Alice'), (('a',), 'a'), (('',), ''), (('one two',), 'two one')])
def test_cases(arguments, expected):
    assert reverse_words(*arguments) == expected

def test_bytearray_textbook_word_reversal():
    from epi_python.chapter_06_strings.pg_073_reverse_words import reverse_words, reverse_words_bytearray
    for sentence in ('Alice likes Bob', 'one two', '', 'a', 'some long example here', 'two  spaces'):
        original=bytearray(sentence.encode('ascii'))
        identity=id(original)
        assert reverse_words_bytearray(original) is None
        assert id(original)==identity
        assert original.decode('ascii')==reverse_words(sentence)
