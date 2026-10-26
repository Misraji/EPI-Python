"""Unit tests for EPI exercise 6.6."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_06_strings.pg_073_reverse_words import reverse_words


@pytest.mark.parametrize(("arguments", "expected"), [(('Alice likes Bob',), 'Bob likes Alice'), (('a',), 'a'), (('',), ''), (('one two',), 'two one')])
def test_cases(arguments, expected):
    assert reverse_words(*arguments) == expected
