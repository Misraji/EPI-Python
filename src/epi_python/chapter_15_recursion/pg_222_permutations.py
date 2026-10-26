"""EPI Python — Exercise 15.3: Generate Permutations

Chapter 15: Recursion
Textbook: pages 222–224 (printed page numbers; problem starts on 222, solution on 223).

PROBLEM (from the textbook)
---------------------------
"This problem is concerned with computing all permutations of an array. For
example, if the array is <2,3,5,7> one output could be <2,3,5,7>,
<2,3,7,5>, <2,5,3,7>, <2,5,7,3>, <2,7,3,5>, <2,7,5,3>, <3,2,5,7>,
<3,2,7,5>, <3,5,2,7>, <3,5,7,2>, <3,7,2,5>, <3,7,5,2>, <5,2,3,7>,
<5,2,7,3>, <5,3,2,7>, <5,3,7,2>, <5,7,2,3>, <5,7,3,2>, <7,2,3,5>,
<7,2,5,3>, <7,3,2,5>, <7,3,5,2>, <7,5,2,3>, <7,5,3,2>. (Any other ordering
is acceptable too.)"

"Write a program which takes as input an array of distinct integers and
generates all permutations of that array. No permutation of the array may
appear more than once."

HINT (from the textbook)
------------------------
"How many possible values are there for the first element?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Let the input array be A, of length n.

Brute force: enumerate every length-n array whose entries come from A and
keep those that are permutations. The enumeration can itself be recursive
(take each length-(n-1) array over A and extend it by each of the n
possible last entries). There are n^n such arrays, so the time and space
costs are enormous.

Better: once a value is used for a position it must not be reused. Every
permutation of A starts with one of A[0], A[1], ..., A[n-1]. So generate
all permutations starting with A[0], then all starting with A[1], and so
on. Permutations starting with A[0] are A[0] followed by every permutation
of A[1 : n-1] — a smaller instance of the same problem, so recursion fits.
To get those starting with A[1], swap A[0] and A[1] and permute the new
A[1 : n-1]; then swap back to restore the original order before trying
A[2], and so on.

Worked example, A = <7,3,5>:
* Start with 7: permute <3,5>.
  - Starting with 3: the rest <5> has length 1, so a single permutation;
    <3,5> has one permutation beginning with 3.
  - Swap 3 and 5: one permutation beginning with 5, namely <5,3>.
  So the permutations beginning with 7 are <7,3,5> and <7,5,3>.
* Swap 7 with 3: permutations beginning with 3 are <3,7,5> and <3,5,7>.
* Finally <5,3,7> and <5,7,3>. Six permutations in all.

The book gives TWO complete programs, both implemented in this file:
1. Recursive swap-and-restore (book: permutations(A) with nested
   directed_permutations(i)) -> `permutations` below.
2. A qualitatively different, iterative algorithm based on Solution 5.11
   (next permutation, page 53), described after the first program's
   analysis (see POST-SOLUTION DISCUSSION) -> `permutations_by_next_permutation`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    permutations([1, 2, 3])                     -> 6 permutations
    permutations_by_next_permutation([2, 1, 3])
        -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
           (lexicographic order, equal to sorted(permutations([2, 1, 3])))
"""


def permutations(values: list[int]) -> list[list[int]]:
    """Enumerate all permutations by swapping each value into each position.

    This is the textbook's first (recursive) implementation, book name
    permutations(A) with nested helper directed_permutations(i), here with
    nested helper `visit`. Unlike the book, it works on a copy, so the
    caller's list is never touched.
    """

    # Type hints (`values: list[int]`, `-> list[list[int]]`,
    # `result: list[list[int]]`) document intended types; Python does not
    # enforce them at run time.
    result: list[list[int]] = []

    # list.copy() makes a shallow copy (a new list holding the same
    # elements). The recursion swaps entries of `remaining` in place, and
    # copying first keeps the caller's `values` list unchanged.
    remaining = values.copy()

    # Nested helper: it reads/mutates the enclosing `result` and
    # `remaining` lists. Mutation does not rebind the names, so no
    # `nonlocal` declaration is needed.
    def visit(position: int) -> None:

        # Every position has been fixed: record a snapshot. `.copy()` is
        # essential because `remaining` keeps changing as we backtrack.
        if position == len(remaining):
            result.append(remaining.copy())
            return

        # Try every possibility for remaining[position]: each value still in
        # the unfixed part remaining[position:] gets a turn at this slot.
        for index in range(position, len(remaining)):

            # `a, b = b, a` is Python's tuple-unpacking swap: the right-hand
            # side is evaluated first into a tuple, then unpacked into the
            # targets, so no temporary variable is needed.
            remaining[position], remaining[index] = remaining[index], remaining[position]

            # Generate all permutations of the entries after `position`.
            visit(position + 1)

            # Swap back to restore the order before trying the next value
            # at this position (the "restore" step of backtracking).
            remaining[position], remaining[index] = remaining[index], remaining[position]

    visit(0)
    return result



