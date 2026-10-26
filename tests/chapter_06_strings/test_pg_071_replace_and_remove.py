"""Independent tests for EPI 6.4.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_06_strings.pg_071_replace_and_remove import replace_and_remove

@pytest.mark.parametrize(("args", "expected"), [
    ((4, ["a", "b", "a", "c", "", ""]), ["d","d","d","d","c"]),
    ((4, list("bbcc")), ["c","c"]),
    ((0, []), []),
    ((3, list("aba")), ["d","d","d","d"]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert replace_and_remove(*copy.deepcopy(args)) == expected

