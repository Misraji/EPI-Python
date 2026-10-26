"""EPI Python — Exercise 16.6: The Knapsack Problem

Chapter 16: Dynamic Programming
Textbook: pages 246–249 (printed page numbers; problem and solution start on 246).

PROBLEM (from the textbook)
---------------------------
"A thief breaks into a clock store. Each clock has a weight and a value,
which are known to the thief. His knapsack cannot hold more than a
specified combined weight. His intention is to take clocks whose total
value is maximum subject to the knapsack's weight constraint.

His problem is illustrated in Figure 16.8 on the next page. If the knapsack
can hold at most 130 ounces, he cannot take all the clocks. If he greedily
chooses clocks, in decreasing order of value-to-weight ratio, he will
choose P, H, O, B, I, and L in that order for a total value of $669.
However, {H, J, O} is the optimum selection, yielding a total value of
$695."

Figure 16.8 (a clock store), value and weight of each clock:
    A $65 20 oz.    B $35 8 oz.     C $245 60 oz.   D $195 55 oz.
    E $65 40 oz.    F $150 70 oz.   G $275 85 oz.   H $155 25 oz.
    I $120 30 oz.   J $320 65 oz.   K $75 75 oz.    L $40 10 oz.
    M $200 95 oz.   N $100 50 oz.   O $220 40 oz.   P $99 10 oz.

"Write a program for the knapsack problem that selects a subset of items
that has maximum value and satisfies the weight constraint. All items have
integer weights and values. Return the value of the subset."

HINT (from the textbook)
------------------------
"Greedy approaches are doomed."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Greedy rules — take the most valuable clock, or the clock with the best
value-to-weight ratio — do not always give the optimum.

Considering all subsets (e.g. with Solution 15.4, page 225) always finds
the optimum, but takes exponential time in the number of clocks, and it
ignores the weight constraint: e.g. no subset containing both F and G can
satisfy it.

Better: use the weight constraint while searching. Ask what the optimum is
if a given clock is chosen and if it is not; each question is a smaller
instance with its own weight limit. For example, choosing clock A means
finding the best value from clocks B-P with capacity 130 - 20 and adding
$65; not choosing A means finding the best value from B-P with capacity
130. The larger of the two is the optimum.

Formally, number the clocks 0 .. n-1 with weight w_i and value v_i. Let
V[i][w] be the optimum when restricted to clocks 0, 1, ..., i-1 with
capacity w. Then

    V[i][w] = max(V[i-1][w], V[i-1][w - w_i] + v_i)   if w_i <= w,
    V[i][w] = V[i-1][w]                                otherwise,

with V[i][w] = 0 as the base cases i = 0 or w = 0.

Figure 16.9 shows a small example with capacity 5 oz. and four items
(drawn as pictures in the book; called items 0-3 here):

    (a) item  value  weight          (b) V table, capacities 0..5
        0     $60    5 oz.           items {0}:        0  0  0  0  0 60
        1     $50    3 oz.           items {0,1}:      0  0  0 50 50 60
        2     $70    4 oz.           items {0,1,2}:    0  0  0 50 70 70
        3     $30    2 oz.           items {0,1,2,3}:  0  0 30 50 70 80

E.g. the lower-right entry is the larger of the entry above it (70) and 30
plus the entry for items {0,1,2} at capacity 5 - 2 = 3 (50), i.e. 80.

The book's program optimum_subject_to_capacity(items, capacity) uses a
namedtuple Item('weight', 'value') and a memoized recursive helper
optimum_subject_to_item_and_capacity(k, available_capacity) with a 2D
cache V initialized to -1. This file instead uses a one-dimensional
bottom-up table (see TEXTBOOK CODE COMPARISON); the book's program is not
in this file.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
Items are (weight, value) tuples:
    [], capacity 10                          -> 0
    [(2, 3), (3, 4), (4, 5)], capacity 5     -> 7   (weights 2 + 3)
    [(2, 10)], capacity 1                    -> 0   (nothing fits)
    [(2, 10), (2, 20)], capacity 4           -> 30  (both items)
"""


def optimum_subject_to_capacity(items: list[tuple[int, int]], capacity: int) -> int:
    """Maximum total value of a 0/1 knapsack; items are (weight, value).

    NOT the book's printed program (a memoized 2D recursion); this is a
    one-dimensional bottom-up form of the same recurrence, using O(capacity)
    space (the book's first variant asks for O(w) space).
    """

    # best[c] = best value achievable with capacity c using the items
    # processed so far. Initially (no items) every capacity gives 0.
    # Type hints (`list[tuple[int, int]]`: a list of 2-tuples of ints) are
    # documentation only; Python does not enforce them.
    best=[0]*(capacity+1)

    # `for weight,value in items` unpacks each (weight, value) tuple into
    # two variables.
    for weight,value in items:

        # range(capacity, weight-1, -1) counts DOWN from capacity to weight
        # (the stop value weight-1 is excluded). Going downward means
        # best[limit-weight] still holds the value from BEFORE this item was
        # considered, so each item is used at most once (0/1 knapsack).
        # Counting upward would let one item be reused many times.
        # Capacities below `weight` cannot hold the item and keep their
        # old values.
        for limit in range(capacity,weight-1,-1):

            # max(a, b) returns the larger: skip the item, or take it and
            # add its value to the best result for the remaining capacity.
            best[limit]=max(best[limit],best[limit-weight]+value)
    return best[capacity]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 248)
