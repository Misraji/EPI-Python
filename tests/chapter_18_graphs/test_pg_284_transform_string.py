"""Unit tests for EPI exercise 18.7."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_18_graphs.pg_284_transform_string import transform_string


@pytest.mark.parametrize(("arguments", "expected"), [(('cat', 'dog', {'cat', 'cog', 'cot', 'dog'}), 3), (('cat', 'cat', set()), 0), (('cat', 'dog', {'dog'}), -1)])
def test_cases(arguments, expected):
    assert transform_string(*arguments) == expected
