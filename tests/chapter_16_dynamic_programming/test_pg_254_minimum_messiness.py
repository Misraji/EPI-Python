# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_254_minimum_messiness import minimum_messiness


@pytest.mark.parametrize(('words','length','expected'), [([],5,0),(['hi'],5,9),(['a','b','c','d'],5,8),(['hello','world'],5,0),(['a','b'],3,0)])
def test_messiness(words,length,expected):
    assert minimum_messiness(words,length)==expected


def test_word_too_long():
    with pytest.raises(ValueError):
        minimum_messiness(['excessive'],3)
