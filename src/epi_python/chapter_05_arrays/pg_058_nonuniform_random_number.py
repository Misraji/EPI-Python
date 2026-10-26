"""EPI Python — Exercise 5.16: Generate Nonuniform Random Numbers

Chapter 5: Arrays
Textbook: pages 58–59 (printed page numbers; the motivation starts at the
bottom of page 58; problem, solution, program, complexity and variant are
on page 59).

PROBLEM (from the textbook)
---------------------------
Context: You must write a load test for a server. From a year of data on
the inter-arrival times of requests, you have computed a histogram of
their distribution, and the load test should generate requests whose
inter-arrival times follow that same distribution. The problem below
formalizes generating such inter-arrival times.

"You are given n numbers as well as probabilities p0, p1, ..., p(n-1),
which sum up to 1. Given a random number generator that produces values
in [0,1) uniformly, how would you generate one of the n numbers according
to the specified probabilities? For example, if the numbers are 3, 5, 7,
11, and the probabilities are 9/18, 6/18, 2/18, 1/18, then in 1000000
calls to your program, 3 should appear roughly 500000 times, 5 should
appear roughly 333333 times, 7 should appear roughly 111111 times, and 11
should appear roughly 55555 times."

HINT (from the textbook)
------------------------
"Look at the graph of the probability that the selected number is less
than or equal to a. What do the jumps correspond to?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The actual values of the numbers do not matter: the task is to pick one
of n outcomes with probabilities p0, ..., p(n-1).

- If every probability were equal (1/n), one call to the generator would
  do: choose outcome i when the random number lies between i/n and
  (i + 1)/n.
- For unequal probabilities, split the unit interval into n disjoint
  segments whose lengths are proportional to the p_j, draw a number
  uniformly in the unit interval, and return the number whose segment it
  falls in.
- The segments are easy to build: use the running sums p0, p0 + p1,
  p0 + p1 + p2, ..., p0 + ... + p(n-1) as the endpoints. For the example
  in the problem the four intervals are [0.0, 0.5), [0.5, 0.833),
  [0.833, 0.944), [0.944, 1.0]. If the uniform draw is 0.873, it lies in
  [0.833, 0.944), the third interval, so the answer is the third number,
  7.
- Finding the interval that contains a number takes O(n) time by a plain
  search of n intervals. Because the array of running sums is sorted,
  binary search finds it in O(log n) time instead.

The book prints one program, `nonuniform_random_number_generation(values,
probabilities)`, implemented here as `nonuniform_random_number`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    nonuniform_random_number(["red", "blue"], [1, 3], random.Random(2))
        -> "red" with probability 1/4, "blue" with probability 3/4.
The weights need not sum to 1 in this file (they are scaled by their
total; see the code).
"""



# Python standard library: binary search in sorted sequences.
# Module documentation: https://docs.python.org/3/library/bisect.html
# bisect_right: https://docs.python.org/3/library/bisect.html#bisect.bisect_right
import bisect

# Python standard library: building blocks for efficient iteration.
# Module documentation: https://docs.python.org/3/library/itertools.html
# accumulate: https://docs.python.org/3/library/itertools.html#itertools.accumulate
import itertools

# Python standard library: pseudo-random number generation.
# Module documentation: https://docs.python.org/3/library/random.html
# random(): https://docs.python.org/3/library/random.html#random.random
# Random class: https://docs.python.org/3/library/random.html#random.Random
import random


