"""Independent tests for EPI 6.7.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_06_strings.pg_074_phone_mnemonics import phone_mnemonic

@pytest.mark.parametrize(("args", "expected"), [
    (("2",), ["A", "B", "C"]),
    (("10",), ["10"]),
    (("",), [""]),
    (("23",), ["AD","AE","AF","BD","BE","BF","CD","CE","CF"]),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert phone_mnemonic(*copy.deepcopy(args)) == expected

