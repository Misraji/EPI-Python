"""EPI Python — Exercise 6.10: Compute All Valid IP Addresses

Chapter 6: Strings
Textbook: pages 77–78 (printed page numbers; problem, solution and start of
the program on 77; end of the program, complexity and variant on 78).

PROBLEM (from the textbook)
---------------------------
A decimal string is a string consisting of digits between 0 and 9.
Internet Protocol (IP) addresses can be written as four decimal strings
separated by periods, e.g., 192.168.1.201. A careless programmer mangles a
string representing an IP address in such a way that all the periods
vanish.

Write a program that determines where to add periods to a decimal string so
that the resulting string is a valid IP address. There may be more than one
valid IP address corresponding to a string, in which case you should print
all possibilities.

For example, if the mangled string is "19216811" then two corresponding IP
addresses are 192.168.1.1 and 19.216.81.1. (There are seven other possible
IP addresses for this string.)

HINT (from the textbook)
------------------------
Use nested loops.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
A valid IP address has three periods, so one can enumerate every placement
of the three periods and check that each of the four resulting substrings
is a number between 0 and 255.

Two refinements reduce the work:
* Space the periods 1 to 3 characters apart (each part has 1 to 3 digits),
  which limits the placements considered.
* Prune: stop extending a placement as soon as a part is invalid.

Worked example from the book, for "19216811": the first period could go
after "1", "19" or "192". If the first part is "1", the second part could
be "9", "92" or "921"; "921" is illegal (greater than 255), so that branch
is not continued.

The book's validity test for a part: "00", "000", "01", etc. are not
valid, but "0" is valid — a part is valid if it is a single digit, or it
does not start with '0' and its value is at most 255.

The book prints one program, get_valid_ip_address(s), with three nested
loops and pruning. This file's get_valid_ip_addresses implements the same
three-nested-loop enumeration of part lengths 1 to 3, but without the
pruning and with a different validity helper (see TEXTBOOK CODE
COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    get_valid_ip_addresses('0000') -> ['0.0.0.0']
    get_valid_ip_addresses('1111') -> ['1.1.1.1']
    get_valid_ip_addresses('123')  -> []   (too short for four parts)
    get_valid_ip_addresses('9999') -> ['9.9.9.9']
"""


# `digits: str` and `-> list[str]` are type hints. `list[str]` means "a list
# of strings" (subscripted built-in, Python 3.9+). Python does not check or
# enforce annotations at run time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
# Generic alias types: https://docs.python.org/3/library/stdtypes.html#types-genericalias
def get_valid_ip_addresses(digits: str) -> list[str]:
    """List valid IPv4 dotted-decimal addresses obtained by inserting dots.

    This is the textbook's nested-loop enumeration (get_valid_ip_address),
    restructured: all four parts are checked together after slicing,
    without the book's early pruning.
    """
    # Nested helper corresponding to the book's is_valid_part. A part is
    # valid when it is non-empty, has at most 3 characters, has no leading
    # zero (except the single part '0'), and its value is at most 255.
    # bool(chunk) is False for the empty string. `and` evaluates left to
    # right and stops at the first false operand, so int(chunk) is only
    # called on a non-empty chunk. int(text) parses a decimal string.
    # bool: https://docs.python.org/3/library/functions.html#bool
    # int: https://docs.python.org/3/library/functions.html#int
    # Boolean operations: https://docs.python.org/3/reference/expressions.html#boolean-operations
    def valid(chunk: str) -> bool:
        return bool(chunk) and len(chunk) <= 3 and (chunk == '0' or chunk[0] != '0') and int(chunk) <= 255
    result = []

    # a, b, c are the positions of the three periods. Each loop allows the
    # next part to be 1, 2 or 3 characters long (range(x + 1, x + 4)).
    # Positions past the end of the string are not excluded here; they
    # simply produce empty parts, which valid() rejects.
    for a in range(1,4):
        for b in range(a + 1, a + 4):
            for c in range(b + 1, b + 4):

                # Slicing never raises for out-of-range bounds: e.g.
                # 'abc'[5:7] == ''. digits[c:] takes everything from c to
                # the end as the fourth part.
                # Slicing: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
                parts = (digits[:a],digits[a:b],digits[b:c],digits[c:])

                # all(iterable) returns True if every item is true (and
                # True for an empty iterable); it stops at the first false
                # item. The argument is a generator expression producing
                # valid(part) lazily for each of the four parts.
                # all: https://docs.python.org/3/library/functions.html#all
                # Generator expressions: https://docs.python.org/3/reference/expressions.html#generator-expressions
                if all(valid(part) for part in parts):

                    # '.'.join(parts) concatenates the four strings with a
                    # period between neighbours: '1.1.1.1'.
                    # str.join: https://docs.python.org/3/library/stdtypes.html#str.join
                    result.append('.'.join(parts))
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 78)
# -------------------------------------------
# The total number of IP addresses is a constant (2^32), so the algorithm
# has O(1) time complexity.
#
# VARIANTS
# --------
# Variant: Solve the analogous problem when the number of periods is a
#          parameter k and the string length is unbounded.
#          (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def get_valid_ip_address(s)` (singular "address") with nested
#   `is_valid_part(s)` returning
#   `len(s) == 1 or (s[0] != '0' and int(s) <= 255)` (book comment:
#   "'00', '000', '01', etc. are not valid, but '0' is valid.");
#   `result, parts = [], [None] * 4`; loops
#   `for i in range(1, min(4, len(s)))`, then
#   `for j in range(1, min(len(s) - i, 4))`, then
#   `for k in range(1, min(len(s) - i - j, 4))`, where i, j, k are part
#   LENGTHS bounded by the remaining string; each part is stored in
#   `parts[...]` and checked immediately (parts 0 and 1 before descending,
#   parts 2 and 3 together in the innermost loop), so invalid prefixes are
#   pruned; appends `'.'.join(parts)`.
# file: renamed `get_valid_ip_addresses(digits: str) -> list[str]` (plural;
#   type hints added); helper renamed `valid(chunk: str) -> bool` with a
#   different but equivalent-for-these-inputs test (`bool(chunk) and
#   len(chunk) <= 3 and (chunk == '0' or chunk[0] != '0') and int(chunk)
#   <= 255`); the loop variables a, b, c are period POSITIONS rather than
#   part lengths, and the ranges are not bounded by len(digits) (out-of-
#   range positions yield empty parts that are rejected); the four parts
#   are built as a tuple and tested together with `all(...)`, so there is
#   no early pruning. The enumeration order, and therefore the order of
#   the results, is the same as the book's.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples: all zeros (leading-zero rule), all ones, a string
    # too short for four parts, and all nines. The comprehensive test
    # suite remains in the separate tests/ folder.
    observed = get_valid_ip_addresses('0000')

    # print() with several arguments writes them separated by a space.
    print("get_valid_ip_addresses:", observed)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert observed == ['0.0.0.0']
    observed = get_valid_ip_addresses('1111')
    print("get_valid_ip_addresses:", observed)
    assert observed == ['1.1.1.1']
    observed = get_valid_ip_addresses('123')
    print("get_valid_ip_addresses:", observed)
    assert observed == []
    observed = get_valid_ip_addresses('9999')
    print("get_valid_ip_addresses:", observed)
    assert observed == ['9.9.9.9']
