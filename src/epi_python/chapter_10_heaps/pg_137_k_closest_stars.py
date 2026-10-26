"""EPI Python — Exercise 10.4: Compute the k Closest Stars

Chapter 10: Heaps
Textbook: pages 137–139 (printed page numbers; problem at the bottom of page
137, hint, solution, program and variant on page 138, the variant's last
sentences at the top of page 139).

PROBLEM (from the textbook)
---------------------------
"Consider a coordinate system for the Milky Way, in which Earth is at
(0, 0, 0). Model stars as points, and assume distances are in light years.
The Milky Way consists of approximately 10^12 stars, and their coordinates
are stored in a file.

How would you compute the k stars which are closest to Earth?"

HINT (from the textbook)
------------------------
"Suppose you know the k closest stars in the first n stars. If the (n + 1)th
star is to be added to the set of k closest stars, which element in that set
should be evicted?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Without memory limits: read all stars into an array and find the k smallest
distances by sorting, or use the selection algorithm of Solution 11.8
(page 153) to find the kth smallest, after which the k smallest are easy to
collect. Both need O(n) space, and this dataset does not fit in RAM.

Streaming idea: only stars near Earth matter. Keep a candidate set holding
the k closest stars seen so far and update it as each star is read. Deciding
whether a new star belongs requires comparing it with the candidate that is
FURTHEST from Earth, so the candidates should live in a container that can
quickly report and remove its maximum and accept new members: a max-heap.

Conceptually: put the first k stars in the max-heap; for each later star, if
it is closer than the furthest candidate, remove that candidate and insert
the new star; otherwise discard the new star. The book simplifies the code:
push every star onto the max-heap, and as soon as it holds k + 1 stars, pop
the maximum.

The book's program defines a class `Star` (fields x, y, z; a `distance`
property computed with math.sqrt; `__lt__` comparing distances) and a
function `find_closest_k_stars(stars, k)`. Python's heapq only provides a
min-heap, so the book pushes tuples (-distance, star): negating the key
turns the min-heap into a max-heap by distance. This file's
`find_closest_k_stars` does NOT reproduce that program; it uses
heapq.nsmallest with a squared-distance key (see the code comparison).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    stars = [(2., 0., 0.), (0., 0., 1.), (3., 3., 0.)]
    find_closest_k_stars(stars, 2) -> [(0., 0., 1.), (2., 0., 0.)]
    (distances 1, 2 and about 4.24; the two nearest, closest first)
"""

# Python standard library: heap queue (priority queue) algorithms.
# Module documentation: https://docs.python.org/3/library/heapq.html
# nsmallest API: https://docs.python.org/3/library/heapq.html#heapq.nsmallest
import heapq


# Type hints (not enforced by Python): `stars` is a list of (x, y, z) float
# triples; `tuple[float, float, float]` describes one such 3-tuple.
def find_closest_k_stars(stars: list[tuple[float, float, float]], k: int) -> list[tuple[float, float, float]]:
    """Return up to k stars nearest origin, ordered by Euclidean distance.

    Repository implementation using heapq.nsmallest; the textbook's
    explicit max-heap program with a `Star` class is not reproduced.
    """
    if k < 0:
        raise ValueError("k must be nonnegative")
    # Comparing squared distances avoids a needless square root.
    # (Squaring is monotonic for non-negative numbers, so ordering by
    # x**2 + y**2 + z**2 gives the same order as by true distance.)

    # heapq.nsmallest(n, iterable, key=func) returns a list of the n items
    # with the smallest key values, smallest first (fewer if the input is
    # shorter; [] when n is 0). Internally it keeps a bounded heap of n
    # items while scanning the input once, roughly the same idea as the
    # book's size-k max-heap: O(len(stars) * log k) time, O(k) extra space.
    # Ties keep their input order.
    #
    # `lambda p: ...` is a small anonymous function; here it maps a star
    # tuple p to its squared distance from the origin. `**` is
    # exponentiation, and p[0], p[1], p[2] are the x, y, z coordinates.
    # Documentation: https://docs.python.org/3/library/heapq.html#heapq.nsmallest
    # Lambda expressions: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
    return heapq.nsmallest(k, stars, key=lambda p: p[0]**2 + p[1]**2 + p[2]**2)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 138)
# --------------------------------------------
# Time complexity O(n log k); space complexity O(k).
#
# VARIANTS
# Variant (stated in the book; no solution given): design an O(n log k) time
# algorithm that reads a sequence of n elements and, for each element from
# the kth one onward, prints the kth largest element read so far. The length
# of the sequence is not known in advance. The algorithm may use no more
# than O(k) additional storage. What are the worst-case inputs for the
# algorithm?


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `class Star` with `__init__(self, x, y, z)`, a `@property distance`
# returning `math.sqrt(self.x**2 + self.y**2 + self.z**2)`, and
# `__lt__(self, rhs)` comparing distances; `def find_closest_k_stars(stars,
# k)` pushes `(-star.distance, star)` onto `max_heap` for every star, pops
# when `len(max_heap) == k + 1`, and returns `[s[1] for s in
# heapq.nlargest(k, max_heap)]` (book comment: "yields the stars sorted
# according from furthest to closest"). The book's program also needs
# `import math`.
# File: no `Star` class and no `math` import; stars are plain
# `(x, y, z)` tuples; parameters typed `stars: list[tuple[float, float,
# float]], k: int`; a ValueError for negative k is added; the whole
# algorithm is the single call `heapq.nsmallest(k, stars, key=...)` using
# squared distance instead of math.sqrt, with no explicit max-heap,
# negation, or k + 1 pop. Output order: the file returns closest first.
# (For the book, nlargest over (-distance, star) tuples returns the largest
# -distance first, i.e. also closest first, despite the comment's wording;
# this is noted for review only.)


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Three stars at distances 2, 1 and sqrt(18) (about 4.24). The two
    # closest are returned, nearest first.
    # `assert` stops the program with an AssertionError if the result
    # differs; pytest provides the thorough automated verification.
    stars = [(2.,0.,0.), (0.,0.,1.), (3.,3.,0.)]
    print("closest stars:", find_closest_k_stars(stars, 2))
    assert find_closest_k_stars(stars, 2) == [(0.,0.,1.), (2.,0.,0.)]
