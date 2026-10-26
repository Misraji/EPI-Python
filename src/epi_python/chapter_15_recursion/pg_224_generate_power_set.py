"""EPI Python — Exercise 15.4: Generate the Power Set

Chapter 15: Recursion
Textbook: pages 224–226 (printed page numbers; problem starts on 224, solution on 225).

PROBLEM (from the textbook)
---------------------------
"The power set of a set S is the set of all subsets of S, including both
the empty set and S itself."  Figure 15.5 illustrates it: the power set of
{0,1,2} is {{}, {0}, {1}, {2}, {0,1}, {1,2}, {0,2}, {0,1,2}}.

"Write a function that takes as input a set and returns its power set."

HINT (from the textbook)
------------------------
"There are 2^n subsets for a given set S of size n. There are 2^k k-bit
words."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute-force recursion: pick any one element. Compute the subsets U that do
not contain it and the subsets V that do. Every subset lies in exactly one
of U or V, so the answer is U union V. Both are computed recursively; the
base case is the empty input set, whose power set is {{}}.

Worked example, S = {0,1,2}:
* Pick 0; first recursively find all subsets of {1,2}.
  - Pick 1, leaving {2}. Pick 2, reaching the base case {{}}.
  - Subsets of {2}: {{}} union {{2}} = {{}, {2}}.
  - Subsets of {1,2}: {{}, {2}} union {{1}, {1,2}}
    = {{}, {2}, {1}, {1,2}}.
* Subsets of {0,1,2}: {{}, {2}, {1}, {1,2}} union
  {{0}, {0,2}, {0,1}, {0,1,2}}
  = {{}, {2}, {1}, {1,2}, {0}, {0,2}, {0,1}, {0,1,2}}.

The book's first program, generate_power_set(input_set), uses a nested
directed_power_set(to_be_selected, selected_so_far) which, for each index,
first recurses WITHOUT the element and then WITH it, appending a copy of
selected_so_far at the end -> `generate_power_set_recursive` below.

The book then gives a second, nonrecursive program based on bit arrays
(described in POST-SOLUTION DISCUSSION) -> `generate_power_set_by_bits`.

The file also contains `generate_power_set`, an iterative "doubling"
formulation that is NOT printed in the book (see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    generate_power_set([])      -> [[]]
    generate_power_set([1])     -> [[], [1]]
    generate_power_set([1, 2])  -> [[], [1], [2], [1, 2]]
"""

# Python standard library: mathematical functions (here, base-2 logarithm).
# Module documentation: https://docs.python.org/3/library/math.html
# math.log2 API: https://docs.python.org/3/library/math.html#math.log2
import math


def generate_power_set(values: list[int]) -> list[list[int]]:
    """Enumerate every subset by repeatedly doubling the family of subsets.

    NOT a textbook implementation: an added iterative formulation. Start
    from [[]]; for each value, add a copy of every existing subset extended
    by that value.
    """

    # Type hints (`values: list[int]`, `-> list[list[int]]`) document
    # intended types only; Python does not enforce them.
    subsets=[[]]
    for value in values:

        # The list comprehension is evaluated completely BEFORE `+=`
        # extends `subsets`, so it only sees the subsets that existed
        # before this value. `subset + [value]` builds a new list, leaving
        # the old subset unchanged. `+=` on a list extends it in place.
        subsets += [subset + [value] for subset in subsets]
    return subsets



def generate_power_set_recursive(values: list[int]) -> list[list[int]]:
    """Textbook's first (recursive include/exclude) implementation.

    Book name generate_power_set(input_set) with nested helper
    directed_power_set(to_be_selected, selected_so_far); here the helper is
    `visit(index, chosen)` and reuses one list with append/pop.
    """
    result: list[list[int]] = []

    # Nested helper: generates all subsets whose intersection with
    # values[0 .. index-1] is exactly `chosen`. It mutates the enclosing
    # `result` list (no `nonlocal` needed since the name is not rebound).
    def visit(index: int, chosen: list[int]) -> None:
        if index == len(values):

            # list.copy() snapshots the selected values before backtracking;
            # without the copy, every stored subset would be the same list
            # object, emptied again by the later pop() calls.
            # Documentation: https://docs.python.org/3/tutorial/datastructures.html
            result.append(chosen.copy())
            return

        # First generate all subsets that do NOT contain values[index].
        visit(index + 1, chosen)

        # Then generate all subsets that DO contain values[index]: add it,
        # recurse, and remove it again with pop() (which removes the last
        # item) so `chosen` is restored for the caller.
        chosen.append(values[index])
        visit(index + 1, chosen)
        chosen.pop()

    visit(0, [])
    return result


