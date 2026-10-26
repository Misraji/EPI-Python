# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_24_honors_class.pg_368_calculate_bonus import calculate_bonus,calculate_bonus_heap


@pytest.mark.parametrize('scores',[[],[1],[1,2],[2,1],[1,2,2,1],[2,1,2],[3,2,1,2,3],[1,1,1],[5,3,4,7,2,2]])
def test_bonus_variants(scores):
    assert calculate_bonus(scores)==calculate_bonus_heap(scores)
