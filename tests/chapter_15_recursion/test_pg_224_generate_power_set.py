"""Unit tests for EPI exercise 15.4."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_15_recursion.pg_224_generate_power_set import generate_power_set


@pytest.mark.parametrize(("arguments", "expected"), [(([],), [[]]), (([1],), [[], [1]]), (([1, 2],), [[], [1], [2], [1, 2]])])
def test_cases(arguments, expected):
    assert generate_power_set(*arguments) == expected


def test_pdf_recursive_and_bit_mask_power_sets():
    import random

    from epi_python.chapter_15_recursion.pg_224_generate_power_set import (
        generate_power_set_recursive,
        generate_power_set_by_bits,
    )

    generator = random.Random(15224)
    for length in range(9):
        values = generator.sample(range(-50, 51), length)
        expected = {frozenset(x) for x in generate_power_set(values)}
        assert {frozenset(x) for x in generate_power_set_recursive(values)} == expected
        assert {frozenset(x) for x in generate_power_set_by_bits(values)} == expected
        assert len(expected) == 2 ** length
