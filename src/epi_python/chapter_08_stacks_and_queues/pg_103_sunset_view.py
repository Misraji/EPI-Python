"""EPI Python — Exercise 8.5: Compute Buildings with a Sunset View

Chapter 8: Stacks and Queues
Textbook: pages 103–104 (printed page numbers; the problem starts at the
bottom of page 103, the solution, program and variant are on page 104).

PROBLEM (from the textbook)
---------------------------
"You are given a series of buildings that have windows facing west. The
buildings are in a straight line, and any building which is to the east of a
building of equal or greater height cannot view the sunset.

Design an algorithm that processes buildings in east-to-west order and
returns the set of buildings which view the sunset. Each building is
specified by its height."

HINT (from the textbook)
------------------------
"When does a building not have a sunset view?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: keep every building in an array, then scan the array in
reverse while tracking the largest height seen so far (the running maximum).
A building whose height is at most the running maximum has its view blocked.
Both time and space are O(n), where n is the number of buildings.

Reducing space: a building lying east of a taller building can never see
the sunset. So keep only the buildings that might still have a view; each
new (more westerly) building can block some of them, found by comparing
heights. Keeping that set in a hash set would mean checking every member
each time a building arrives.

Better: if the new building is shorter than some building in the set, it
cannot block any building further east than that one. This suggests keeping
the candidates in last-in, first-out order so the comparison can stop early.

Algorithm: keep a stack of the buildings that currently have a view. When a
building b arrives, while the stack top is not taller than b (the book's
program uses height >= top's height), pop it: every popped building lies
east of a building at least as tall. Then push b.

Even though a single step may pop many buildings, each building is pushed
once and popped at most once, so processing n buildings takes O(n) time, and
the stack always holds exactly the buildings that currently have a view.

The memory is O(n), and this bound is tight even when only one building ends
up with a view: take a west-most building that is the tallest, with the other
n - 1 buildings decreasing in height from east to west (all of them stay on
the stack until the last building arrives). In the best case, e.g. when
buildings arrive in increasing height, only O(1) space is used. The
brute-force approach, by contrast, always uses O(n) space.

The book's program is `examine_buildings_with_sunset(sequence)`. NOTE: this
file's function of the same name does NOT implement the book's stack
program; it implements the reverse scan with a running maximum (the book's
brute-force idea) over a list. See the code comparison at the end.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    examine_buildings_with_sunset([3, 7, 8, 3, 6, 1]) -> [2, 4, 5]
    (indices whose height is greater than every height after them)
"""


def examine_buildings_with_sunset(heights: list[int]) -> list[int]:
    """Return west-to-east indices of buildings visible toward the east.

    Repository implementation using a reverse scan with a running maximum
    (the textbook's brute-force idea), not the textbook's stack program.
    """

    # A building is visible exactly when every building to its right is shorter.
    visible = []

    # float('-inf') is negative infinity: a float smaller than every number,
    # so the first comparison `heights[i] > highest_to_east` is always True.
    # Documentation: https://docs.python.org/3/library/functions.html#float
    highest_to_east = float('-inf')

    # range(start, stop, step) with step -1 counts DOWN from len-1 to 0
    # (stop -1 is excluded), so the list is scanned from right to left.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#range
    for i in range(len(heights) - 1, -1, -1):

        # Strictly greater: a building of equal height to its right blocks
        # it, matching the book's "equal or greater height" rule.
        if heights[i] > highest_to_east:
            visible.append(i)
            highest_to_east = heights[i]

    # The slice [::-1] (start and stop omitted, step -1) makes a reversed
    # copy of the list, turning right-to-left discovery order into
    # increasing index order.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
    return visible[::-1]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 104)
# --------------------------------------------
# The complexity discussion for the stack algorithm (O(n) time; O(n) space,
# tight even with one visible building; O(1) best case; brute force always
# O(n) space) appears before the program in the book and is summarised in
# the module docstring above. Nothing further follows the program except
# the variant.
#
# VARIANTS
# Variant (stated in the book; no solution given): solve the problem subject
# to the same constraints when the buildings are presented in west-to-east
# order.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def examine_buildings_with_sunset(sequence)` builds a namedtuple
# type `BuildingWithHeight('id', 'height')` (from `collections`), keeps a
# stack `candidates`, iterates with `enumerate(sequence)` in arrival
# (east-to-west) order, pops while `building_height >=
# candidates[-1].height`, pushes the new building, and returns
# `[candidate.id for candidate in reversed(candidates)]`. It works on a
# stream (any iterable) and uses O(1) space in the best case.
# File: parameter `heights: list[int]` with `-> list[int]`; no stack, no
# namedtuple, no `collections` import. It scans the list from the last
# index to the first with a running maximum (`highest_to_east`) and
# reverses the result with `[::-1]`. This is the book's brute-force
# approach, so it requires the whole list (random access, len) and always
# needs the full input in memory; the book's stack program is missing.
# Docstring/direction: the file describes indices as "west-to-east" with
# visibility "toward the east", whereas the book's input is east-to-west
# with the sunset to the west. Both treat building i as visible when every
# building after it in the sequence is strictly shorter, so they select the
# same set of indices, but the order differs: for [3, 7, 8, 3, 6, 1] the
# book's program returns [5, 4, 2] (reversed stack) and the file returns
# [2, 4, 5].


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Index 2 (height 8) is taller than everything after it; index 4
    # (height 6) beats the final 1; index 5 is last, so nothing follows it.
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, pytest does the thorough testing.
    print("sunset-visible indices:", examine_buildings_with_sunset([3,7,8,3,6,1]))
    assert examine_buildings_with_sunset([3,7,8,3,6,1]) == [2,4,5]
