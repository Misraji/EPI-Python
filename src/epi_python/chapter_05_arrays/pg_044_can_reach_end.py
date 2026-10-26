"""EPI Python — Exercise 5.4: Advancing Through an Array

Chapter 5: Arrays
Textbook: pages 44–45 (printed page numbers; the game is described on page
44, and the problem, solution and variant are on page 45).

PROBLEM (from the textbook)
---------------------------
Context: In a board game, each position holds a nonnegative integer giving
the maximum distance you can advance from it in one move. You start at the
first position and win by reaching the last one. The book's example:
A = <3,3,1,0,2,0,1> can be won by taking 1 step from A[0] to A[1], then 3
steps from A[1] to A[4], then 2 steps from A[4] to A[6], the last position
(each move is valid because A[0] = 3 >= 1, A[1] = 3 >= 3, A[4] = 2 >= 2).
If instead A = <3,2,0,0,2,0,1>, it is impossible to advance past position
3, so the game cannot be won.

"Write a program which takes an array of n integers, where A[i] denotes
the maximum you can advance from index i, and returns whether it is
possible to advance to the last index starting from the beginning of the
array."

HINT (from the textbook)
------------------------
"Analyze each location, starting from the beginning."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
A tempting idea is to jump as far as possible on every move. That fails
because it can jump over an index holding a large value. Book example:
for A = <2,4,1,1,0,2,3>, the greedy jump goes to index 2 (value 1), then
to index 3, and then it is stuck. Going to index 1 instead (value 4)
reaches index 5, and from there index 6 is reachable.

That suggests looking at every entry in turn while tracking the furthest
index proven reachable so far. From index i the furthest point is
i + A[i]. If, before the end of the array, we arrive at an index i that is
itself the furthest proven reachable index (and we cannot get past it),
the last index is unreachable; otherwise we reach the end.

Book examples:
  - A = <3,3,1,0,2,0,1>: the furthest reachable index evolves as
    0, 3, 4, 4, 4, 6, 6, 7, which reaches the last index, 6.
  - A = <3,2,0,0,2,0,1>: it evolves as 0, 3, 3, 3, 3, and then no further
    progress is possible, so the last index cannot be reached.

The book notes that the program is robust to negative entries, because it
keeps the maximum of the previously proven reach and i + A[i].

The book prints one program, implemented here as `can_reach_end`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [0] -> True   (already at the last index)
    []  -> True   (this file's convention for an empty board)
"""


# `max_steps: list[int]` and `-> bool` are type hints documenting the
# expected argument and return types. Python does not enforce them at run
# time. `list[int]` requires Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def can_reach_end(max_steps: list[int]) -> bool:
    """Textbook `can_reach_end(A)`, written with a `for` loop.

    Invariant: every index from 0 up through `farthest` is reachable.
    """
    farthest = 0
    last = len(max_steps) - 1

    # `enumerate(sequence)` yields (index, value) pairs: (0, A[0]),
    # (1, A[1]), ... so the loop gets both i and A[i] without indexing.
    # Documentation: https://docs.python.org/3/library/functions.html#enumerate
    for index, steps in enumerate(max_steps):

        # If this index lies beyond everything proven reachable, no path
        # gets here (or anywhere later), so stop scanning.
        if index > farthest:
            break

        # `max()` keeps the previously proved frontier if this index cannot
        # advance as far. This is also what makes negative entries
        # harmless, as the book points out.
        # Documentation: https://docs.python.org/3/library/functions.html#max
        farthest = max(farthest, index + steps)

        # Early exit as soon as the last index is proven reachable.
        if farthest >= last:
            return True

    # Reached only if the scan stopped short of the last index, or if the
    # list was empty (then last == -1 and the result is True).
    return last < 0


# TEXTBOOK POST-SOLUTION DISCUSSION (page 45)
# ------------------------------------------
# The time complexity is O(n). Beyond the input array, the program keeps
# only three integer variables, so the additional space is O(1).
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Write a program to
# compute the minimum number of steps needed to advance to the last
# location.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def can_reach_end(A)`; file: parameter renamed `max_steps`,
#   type hints added.
# - Book variables `furthest_reach_so_far`, `last_index`, `i`; file:
#   `farthest`, `last`, `index`.
# - Book uses a `while i <= furthest_reach_so_far and
#   furthest_reach_so_far < last_index:` loop with `i += 1`, then
#   `return furthest_reach_so_far >= last_index`. File restructures this
#   as a `for ... in enumerate(...)` loop with `break` when the index
#   passes the frontier, an early `return True`, and a final
#   `return last < 0` (which handles the empty list the same way the
#   book's final comparison would: True).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (board, expected answer). The first two boards are
    # the book's winnable and unwinnable examples; [0] and [] are added
    # boundary cases.
    for steps,expected in (([3,3,1,0,2,0,1],True),
                           ([3,2,0,0,2,0,1],False),([0],True),([],True)):
        result = can_reach_end(steps)

        # An f-string (prefix f) evaluates each {expression} and inserts
        # its text into the string.
        # Documentation: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
        print(f"reachable({steps}) = {result}")

        # `assert` stops the program with an AssertionError if the result
        # differs from the expectation. `is` compares identity; True and
        # False are single objects, so `is` checks for the exact bool.
        # pytest provides the more thorough automated verification.
        assert result is expected
