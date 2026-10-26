"""EPI Python — Exercise 6.7: Compute All Mnemonics for a Phone Number

Chapter 6: Strings
Textbook: pages 74–75 (printed page numbers; problem, keypad figure,
solution and start of the program on 74; rest of the program, complexity
and variant on 75).

PROBLEM (from the textbook)
---------------------------
Each digit, apart from 0 and 1, in a phone keypad corresponds to one of
three or four letters of the alphabet, as shown in Figure 6.1. Since words
are easier to remember than numbers, it is natural to ask if a 7 or
10-digit phone number can be represented by a word. For example, "2276696"
corresponds to "ACRONYM" as well as "ABPOMZN".

    Figure 6.1 (phone keypad):  1      2 ABC   3 DEF
                                4 GHI  5 JKL   6 MNO
                                7 PQRS 8 TUV   9 WXYZ
                                *      0       #

Write a program which takes as input a phone number, specified as a string
of digits, and returns all possible character sequences that correspond to
the phone number. The cell phone keypad is specified by a mapping that
takes a digit and returns the corresponding set of characters. The
character sequences do not have to be legal words or phrases.

HINT (from the textbook)
------------------------
Use recursion.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force for a 7-digit number: form 7 ranges of characters, one per
digit. For "2276696" the ranges are 'A'-'C', 'A'-'C', 'P'-'S', 'M'-'O',
'M'-'O', 'W'-'Z', and 'M'-'O'. Then use 7 nested for-loops, one loop
variable per range, to enumerate every mnemonic. The drawbacks are
repetitive code and inflexibility (the number of loops is fixed by the
number of digits).

General rule: an enumeration like this is best done with recursion. The
execution path is essentially that of the nested loops, but the language
(the compiler, in the book's words) handles the looping. The recursive
helper fills in one position of a partial mnemonic with each possible
character for that digit and recurses on the next position; when every
digit has been processed, a copy of the partial mnemonic is added to the
result. In the book's mapping, 0 and 1 map to themselves.

The book prints one program, phone_mnemonic(phone_number), with a nested
helper and a module-level MAPPING tuple; this file's phone_mnemonic and
PHONE implement it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    phone_mnemonic("23") -> ['AD', 'AE', 'AF', 'BD', 'BE', 'BF',
                             'CD', 'CE', 'CF']   (3 x 3 = 9 strings)
"""


# The mapping from digit to corresponding characters (book comment).
# A tuple indexed by digit: PHONE[2] == "ABC". Digits 0 and 1 map to
# themselves, so they appear unchanged in every mnemonic. A tuple is used
# because the table never changes; an upper-case module-level name is the
# Python convention for a constant (not enforced by the language).
PHONE = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")


# `phone_number: str` and `-> list[str]` are type hints. `list[str]` means
# "a list of strings" (subscripted built-in, Python 3.9+). Python does not
# check or enforce annotations at run time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
# Generic alias types: https://docs.python.org/3/library/stdtypes.html#types-genericalias
def phone_mnemonic(phone_number: str) -> list[str]:
    """Generate every letter sequence represented by a keypad number.

    This is the textbook's recursive phone_mnemonic implementation, with
    an added check that the input contains only digits.
    """
    # any(iterable) returns True as soon as one item is true (and False
    # for an empty iterable). The argument is a generator expression,
    # which produces one boolean per character lazily, so any() can stop
    # at the first non-digit. `ch not in "0123456789"` tests whether the
    # one-character string ch is absent from the digit string.
    # any: https://docs.python.org/3/library/functions.html#any
    # Generator expressions: https://docs.python.org/3/reference/expressions.html#generator-expressions
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if any(ch not in "0123456789" for ch in phone_number):
        raise ValueError("Phone number must contain only digits")
    result = []

    # [''] * n builds a list of n empty strings (list repetition). This is
    # the partial mnemonic: one slot per digit, overwritten as the search
    # proceeds.
    # Docs: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
    candidate = [''] * len(phone_number)

    # Nested recursive helper (the book's phone_mnemonic_helper). It reads
    # and mutates `result` and `candidate` from the enclosing function (a
    # closure); mutating a list does not need `nonlocal`, only rebinding
    # a name would.
    def search(pos: int) -> None:
        if pos == len(phone_number):

            # All digits are processed, so add the partial mnemonic to the
            # result (book comment). ''.join(candidate) builds a NEW,
            # immutable string from the list; a copy is needed because
            # later calls keep modifying `candidate`.
            # str.join: https://docs.python.org/3/library/stdtypes.html#str.join
            result.append(''.join(candidate))
            return

        # Try all possible characters for this digit (book comment).
        # int('7') converts the digit character to the integer 7, used as
        # an index into PHONE; iterating over a str yields its characters.
        # int: https://docs.python.org/3/library/functions.html#int
        for letter in PHONE[int(phone_number[pos])]:
            candidate[pos] = letter
            search(pos + 1)

    search(0)
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 75)
# -------------------------------------------
# Each digit has at most 4 possible characters, so the number of recursive
# calls T(n) satisfies T(n) <= 4 T(n - 1), where n is the number of digits;
# this solves to T(n) = O(4^n).
# A call that recurses spends O(1) time inside the function, not counting
# the recursive calls. Each base case copies a string of length n and adds
# it to the result, taking O(n) time. Hence the time complexity is
# O(4^n n).
#
# VARIANTS
# --------
# Variant: Solve the same problem without using recursion.
#          (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: module-level `MAPPING = ('0', '1', 'ABC', ..., 'WXYZ')`;
#   `def phone_mnemonic(phone_number)` with nested
#   `def phone_mnemonic_helper(digit)`; the partial mnemonic is created as
#   `[0] * len(phone_number)` (in the statement
#   `mnemonics, partial_mnemonic = [], [0] * len(phone_number)`) after the
#   helper is defined; base case appends `''.join(partial_mnemonic)`;
#   loop `for c in MAPPING[int(phone_number[digit])]`; returns `mnemonics`.
# file: the table is named `PHONE` (same contents); signature
#   `phone_mnemonic(phone_number: str) -> list[str]` (type hints added);
#   adds a ValueError check that every character is a digit (the book
#   does no validation); the lists are named `result` and `candidate`,
#   created before the helper, with `candidate` filled with '' instead of
#   0; the helper is named `search(pos: int) -> None` and uses an early
#   `return` instead of `else:`; loop variable renamed `letter`. Same
#   algorithm and results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added example: "23" has 3 x 3 = 9 mnemonics. The comprehensive test
    # suite remains in the separate tests/ folder.
    print("phone 23:", phone_mnemonic("23"))

    # `assert` stops the program with an AssertionError if the condition
    # is false. This is a quick smoke check; pytest provides the more
    # thorough automated verification.
    assert len(phone_mnemonic("23")) == 9
