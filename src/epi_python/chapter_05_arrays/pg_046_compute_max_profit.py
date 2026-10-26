"""EPI Python — Exercise 5.6: Buy and Sell a Stock Once

Chapter 5: Arrays
Textbook: pages 46–47 (printed page numbers; the problem is introduced at
the bottom of page 46 and stated and solved on page 47).

PROBLEM (from the textbook)
---------------------------
Context: "This problem is concerned with the problem of optimally buying
and selling a stock once, as described on Page 2. As an example, consider
the following sequence of stock prices:
<310,315,275,295,260,270,290,230,255,250>. The maximum profit that can be
made with one buy and one sell is 30—buy at 260 and sell at 290. Note that
260 is not the lowest price, nor 290 the highest price."

"Write a program that takes an array denoting the daily stock price, and
returns the maximum profit that could be made by buying and then selling
one share of that stock. There is no need to buy if no profit is
possible."

HINT (from the textbook)
------------------------
"Identifying the minimum and maximum is not enough since the minimum may
appear after the maximum height. Focus on valid differences."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The book refers back to its introduction (page 2), where several
algorithms for this problem were developed. The one used here: walk
through the array and, at each entry, take the difference between the
current price and the minimum price seen so far; the answer is the
largest such difference.

Book example for <310,315,275,295,260,270,290,230,255,250>:
  - minimum seen so far, day by day:
        <310,310,275,275,260,260,260,230,230,230>
  - best profit if selling on each day (price minus that minimum):
        <0,5,0,20,0,10,30,0,25,20>
  - the overall maximum is 30: buy at 260 and sell at 290.

(A brute-force check of every buy/sell pair, O(n^2), is discussed in the
book's introduction rather than in this exercise.)

The book prints one program, `buy_and_sell_stock_once`, implemented here
as `compute_max_profit`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [5, 4, 3] -> 0.0   (prices only fall: do not buy)
    []        -> 0.0
    [1, 5]    -> 4.0
"""



# `prices: list[float]` and `-> float` are type hints documenting the
# expected argument and return types. Python does not enforce them at run
# time (ints work fine here too). `list[float]` requires Python 3.9+.
# Documentation: https://docs.python.org/3/library/typing.html
def compute_max_profit(prices: list[float]) -> float:
    """Largest profit obtainable by one buy followed by one sell.

    This is the textbook's `buy_and_sell_stock_once(prices)` program.
    """

    # `float("inf")` is positive infinity: it compares greater than every
    # finite number, so the first real price always replaces it in min().
    # Documentation: https://docs.python.org/3/library/functions.html#float
    min_seen = float("inf")

    # Start at 0.0 because "there is no need to buy if no profit is
    # possible": the answer is never negative.
    max_profit = 0.0
    for price in prices:

        # min() / max() of two values return the smaller / larger one.
        # Updating the minimum first means a sale on the same day as the
        # purchase is considered, which just yields a profit of 0.
        # Documentation: https://docs.python.org/3/library/functions.html#min
        min_seen = min(min_seen, price)
        max_profit = max(max_profit, price - min_seen)
    return max_profit


# TEXTBOOK POST-SOLUTION DISCUSSION (page 47)
# ------------------------------------------
# The time complexity is O(n) and the space complexity is O(1), where n is
# the length of the array.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Write a program that
# takes an array of integers and finds the length of a longest subarray
# all of whose entries are equal.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def buy_and_sell_stock_once(prices)`; file: function renamed
#   `compute_max_profit`, type hints added.
# - Book initialises both at once:
#   `min_price_so_far, max_profit = float('inf'), 0.0`; file uses two
#   statements and renames `min_price_so_far` to `min_seen`.
# - Book loop body: computes `max_profit_sell_today = price -
#   min_price_so_far`, updates `max_profit`, THEN updates the minimum.
#   File updates the minimum FIRST, then `max_profit` directly from
#   `price - min_seen` (no `max_profit_sell_today` variable). The
#   returned value is the same, since the extra same-day pair only adds a
#   candidate profit of 0.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    #
    # The first price list is the book's example (answer 30). The others
    # are added: falling prices, no prices, and a simple rise.
    # print() with several arguments separates them with a space.
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value; pytest provides the more thorough
    # automated verification. Note that 30 == 30.0 is True in Python.
    observed = compute_max_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
    print("compute_max_profit:", observed)
    assert observed == 30.0
    observed = compute_max_profit([5, 4, 3])
    print("compute_max_profit:", observed)
    assert observed == 0.0
    observed = compute_max_profit([])
    print("compute_max_profit:", observed)
    assert observed == 0.0
    observed = compute_max_profit([1, 5])
    print("compute_max_profit:", observed)
    assert observed == 4.0
