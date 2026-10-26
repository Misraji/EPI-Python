"""Pytest verification for EPI 13.3 (printed page 184)."""

# pytest can parametrically check representative cases.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_13_sorting.pg_184_eliminate_duplicate_names import Name, eliminate_duplicate


@pytest.mark.parametrize(('records','first_names'), [
    ([], []),
    ([('Amy', 'Z')], ['Amy']),
    ([('Ian','Botham'), ('David','Gower'), ('Ian','Bell')], ['David','Ian']),
    ([('C','C'),('B','B'),('A','A')], ['A','B','C']),
    ([('A','Z'),('A','A')], ['A']),
])
def test_eliminate(records, first_names):
    values = [Name(*record) for record in records]
    eliminate_duplicate(values)
    assert [item.first_name for item in values] == first_names
