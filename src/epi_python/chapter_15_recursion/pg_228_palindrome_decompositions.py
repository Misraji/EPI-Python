"""EPI Python — Exercise 15.7: Generate Palindromic Decompositions

Chapter 15: Recursion
Textbook: pages 228–229 (printed page numbers; problem and solution start on 228).

PROBLEM (from the textbook)
---------------------------
"A string is said to be palindromic if it reads the same backwards and
forwards. A decomposition of a string is a set of strings whose
concatenation is the string. For example, "611116" is palindromic, and
"611", "11", "6" is one decomposition for it."

"Compute all palindromic decompositions of a given string. For example, if
the string is "0204451881", then the decomposition "020", "44", "5", "1881"
is palindromic, as is "020", "44", "5", "1", "88", "1". However, "02044",
"5", "1881" is not a palindromic decomposition."

HINT (from the textbook)
------------------------
"Focus on the first palindromic string in a palindromic decomposition."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: generate every decomposition and keep the ones made only of
palindromes. All decompositions are produced by choosing a prefix of
length 1, 2, ... as the first piece and recursively decomposing the rest.
There are 2^(n-1) decompositions of a length-n string (each one matches an
n-bit vector whose 1s mark where pieces start). This is wasteful because it
keeps extending decompositions that can never be palindromic, e.g. those
starting with "02" for "0204451881".

Directed approach: only enumerate decompositions whose FIRST piece is a
palindrome, then recurse on the remaining suffix.

Worked example, "0204451881":
* Its palindromic prefixes are "0" and "020", so recurse on "204451881"
  and on "4451881".
* For "204451881" the only palindromic prefix is "2"; recurse on
  "04451881".
* For "04451881" the only palindromic prefix is "0"; recurse on the
  remaining suffix (printed in the book as "4451991").
* For that suffix, "4" and "44" are palindromic prefixes, so recurse on
  the strings after each (printed as "451991" and "51991").
(The book's text at this point prints "4451991", "451991" and "51991",
which do not match the suffixes of "0204451881"; this looks like a
misprint for "4451881", "451881" and "51881".)

The book gives TWO programs, both implemented in this file:
1. palindrome_decompositions(input) with nested
   directed_palindrome_decompositions(offset, partial_partition)
   -> `palindrome_decompositions`.
2. A "Pythonic" solution that uses bottom-up construction in a single
   list comprehension -> `palindrome_decompositions_pythonic`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    'aab' -> [['a', 'a', 'b'], ['aa', 'b']]   (from both implementations)
"""


def palindrome_decompositions(text: str) -> list[list[str]]:
    """Textbook's first (directed recursive) implementation.

    Book: palindrome_decompositions(input) with nested
    directed_palindrome_decompositions(offset, partial_partition).
    """

    # Type hints (`text: str`, `-> list[list[str]]`) document intended
    # types only; Python does not enforce them.
    result: list[list[str]] = []

    # Nested helper: decompose text[offset:], given that text[:offset] has
    # already been split into the palindromes in `partial_partition`.
    def directed_palindrome_decompositions(offset: int, partial_partition: list[str]) -> None:

        # The whole string has been consumed: record a copy of the pieces.
        # list(...) copies the list (the book does the same).
        if offset == len(text):
            result.append(list(partial_partition))
            return

        # Try every possible end index i of the next piece, text[offset:i].
        for i in range(offset + 1, len(text) + 1):

            # Slicing `s[a:b]` returns the substring from index a up to but
            # not including b. `s[::-1]` is a slice with step -1, which
            # returns the string reversed; equality with the original means
            # the piece is a palindrome.
            prefix = text[offset:i]
            if prefix == prefix[::-1]:

                # `partial_partition + [prefix]` builds a NEW list, so the
                # caller's list is unchanged and no undo step is needed.
                directed_palindrome_decompositions(i, partial_partition + [prefix])

    directed_palindrome_decompositions(0, [])
    return result


def palindrome_decompositions_pythonic(text: str) -> list[list[str]]:
    """Textbook's second, "Pythonic" implementation (bottom-up construction).

    For every palindromic prefix text[:i], prepend it to each palindromic
    decomposition of the rest text[i:].
    """

    # This is a single list comprehension with TWO `for` clauses and an
    # `if` filter, read left to right like nested loops:
    #     for i in range(1, len(text) + 1):
    #         if text[:i] is a palindrome:
    #             for right in <decompositions of text[i:]>:
    #                 produce [text[:i]] + right
    #
    # `A or B` returns A if A is truthy, otherwise B. An empty list is
    # falsy, so when `text` is empty (the comprehension produces nothing)
    # the function returns [[]]: exactly one decomposition, with no pieces.
    # That is the base case that lets the recursive call on the final
    # suffix contribute one (empty) `right` list. (A nonempty string always
    # has at least one decomposition — all single characters — so the
    # `or` only fires for the empty string.)
    return ([[text[:i]] + right
             for i in range(1, len(text) + 1)
             if text[:i] == text[:i][::-1]
             for right in palindrome_decompositions_pythonic(text[i:])]
            or [[]])


# TEXTBOOK POST-SOLUTION DISCUSSION (page 229)
# --------------------------------------------
# Worst-case time is still O(n * 2^n), for instance when the input is n
# copies of one character (every decomposition is palindromic). But the
# directed program has a far better best case than brute force, e.g. when
# the string has very few palindromic decompositions.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * First program: book parameter `input`; file parameter `text: str`
#   (book's name shadows the built-in input()). Type hints added to the
#   outer function, helper and `result`. Book initializes `result = []`
#   after defining the helper; file initializes it before. Otherwise the
#   code matches the book's listing.
# * Second program: matches the book's listing except the type hints
#   (`text: str`, `-> list[list[str]]`). The book's comment "Pythonic
#   solution uses bottom-up construction." is reflected in the docstring.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Run both textbook implementations on the same added example.
    # Functions are objects, so they can be placed in a tuple and looped
    # over; `function.__name__` is the function's name as a string.
    # sorted(...) makes the comparison independent of output order.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite is thorough.
    for function in (palindrome_decompositions, palindrome_decompositions_pythonic):
        result = function('aab')
        print(function.__name__, result)
        assert sorted(result) == [['a', 'a', 'b'], ['aa', 'b']]
