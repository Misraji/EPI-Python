"""EPI Python — Exercise 13.9: Team Photo Day—1

Chapter 13: Sorting
Textbook: pages 193–194 (printed page numbers; problem and solution start on 193).

PROBLEM (from the textbook)
---------------------------
"You are a photographer for a soccer meet. You will be taking pictures of
pairs of opposing teams. All teams have the same number of players. A team
photo consists of a front row of players and a back row of players. A player
in the back row must be taller than the player in front of him, as
illustrated in Figure 13.3. All players in a row must be from the same
team."

Figure 13.3: "A team photo. Each team has 11 players, and each player in the
back row is taller than the corresponding player in the front row."

"Design an algorithm that takes as input two teams and the heights of the
players in the teams and checks if it is possible to place players to take
the photo subject to the placement constraint."

HINT (from the textbook)
------------------------
"First try some concrete inputs, then make a general conclusion."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: try every permutation of one team and compare it element by
element with the other team. With n players per team, enumerating
permutations costs O(n!) and checking each one costs O(n), so O(n! x n):
clearly unacceptable.

Insight: focus on the players that are hardest to place. To put Team A
behind Team B: if A's tallest player is not taller than B's tallest player,
the constraint cannot be satisfied. If A's tallest IS taller, he should
stand behind B's tallest, because B's tallest is the hardest to place.
Repeating the argument for the remaining players, A's second tallest must be
taller than B's second tallest, and so on.

So sort both teams' heights and compare them position by position: A's
tallest with B's tallest, second tallest with second tallest, etc.
Figure 13.4 ("The teams from Figure 13.3 in sorted order") shows the sorted
rows. The book's program tests whether a given team can be placed in front
of another team.

The function below implements this sorted pairwise comparison (it also
tries the opposite orientation; see the code comparison).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    team_a=[1,4,3], team_b=[2,6,5] -> True  (sorted 1<2, 3<5, 4<6)
"""


# Type hints: two lists of integer heights in, a bool out. Python does not
# enforce annotations at run time.
def valid_placement_exists(team_a: list[int], team_b: list[int]) -> bool:
    """Return whether one team can stand strictly behind the other at all positions.

    This is the textbook's sorted-comparison implementation, applied in both
    orientations (team_a in front, or team_b in front).
    """

    # Added check (not in the book, which assumes equal team sizes):
    # different sizes cannot be paired one-to-one.
    if len(team_a) != len(team_b):
        return False

    # sorted() returns NEW ascending lists; the caller's lists are unchanged.
    # Tuple unpacking assigns both results in one statement.
    # Documentation: https://docs.python.org/3/library/functions.html#sorted
    a, b = sorted(team_a), sorted(team_b)

    # zip(a, b) pairs the i-th shortest of each team: (a[0], b[0]),
    # (a[1], b[1]), ... (it stops at the shorter input; equal lengths here).
    # `x < y for x, y in zip(a, b)` is a generator expression producing one
    # boolean per pair, lazily.
    # all(iterable) returns True if every item is true (and True for an
    # empty iterable); it stops at the first False.
    # The first all(...) tests team_a in front of team_b (each a strictly
    # shorter); the second tests the reverse. `or` evaluates the second only
    # if the first is False.
    # Documentation: https://docs.python.org/3/library/functions.html#zip
    # Documentation: https://docs.python.org/3/library/functions.html#all
    return all(x < y for x, y in zip(a,b)) or all(y < x for x, y in zip(a,b))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 194)
# --------------------------------------------
# The time complexity is that of sorting, i.e. O(n log n).
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `class Team` with a nested `Player = collections.namedtuple(
#   'Player', ('height'))`, `__init__(self, height)` storing
#   `self._players = [Team.Player(h) for h in height]`, and a
#   `@staticmethod valid_placement_exists(A, B)` (book comment "Checks if A
#   can be placed in front of B.") returning
#   `all(a < b for a, b in zip(sorted(A._players), sorted(B._players)))`.
# - File: no Team class or Player namedtuple; a module-level function
#   `valid_placement_exists(team_a: list[int], team_b: list[int]) -> bool`
#   taking plain height lists. It adds an unequal-length check, stores the
#   sorted lists in `a`, `b`, and returns True if EITHER orientation works
#   (the book's method checks only "A in front of B").


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # An added example (not from the book): sorted, team a is [1,3,4] and
    # team b is [2,5,6], so a can stand in front of b.
    a=[1,4,3]
    b=[2,6,5]
    print('Can photograph:', valid_placement_exists(a,b))

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert valid_placement_exists(a,b)
