"""Independent tests for EPI 12.4.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_12_hash_tables.pg_166_lca_close_ancestors import lca_close_value

@pytest.mark.parametrize(("args", "expected"), [
    (((4,(2,(1,None,None),(3,None,None)),(6,None,None)),1,3), 2),
    (((4,(2,None,None),(6,None,None)),2,6), 4),
    (((4,None,None),4,4), 4),
    (((4,None,None),4,99), None),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert lca_close_value(*copy.deepcopy(args)) == expected

