"""Unit tests for EPI exercise 6.8."""

# pytest parametrization documentation:
# https://docs.pytest.org/en/stable/how-to/parametrize.html
import pytest

from epi_python.chapter_06_strings.pg_075_look_and_say import look_and_say


@pytest.mark.parametrize(("arguments", "expected"), [((1,), '1'), ((2,), '11'), ((3,), '21'), ((4,), '1211'), ((5,), '111221')])
def test_cases(arguments, expected):
    assert look_and_say(*arguments) == expected

def test_pdf_pythonic_look_and_say_matches_original():
    from epi_python.chapter_06_strings.pg_075_look_and_say import look_and_say, look_and_say_pythonic
    expected=['1','11','21','1211','111221','312211','13112221','1113213211']
    for i, answer in enumerate(expected, 1):
        assert look_and_say(i) == look_and_say_pythonic(i) == answer
