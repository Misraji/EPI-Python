"""EPI Python — Exercise 5.12: Sample Offline Data

Chapter 5: Arrays
Textbook: pages 54–55 (printed page numbers; problem and solution start on
page 54, the worked example, program and remarks are on page 55).

PROBLEM (from the textbook)
---------------------------
Context: "This problem is motivated by the need for a company to select a
random subset of its customers to roll out a new feature to. For example,
a social networking company may want to see the effect of a new UI on
page visit duration without taking the chance of alienating all its users
if the rollout is unsuccessful."

"Implement an algorithm that takes as input an array of distinct elements
and a size, and returns a subset of the given size of the array elements.
All subsets should be equally likely. Return the result in input array
itself."

HINT (from the textbook)
------------------------
"How would you construct a random subset of size k + 1 given a random
subset of size k?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Let A be the input array, n its length and k the requested size.

- Naive idea 1: walk through A and keep each entry with probability k/n.
  On average k entries are kept, but the actual number can be more or
  fewer than k.
- Naive idea 2: list every subset of size k and pick one at random. There
  are C(n, k) ("n choose k") such subsets, so time and space are huge,
  and enumerating them is itself nontrivial (the book points to Problem
  15.5 on page 226).

Key idea: build a random subset of size exactly k by first building one
of size k - 1 and then adding one more element chosen at random from the
rest.
  - k = 1 is easy: call the random number generator once, take the value
    mod n (call it r), and swap A[0] with A[r]. A[0] is the answer.
  - For k > 1: pick one element as above, then repeat the same process on
    the n - 1 element subarray A[1, n - 1]. In the end the random subset
    occupies A[0, k - 1] and the other elements occupy the last n - k
    slots.

Why it is uniform (intuition only; the book does not give the formal
proof): if all size-k subsets are equally likely, the construction makes
all size-(k + 1) subsets equally likely too. The formal argument is by
induction, with the hypothesis that every permutation of every size-k
subset of A is equally likely to appear in A[0, k - 1].

Book worked example: A = <3,7,5,11>, size 3.
  1. Random integer in [0, 3]; suppose 2. Swap A[0] and A[2]:
     <5,7,3,11>.
  2. Random integer in [1, 3]; suppose 3. Swap A[1] and A[3]:
     <5,11,3,7>.
  3. Random integer in [2, 3]; suppose 2. Swapping A[2] with itself
     leaves the array unchanged.
  The random subset is the first three entries, {5, 11, 3}.

The book prints one program, `random_sampling(k, A)`, implemented here
with the same name.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    random_sampling(3, [0, 1, 2, 3, 4, 5], random.Random(11))
        -> some 3 distinct values from the list (reproducible with the
           fixed seed 11).
"""



# Python standard library: pseudo-random number generation.
# Module documentation: https://docs.python.org/3/library/random.html
# randint: https://docs.python.org/3/library/random.html#random.randint
# Random class: https://docs.python.org/3/library/random.html#random.Random
import random


# Type hints: `k: int`, `values: list[int]`, `-> list[int]` document the
# intended types; Python does not enforce them at run time. `rng=None`
# gives the parameter a default value, so callers may omit it.
# Documentation: https://docs.python.org/3/library/typing.html
def random_sampling(k: int, values: list[int], rng=None) -> list[int]:
    """Uniformly choose k array elements using partial Fisher–Yates shuffle.

    This is the textbook's `random_sampling(k, A)` program. As the book
    requires, the sample ends up in values[:k] of the input list itself;
    the function additionally returns a copy of that prefix.
    """

    # Chained comparison: `0 <= k <= len(values)` means
    # `0 <= k and k <= len(values)`. This guard is not in the book.
    # Documentation: https://docs.python.org/3/library/exceptions.html#ValueError
    if not 0 <= k <= len(values):
        raise ValueError("k must be between zero and len(values)")

    # `X if condition else Y` is a conditional expression. With no `rng`
    # supplied, use the `random` module itself; its module-level functions
    # (random.randint, ...) share one hidden generator. Otherwise use the
    # given object, e.g. a seeded random.Random, which has the same
    # methods; this makes results reproducible for demos and tests.
    # Documentation: https://docs.python.org/3/reference/expressions.html#conditional-expressions
    rng = random if rng is None else rng
    for i in range(k):

        # Book comment: "Generate a random index in [i, len(A) - 1]."
        # randint(a, b) returns a random integer N with a <= N <= b: BOTH
        # endpoints are included (unlike range(), whose stop is excluded).
        # Each index in i..n-1 is equally likely.
        j = rng.randint(i, len(values) - 1)

        # Swap the chosen element into position i (tuple packing and
        # unpacking). Positions 0..i now hold the sample built so far.
        values[i], values[j] = values[j], values[i]

    # `values[:k]` is a slice: a NEW list with the first k elements.
    return values[:k]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 55)
# ------------------------------------------
# The algorithm clearly uses O(1) additional space, and its time
# complexity is O(k) to select the elements.
#
# It calls the random number generator k times. When k is bigger than
# n/2, one can do better by instead choosing the n - k elements to REMOVE
# from the set. For example, when k = n - 1 this replaces n - 1 calls to
# the random number generator with a single call.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): The rand() function in
# the standard C library returns a uniformly random number in
# [0, RAND_MAX - 1]. Does rand() mod n generate a number uniformly
# distributed in [0, n - 1]?


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def random_sampling(k, A)`; file: `random_sampling(k, values,
#   rng=None)` with type hints and an extra optional `rng` parameter
#   (book calls `random.randint` directly).
# - Book variable `r`; file `j`.
# - The file adds a range check on k (`raise ValueError`).
# - Book returns None (the sample is A[0, k - 1]); file also returns the
#   slice `values[:k]`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # random.Random(seed) constructs an independent pseudo-random number
    # generator. Giving it a fixed seed (11) makes the "random" choices
    # the same on every run, so the example is reproducible.
    # Documentation: https://docs.python.org/3/library/random.html#random.Random
    seeded = random.Random(11)

    # `list(range(6))` is [0, 1, 2, 3, 4, 5]; this example is added for
    # learning.
    values = list(range(6))
    selected = random_sampling(3, values, seeded)

    # print() with several arguments separates them with a space.
    print("offline sample:", selected)

    # `assert` stops the program with an AssertionError if the condition
    # is false. set() keeps only distinct items, so a set of size 3 shows
    # the three sampled values are all different. pytest provides the
    # more thorough automated verification.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#set
    assert len(selected) == 3 and len(set(selected)) == 3
