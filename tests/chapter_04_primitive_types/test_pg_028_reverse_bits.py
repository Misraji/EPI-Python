"""Parameterized tests for EPI exercise 4.3.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_04_primitive_types.pg_028_reverse_bits import reverse_bits


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [((0, 8), 0), ((1, 8), 128), ((3, 4), 12), ((5, 4), 10), ((255, 8), 255)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = reverse_bits(*arguments)
    assert observed == expected



def test_lookup_table_matches_brute_force():
    """Validate both textbook methods across random unsigned 64-bit words."""
    from random import Random
    from epi_python.chapter_04_primitive_types.pg_028_reverse_bits import reverse_bits_brute_force
    rng = Random(4103)
    for _ in range(1500):
        x = rng.getrandbits(64)
        assert reverse_bits(x) == reverse_bits_brute_force(x)
