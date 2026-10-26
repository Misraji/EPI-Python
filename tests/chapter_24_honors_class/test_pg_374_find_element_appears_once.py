# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_374_find_element_appears_once import find_element_appears_once


@pytest.mark.parametrize(('values','unique'),[([2,2,2,5],5),([7,7,7,-3],-3),([0,0,0,9],9),([-1,-1,-1,-2],-2)])
def test_unique(values,unique):
    assert find_element_appears_once(values)==unique