def generate_power_set_by_bits(values: list[int]) -> list[list[int]]:
    """Textbook's second (nonrecursive, integer bit-mask) implementation.

    Bit i of `mask` set means values[i] is in the subset.
    """
    result: list[list[int]] = []

    # `1 << n` shifts 1 left by n bits, i.e. computes 2**n. Python ints are
    # unbounded, so this never overflows (unlike fixed-width languages),
    # although the loop is only practical for small n. range(2**n) yields
    # every n-bit pattern 0 .. 2**n - 1 exactly once.
    for mask in range(1 << len(values)):
        subset: list[int] = []
        remaining = mask

        # A nonzero int is truthy, so the loop runs until all set bits of
        # `remaining` have been processed.
        while remaining:

            # x & ~(x - 1) isolates the lowest set bit, always a power of 2.
            # `~y` is bitwise NOT; for Python's unbounded ints it equals
            # -y - 1 (two's-complement view with infinitely many sign bits).
            # `&` is bitwise AND. Example: x = 0b0110 -> x - 1 = 0b0101,
            # ~(x - 1) = ...1010, x & ~(x - 1) = 0b0010.
            lowest_bit = remaining & ~(remaining - 1)

            # math.log2(power_of_two) identifies that bit's zero-based index
            # (log2(1) = 0.0, log2(2) = 1.0, log2(4) = 2.0, ...). It returns
            # a float, so int(...) converts it to an int usable as a list
            # index. For exact powers of two the result is exact.
            # This follows the textbook's printed bit-mask algorithm.
            # Documentation: https://docs.python.org/3/library/math.html#math.log2
            bit_index = int(math.log2(lowest_bit))
            subset.append(values[bit_index])

            # `x &= x - 1` clears the lowest set bit of x (augmented
            # assignment form of x = x & (x - 1)).
            remaining &= remaining - 1
        result.append(subset)
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 225–226)
# -------------------------------------------------
# Recursive program: the number of calls satisfies C(n) = 2C(n - 1), so
# C(n) = O(2^n). Each call spends O(n) time, so the time is O(n * 2^n). The
# space is also O(n * 2^n): there are 2^n subsets with average size n/2.
# If the subsets only need to be printed instead of returned, printing in
# place of storing reduces space to O(n); the time stays the same.
#
# Bit-array idea: fix an order of S's elements. The 2^n bit arrays of
# length n correspond one-to-one with the subsets of S: the 1s mark which
# elements are present. E.g. for S = {a,b,c,d}, the bit array <1,0,1,1>
# stands for {a,c,d}. This gives a nonrecursive algorithm.
#
# When n is at most the word width of the machine/language, enumerate the
# integers in [0, 2^n - 1] and, for each, extract the indices of its set
# bits: isolate the lowest set bit with y = x & ~(x - 1) (described on
# page 23) and take log y to get its index; then clear that bit.
#
# Each subset takes O(n) to compute, so the time is O(n * 2^n). This is
# very fast in practice, and if the subsets only need to be enumerated
# (e.g. printed) rather than returned, the space is O(n).
#
# VARIANTS (stated in the book; no solution given)
# ------------------------------------------------
# Solve this problem when the input array may have duplicates, i.e. denotes
# a multiset. No multiset may be repeated. For example, for A = <1,2,3,2>
# return <<>, <1>, <2>, <3>, <1,2>, <1,3>, <2,2>, <2,3>, <1,2,2>, <1,2,3>,
# <2,2,3>, <1,2,2,3>>.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * `generate_power_set` (doubling with a list comprehension) is NOT in the
#   book; it is a helper/extra formulation added in this file, and it uses
#   the book's first-program name for a different algorithm.
# * Book recursive program `generate_power_set(input_set)` with nested
#   `directed_power_set(to_be_selected, selected_so_far)` -> file
#   `generate_power_set_recursive(values)` with nested
#   `visit(index, chosen)`. Book passes a NEW list
#   `selected_so_far + [input_set[to_be_selected]]` to the second call and
#   stores `list(selected_so_far)`; file mutates one list with
#   `append`/`pop` and stores `chosen.copy()`. Exclude-then-include order is
#   the same. Book's two comments are reproduced in spirit above.
# * Book bit-mask program `generate_power_set(S)` -> file
#   `generate_power_set_by_bits(values)`; book variable names
#   `int_for_subset`, `bit_array` -> `mask`, `remaining`. Book appends
#   `int(math.log2(bit_array & ~(bit_array - 1)))`, i.e. the bit INDEX, to
#   the subset; file appends `values[bit_index]`, the element at that index
#   (the two agree only when values[i] == i, as in S = {0,1,2}).
# * Type hints added throughout the file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples for the (non-textbook) doubling version: the empty
    # set, one element and two elements; the exact output order is checked.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, pytest in tests/ is thorough.
    observed = generate_power_set([])
    print("generate_power_set:", observed)
    assert observed == [[]]
    observed = generate_power_set([1])
    print("generate_power_set:", observed)
    assert observed == [[], [1]]
    observed = generate_power_set([1, 2])
    print("generate_power_set:", observed)
    assert observed == [[], [1], [2], [1, 2]]

    # All textbook variants must yield the same family of subsets.
    # Lists cannot go into a set (they are unhashable), so each subset is
    # converted with tuple(...) and a set comprehension `{... for ...}`
    # collects them; comparing sets ignores the order of the subsets.
    expected = {(), (1,), (2,), (1, 2)}
    for method in (generate_power_set, generate_power_set_recursive, generate_power_set_by_bits):
        assert {tuple(subset) for subset in method([1, 2])} == expected
    print("Recursive and bit-mask power sets: passed")
