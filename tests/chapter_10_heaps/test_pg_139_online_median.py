"""Parameterized checks of EPI 10.5 educational solution."""

# pytest API: https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_10_heaps.pg_139_online_median import online_median


@pytest.mark.parametrize(("arguments", "expected"), [(([],), []), (([1],), [1.0]), (([1, 2],), [1.0, 1.5]), (([1, 0, 3, 5, 2],), [1.0, 0.5, 1.0, 2.0, 2.0])])
def test_examples(arguments, expected):
    assert online_median(*arguments) == expected