# --------------------------------------------
# The book's algorithm computes V[n-1][w] in O(nw) time and uses O(nw)
# space (n items, capacity w).
#
# VARIANTS (pages 248–249; each stated in the book; no solution given)
# --------------------------------------------------------------------
# 1. Solve the same problem using O(w) space.
# 2. Solve the same problem using O(C) space, where C is the number of
#    weights between 0 and w that can be achieved. For example, if the
#    weights are 100, 200, 200, 500 and w = 853, then C = 9, corresponding
#    to the weights 0, 100, 200, 300, 400, 500, 600, 700, 800.
# 3. Solve the fractional knapsack problem: the thief may take a fraction
#    of an item (e.g. by breaking it), and the value of a fraction of an
#    item is that fraction times the item's value.
# 4. "Divide-the-spoils-fairly": two thieves want to split the stolen items
#    into two groups whose values differ as little as possible. For the
#    clocks of Figure 16.8, an optimum split is {A, G, J, M, O, P} to one
#    thief and the rest to the other; the first set is worth $1179 and the
#    second $1180. An equal split is impossible because the total value is
#    odd. Write a program to solve the divide-the-spoils-fairly problem.
# 5. Solve divide-the-spoils-fairly with the additional constraint that the
#    thieves have the same number of items.
# 6. The US President is elected by the Electoral College. All electors
#    from each state, as well as Washington, D.C., vote for the same
#    candidate. Write a program to determine if a tie is possible in a
#    presidential election with two candidates. Table 16.2 (electoral
#    college votes):
#      Alabama 9, Alaska 3, Arizona 11, Arkansas 6, California 55,
#      Colorado 9, Connecticut 7, Delaware 3, Florida 29, Georgia 16,
#      Hawaii 4, Idaho 4, Illinois 20, Indiana 11, Iowa 6, Kansas 6,
#      Kentucky 8, Louisiana 8, Maine 4, Maryland 10, Massachusetts 11,
#      Michigan 16, Minnesota 10, Mississippi 6, Missouri 10, Montana 3,
#      Nebraska 5, Nevada 6, New Hampshire 4, New Jersey 14, New Mexico 5,
#      New York 29, North Carolina 15, North Dakota 3, Ohio 18,
#      Oklahoma 7, Oregon 7, Pennsylvania 20, Rhode Island 4,
#      South Carolina 9, South Dakota 3, Tennessee 11, Texas 38, Utah 6,
#      Vermont 3, Virginia 13, Washington 12, West Virginia 5,
#      Wisconsin 10, Wyoming 3, Washington, D.C. 3.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Book defines `Item = collections.namedtuple('Item', ('weight',
#   'value'))` and accesses `items[k].weight` / `items[k].value`; file
#   takes plain `(weight, value)` tuples and has no `collections` import.
# * Book: `optimum_subject_to_capacity(items, capacity)` with nested
#   memoized `optimum_subject_to_item_and_capacity(k, available_capacity)`
#   (returns 0 when k < 0; caches in `V = [[-1] * (capacity + 1) for _ in
#   items]`; computes `without_curr_item`, `with_curr_item`, stores their
#   max); returns `optimum_subject_to_item_and_capacity(len(items) - 1,
#   capacity)`.
# * File: same function name and parameters (with type hints), but an
#   iterative 1D table `best` filled with descending capacities; no
#   recursion, no 2D cache. O(capacity) space instead of O(n * capacity).
# * The book's memoized implementation (and its comments, e.g. "Returns
#   the optimum value when we choose from items[:k + 1] and have a capacity
#   of available_capacity.", "No items can be chosen.") is MISSING from the
#   file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples: no items, an ordinary case, an item too heavy to fit,
    # and two items that both fit.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite is thorough.
    result=optimum_subject_to_capacity([], 10)
    print('optimum_subject_to_capacity', result)
    assert result == 0
    result=optimum_subject_to_capacity([(2, 3), (3, 4), (4, 5)], 5)
    print('optimum_subject_to_capacity', result)
    assert result == 7
    result=optimum_subject_to_capacity([(2, 10)], 1)
    print('optimum_subject_to_capacity', result)
    assert result == 0
    result=optimum_subject_to_capacity([(2, 10), (2, 20)], 4)
    print('optimum_subject_to_capacity', result)
    assert result == 30
