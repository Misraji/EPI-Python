"""EPI Python — Exercise 15.10: Compute a Gray Code

Chapter 15: Recursion
Textbook: pages 232–233 (printed page numbers; problem and solution start on 232).

PROBLEM (from the textbook)
---------------------------
"An n-bit Gray code is a permutation of {0, 1, 2, ..., 2^n - 1} such that
the binary representations of successive integers in the sequence differ
in only one place. (This is with wraparound, i.e., the last and first
elements must also differ in only one place.) For example, both
<(000)2, (100)2, (101)2, (111)2, (110)2, (010)2, (011)2, (001)2>
= <0, 4, 5, 7, 6, 2, 3, 1> and <0, 1, 3, 2, 6, 7, 5, 4> are Gray codes for
n = 3."

"Write a program which takes n as input and returns an n-bit Gray code."

HINT (from the textbook)
------------------------
"Write out Gray codes for n = 2, 3, 4."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: enumerate all sequences of length 2^n whose entries are n-bit
integers, test each for the Gray code property, and stop at the first
success. There are 2^(n * 2^n) such sequences — astronomically many.
Enumerating only permutations of 0, 1, ..., 2^n - 1 (entries must be
distinct) helps, but the cost is still very high.

Directed enumeration (the book's first program): grow the sequence one
value at a time, adding a value only if it is not already in the sequence
and differs in exactly one bit from the previous value. For the last value,
also check that it differs in one bit from the first value.
Example, n = 4: start with (0000)2. Flipping bits of (0000)2 one at a time
gives (0001)2, not yet present, so append it. Flipping bits of (0001)2 gives
(0000)2 (already present) and then (0011)2, which is new, so the sequence
becomes <(0000)2, (0001)2, (0011)2>. The book then lists the next few
values, starting with (0010)2 and ending with (0111)2.
NOTE ON A PROBABLE BOOK MISPRINT: a high-resolution render of page 232
confirms the book prints the next values as (0010)2, (0011)2, (0111)2.
(0011)2 is already in the sequence, so the middle value is almost certainly
a misprint; following the algorithm, the value after (0010)2 would be
(0110)2. Recorded as printed.
-> `gray_code_backtracking` below.

A more analytical solution (the book's second program), found by studying
small cases: <(00)2, (01)2, (11)2, (10)2> is a 2-bit Gray code. To reach
n = 3, simply putting a 0 in front of each entry and then a 1 in front of
each entry, and concatenating, fails: the step from (010)2 to (100)2
changes two bits (everywhere else the property holds). Because a Gray code
also differs in one place when it wraps around, putting 1 in front of the
REVERSED 2-bit sequence fixes the transition from leading 0 to leading 1.
For n = 3 this gives <(000)2, (001)2, (011)2, (010)2, (110)2, (111)2,
(101)2, (100)2>. The general solution combines recursion with this
reversal ("reflection") -> `gray_code` below.

The book also prints a third, "Pythonic" version, gray_code_pythonic, which
builds the same reflected sequence iteratively with a list comprehension;
it is NOT in this file (see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    gray_code(3) -> [0, 1, 3, 2, 6, 7, 5, 4]   (the book's second n = 3
                                               example and the reflected
                                               sequence shown above)
    len(gray_code_backtracking(3)) == 8
"""


