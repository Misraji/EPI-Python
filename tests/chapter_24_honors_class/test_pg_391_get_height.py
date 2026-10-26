# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_391_get_height import get_height


@pytest.mark.parametrize(('c','d','expected'),[(0,5,0),(1,5,5),(2,5,15),(2,3,6),(3,3,7),(3,4,14),(5,1,1)])
def test_height(c,d,expected):
    assert get_height(c,d)==expected
