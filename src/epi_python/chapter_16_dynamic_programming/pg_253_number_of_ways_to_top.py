"""EPI Python — Exercise 16.10: Count the Number of Moves to Climb Stairs

Chapter 16: Dynamic Programming
Textbook: pages 253–254 (printed page numbers; problem starts on 253, solution on 254).

PROBLEM (from the textbook)
---------------------------
"You are climbing stairs. You can advance 1 to k steps at a time. Your
destination is exactly n steps up."

"Write a program which takes as inputs n and k and returns the number of
ways in which you can get to your destination. For example, if n = 4 and
k = 2, there are five ways in which to get to the destination:
  * four single stair advances,
  * two single stair advances followed by a double stair advance,
  * a single stair advance followed by a double stair advance followed by a
    single stair advance,
  * a double stair advance followed by two single stairs advances, and
  * two double stair advances."

HINT (from the textbook)
------------------------
"How many ways are there in which you can take the last step?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute-force enumeration makes no sense: there are exponentially many
possibilities.

The first advance can be 1, 2, ..., k steps, and each choice leads to
different ways of reaching the top, so the number of ways F(n, k)
satisfies

    F(n, k) = sum over i = 1 .. k of F(n - i, k).

Worked example: F(4, 2) = F(4-2, 2) + F(4-1, 2).
* F(4-2, 2) = F(4-2-2, 2) + F(4-2-1, 2). F(0, 2) and F(1, 2) are base
  cases with value 1, so F(4-2, 2) = 2.
* F(4-1, 2) = F(4-1-2, 2) + F(4-1-1, 2). The first term is a base case
  (1); the second was already computed (2). So F(4-1, 2) = 3.
* Therefore F(4, 2) = 3 + 2 = 5.

The book's program number_of_ways_to_top(top, maximum_step) caches the
values F(i, k), 0 <= i <= n, with a nested memoized recursion
compute_number_of_ways_to_h(h) and a list number_of_ways_to_h. This file
computes the same values BOTTOM-UP instead (see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    (top=0, max_step=2) -> 1   (already at the top: the empty sequence)
    (top=1, max_step=2) -> 1
    (top=2, max_step=2) -> 2   (1+1, 2)
    (top=3, max_step=2) -> 3   (1+1+1, 1+2, 2+1)
"""


def number_of_ways_to_top(top: int, max_step: int) -> int:
    """Count ordered ways to climb `top` stairs with advances of 1..max_step.

    Computes the textbook's recurrence F(n, k) = sum F(n - i, k) bottom-up
    (the book uses a memoized recursion instead).
    """

    # ways[h] = number of ways to reach height h. ways[0] = 1 counts the
    # empty sequence of advances. `[0]*(top+1)` builds top + 1 zeros.
    # Type hints such as `top: int` are not enforced by Python.
    ways=[0]*(top+1)
    ways[0]=1
    for height in range(1,top+1):

        # The last advance has `step` stairs, 1 <= step <= min(max_step,
        # height) (it cannot overshoot below height 0). `sum(generator)`
        # adds the values produced by the generator expression without
        # building an intermediate list.
        ways[height]=sum(ways[height-step] for step in range(1,min(max_step,height)+1))
    return ways[top]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 254)
# --------------------------------------------
# Each entry takes O(k) time to fill, so the total time is O(kn). The space
# is O(n).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Book: `def number_of_ways_to_top(top, maximum_step)` with nested
#   memoized `compute_number_of_ways_to_h(h)` (base case `if h <= 1:
#   return 1`; fills `number_of_ways_to_h[h]` with `sum(
#   compute_number_of_ways_to_h(h - i) for i in range(1,
#   min(maximum_step, h) + 1))` when it is 0); cache
#   `number_of_ways_to_h = [0] * (top + 1)`.
# * File: parameter `maximum_step` renamed `max_step`, type hints added,
#   and an iterative bottom-up loop over `height` with list `ways` and
#   `ways[0] = 1` (no recursion, no `h <= 1` base case). Results are the
#   same for top >= 0.
# * The book's memoized recursive implementation is MISSING from the file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added small examples with max_step = 2 (counts follow the Fibonacci
    # numbers 1, 1, 2, 3, 5, ...; the book's n = 4 example would give 5).
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite is thorough.
    observed = number_of_ways_to_top(0, 2)
    print("number_of_ways_to_top:", observed)
    assert observed == 1
    observed = number_of_ways_to_top(1, 2)
    print("number_of_ways_to_top:", observed)
    assert observed == 1
    observed = number_of_ways_to_top(2, 2)
    print("number_of_ways_to_top:", observed)
    assert observed == 2
    observed = number_of_ways_to_top(3, 2)
    print("number_of_ways_to_top:", observed)
    assert observed == 3
