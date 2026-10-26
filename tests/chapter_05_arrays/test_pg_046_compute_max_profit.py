"""Parameterized tests for EPI exercise 5.6.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_05_arrays.pg_046_compute_max_profit import compute_max_profit


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(([310, 315, 275, 295, 260, 270, 290, 230, 255, 250],), 30.0), (([5, 4, 3],), 0.0), (([],), 0.0), (([1, 5],), 4.0)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = compute_max_profit(*arguments)
    assert observed == expected
