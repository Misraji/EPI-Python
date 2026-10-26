# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_249_decompose_into_dictionary_words import decompose_into_dictionary_words


@pytest.mark.parametrize(('text','words','possible'), [
    ('bedbathandbeyond',{'bed','bath','and','beyond'},True),
    ('catdog',{'cat','dog'},True),
    ('catdot',{'cat','dog'},False),
    ('aaaa',{'a','aa'},True),
    ('',{'a'},True),
])
def test_decompose(text, words, possible):
    parts=decompose_into_dictionary_words(text,words)
    assert (bool(parts) or not text) is possible
    assert ''.join(parts)==text if possible else parts==[]
    assert set(parts)<=words
