"""EPI Python — Exercise 24.27: Measure with Defective Jugs

Chapter 24: Honors Class
Textbook: pages 388–389 (printed page numbers; problem starts on 388,
solution on 389).

PROBLEM (from the textbook)
---------------------------
"You have three measuring jugs, A, B, and C. The measuring marks have worn
out, making it impossible to measure exact volumes. Specifically, each time
you measure with A, all you can be sure of is that you have a volume that is
in the range [230,240] mL. (The next time you use A, you may get a different
volume—all that you know with certainty is that the quantity will be in
[230,240] mL.) Jugs B and C can be used to measure a volume in [290,310] mL
and in [500,515] mL, respectively. Your recipe for chocolate chip cookies
calls for at least 2100 mL and no more than 2300 mL of milk.

Write a program that determines if there exists a sequence of steps by which
the required amount of milk can be obtained using the worn-out jugs. The
milk is being added to a large mixing bowl, and hence cannot be removed from
the bowl. Furthermore, it is not possible to pour one jug's contents into
another. Your scheme should always work, i.e., return between 2100 and 2300
mL of milk, independent of how much is chosen in each individual step, as
long as that quantity satisfies the given constraints."

HINT (from the textbook)
------------------------
"Solve the n jugs case."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Recursion fits naturally. Suppose jug A is used for the last step. Its pour
may be as little as 230 mL, so beforehand we must have reliably measured at
least 2100 - 230 = 1870 mL (less than that risks ending too low). It may be
as much as 240 mL, so beforehand we must have at most 2300 - 240 = 2060 mL.
In general, the target range [L, H] is achievable using jug [low, high] as
the last step if [L - low, H - high] is achievable (or if the jug alone
lands inside [L, H]). The range is unachievable if no jug works as the last
step. Intermediate results are cached to cut down the number of recursive
calls.

The book implements a general function for n jugs; check_feasible below
follows it, with the cache made local to each top-level call.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
None beyond the book's instance: jugs [230,240], [290,310], [500,515] and
target [2100, 2300] -> feasible (used in the __main__ block).
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# namedtuple API: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


# collections.namedtuple creates a tuple subclass with named fields. A Jug
# records the guaranteed range [low, high] that one use of the jug pours.
# Named tuples are immutable and hashable. Matches the book's definition.
Jug=namedtuple('Jug',('low','high'))

# A VolumeRange is a target interval [low, high] still to be measured.
# Because named tuples are hashable, VolumeRange values can be stored in a
# set, which is how failed subproblems are cached. (The book defines this
# type inside its function.)
VolumeRange=namedtuple('VolumeRange',('low','high'))


# Type hints: `jugs: list[Jug]`, integer bounds, `-> bool`. Annotations are
# documentation only; Python does not enforce them.
def check_feasible(jugs: list[Jug],lower: int,upper: int) -> bool:
    """Return True if some sequence of jug uses always lands in [lower, upper].

    This is the textbook's general n-jug recursive solution with a cache
    of impossible ranges; here the cache is created fresh for each call.
    """

    # Annotated empty set: `set[VolumeRange]` documents the element type.
    # It records ranges already shown to be impossible.
    visited: set[VolumeRange]=set()

    # helper(l, h): can the range [l, h] be measured reliably?
    def helper(l,h):
        state=VolumeRange(l,h)

        # Failure cases: an empty interval (l > h); a range already known to
        # be impossible (`in` on a set is an average O(1) hash lookup); or a
        # range entirely below zero (no volume can be negative). Note that
        # l < 0 with h >= 0 is still allowed: then "nothing more" is fine at
        # the low end.
        if l>h or state in visited or (l<0 and h<0):return False

        # Checks the volume for each jug to see if it is possible (book's
        # comment): either this jug alone always lands in [l, h], or using it
        # last leaves the subproblem [l - low, h - high].
        for jug in jugs:
            if l<=jug.low and jug.high<=h:
                return True
            if helper(l-jug.low,h-jug.high):
                return True

        # Marks this range as impossible (book's comment). set.add inserts
        # an element. Docs: https://docs.python.org/3/library/stdtypes.html#frozenset.add
        visited.add(state)
        return False
    return helper(lower,upper)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 389)
# --------------------------------------------
# Time: O((L + 1)(H + 1)n). Apart from its recursive calls, each call does
# O(n) work (one test per jug), and thanks to the cache there are at most
# (L + 1)(H + 1) distinct calls (the book names the recursive function
# "CheckFeasibleHelper" in this paragraph). Space: O((L + 1)(H + 1)), the
# upper bound on the cache size.
#
# The problem can also be formulated as an Integer Linear Program (ILP), but
# interviewers usually will not accept a reduction to ILP, since it shows no
# programming skill.
#
# VARIANTS
# --------
# * Suppose jug i can be used to measure any quantity in [l_i, u_i] exactly.
#   Determine if it is possible to measure a quantity of milk between L and
#   U. (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Signature: book `def check_feasible(jugs, L, H, c=set())`, recursing on
#   itself with a mutable default-argument cache `c` that persists across
#   top-level calls; file `check_feasible(jugs: list[Jug], lower: int,
#   upper: int) -> bool` with a fresh `visited` set per call and a nested
#   `helper(l, h)` that does the recursion.
# * VolumeRange: book defines it inside the function on every call; file
#   defines it once at module level (and imports `namedtuple` directly
#   instead of using `collections.namedtuple`).
# * Loop: book uses one `any((L <= j.low and j.high <= H) or
#   check_feasible(jugs, L - j.low, H - j.high) for j in jugs)`; file uses
#   an explicit `for` loop with two `if ... return True` tests. Same logic.
# * The failure test and `c.add(...)` / `visited.add(...)` match.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # The book's instance: jugs A, B, C and a 2100..2300 mL target.
    choices=[Jug(230,240),Jug(290,310),Jug(500,515)]
    print('Feasible 2100..2300:',check_feasible(choices,2100,2300))

    # `assert` stops with an AssertionError if the condition is false; a
    # quick smoke check. pytest provides the more thorough verification.
    assert check_feasible(choices,2100,2300)
