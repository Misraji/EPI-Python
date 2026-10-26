"""EPI Python — Exercise 13.4: Smallest Nonconstructible Value

Chapter 13: Sorting
Textbook: pages 185–186 (printed page numbers; problem and solution start on 185).

PROBLEM (from the textbook)
---------------------------
"Given a set of coins, there are some amounts of change that you may not be
able to make with them, e.g., you cannot create a change amount greater
than the sum of the your coins. For example, if your coins are
1,1,1,1,1,5,10,25, then the smallest value of change which cannot be made
is 21."

"Write a program which takes an array of positive integers and returns the
smallest number which is not to the sum of a subset of elements of the
array." [sic: the printed sentence reads "not to the sum"; it means "not
equal to the sum".]

HINT (from the textbook)
------------------------
"Manually solve for a few short arrays."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: try every value 1, 2, 3, ... and test whether it is the sum of
some subset of the array. There is no simple efficient algorithm for that
subset-sum test; heuristics exist, but the program becomes unwieldy.

Insight from small examples:
- <1,2> produces 1,2,3 and <1,3> produces 1,3,4.
- Trivially, the smallest element is a lower bound on what can be made:
  without a 1 the value 1 cannot be produced. However 2 might be produced
  without a 2 being present, since there may be two or more 1s.
- <1,2,4> produces 1..7, while <1,2,5> produces 1,2,3,5,6,7,8.

Generalization: suppose a collection can produce every value up to and
including V, but not V + 1. Add a new element u.
- If u <= V + 1, every value up to and including V + u can now be produced,
  and V + u + 1 cannot.
- If u > V + 1, then V + 1 still cannot be produced, even with u.

The order of the elements does not change which amounts are constructible,
but sorting lets us stop as soon as an element is too large to help, since
all later elements are at least as large. Precisely, let M[i - 1] be the
maximum constructible amount using the first i elements of the sorted
array. If the next element x exceeds M[i - 1] + 1, then M[i - 1] remains the
maximum, so stop and return M[i - 1] + 1. Otherwise set M[i] = M[i - 1] + x
and continue with element i + 1.

Worked example from the book: <12,2,1,15,2,4> sorts to <1,2,2,4,12,15>.
- First element 1: can make everything up to 1.
- 2 <= 1 + 1: everything up to 3.
- 2: everything up to 5.
- 4: everything up to 9.
- 12 > 9 + 1: 10 cannot be made. Stop; the answer is 10.

The function below is the book's single implementation (with a different
bookkeeping variable; see the code comparison).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []            -> 1   (nothing can be made)
    [1, 1, 3, 4]  -> 10  (1..9 can be made)
    [1, 2, 2]     -> 6
    [2, 3]        -> 1   (no 1 present)
"""


# Type hints: `coins: list[int]` and `-> int` document the expected types;
# Python does not enforce annotations at run time.
def smallest_nonconstructible_value(coins: list[int]) -> int:
    """Smallest positive amount not formable from a subset of positive coins.

    This is the textbook's implementation (sort, then extend the
    constructible range greedily).
    """

    # sorted(iterable) returns a NEW list containing the items in ascending
    # order; the caller's `coins` list is left unchanged (unlike list.sort,
    # which sorts in place). Ascending order is what lets the loop stop at
    # the first coin that is too large.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    ordered=sorted(coins)

    # Invariant: every amount 1 .. smallest_missing - 1 can be made from the
    # coins seen so far, and smallest_missing cannot. This equals the
    # book's M[i - 1] + 1.
    smallest_missing=1
    for coin in ordered:

        # coin > smallest_missing is the book's test x > M[i - 1] + 1: this
        # coin (and every later, larger coin) is too big to fill the gap.
        if coin > smallest_missing:
            break

        # Otherwise every amount up to (smallest_missing - 1) + coin is now
        # constructible, i.e. M[i] = M[i - 1] + x.
        smallest_missing += coin
    return smallest_missing


# TEXTBOOK POST-SOLUTION DISCUSSION (page 186)
# --------------------------------------------
# With n the length of the array: O(n log n) to sort plus O(n) to iterate,
# so O(n log n) time overall.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def smallest_nonconstructible_value(A):` keeps
# `max_constructible_value = 0`, iterates `for a in sorted(A):`, breaks when
# `a > max_constructible_value + 1`, adds `a`, and returns
# `max_constructible_value + 1`. File: parameter renamed `coins: list[int]`
# with `-> int`, the sorted copy is stored in a separate variable `ordered`,
# and the tracked quantity is `smallest_missing` (= the book's
# max_constructible_value + 1), initialised to 1, tested with
# `coin > smallest_missing`, and returned directly. Same results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Demonstrations (added for learning) check representative behaviour:
    # empty input, a run reaching 9, duplicates, and missing 1.
    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    observed = smallest_nonconstructible_value([])
    print("smallest_nonconstructible_value:", observed)
    assert observed == 1
    observed = smallest_nonconstructible_value([1, 1, 3, 4])
    print("smallest_nonconstructible_value:", observed)
    assert observed == 10
    observed = smallest_nonconstructible_value([1, 2, 2])
    print("smallest_nonconstructible_value:", observed)
    assert observed == 6
    observed = smallest_nonconstructible_value([2, 3])
    print("smallest_nonconstructible_value:", observed)
    assert observed == 1