def permutations_by_next_permutation(values: list[int]) -> list[list[int]]:
    """Enumerate permutations as successive lexicographic successors.

    This is the textbook's second implementation (the one built on the
    next-permutation algorithm of Solution 5.11). The book calls a separate
    next_permutation(A) function; this file inlines that step. The values
    are sorted first (as the book's text describes); the caller's list is
    not changed. Assumes distinct input elements, as specified in EPI 15.3.
    """

    # sorted(iterable) returns a NEW list in ascending order and leaves the
    # argument untouched. Starting from the smallest arrangement guarantees
    # that the successor chain visits every permutation exactly once.
    current = sorted(values)
    result = [current.copy()]

    while True:

        # Find the rightmost ascending adjacent pair. All elements to its
        # right form a nonincreasing suffix. If there is none (pivot < 0),
        # `current` is the largest (fully descending) arrangement and the
        # enumeration is finished.
        pivot = len(current) - 2
        while pivot >= 0 and current[pivot] >= current[pivot + 1]:
            pivot -= 1
        if pivot < 0:
            break

        # Swap the pivot with the smallest suffix element that is greater
        # than it. Because the suffix is nonincreasing, scanning from the
        # right end finds that element first. The parenthesized right-hand
        # side is the same tuple-unpacking swap, split across lines.
        successor = len(current) - 1
        while current[successor] <= current[pivot]:
            successor -= 1
        current[pivot], current[successor] = (
            current[successor], current[pivot]
        )

        # Slice assignment: `lst[i:] = iterable` replaces everything from
        # index i to the end with the items of the iterable (the list keeps
        # its identity). `reversed(seq)` returns a lazy reverse iterator;
        # the right-hand slice is a copy made before assignment, so reading
        # and writing the same region is safe. Reversing the (still
        # nonincreasing) suffix makes it ascending, giving the smallest
        # arrangement that is larger than before.
        current[pivot + 1 :] = reversed(current[pivot + 1 :])
        result.append(current.copy())

    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 223–224)
# -------------------------------------------------
# Recursive program: each call does O(1) work apart from its subcalls (and
# the copying of a finished permutation), so the cost is governed by the
# number of calls C(n). It satisfies C(n) = 1 + n*C(n - 1) for n >= 1, with
# C(0) = 1. Expanding gives
#     C(n) = 1 + n + n(n-1) + n(n-1)(n-2) + ... + n!
#          = n!(1/n! + 1/(n-1)! + 1/(n-2)! + ... + 1/1!).
# The sum 1 + 1/1! + 1/2! + ... + 1/n! tends to Euler's number e, so C(n)
# tends to (e - 1)n!, i.e. O(n!). Each call also does O(n) work outside the
# recursive calls, so the total time is O(n * n!).
#
# A different algorithm: Solution 5.11 (page 53) computes the permutation
# that follows a given one in lexicographic order, e.g. <2,3,1,4> is
# followed by <2,3,4,1>. That solves this problem too: the n distinct
# entries can be thought of as 1, 2, ..., n, with 1 the smallest. For
# example, <7,3,5> is first sorted to <3,5,7>; repeated next-permutation
# steps then give <3,7,5>, <5,3,7>, <5,7,3>, <7,3,5>, <7,5,3>. The book's
# second program records a copy of A, replaces A with next_permutation(A),
# and stops when that returns an empty result. Its time complexity is
# O(n * n!): there are n! permutations and storing each takes O(n) time.
#
# VARIANTS (stated in the book; no solution given)
# ------------------------------------------------
# Solve Problem 15.3 when the input array may have duplicates, without
# repeating any permutation. For example, for A = <2,2,3,0> the output
# should be <2,2,0,3>, <2,2,3,0>, <2,0,2,3>, <2,0,3,2>, <2,3,2,0>,
# <2,3,0,2>, <0,2,2,3>, <0,2,3,2>, <0,3,2,2>, <3,2,2,0>, <3,2,0,2>,
# <3,0,2,2>.


# TEXTBOOK CODE COMPARISON
# ------------------------
# First program:
# * Book `def permutations(A)` with nested `directed_permutations(i)`;
#   file `def permutations(values: list[int]) -> list[list[int]]` with
#   nested `visit(position: int)`; loop variable `j` -> `index`. Type hints
#   added.
# * Book permutes `A` itself in place (restoring it by swapping back);
#   file first copies it into `remaining`, so the input is never mutated.
# * Base case: book `if i == len(A) - 1:` (stops when one entry is left);
#   file `if position == len(remaining):` (one extra level of recursion).
#   Results agree for non-empty input; for an empty list the book returns
#   [] while the file returns [[]].
# Second program:
# * Book reuses `next_permutation(A)` from Solution 5.11 in a
#   `while True` loop (`result.append(A.copy()); A = next_permutation(A);
#   if not A: break`) and the listing does not sort A (the text says to
#   sort first). File: separate function name
#   `permutations_by_next_permutation`, sorts with `sorted(values)` first,
#   and inlines the next-permutation steps (find pivot, swap with
#   successor, reverse suffix) instead of calling a helper.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added example: [1, 2, 3] has 3! = 6 permutations.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite in tests/ is
    # the thorough verification.
    result = permutations([1, 2, 3])
    print("All permutations:", result)
    assert len(result) == 6

    # Compare the book's swap-and-backtrack and next-permutation methods.
    # The next-permutation version produces lexicographic (sorted) order,
    # so the swap version's output is sorted with `sorted(...)` before the
    # comparison.
    assert sorted(permutations([2, 1, 3])) == permutations_by_next_permutation([2, 1, 3])
    print("Lexicographic permutation enumeration: passed")
