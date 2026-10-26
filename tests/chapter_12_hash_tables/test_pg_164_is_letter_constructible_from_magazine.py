"""Tests for EPI exercise 12.2 (textbook pages 164–165).

Run from the repository's top directory:
    python -m pytest tests/chapter_12_hash_tables -v

pytest discovers test modules whose names begin with `test_` and test
functions whose names begin with `test_`. No custom test runner is needed.
"""

import itertools

import pytest


from epi_python.chapter_12_hash_tables.pg_164_is_letter_constructible_from_magazine import (  # noqa: E402
    is_letter_constructible_from_magazine,
    is_letter_constructible_from_magazine_pythonic,
)


# Both textbook functions solve the same problem. Tests should check
# both versions against identical input/output expectations.
IMPLEMENTATIONS = (
    is_letter_constructible_from_magazine,
    is_letter_constructible_from_magazine_pythonic,
)


# Each tuple is one test case: (letter, magazine, expected answer).
# These are additional tests derived from the textbook's problem statement,
# not an assertion that the book itself lists these example inputs.
CASES = (
    ("aab", "baa", True),
    ("aab", "ab", False),
    ("aab", "baaabb", True),
    ("", "", True),
    ("", "abc", True),
    ("a", "", False),
    ("a", "a", True),
    ("abc", "cba", True),
    ("abc", "ab", False),
    ("AAA", "AA", False),
    ("A", "a", False),
    ("a b", "b a", True),
    ("a b", "ab", False),
    ("a!", "!a", True),
    ("a!", "aa", False),
    ("éé", "é", False),
    ("éé", "ééé", True),
)


# pytest.mark.parametrize runs the decorated test repeatedly with the
# arguments supplied here. `ids` gives readable labels in verbose output.
#
# Stacking two parametrize decorators makes pytest run EVERY combination:
# each of the two implementations is tested against every example.
@pytest.mark.parametrize(
    "implementation", IMPLEMENTATIONS, ids=("frequency-table", "counter-subtraction")
)
@pytest.mark.parametrize(
    ("letter", "magazine", "expected"),
    CASES,
    ids=[f"case-{number:02d}" for number in range(len(CASES))],
)
def test_hand_selected_cases(implementation, letter, magazine, expected):
    """Check normal inputs, duplicates, empty strings, and literal characters."""

    # pytest inspects ordinary Python `assert` statements and provides a
    # detailed comparison of observed and expected values when they fail.
    assert implementation(letter, magazine) is expected


def reference_constructible(letter_text, magazine_text):
    """Independent, simple reference method used only for small test inputs."""

    # str.count(substring) returns the number of nonoverlapping appearances
    # of substring inside a string. Here each substring is one character.
    # set(letter_text) keeps only distinct required characters, and all()
    # requires the frequency condition to hold for every one of them.
    # This deliberately simple reference may be slower than the EPI code.
    return all(
        letter_text.count(character) <= magazine_text.count(character)
        for character in set(letter_text)
    )


def all_short_strings(alphabet, max_length):
    """Produce every string over a small alphabet up to max_length."""
    result = [""]
    for length in range(1, max_length + 1):

        # itertools.product(alphabet, repeat=k) enumerates every ordered
        # k-character tuple from alphabet, allowing repeated characters.
        # For alphabet='ab', repeat=2 gives aa, ab, ba, and bb as tuples.
        # ''.join(...) converts each tuple of characters into a string.
        for characters in itertools.product(alphabet, repeat=length):
            result.append("".join(characters))
    return result


# The two possible characters keep this exhaustive test inexpensive while
# still covering repeated characters and different orderings. By using the
# independent reference above, the two textbook implementations cannot
# hide the same error merely by agreeing with each other.
@pytest.mark.parametrize(
    "implementation", IMPLEMENTATIONS, ids=("frequency-table", "counter-subtraction")
)
def test_all_short_strings_against_reference(implementation):
    """Exhaustively compare against the reference for strings of length 0–4."""
    strings = all_short_strings("ab", max_length=4)
    for letter in strings:
        for magazine in strings:
            assert implementation(letter, magazine) is reference_constructible(
                letter, magazine
            ), (letter, magazine)
