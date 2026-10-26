# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_354_find_biggest_n_minus_one_product import find_biggest_n_minus_one_product,find_biggest_n_minus_one_product_by_sign


@pytest.mark.parametrize('a',[[3,2,5,4],[3,2,-1,4],[3,2,-1,4,-1,6],[-2,-3,-4],[0,2,3],[0,-2,-3],[0,0,3],[-1,-1,0],[1,2]])
def test_variants(a):
    oracle=max(__import__('math').prod(a[:i]+a[i+1:]) for i in range(len(a)))
    assert find_biggest_n_minus_one_product(a)==oracle
    assert find_biggest_n_minus_one_product_by_sign(a)==oracle
