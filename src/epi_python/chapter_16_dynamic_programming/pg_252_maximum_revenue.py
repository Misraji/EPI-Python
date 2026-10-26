"""EPI Python — Exercise 16.9: Pick Up Coins for Maximum Gain

Chapter 16: Dynamic Programming
Textbook: pages 252–253 (printed page numbers; problem and solution start on 252).

PROBLEM (from the textbook)
---------------------------
"In the pick-up-coins game, an even number of coins are placed in a line,
as in Figure 16.11. Two players take turns at choosing one coin each—they
can only choose from the two coins at the ends of the line. The game ends
when all the coins have been picked up. The player whose coins have the
higher total value wins. A player cannot pass his turn."

Figure 16.11 (a row of coins, in cents):
    25 5 10 5 10 5 10 25 1 25 1 25 1 25 5 10

"Design an efficient algorithm for computing the maximum total value for
the starting player in the pick-up-coins game."

HINT (from the textbook)
------------------------
"Relate the best play for the first player to the best play for the second
player."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Greedy (always take the larger end coin) is not optimal. With coins
5, 25, 10, 1: greedy first player takes 5, the second takes 25, the first
takes 10, the second gets 1 — totals 15 versus 26. Taking 1 first is
better: the second player must then expose the 25, and the first player
ends with 26. Greedy ignores the opportunities it creates for the
opponent; the first player must balance taking high coins against what is
left for the second player.

Assume the second player always plays as well as possible, i.e. maximizes
his own revenue (the sum of his coins). Let R(a, b) be the maximum revenue
a player can get when it is his turn and coins a..b (inclusive) remain, C
the array of coin values, and S(a, b) the sum of C[a..b]. Taking coin a
yields C[a] + S(a+1, b) - R(a+1, b); taking coin b yields
C[b] + S(a, b-1) - R(a, b-1). So

    R(a, b) = max(C[a] + S(a+1, b) - R(a+1, b), C[b] + S(a, b-1) - R(a, b-1)),

which DP solves easily.

A slightly different recurrence: since the total is fixed, maximizing the
second player's revenue is the same as minimizing the first player's. So

    R(a, b) = max( C[a] + min(R(a+2, b), R(a+1, b-1)),
                   C[b] + min(R(a+1, b-1), R(a, b-2)) )   if a <= b,
    R(a, b) = 0                                            otherwise.

The strategy minimizes the maximum revenue the opponent can gain; this
"min-max" form has the advantage of not needing S(a+1, b) and S(a, b-1).

Examples from the book: for coins <10, 25, 5, 1, 10, 5> the optimum for the
first player is 31; some subproblems are <10, 25> (25), <5, 1> (5) and
<5, 1, 10, 5> (15). For the coins of Figure 16.11 the first player can
guarantee at least 140 cents whatever the second player does; if both
players always take the more valuable end coin, the first player gets only
120 cents.

The book's program maximum_revenue(coins) solves for R with DP using a
nested memoized compute_maximum_revenue_for_range(a, b) and a 2D cache
maximum_revenue_for_range. This file implements the same program.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
None: the __main__ example <10, 25, 5, 1, 10, 5> -> 31 is the book's.
"""


def maximum_revenue(coins: list[int]) -> int:
    """Return the best total the first player can guarantee (textbook version).

    Memoized "min-max" recursion over coin ranges. An empty list returns 0
    (a guard not in the book).
    """

    # Type hints such as `list[int]` document intended types only.
    if not coins:
        return 0

    # Cache: maximum_revenue_for_range[a][b] = R(a, b), with 0 meaning "not
    # computed yet". The comprehension gives each row its own list (one row
    # per coin; `_` is an unused loop variable).
    maximum_revenue_for_range = [[0] * len(coins) for _ in coins]

    # Nested memoized helper computing R(a, b); it reads/assigns items of the
    # enclosing cache (no `nonlocal` needed, the name is not rebound).
    def compute_maximum_revenue_for_range(a: int,b: int) -> int:

        # No coins left.
        if a > b:
            return 0
        if maximum_revenue_for_range[a][b] == 0:

            # Take coin a: the opponent then leaves us the worse (min) of
            # the two ranges he can leave, (a+2, b) or (a+1, b-1).
            max_revenue_a = coins[a] + min(
                compute_maximum_revenue_for_range(a+2,b),
                compute_maximum_revenue_for_range(a+1,b-1))

            # Take coin b: likewise, ranges (a+1, b-1) or (a, b-2).
            max_revenue_b = coins[b] + min(
                compute_maximum_revenue_for_range(a+1,b-1),
                compute_maximum_revenue_for_range(a,b-2))
            maximum_revenue_for_range[a][b] = max(max_revenue_a,max_revenue_b)
        return maximum_revenue_for_range[a][b]

    return compute_maximum_revenue_for_range(0,len(coins)-1)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 253)
# --------------------------------------------
# R(a, b) has O(n^2) possible arguments (n coins), and each is computed in
# O(1) time from previously computed values, so R is computed in O(n^2)
# time.
#
# (Note on the cache, not from the book: 0 marks "not computed", so a range
# whose true value is 0 — e.g. all-zero coins — is simply recomputed; this
# affects speed only, not the answer.)
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * File adds the guard `if not coins: return 0` and type hints.
# * Book creates `maximum_revenue_for_range` after defining the helper;
#   file creates it before.
# * Otherwise the code matches the book's listing (the book's comment
#   "No coins left." is reproduced above).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # The book's own example: for <10, 25, 5, 1, 10, 5> the first player
    # can guarantee 31.
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, the pytest suite is thorough.
    print('Optimal first-player winnings:',maximum_revenue([10,25,5,1,10,5]))
    assert maximum_revenue([10,25,5,1,10,5]) == 31
