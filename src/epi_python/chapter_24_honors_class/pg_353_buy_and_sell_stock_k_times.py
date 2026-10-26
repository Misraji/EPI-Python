"""EPI Python — Exercise 24.3: Buy and Sell a Stock k Times

Chapter 24: Honors Class
Textbook: pages 353–354 (printed page numbers; problem, solution and most of
the program are on 353; the program ends and the variant is on 354).

PROBLEM (from the textbook)
---------------------------
This problem generalizes the buy and sell problem introduced on Page 1.

Write a program to compute the maximum profit that can be made by buying
and selling a share k times over a given day range. Your program takes k
and an array of daily stock prices as input.

HINT (from the textbook)
------------------------
The book prints no hint for this exercise.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Straightforward algorithm: for j from 1 to k, scan the array A and record,
for each index i, the best result for the prefix A[0..i] using j buy-sell
pairs, storing these in an auxiliary array of length n. This takes O(k n^2)
time; by reusing arrays the extra space can be cut to O(n).

Better: O(kn) time and O(k) extra space. Define
  * B[j][i] — the most money you can have if you must make j - 1 buy-sell
    transactions before day i and then buy on day i;
  * S[j][i] — the maximum profit achievable with j buys and sells, where the
    j-th sell happens on day i.
They satisfy a mutual recurrence:
    S[j][i] = A[i] + max over i' < i of B[j][i']
    B[j][i] = (max over i' < i of S[j-1][i']) - A[i]

The key to O(kn) is that computing B and S needs only the running maxima
max_{i'<i} B[j][i'] and max_{i'<i} S[j-1][i']. Each can be maintained in
constant time per (i, j) with a conditional update, which is what the
program does. The book prints one program, `buy_and_sell_stock_k_times`.

How the program's two arrays map to the recurrence (explanatory note):
  * max_profits[j] — best profit so far ending in j + 1 completed sells
    (the running max of S for j + 1 transactions).
  * min_prices[j] — the smallest "effective price" paid for the (j + 1)-th
    buy: the price minus the profit already banked from j earlier
    transactions. Its negation is the running max of B.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    prices=[3, 2, 6, 5, 0, 3], k=2 -> 7   (buy 2 sell 6, buy 0 sell 3)
"""


def buy_and_sell_stock_k_times(prices: list[float], k: int) -> float:
    """Maximum profit from at most k buy-sell pairs (textbook O(kn) version).

    This is the textbook's single printed implementation, with small
    restructurings listed in TEXTBOOK CODE COMPARISON below.

    Type hints (`prices: list[float]`, `k: int`, `-> float`) document the
    expected types; Python does not enforce them at run time.
    """

    # `not k` is True when k == 0; `not prices` is True for an empty list
    # (empty containers are falsy). With no transactions allowed or no
    # prices, the profit is 0.0.
    if not k or not prices:
        return 0.0

    # With n prices there are at most n // 2 useful buy-sell pairs, so when
    # 2k >= n the limit on k never binds: the best strategy is to take
    # every day-to-day price increase.
    if 2*k>=len(prices):

        # Slicing: prices[:-1] is every price except the last; prices[1:] is
        # every price except the first.
        # zip(a, b) yields pairs (a[0], b[0]), (a[1], b[1]), ... and stops at
        # the shorter input, so here it yields (today, tomorrow) pairs.
        # https://docs.python.org/3/library/functions.html#zip
        #
        # `max(0.0, b-a)` keeps only gains (a drop contributes 0).
        # sum(...) over a generator expression adds the values one at a time
        # without building an intermediate list.
        # https://docs.python.org/3/library/functions.html#sum
        return sum(max(0.0,b-a) for a,b in zip(prices[:-1],prices[1:]))

    # float('inf') is positive infinity: every real price compares smaller,
    # so the first min() for each slot picks a real value.
    # https://docs.python.org/3/library/functions.html#float
    #
    # `[x] * k` builds a list of k copies of x. This is safe here because
    # numbers are immutable (repeating a mutable object like a list would
    # share one object k times).
    min_prices=[float('inf')]*k
    max_profits=[0.0]*k

    for price in prices:

        # reversed(iterable) yields items from last to first; here it walks
        # transaction counts k-1, ..., 0. Going backward means that when
        # slot i reads max_profits[i-1], that value has not yet been updated
        # for today, so a buy and the previous sell are not both credited to
        # the same day.
        # https://docs.python.org/3/library/functions.html#reversed
        for i in reversed(range(k)):

            # Running max of S: selling at today's price against the best
            # effective buy price for transaction i + 1.
            max_profits[i]=max(max_profits[i],price-min_prices[i])

            # Running max of B (stored negated as a minimum): the effective
            # cost of buying today is the price minus the profit already
            # banked from the first i transactions.
            # `X if cond else Y` is a conditional expression: it evaluates to
            # X when cond is true, otherwise Y. The first transaction has no
            # earlier profit to subtract.
            min_prices[i]=min(min_prices[i],price-(0 if i==0 else max_profits[i-1]))

    # Index -1 is the last element: the best profit using up to k
    # transactions.
    return max_profits[-1]


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 353–354)
# -------------------------------------------------
# The book's analysis is the one stated before the program: the improved
# algorithm runs in O(kn) time and uses O(k) additional space (two arrays of
# length k), versus O(kn^2) time for the straightforward approach.
#
# VARIANTS
# 1. Write a program that determines the maximum profit that can be obtained
#    when you can buy and sell a single share an unlimited number of times,
#    subject to the constraint that a buy must occur more than one day after
#    the previous sell. (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def buy_and_sell_stock_k_times(prices, k)`; first test `if not k:
#   return 0.0`; `elif 2 * k >= len(prices): return sum(max(0, b - a) for a, b
#   in zip(prices[:-1], prices[1:]))`; `min_prices, max_profits =
#   [float('inf')] * k, [0] * k`; inner loop `for i in reversed(list(range(k)))`;
#   same two update statements; `return max_profits[-1]`.
# file: same name and parameter names, type hints added; the first test is
#   extended to `if not k or not prices` (an empty price list returns 0.0
#   early); `elif` became a separate `if`; `max(0.0, ...)` instead of
#   `max(0, ...)`; the two lists are assigned on separate lines and
#   max_profits starts as `[0.0] * k`; `reversed(range(k))` without the
#   `list(...)` wrapper. Algorithm and results are the same.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # One example: with k = 2 the best trades are buy at 2 / sell at 6 and
    # buy at 0 / sell at 3, a total profit of 7.
    # `assert` raises AssertionError if the result differs; the separate
    # tests/ folder holds the thorough pytest suite.
    values=[3,2,6,5,0,3]
    profit=buy_and_sell_stock_k_times(values,2)
    print('Maximum profit for two trades:',profit)
    assert profit==7
