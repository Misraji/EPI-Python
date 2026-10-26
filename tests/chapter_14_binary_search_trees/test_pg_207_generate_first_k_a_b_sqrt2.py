from itertools import product
from math import sqrt
from epi_python.chapter_14_binary_search_trees.pg_207_generate_first_k_a_b_sqrt2 import generate_first_k_a_b_sqrt2


def test_first_values():
    assert generate_first_k_a_b_sqrt2(4)==[0.0,1.0,sqrt(2),2.0]
    assert generate_first_k_a_b_sqrt2(0)==[]


def test_brute_force():
    for k in range(1,30):
        expected=sorted(a+b*sqrt(2) for a,b in product(range(k),repeat=2))[:k]
        got=generate_first_k_a_b_sqrt2(k)
        assert len(got)==k
        assert all(abs(a-b)<1e-9 for a,b in zip(got,expected))
