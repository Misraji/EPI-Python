"""EPI Python — Exercise 5.13: Sample Online Data

Chapter 5: Arrays
Textbook: pages 55–56 (printed page numbers; problem and solution start on
page 55, the worked example, program and remarks are on page 56).

PROBLEM (from the textbook)
---------------------------
Context: "This problem is motivated by the design of a packet sniffer that
provides a uniform sample of packets for a network session."

"Design a program that takes as input a size k, and reads packets,
continuously maintaining a uniform random subset of size k of the read
packets."

HINT (from the textbook)
------------------------
"Suppose you have a procedure which selects k packets from the first
n >= k packets as specified. How would you deal with the (n + 1)th
packet?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: store every packet read so far, and after each new packet
run the offline sampling algorithm (Solution 5.12) to pick k of them.
Space is O(n) after n packets, and time is O(nk), because every packet
triggers a call to Solution 5.12.

It may look impossible to do better, since after the nth packet we must
choose k packets uniformly from all n. But suppose we already hold a
uniformly random k-subset of the first n packets. When packet n + 1
arrives, it should be in the new subset with probability k/(n + 1). If it
is chosen, removing one member of the existing subset uniformly at random
and inserting the new packet yields a uniformly random subset of the
n + 1 packets.

The formal correctness proof is by induction on the number of packets
read; the hypothesis is that all k-sized subsets are equally likely after
n >= k packets have been read.

Book worked example: k = 2, packets arrive in order p, q, r, t, u, v.
  - Keep the first two: {p, q}.
  - r is selected with probability 2/3; suppose it is not. Still {p, q}.
  - t is selected with probability 2/4; suppose it is. Pick one of {p, q}
    uniformly to replace with t; say q. Now {p, t}.
  - u is selected with probability 2/5; suppose it is. Pick one of {p, t}
    uniformly to replace; say t. Now {p, u}.
  - v is selected with probability 2/6; suppose it is not. The random
    subset stays {p, u}.

The book prints one program, `online_random_sample(it, k)`, implemented
here with the same name. (Picking a random index in [0, count - 1] and
replacing only when it is below k combines both random choices, "is the
new packet selected?" and "which old one does it replace?", into one
call.)

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    online_random_sample(iter(range(10)), 3, random.Random(42))
        -> 3 distinct values from 0..9 (reproducible with seed 42).
"""

# Python standard library: building blocks for efficient iteration.
# Module documentation: https://docs.python.org/3/library/itertools.html
# islice API: https://docs.python.org/3/library/itertools.html#itertools.islice
import itertools

# Python standard library: pseudo-random number generation.
# Module documentation: https://docs.python.org/3/library/random.html
# randrange: https://docs.python.org/3/library/random.html#random.randrange
# Random class: https://docs.python.org/3/library/random.html#random.Random
import random


# Type hints: `k: int` and `-> list` document intended types; `stream` is
# left unannotated (any iterable works). Python does not enforce
# annotations at run time. `rng=None` is a default parameter value.
# Documentation: https://docs.python.org/3/library/typing.html
def online_random_sample(stream, k: int, rng=None) -> list:
    """Maintain a size-k uniform reservoir while consuming a stream once.

    This is the textbook's `online_random_sample(it, k)` program.
    """

    # Guard added in this repository (not in the book).
    # Documentation: https://docs.python.org/3/library/exceptions.html#ValueError
    if k < 0:
        raise ValueError("k must be nonnegative")

    # `X if condition else Y` is a conditional expression: use the
    # `random` module's shared generator unless a generator object (for
    # example a seeded random.Random) was supplied.
    rng = random if rng is None else rng

    # `iter()` obtains an iterator; generators can be consumed only once.
    # Taking an iterator here means islice() below and the `for` loop
    # afterwards share one position in the stream: the loop continues
    # exactly where islice stopped. (If `stream` were a list and we looped
    # over the list itself, the loop would restart at the first element.)
    # Documentation: https://docs.python.org/3/library/functions.html#iter
    iterator = iter(stream)

    # Book comment: "Stores the first k elements."
    # `islice(iterator, k)` lazily retrieves the FIRST k elements only, and
    # CONSUMES them from the iterator. This does not materialize the entire
    # source iterable, so it works for huge input streams and file-backed
    # iterators as well as Python lists. If fewer than k items exist it
    # simply yields fewer. `list(...)` collects the yielded items.
    # Documentation: https://docs.python.org/3/library/itertools.html#itertools.islice
    reservoir = list(itertools.islice(iterator, k))

    # The book states this as an assumption ("there are at least k
    # elements in the stream"); the file checks it explicitly.
    if len(reservoir) != k:
        raise ValueError("The stream provided fewer than k entries")

    # Book comment: "Have read the first k elements."
    # `enumerate(iterator, start=k+1)` pairs each remaining element with a
    # running count that starts at k + 1, i.e. the number of items seen so
    # far including this one (the book's `num_seen_so_far`).
    # Documentation: https://docs.python.org/3/library/functions.html#enumerate
    for count, element in enumerate(iterator, start=k + 1):

        # Book comment: "Generate a random number in [0, num_seen_so_far -
        # 1], and if this number is in [0, k - 1], we replace that element
        # from the sample with x."
        # randrange(count) samples uniformly from integers 0..count-1
        # (the stop value `count` is excluded, like range()).
        # If the slot lies within the reservoir, replace the old element.
        # That happens with probability k / count, and each reservoir slot
        # is equally likely to be the one replaced.
        # Documentation: https://docs.python.org/3/library/random.html#random.randrange
        slot = rng.randrange(count)
        if slot < k:
            reservoir[slot] = element
    return reservoir


# TEXTBOOK POST-SOLUTION DISCUSSION (page 56)
# ------------------------------------------
# Each element of the stream costs O(1) time, so the total time is
# proportional to the number of elements read. The space complexity is
# O(k).
#
# At every step all subsets are equally likely. However, successive
# subsets are not independent of each other: consecutive ones differ in
# at most one element. In contrast, the subsets produced by the brute-force
# approach are independent from one iteration to the next.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def online_random_sample(it, k)` (comment: "Assumption: there
#   are at least k elements in the stream."). File:
#   `online_random_sample(stream, k, rng=None)` with type hints and an
#   optional generator parameter; it calls `iter(stream)` first, so it
#   also accepts lists.
# - File adds two ValueError checks (negative k; fewer than k elements).
# - Book: `sampling_results` and a manual counter
#   `num_seen_so_far = k` incremented inside `for x in it:`; file:
#   `reservoir` with `enumerate(iterator, start=k + 1)` providing the
#   count. Book variable `idx_to_replace`; file `slot`.
# - Book calls `random.randrange` directly; file calls `rng.randrange`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # `Random(seed)` builds an isolated reproducible pseudorandom generator:
    # the same seed (42) gives the same sample on every run.
    # Documentation: https://docs.python.org/3/library/random.html#random.Random
    rng = random.Random(42)

    # Added example: sample 3 of the numbers 0..9 from an iterator, which
    # behaves like a stream that can be read only once.
    selected = online_random_sample(iter(range(10)), 3, rng)

    # print() with several arguments separates them with a space.
    print('online sample:', selected)

    # `assert` stops the program with an AssertionError if the condition
    # is false. set() keeps distinct values only, so a set of size 3 shows
    # the three sampled values are different. pytest provides the more
    # thorough automated verification.
    assert len(selected) == 3 and len(set(selected)) == 3
