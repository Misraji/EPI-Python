"""EPI Python — Exercise 24.2: Find the First Missing Positive Entry

Chapter 24: Honors Class
Textbook: pages 352–353 (printed page numbers; problem and solution start on
352, the program and its analysis are on 353).

PROBLEM (from the textbook)
---------------------------
Let A be an array of length n. Design an algorithm to find the smallest
positive integer which is not present in A. You do not need to preserve the
contents of A. For example, if A = <3, 5, 4, -1, 5, 1, -1>, the smallest
positive integer not present in A is 2.

HINT (from the textbook)
------------------------
First, find an upper bound for x.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: sort A, then walk through it looking for the first gap in the
entries after reaching an entry equal to 0. This costs as much as sorting,
O(n log n).

Since only the smallest missing positive number is wanted, sorting is more
than necessary. One alternative stores A's entries in a hash table S and
then tries 1, 2, 3, ... until one is not in S. Building S is O(n); the
lookups are also O(n), because with only n entries some value no larger
than n + 1 must be missing. Total time O(n), but space is O(n) (e.g. when
all entries are distinct positive integers).

The hint reduces the space. Instead of an external hash table, use A
itself as the record of which positive integers are present:
  * If A contains k with 1 <= k <= n, set A[k - 1] to k. The "- 1" is
    needed because all n slots are used, index 0 recording the presence
    of 1.
  * Before overwriting A[k - 1], its existing entry must be saved if it is
    itself between 1 and n (it is swapped into the current position).
  * Because A has n entries, the smallest missing positive number cannot
    exceed n + 1, so values outside 1..n can be ignored.

Worked example from the book: A = <3, 4, 0, 2>, n = 4.
  * Record 3 by writing it to A[3 - 1] = A[2]; the entry there (2) is saved
    by writing it to A[0]. Now A = <0, 4, 3, 2>.
  * 0 is outside the range of interest, so advance to A[1] = 4, which is in
    range. Write 4 to A[4 - 1] and move the value found there into index 1:
    A becomes <0, 2, 3, 4>.
  * A[1] already shows that 2 is present, so advance; the same holds for
    A[2] and A[3].
  * A second pass looks for the first index i with A[i] != i + 1; that is
    index 0, so the answer for the example is 1.

The book prints one program, `find_first_missing_positive(A)`; this file's
`first_missing_positive` follows the same placement idea (differences are
listed in TEXTBOOK CODE COMPARISON below).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []              -> 1   (nothing present)
    [1, 2, 3]       -> 4   (all of 1..n present, so n + 1)
    [3, 4, -1, 1]   -> 2
    [1, 1]          -> 2   (duplicates)
"""


def first_missing_positive(values: list[int]) -> int:
    """Smallest missing positive integer (textbook's in-array placement).

    Follows the textbook's `find_first_missing_positive` algorithm, but
    works on a copy of the input instead of overwriting it, and uses an
    explicit second loop instead of `next(...)`.

    Type hints: `values: list[int]` documents a list of integers and
    `-> int` the return type. Python does not enforce annotations at run
    time; they help readers and type checkers.
    """

    # list.copy() returns a new shallow copy of the list. The book allows
    # destroying A, but this file keeps the caller's list unchanged at the
    # cost of O(n) extra space (the book's version uses O(1)).
    # https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
    data=values.copy()
    n=len(data)

    # First pass: record which values in 1..n are present by moving value v
    # to index v - 1.
    for i in range(n):

        # `1<=data[i]<=n` is a chained comparison, meaning
        # `1 <= data[i] and data[i] <= n`.
        # The loop keeps swapping while the current entry is in range and
        # its home slot does not already hold the same value. The second
        # test prevents an infinite loop on duplicates such as [1, 1].
        # Each swap puts at least one value into its home slot for good, so
        # the total number of swaps over the whole pass is at most n.
        while 1<=data[i]<=n and data[data[i]-1] != data[i]:
            target=data[i]-1

            # Tuple swap: the right side is evaluated completely before the
            # assignment, so the two entries are exchanged without a
            # temporary. `target` was computed first so that the index does
            # not change mid-assignment (the book writes the swap with the
            # index expression inline, in an order that works).
            data[i],data[target]=data[target],data[i]

    # Second pass: the first index whose entry is not index + 1 means that
    # index + 1 is absent.
    #
    # enumerate(iterable) yields (index, element) pairs, here (0, data[0]),
    # (1, data[1]), ..., so both are available without manual counting.
    # https://docs.python.org/3/library/functions.html#enumerate
    for index,value in enumerate(data):
        if value != index+1:
            return index+1

    # Every value 1..n is present (or the list is empty), so n + 1 is the
    # smallest missing positive integer.
    return n+1


# TEXTBOOK POST-SOLUTION DISCUSSION (page 353)
# --------------------------------------------
# Time: O(n), because a constant amount of work is done per entry (each
# swap places a value permanently, so the inner loop does O(n) work in
# total).
# Space: O(1) in the book, because A itself is reused. (This file's version
# copies the input, so it uses O(n) additional space.)
#
# VARIANTS
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def find_first_missing_positive(A)` — modifies A in place; the
#   while-loop test is `1 <= A[i] <= len(A) and A[i] != A[A[i] - 1]`; the
#   swap is the one-liner `A[A[i] - 1], A[i] = A[i], A[A[i] - 1]`; the
#   second pass is `return next((i + 1 for i, a in enumerate(A) if a != i + 1),
#   len(A) + 1)`. The book's explanatory code comments describe both passes.
# file: renamed `first_missing_positive(values: list[int]) -> int`, type
#   hints added; works on `data = values.copy()` (input preserved, O(n) extra
#   space instead of O(1)); `n = len(data)` cached; the swap target index is
#   stored in a separate variable `target`; the comparison is written
#   `data[data[i]-1] != data[i]`; the generator/`next` second pass is
#   replaced by an explicit `for` loop with `return index+1` and a final
#   `return n+1`. Same results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior: an empty
    # list, a list holding all of 1..n, an unsorted list with a negative
    # value, and a list with duplicates.
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value. These are quick smoke checks;
    # pytest provides the more thorough automated verification.
    observed = first_missing_positive([])
    print("first_missing_positive:", observed)
    assert observed == 1
    observed = first_missing_positive([1, 2, 3])
    print("first_missing_positive:", observed)
    assert observed == 4
    observed = first_missing_positive([3, 4, -1, 1])
    print("first_missing_positive:", observed)
    assert observed == 2
    observed = first_missing_positive([1, 1])
    print("first_missing_positive:", observed)
    assert observed == 2
