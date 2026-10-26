"""EPI Python — Exercise 24.29: Determine the Critical Height

Chapter 24: Honors Class
Textbook: pages 391–392 (printed page numbers; problem starts on 391,
solution on 392).

PROBLEM (from the textbook)
---------------------------
"You need to test the design of a protective case. Specifically, the case
can protect the enclosed device from a fall from up to some number of
floors, and you want to determine what that number of floors is." The book
lists its assumptions:

* All cases have identical physical properties: if one breaks when falling
  from a level, all of them do.
* A case that survives a fall can be reused; a broken case is discarded.
* If a case breaks when dropped, it would break from a higher floor; if it
  survives, it would survive a shorter fall.

It is not ruled out that cases break from first-floor windows, nor that they
survive drops from 36th-floor windows. There is a floor at or above which
the case breaks, and below which it stays intact; the ground floor is
numbered zero and the case does not break when dropped from it. Only a fixed
number of drops is allowed before the building supervisor stops you.

Examples from the book: with one case and 5 drops, the best is to test 5
floors, trying floors 1, 2, 3, 4, 5 in order; no floor can be skipped, since
if the case broke right after a skipped floor we could not tell whether the
critical floor was the tested one or the skipped one. If it never breaks, it
is known to survive a fifth-floor drop. With two cases and 5 drops one can
do better, e.g. drop from floors 2, 4, 6, 8, 9. If it breaks on one of the
first four drops, the critical floor is narrowed to that floor or the one
below, which the second case settles. If it breaks on the fifth drop the
critical floor is 9; if not, it survives a ninth-floor drop. So two cases
beat one.

"Given c cases and a maximum of d allowable drops, what is the maximum
number of floors that you can test in the worst-case?"

HINT (from the textbook)
------------------------
"Write a recurrence relation."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Let F(c, d) be the largest number of floors testable with c identical cases
and at most d drops. Clearly F(1, d) = d. Assume F(i, j) is known for all
i <= c and j <= d.

With c + 1 cases and d drops, make the first drop from floor
F(c, d - 1) + 1:
* if the case breaks, the remaining c cases and d - 1 drops pin down the
  floor exactly, since it lies in [1, F(c, d - 1)];
* if it survives, continue upward, covering F(c + 1, d - 1) more floors, up
  to floor F(c, d - 1) + 1 + F(c + 1, d - 1).

Hence the recurrence

    F(c + 1, d) = F(c, d - 1) + 1 + F(c + 1, d - 1),

which the book computes by dynamic programming (memoized recursion). The
single program is implemented below as get_height.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    get_height(2, 5) -> 15
"""


# Type hints: `cases: int`, `drops: int`, `-> int`. They document expected
# types; Python does not enforce annotations at run time.
def get_height(cases: int,drops: int) -> int:
    """Return F(cases, drops), the most floors testable in the worst case.

    This is the textbook's single implementation (memoized recursion on
    F(c, d) = F(c, d - 1) + F(c - 1, d - 1) + 1).
    """

    # Memo table with -1 meaning "not computed yet". The list comprehension
    # builds cases + 1 separate rows, each a new list of drops + 1 values.
    # (Writing [[-1] * (drops + 1)] * (cases + 1) would instead repeat one
    # shared row object.) `_` is the conventional name for an unused loop
    # variable.
    table=[[-1]*(drops+1) for _ in range(cases+1)]

    # Nested helper computing F(c, d); it reads `table` from the enclosing
    # function (mutating its items needs no `nonlocal`).
    def helper(c,d):

        # No cases or no drops: no floors can be tested.
        if c==0 or d==0:return 0

        # One case: must test floors one at a time, so F(1, d) = d.
        if c==1:return d

        # Compute and store F(c, d) the first time it is needed.
        if table[c][d]==-1:
            table[c][d]=helper(c,d-1)+helper(c-1,d-1)+1
        return table[c][d]
    return helper(cases,drops)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 392)
# --------------------------------------------
# Time and space complexity are both O((c + 1)(d + 1)): one table entry per
# (cases, drops) pair, each computed in O(1) time from two others.
#
# VARIANTS
# --------
# * Solve the same problem with O(c) space.
#   (stated in the book; no solution given)
# * How would you compute the minimum number of drops needed to find the
#   breaking point from 1 to F floors using c cases?
#   (stated in the book; no solution given)
# * Men numbered from 1 to n are arranged in a circle in clockwise order.
#   Every k-th man is removed until only one man remains. What is the number
#   of the last man? (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Signature: book `def get_height(cases, drops)`; file adds `int` type
#   hints and `-> int`.
# * Helper: book `get_height_helper(cases, drops)` with an
#   `if ... return 0 / elif cases == 1: return drops` chain; file
#   `helper(c, d)` with two separate one-line `if` statements. Same logic.
# * Table: book `F = [[-1] * (drops + 1) for i in range(cases + 1)]`
#   created after the helper definition; file `table=...` (loop variable
#   `_`) created before it.
# * Recurrence: book `get_height_helper(cases, drops - 1) +
#   get_height_helper(cases - 1, drops - 1) + 1`; file identical with the
#   renamed helper.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: two cases and five drops can test 15 floors.
    print('Two cases, five drops:',get_height(2,5))

    # `assert` stops with an AssertionError if the condition is false; a
    # quick smoke check. pytest provides the more thorough verification.
    assert get_height(2,5)==15
