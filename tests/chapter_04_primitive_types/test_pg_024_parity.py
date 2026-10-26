"""Parameterized tests for EPI exercise 4.1.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_04_primitive_types.pg_024_parity import parity


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0,), 0), ((1,), 1), ((3,), 0), ((7,), 1), ((10,), 0), ((15,), 0)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = parity(*arguments)
    assert observed == expected


def test_all_four_textbook_parity_methods():
    """Every complete version printed on pp.24–26 gets exercised."""
    from random import Random
    from epi_python.chapter_04_primitive_types.pg_024_parity import (
        parity_brute_force,
        parity_erase_lowest_set_bit,
        parity_lookup_table,
        parity_xor_folding,
    )

    generator = Random(4101)
    for word in (0, 1, 0b1011, 0b10001000, (1 << 64) - 1):
        expected = word.bit_count() & 1
        for algorithm in (
            parity_brute_force, parity_erase_lowest_set_bit,
            parity_lookup_table, parity_xor_folding,
        ):
            assert algorithm(word) == expected
    for _ in range(1500):
        word = generator.getrandbits(64)
        expected = word.bit_count() & 1
        for algorithm in (
            parity_brute_force, parity_erase_lowest_set_bit,
            parity_lookup_table, parity_xor_folding,
        ):
            assert algorithm(word) == expected
