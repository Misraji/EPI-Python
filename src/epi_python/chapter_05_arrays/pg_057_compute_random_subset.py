"""EPI Python — Exercise 5.15: Compute a Random Subset

Chapter 5: Arrays
Textbook: pages 57–58 (printed page numbers; problem and start of the
solution on page 57, the rest of the solution, program and complexity on
page 58).

PROBLEM (from the textbook)
---------------------------
Context: "The set {0,1,2,...,n - 1} has C(n, k) = n!/((n - k)!k!) subsets
of size k. We seek to design an algorithm that returns any one of these
subsets with equal probability."

"Write a program that takes as input a positive integer n and a size
k <= n, and returns a size-k subset of {0,1,2,...,n - 1}. The subset
should be represented as an array. All subsets should be equally likely
and, in addition, all permutations of elements of the array should be
equally likely. You may assume you have a function which takes as input a
nonnegative integer t and returns an integer in the set {0,1,...,t - 1}
with uniform probability."

HINT (from the textbook)
------------------------
"Simulate Solution 5.12 on Page 54, using an appropriate data structure to
reduce space."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
1. Like the brute force of Solution 5.14, keep drawing random numbers in
   0..n - 1 until k distinct values have appeared. This degrades in the
   same way when k is close to n, and needs O(k) extra space.

2. Imitate offline sampling (Solution 5.12) on an array with A[i] = i,
   stopping after k iterations. Creating the array costs O(n) space and
   O(n) time; after that, producing the subset takes O(k) time.

3. When k is much smaller than n, almost all of the array is untouched,
   i.e. A[i] = i. Simulate A with a hash table H that records only the
   entries the algorithm has changed; every other entry implicitly has
   its default value, its own index. Conceptually H holds the touched
   entries A[i], which may differ from i. H's keys and values come from
   {0,1,...,n - 1}, and H is updated as the algorithm advances:
     - if i is in H, its value in H is what the brute-force algorithm
       would have stored in A[i];
     - if i is not in H, then implicitly A[i] = i.
   At most k entries are tracked, so for small k this saves time and
   space compared with initializing and updating an array of length n.

   H starts empty. Do k iterations: choose a random integer r (the book's
   text writes the range as [0, n - 1 - i], where i is the iteration
   count starting at 0; its program draws from [i, n - 1]). There are
   four cases, depending on whether each of the two entries being swapped
   is already in H or not. The answer is A[0, k - 1], read from H.

Book worked example, n = 100, k = 4 (H shown as (key, value) pairs):
  - Draw 28: H = (0,28), (28,0). So A[0] = 28 and A[28] = 0; every other
    A[i] = i.
  - Draw 42: H = (0,28), (28,0), (1,42), (42,1).
  - Draw 28 again: H = (0,28), (28,2), (1,42), (42,1), (2,0).
  - Draw 64 (the book labels this one "third iteration" again; it is the
    fourth): H = (0,28), (28,2), (1,42), (42,1), (2,0), (3,64), (64,3).
  The random subset is the values at indices 0, 1, 2, 3: <28,42,0,64>.

The book prints one program, `random_subset(n, k)`, implemented here with
the same name.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    random_subset(100, 5, random.Random(12))
        -> 5 distinct integers from 0..99 (reproducible with seed 12).
"""



# Python standard library: pseudo-random number generation.
# Module documentation: https://docs.python.org/3/library/random.html
# randrange: https://docs.python.org/3/library/random.html#random.randrange
# Random class: https://docs.python.org/3/library/random.html#random.Random
import random


# Type hints: `n: int`, `k: int`, `-> list[int]` document intended types;
# Python does not enforce them at run time. `rng=None` is a default value
# so callers may omit the generator.
# Documentation: https://docs.python.org/3/library/typing.html
def random_subset(n: int, k: int, rng=None) -> list[int]:
    """Select k distinct members of range(n) using a sparse virtual shuffle.

    This is the textbook's `random_subset(n, k)` program.
    """

    # Chained comparison `0 <= k <= n` means `0 <= k and k <= n`. This
    # guard is not in the book.
    # Documentation: https://docs.python.org/3/library/exceptions.html#ValueError
    if not 0 <= k <= n:
        raise ValueError("Expected 0 <= k <= n")

    # `X if condition else Y` is a conditional expression: use the
    # `random` module's shared generator unless a generator object (such as
    # a seeded random.Random) was supplied.
    rng = random if rng is None else rng

    # The hash table H: a dict from array index to the value the virtual
    # array holds there, for touched indices only. `dict[int, int]` is a
    # variable annotation (a type hint, not enforced at run time); `{}`
    # creates an empty dict.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#dict
    changed: dict[int, int] = {}
    for i in range(k):

        # Book comment: "Generate a random index between i and n - 1,
        # inclusive." randrange(i, n) excludes its stop value n, so the
        # result lies in i..n-1.
        r = rng.randrange(i, n)

        # dict.get(key, default) returns the stored value, or `default`
        # if the key is absent. Using the index itself as the default is
        # exactly the rule "if i is not in H, then A[i] = i".
        # Documentation: https://docs.python.org/3/library/stdtypes.html#dict.get
        x, y = changed.get(i, i), changed.get(r, r)

        # Swap the two virtual entries by recording both new values in the
        # dict (tuple packing/unpacking). This handles all four cases (both,
        # one, or neither key already present) and also i == r.
        changed[i], changed[r] = y, x

    # List comprehension: after k iterations every index 0..k-1 has been
    # written into `changed`, so these lookups cannot fail.
    return [changed[i] for i in range(k)]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 58)
# ------------------------------------------
# The time complexity is O(k): each iteration does a bounded number of
# operations. The space complexity is also O(k), since H and the result
# array never hold more than k entries. (Strictly, H can hold up to 2k
# keys, as the worked example shows; that is still O(k).)
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def random_subset(n, k)`; file: `random_subset(n, k, rng=None)`
#   with an optional generator parameter and type hints; adds a range
#   check on k (`raise ValueError`).
# - Book names `changed_elements`, `rand_idx`, `rand_idx_mapped`,
#   `i_mapped`; file names `changed` (with a `dict[int, int]` annotation),
#   `r`, `y`, `x`.
# - Book writes the swap as two separate assignments
#   (`changed_elements[rand_idx] = i_mapped` then
#   `changed_elements[i] = rand_idx_mapped`); file does both in one tuple
#   assignment `changed[i], changed[r] = y, x` (same result).
# - Book calls `random.randrange(i, n)`; file `rng.randrange(i, n)`.
#   Final list comprehension matches.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # random.Random(seed) constructs an independent pseudo-random number
    # generator; the fixed seed 12 makes this added example reproducible.
    # Documentation: https://docs.python.org/3/library/random.html#random.Random
    sample = random_subset(100, 5, random.Random(12))

    # print() with several arguments separates them with a space.
    print("random subset:", sample)

    # `assert` stops the program with an AssertionError if the condition
    # is false. set() keeps distinct values, so size 5 means no repeats.
    # all(...) returns True when every item of the generator expression is
    # true: here, every sampled value lies in 0..99. pytest provides the
    # more thorough automated verification.
    # Documentation: https://docs.python.org/3/library/functions.html#all
    assert len(set(sample)) == 5 and all(0 <= x < 100 for x in sample)
