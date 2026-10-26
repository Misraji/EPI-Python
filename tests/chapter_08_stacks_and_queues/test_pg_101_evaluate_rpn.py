"""Parameterized tests for EPI exercise 8.2.

pytest documentation: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest is installed as a development dependency, not part of Python itself.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

from epi_python.chapter_08_stacks_and_queues.pg_101_evaluate_rpn import evaluate_rpn


@pytest.mark.parametrize(
    ("arguments", "expected"),
    [(('3,4,+',), 7), (('3,4,+,2,*',), 14), (('6,3,/,2,-',), 0), (('-7,3,/',), -2)],
)
def test_examples(arguments, expected):
    """Run book-inspired normal cases and explicitly selected edge cases."""
    observed = evaluate_rpn(*arguments)
    assert observed == expected