# Type hints document intended types (a list of ints, a list of floats,
# an int result); Python does not enforce them, and the demo below
# actually passes strings and ints. `rng=None` is a default parameter.
# Documentation: https://docs.python.org/3/library/typing.html
def nonuniform_random_number(values: list[int], probabilities: list[float], rng=None) -> int:
    """Draw values with prescribed nonnegative weights.

    This is the textbook's `nonuniform_random_number_generation` program,
    with input checks and weight scaling added.
    """

    # Input checks added in this repository (not in the book).
    # Documentation: https://docs.python.org/3/library/exceptions.html#ValueError
    if len(values) != len(probabilities) or not values:
        raise ValueError("Expected nonempty equally sized value/weight arrays")

    # any(...) is True if at least one item of the generator expression is
    # true (here: some weight is negative). sum() adds all the weights.
    # Documentation: https://docs.python.org/3/library/functions.html#any
    if any(weight < 0 for weight in probabilities) or sum(probabilities) <= 0:
        raise ValueError("Weights must be nonnegative and not all zero")

    # `X if condition else Y` is a conditional expression: use the
    # `random` module's shared generator unless a generator object (such as
    # a seeded random.Random) was supplied.
    rng = random if rng is None else rng

    # itertools.accumulate(iterable) lazily yields running totals:
    # accumulate([0.2, 0.3, 0.5]) produces 0.2, 0.5, 1.0. These are the
    # right-hand endpoints of the intervals described in the book.
    # `list(...)` collects them so they can be indexed and binary-searched.
    # (Floating-point rounding may make the last total slightly different
    # from 1.0.)
    # Documentation: https://docs.python.org/3/library/itertools.html#itertools.accumulate
    cumulative = list(itertools.accumulate(probabilities))

    # rng.random() returns a float uniformly distributed in [0.0, 1.0).
    # Multiplying by the total weight (`cumulative[-1]`, the last running
    # sum) spreads it over [0, total), so weights need not sum to 1.
    choice = rng.random() * cumulative[-1]

    # bisect.bisect_right(a, x) returns the index where x would be inserted
    # into the sorted list a to keep it sorted, placed AFTER any entries
    # equal to x; i.e. the index of the first endpoint strictly greater
    # than x. That index is exactly the interval containing x. Example:
    # with endpoints [0.5, 0.833, 0.944, 1.0], x = 0.873 gives index 2,
    # the third interval. bisect_right places an exact boundary in the
    # following bucket, matching the half-open intervals [lo, hi).
    # It runs in O(log n) time (binary search).
    # Documentation: https://docs.python.org/3/library/bisect.html#bisect.bisect_right
    index = bisect.bisect_right(cumulative, choice)

    # min() clamps the index to the last valid position, a safety net in
    # case rounding ever makes `choice` reach the final endpoint.
    return values[min(index, len(values) - 1)]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 59)
# ------------------------------------------
# Computing one value takes O(n) time, dominated by building the array of
# interval endpoints; that array also makes the space complexity O(n).
#
# Once the array exists, each further value costs one call to the uniform
# random number generator plus a binary search, i.e. O(log n).
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Given a random number
# generator that produces values in [0, 1] uniformly, how would you
# generate a value X from T according to a continuous probability
# distribution, such as the exponential distribution?


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def nonuniform_random_number_generation(values, probabilities)`;
#   file: `nonuniform_random_number(values, probabilities, rng=None)` with
#   type hints and an optional generator parameter.
# - File adds two ValueError checks (length/emptiness; negative or
#   all-zero weights). Not in the book.
# - Book: `prefix_sum_of_probabilities = list(itertools.accumulate(
#   probabilities))`, then
#   `interval_idx = bisect.bisect(prefix_sum_of_probabilities,
#   random.random())`, `return values[interval_idx]`. File: names
#   `cumulative`/`index`; uses `bisect.bisect_right` (the same function as
#   `bisect.bisect`); scales the random number by the total weight
#   (`* cumulative[-1]`); and clamps the index with
#   `min(index, len(values) - 1)`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # random.Random(seed) constructs an independent pseudo-random number
    # generator; the fixed seed 2 makes this added example reproducible.
    # The weights [1, 3] mean "blue" should come up three times as often
    # as "red".
    # Documentation: https://docs.python.org/3/library/random.html#random.Random
    value = nonuniform_random_number(["red", "blue"], [1, 3], random.Random(2))

    # print() with several arguments separates them with a space.
    print("weighted choice:", value)

    # `assert` stops the program with an AssertionError if the condition
    # is false; here it only checks that one of the inputs was returned.
    # pytest provides the more thorough automated verification.
    assert value in ("red", "blue")
