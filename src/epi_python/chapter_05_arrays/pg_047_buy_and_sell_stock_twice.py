"""EPI Python — Exercise 5.7: Buy and Sell a Stock Twice

Chapter 5: Arrays
Textbook: pages 47–48 (printed page numbers; problem and solution start on
page 47 and finish on page 48).

PROBLEM (from the textbook)
---------------------------
Context: "The max difference problem, introduced on Page 1, formalizes
the maximum profit that can be made by buying and then selling a single
share over a given day range."

"Write a program that computes the maximum profit that can be made by
buying and selling a share at most twice. The second buy must be made on
another date after the first sale."

HINT (from the textbook)
------------------------
"What do you need to know about the first i elements when processing the
(i + 1)th element?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
- Brute force: try every combination of buy-sell-buy-sell days, O(n^4).
- Improvement to O(n^2): split A into two subarrays at every possible
  point and run the O(n) single-transaction algorithm (Exercise 5.6) on
  each side.
- Both waste work because they do not reuse earlier computations. Instead:
  1. Forward pass: record F[j], the best single buy-and-sell profit within
     A[0, j], for each day j.
  2. Backward pass: compute B[j], the best single buy-and-sell profit
     within A[j, n - 1], i.e. buying and selling on or after day j.
  3. Combine: for each day i, M[i] = F[i - 1] + B[i] is the best profit
     when one transaction finishes before day i and the other happens on
     or after day i. F[-1] is taken as 0, because the second buy must come
     strictly after the first sale.

Book example: A = <12,11,13,9,12,8,14,13,15>.
  F = <0,0,2,2,3,3,6,6,7>   (best single trade by day i, inclusive)
  B = <7,7,7,7,7,7,2,2,0>   (best single trade on or after day i)
  M = <7,7,7,9,9,10,5,8,6>
so the maximum profit is 10.

The book prints one program, `buy_and_sell_stock_twice`, implemented here
with the same name.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []           -> 0.0
    [1, 5]       -> 4.0    (only one transaction is possible)
    [1, 5, 2, 10] -> 12.0  (1 -> 5 then 2 -> 10)
    [5, 4, 3, 2] -> 0.0    (never profitable)
"""



# `prices: list[float]` and `-> float` are type hints: they document the
# intended types, but Python does not enforce them at run time (int
# prices work too). `list[float]` requires Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def buy_and_sell_stock_twice(prices: list[float]) -> float:
    """Best total gain from at most two non-overlapping transactions.

    This is the textbook's `buy_and_sell_stock_twice(prices)` program
    (forward phase, then backward phase), restructured slightly; see
    TEXTBOOK CODE COMPARISON.
    """

    # Empty list is falsy: no trades are possible.
    if not prices:
        return 0.0

    # `float('inf')` is positive infinity; any real price is smaller, so
    # the first min() call replaces it.
    # Documentation: https://docs.python.org/3/library/functions.html#float
    lowest = float('inf')
    first_best = 0.0
    left_profits = []

    # Forward phase (book comment: "For each day, we record maximum profit
    # if we sell on that day"). left_profits[i] ends up as F[i]: the best
    # single-transaction profit within prices[0..i].
    for p in prices:
        lowest = min(lowest, p)
        first_best = max(first_best, p - lowest)

        # list.append adds one item at the end of the list.
        # Documentation: https://docs.python.org/3/tutorial/datastructures.html
        left_profits.append(first_best)

    # `float('-inf')` is negative infinity, smaller than any real price, so
    # the first max() call replaces it.
    highest = float('-inf')
    second_best = 0.0
    best_total = 0.0

    # Backward phase (book comment: "For each day, find the maximum profit
    # if we make the second buy on that day").
    # `range(len(prices) - 1, -1, -1)` counts down n-1, n-2, ..., 0
    # (arguments: start, stop exclusive, step).
    for i in range(len(prices) - 1, -1, -1):

        # `highest` is the largest price on or after day i; buying on day i
        # and selling at `highest` gives one candidate second trade.
        highest = max(highest, prices[i])

        # second_best is B[i]: best single trade on or after day i.
        second_best = max(second_best, highest - prices[i])

        # Combine with F[i - 1]. `X if cond else Y` is a conditional
        # expression; `if i` is False only when i == 0, where the book
        # takes F[-1] as 0 (no trade can finish before day 0). Without
        # this guard, left_profits[-1] would silently read the LAST item,
        # since negative indices count from the end in Python.
        # Documentation: https://docs.python.org/3/reference/expressions.html#conditional-expressions
        best_total = max(best_total, (left_profits[i - 1] if i else 0.0) + second_best)
    return best_total


# TEXTBOOK POST-SOLUTION DISCUSSION (page 48)
# ------------------------------------------
# The time complexity is O(n). The additional space complexity is O(n):
# the array that stores the best solutions for the prefix subarrays.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Solve the same problem
# in O(n) time and O(1) space.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Name and parameter match the book (`buy_and_sell_stock_twice(prices)`);
#   type hints added. The `if not prices: return 0.0` guard is not in the
#   book.
# - Book: `max_total_profit, min_price_so_far = 0.0, float('inf')` and
#   `first_buy_sell_profits = [0] * len(prices)` filled by index in a
#   `for i, price in enumerate(prices)` loop. File: separate variables
#   `lowest`, `first_best`, and `left_profits` built with `append`.
# - Book's backward loop is `for i, price in
#   reversed(list(enumerate(prices[1:], 1)))`, i.e. days n-1 down to 1,
#   and updates `max_total_profit = max(max_total_profit,
#   max_price_so_far - price + first_buy_sell_profits[i - 1])` directly,
#   reusing the forward maximum as its starting value. File: loops days
#   n-1 down to 0 with `range(len(prices) - 1, -1, -1)`, keeps an extra
#   running `second_best` (B[i]) and a separate `best_total` starting at
#   0.0, and uses `(left_profits[i - 1] if i else 0.0)` for day 0.
# - Variable names differ: `max_price_so_far` -> `highest`,
#   `max_total_profit` -> `first_best` / `best_total`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    #
    # These examples are added for learning (empty input, one possible
    # trade, two trades, falling prices). print() with several arguments
    # separates them with a space. `assert` stops the program with an
    # AssertionError if a result differs from the expected value; pytest
    # provides the more thorough automated verification.
    observed = buy_and_sell_stock_twice([])
    print("buy_and_sell_stock_twice:", observed)
    assert observed == 0.0
    observed = buy_and_sell_stock_twice([1, 5])
    print("buy_and_sell_stock_twice:", observed)
    assert observed == 4.0
    observed = buy_and_sell_stock_twice([1, 5, 2, 10])
    print("buy_and_sell_stock_twice:", observed)
    assert observed == 12.0
    observed = buy_and_sell_stock_twice([5, 4, 3, 2])
    print("buy_and_sell_stock_twice:", observed)
    assert observed == 0.0
