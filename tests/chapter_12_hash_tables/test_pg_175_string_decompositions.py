"""Independent tests for EPI 12.10.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_12_hash_tables.pg_175_string_decompositions import find_all_substrings

@pytest.mark.parametrize(("args", "expected"), [
    (("barfoothefoobarman", ["foo", "bar"]), [0,9]),
    (("wordgoodgoodgoodbestword", ["word","good","best","good"]), [8]),
    (("abc", []), []),
    (("aaa", ["a","a"]), [0,1]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert find_all_substrings(*copy.deepcopy(args)) == expected