def gray_code_backtracking(num_bits: int) -> list[int]:
    """Textbook's first implementation: directed search with backtracking.

    Book: gray_code(num_bits) with nested directed_gray_code(history) and
    differs_by_one_bit(x, y). Returns [0] for num_bits < 1.
    """

    # Type hints (`num_bits: int`, `-> list[int]`) document intended types
    # only; Python does not enforce them at run time.
    if num_bits < 1:
        return [0]

    # True when x and y differ in exactly one bit position.
    def differs_by_one_bit(x: int, y: int) -> bool:

        # `^` is bitwise XOR: a result bit is 1 where x and y differ.
        bit_difference = x ^ y

        # A nonzero number with exactly one 1 bit is a power of two, and
        # `d & (d - 1)` clears the lowest set bit, so it is 0 exactly when d
        # has a single 1 bit. `d and not (...)` therefore means "d is
        # nonzero and has only one 1 bit". `and` returns one of its operands
        # (possibly the int 0), so `bool(...)` converts it to True/False.
        return bool(bit_difference and not (bit_difference & (bit_difference - 1)))

    result = [0]

    # A set gives O(1) average-time membership tests for "is this code
    # already in the sequence?"; `{0}` is a set literal with one element.
    history = {0}

    # Nested recursive search; returns True once `result` holds a complete
    # Gray code. It mutates the enclosing `result` and `history` (no
    # `nonlocal` needed because the names are never rebound).
    def directed_gray_code() -> bool:

        # `1 << num_bits` is 2**num_bits, the length of a complete code.
        # Then check the wraparound condition between first and last codes.
        # `result[-1]` is the last element (negative indices count from the
        # end).
        if len(result) == 1 << num_bits:
            return differs_by_one_bit(result[0], result[-1])

        # Try flipping each bit of the last code. `x ^ (1 << bit)` toggles
        # bit number `bit` of x (0 -> 1 or 1 -> 0).
        for bit in range(num_bits):
            candidate = result[-1] ^ (1 << bit)
            if candidate not in history:
                history.add(candidate)
                result.append(candidate)
                if directed_gray_code():
                    return True

                # Backtrack: remove the candidate from both structures.
                # set.remove(x) deletes x (KeyError if absent); list.pop()
                # removes the last item.
                history.remove(candidate)
                result.pop()
        return False

    # `assert` raises AssertionError if the search failed. (Note that
    # assert statements are skipped when Python runs with -O, but the call
    # inside is still needed for its side effect of filling `result`, so
    # under -O `result` would stay [0]. This is a property of the existing
    # code, recorded here only for understanding.)
    assert directed_gray_code()
    return result


def gray_code(num_bits: int) -> list[int]:
    """Textbook's second implementation: recursive reflection.

    Book name gray_code(num_bits); the result is the (num_bits - 1)-bit code
    followed by its reverse with the new leading bit set.
    """

    # Base case: the 0-bit Gray code is the single value 0.
    if num_bits == 0:
        return [0]

    # These implicitly begin with 0 at bit-index (num_bits - 1).
    prev = gray_code(num_bits - 1)

    # `1 << (num_bits - 1)` is an int whose only 1 bit is at index
    # num_bits - 1: the new leading bit.
    leading_bit_one = 1 << (num_bits - 1)

    # Add a 1 at bit-index (num_bits - 1) to every entry, processing them in
    # reverse order to achieve the reflection. `reversed(seq)` returns a
    # lazy reverse iterator (it does not copy the list). `|` is bitwise OR;
    # since `value` has no bit at that index, `leading_bit_one | value`
    # equals leading_bit_one + value. `prev + [...]` concatenates two lists
    # into a new list.
    return prev + [leading_bit_one | value for value in reversed(prev)]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 233)
# --------------------------------------------
# For the reflection solution, assuming the integers fit in a machine word,
# the time T(n) satisfies T(n) = T(n - 1) + O(2^(n-1)), so the time
# complexity is O(2^n).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# First program (backtracking):
# * Book name `gray_code(num_bits)`; file `gray_code_backtracking`.
#   Type hints added.
# * Book's nested `directed_gray_code(history)` takes the history set as a
#   parameter and is started with `directed_gray_code(set([0]))`; file
#   keeps `history = {0}` in the enclosing scope and the helper takes no
#   parameters.
# * Book's `differs_by_one_bit` is nested INSIDE directed_gray_code and
#   returns `bit_difference and not (...)` (may be an int); file defines it
#   at the outer level and wraps the result in `bool(...)`.
# * Book loop variable `i` with `previous_code = result[-1]` and
#   `candidate_next_code`; file `bit`, `candidate`. Book undoes with
#   `del result[-1]`; file with `result.pop()`.
# * File adds the early `if num_bits < 1: return [0]` and wraps the
#   initial call in `assert`; the book ignores the call's return value.
# Second program (reflection):
# * Book local `gray_code_num_bits_minus_1` and loop variable `i`; file
#   `prev` and `value`. Type hints added. Otherwise matches; the book's
#   comments are reproduced above.
# Third program:
# * Book `gray_code_pythonic(num_bits)` (`result = [0]; for i in
#   range(num_bits): result += [x + 2**i for x in reversed(result)]`) is
#   MISSING from this file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Print the reflected 3-bit code and check that both implementations
    # produce 2**3 = 8 codes. A chained comparison `a == b == c` means
    # `a == b and b == c`.
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, the pytest suite is thorough.
    print('3-bit Gray code:', gray_code(3))
    assert len(gray_code(3)) == len(gray_code_backtracking(3)) == 8
