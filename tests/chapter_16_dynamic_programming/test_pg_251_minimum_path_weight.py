# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_16_dynamic_programming.pg_251_minimum_path_weight import minimum_path_weight


@pytest.mark.parametrize(('triangle','expected'), [
    ([],0),([[5]],5),([[2],[3,4]],5),([[2],[3,4],[6,5,7],[4,1,8,3]],11),
    ([[-1],[-2,-3]],-4),
])
def test_path(triangle,expected):
    assert minimum_path_weight(triangle)==expected
