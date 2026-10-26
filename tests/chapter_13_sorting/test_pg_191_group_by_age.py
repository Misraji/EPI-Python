"""Pytest verification for EPI 13.8 (printed page 191)."""

# Standard-library Counter counts values in a sequence.
# Documentation: https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter

from epi_python.chapter_13_sorting.pg_191_group_by_age import Person, group_by_age


def test_group_by_age():
    values = [Person(10,'a'),Person(20,'b'),Person(10,'c'),Person(30,'d'),Person(20,'e')]
    before = Counter((p.age,p.name) for p in values)
    group_by_age(values)
    assert Counter((p.age,p.name) for p in values) == before
    ages = [p.age for p in values]
    for age in set(ages):
        indices = [i for i,x in enumerate(ages) if x==age]
        assert indices == list(range(min(indices),max(indices)+1))


def test_empty():
    values=[]
    group_by_age(values)
    assert values==[]
