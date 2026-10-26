# pytest parametrize documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_15_recursion.pg_228_palindrome_decompositions import palindrome_decompositions, palindrome_decompositions_pythonic


@pytest.mark.parametrize('text', ['', 'x', 'aab', 'abba', '010', 'aaaa'])
def test_implementations_agree(text):
    results = [sorted(fn(text)) for fn in (palindrome_decompositions, palindrome_decompositions_pythonic)]
    assert results[0] == results[1]
    for parts in results[0]:
        assert ''.join(parts) == text
        assert all(x == x[::-1] for x in parts)


def test_aab():
    assert sorted(palindrome_decompositions('aab')) == [['a','a','b'], ['aa','b']]
