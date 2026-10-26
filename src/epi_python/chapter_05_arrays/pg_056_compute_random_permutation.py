"""EPI Python — Exercise 5.14: Compute a Random Permutation

Chapter 5: Arrays
Textbook: pages 56–57 (printed page numbers; problem at the bottom of page
56, hint, solution, program and complexity on page 57).

PROBLEM (from the textbook)
---------------------------
Context: "Generating random permutations is not as straightforward as it
seems. For example, iterating through <0,1,...,n - 1> and swapping each
element with another randomly selected element does not generate all
permutations with equal probability. One way to see this is to consider
the case n = 3. The number of permutations is 3! = 6. The total number of
ways in which we can choose the elements to swap is 3^3 = 27 and all are
equally likely. Since 27 is not divisible by 6, some permutations
correspond to more ways than others, so not all permutations are equally
likely."

"Design an algorithm that creates uniformly random permutations of
{0,1,...,n - 1}. You are given a random number generator that returns
integers in the set {0,1,...,n - 1} with equal probability; use as few
calls to it as possible."

HINT (from the textbook)
------------------------
"If the result is stored in A, how would you proceed once A[n - 1] is
assigned correctly?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: repeatedly draw random numbers between 0 and n - 1
inclusive; if a number was already drawn, discard it and try again. A
hash table is a good way to remember which values have been picked.

Book example, n = 4: the draws might be 1, 2, 1 (repeat), 3, 1 (repeat),
2 (repeat), 0 (now all of 0..3 have appeared). The resulting permutation
is <1,2,3,0>.

All permutations are clearly equally likely this way. Extra space beyond
the result is O(n) for the hash table. The time is harder to analyze:
early draws almost always give new values, but collecting the last few
takes many tries. Computing the expected number of tries is the Coupon
Collector's Problem; the average is known to be O(n log n).

To improve, avoid repeats by limiting which values the next draw can
choose from. Apply Solution 5.12 (offline sampling, page 54) to
<0,1,2,...,n - 1> with k = n. At each step the array is split into the
permutation built so far and the values still available. The returned
SET is always {0,1,...,n - 1}, but all n! orderings of it are equally
likely.

Book example, n = 4, starting from <0,1,2,3>:
  1. Random number in [0, 3]; suppose 1. Array becomes <1,0,2,3>.
  2. Random number in [1, 3]; suppose 3. Array becomes <1,3,0,2>.
  3. Random number in [2, 3]; suppose 3. Array becomes <1,3,2,0>.
  This is the returned result.

The book prints one program, `compute_random_permutation(n)`, which calls
`random_sampling(n, permutation)` from Exercise 5.12; the file implements
it with the same name (inlining that sampling loop).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    compute_random_permutation(8, random.Random(42))
        -> some ordering of 0..7 (reproducible with seed 42).
"""



# Python standard library: pseudo-random number generation.
# Module documentation: https://docs.python.org/3/library/random.html
# randrange: https://docs.python.org/3/library/random.html#random.randrange
# Random class: https://docs.python.org/3/library/random.html#random.Random
import random


# Type hints: `n: int` and `-> list[int]` document intended types; Python
# does not enforce them at run time. `rng=None` is a default parameter
# value, so callers may omit it.
# Documentation: https://docs.python.org/3/library/typing.html
def compute_random_permutation(n: int, rng=None) -> list[int]:
    """Construct a random permutation of integers from zero through n-1.

    This is the textbook's `compute_random_permutation(n)` program, with
    the offline-sampling loop of Exercise 5.12 written inline.
    """

    # Guard added in this repository (not in the book).
    # Documentation: https://docs.python.org/3/library/exceptions.html#ValueError
    if n < 0:
        raise ValueError("n must be nonnegative")

    # `X if condition else Y` is a conditional expression: use the
    # `random` module's shared generator unless a generator object (e.g. a
    # seeded random.Random, which has the same methods) was supplied.
    rng = random if rng is None else rng

    # `list(range(n))` builds [0, 1, ..., n - 1].
    permutation = list(range(n))

    # Partial Fisher–Yates shuffle with k = n (Solution 5.12).
    for i in range(n):

        # randrange(i, n) returns a random integer from i up to n - 1: the
        # stop value n is excluded, as in range(). This is the same range
        # as the book's randint(i, n - 1), whose end point is included.
        j = rng.randrange(i, n)

        # Swap the chosen value into position i (tuple packing/unpacking).
        permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation


# TEXTBOOK POST-SOLUTION DISCUSSION (page 57)
# ------------------------------------------
# The time complexity is O(n). As a bonus, no storage is needed beyond the
# permutation array itself.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def compute_random_permutation(n)` with body
#   `permutation = list(range(n)); random_sampling(n, permutation);
#   return permutation`, reusing Exercise 5.12's function. File: same
#   name plus an optional `rng` parameter and type hints; it inlines the
#   sampling loop using `rng.randrange(i, n)` instead of calling
#   `random_sampling` (which uses `random.randint(i, len(A) - 1)`).
# - File adds a `n < 0` ValueError guard.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # random.Random(seed) constructs an independent pseudo-random number
    # generator; the fixed seed 42 makes this added example reproducible.
    # Documentation: https://docs.python.org/3/library/random.html#random.Random
    permutation = compute_random_permutation(8, random.Random(42))

    # print() with several arguments separates them with a space.
    print("permutation:", permutation)

    # `assert` stops the program with an AssertionError if the condition
    # is false. sorted() returns a new sorted list; if it equals [0..7],
    # the result contains each of 0..7 exactly once. pytest provides the
    # more thorough automated verification.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    assert sorted(permutation) == list(range(8))
