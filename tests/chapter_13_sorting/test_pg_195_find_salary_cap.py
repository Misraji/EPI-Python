"""Pytest verification for EPI 13.11 (printed page 195)."""

# pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_13_sorting.pg_195_find_salary_cap import find_salary_cap


@pytest.mark.parametrize(('target','salaries','expected'), [
    (0,[10,20],0), (40,[10,20,30],15), (60,[10,20,30],30),
    (61,[10,20,30],-1), (0,[],0), (1,[],-1),
])
def test_salary(target,salaries,expected):
    assert find_salary_cap(target,salaries) == pytest.approx(expected)


def test_property_for_targets():
    salaries=[22,100,10,65,15]
    for target in range(0,int(sum(salaries))+1):
        cap=find_salary_cap(target,salaries)
        assert sum(min(x,cap) for x in salaries) == pytest.approx(target)
