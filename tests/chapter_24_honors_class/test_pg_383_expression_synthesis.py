# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_383_expression_synthesis import expression_synthesis


@pytest.mark.parametrize(('digits','target','possible'), [([1,2,3],6,True),([1,2,3],7,True),([1,2,3],15,True),([1,2,3],123,True),([1,2,3],11,False),([0,0],0,True),([],0,False)])
def test_synthesis(digits,target,possible):
    assert expression_synthesis(digits,target) is possible
