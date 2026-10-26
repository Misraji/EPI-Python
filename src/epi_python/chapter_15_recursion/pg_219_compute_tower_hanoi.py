"""EPI Python — Exercise 15.1: The Towers of Hanoi Problem

Chapter 15: Recursion
Textbook: pages 219–221 (printed page numbers; problem and solution start on 219, variants end on 221).

PROBLEM (from the textbook)
---------------------------
"A peg contains rings in sorted order, with the largest ring being the
lowest. You are to transfer these rings to another peg, which is initially
empty."  (Figure 15.2 shows a Tower of Hanoi with 6 rings: (a) the initial
configuration with all rings on P1, (b) the desired configuration with all
rings on P2.)

"Write a program which prints a sequence of operations that transfers n
rings from one peg to another. You have a third peg, which is initially
empty. The only operation you can perform is taking a single ring from the
top of one peg and placing it on the top of another peg. You must never
place a larger ring above a smaller ring."

HINT (from the textbook)
------------------------
"If you know how to transfer the top n - 1 rings, how does that help move
the nth ring?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The book finds the key idea by working small examples:

* Three rings: first move the top two rings onto the third peg; then move
  the bottom (largest) ring onto the second peg; finally move the two rings
  from the third peg onto the second peg, using the first peg as the
  go-between.
* Four rings: the same pattern one level up — move the top three rings to
  the third peg, move the largest ring to the second peg, then move the
  three rings from the third peg to the second peg via the first peg.

In both examples the first and last steps are themselves smaller Towers of
Hanoi problems (with different source/destination/intermediate pegs). That
self-similarity is what suggests recursion. Figure 15.3 illustrates it for
n = 6:

    (a) move all but the lowest ring from P1 to P3, using P2 as intermediary;
    (b) move the lowest ring from P1 to P2;
    (c) move the rings on P3 to P2, using P1 as intermediary;
    (d) solved.

The book's program, compute_tower_hanoi(num_rings), has a nested helper
compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg)
that does exactly these three steps when num_rings_to_move > 0. The book's
version also keeps an explicit list of pegs (each peg a list of ring sizes)
and physically moves rings between them, while appending each
[from_peg, to_peg] move to a result list. This file implements the same
recursion (see TEXTBOOK CODE COMPARISON at the end for the differences).

Peg numbering in this file: 0 = source (P1), 1 = destination (P2),
2 = spare (P3). A move (a, b) means "take the top ring of peg a and place
it on peg b".

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    n=0 -> []                                   (nothing to move)
    n=1 -> [(0, 1)]
    n=2 -> [(0, 2), (0, 1), (2, 1)]             (3 = 2^2 - 1 moves)
    n=3 -> [(0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1)]
                                                (7 = 2^3 - 1 moves)
"""


def compute_tower_hanoi(n: int) -> list[tuple[int, int]]:
    """List the (source, destination) peg moves that transfer n rings.

    This is the textbook's recursive Towers of Hanoi solution
    (compute_tower_hanoi with the nested compute_tower_hanoi_steps helper),
    written here with a nested helper named `transfer` and without the
    book's explicit peg simulation. Moves are returned in the order they
    must be performed.
    """

    # Type hints: `n: int` and `-> list[tuple[int, int]]` above, and
    # `moves: list[tuple[int, int]]` below, are annotations. They document
    # the intended types (a list of 2-tuples of ints) for readers and tools
    # such as mypy, but Python does NOT check or enforce them at run time.
    # Writing `list[...]` / `tuple[...]` directly (instead of typing.List)
    # is allowed from Python 3.9 onward.
    moves: list[tuple[int, int]] = []

    # A nested function (a function defined inside another function) can
    # read the variables of the enclosing function. Here `transfer` appends
    # to the enclosing `moves` list. Mutating the list with .append() does
    # not rebind the name `moves`, so no `nonlocal` declaration is needed.
    def transfer(count: int, source: int, target: int, spare: int) -> None:

        # Base case: moving zero rings needs no moves. (The book writes the
        # same condition the other way round: `if num_rings_to_move > 0:`.)
        if count == 0:
            return

        # Step 1: move the top count - 1 rings out of the way, from the
        # source onto the spare peg, using the target as the intermediate.
        transfer(count - 1, source, spare, target)

        # Step 2: the largest of these `count` rings is now alone on the
        # source and the target is empty (or holds only larger rings), so it
        # can be moved directly. `(source, target)` builds a 2-tuple.
        moves.append((source, target))

        # Step 3: move the count - 1 rings from the spare peg onto the
        # target, on top of the ring just moved, using the source as the
        # intermediate.
        transfer(count - 1, spare, target, source)

    # Transfer all n rings from peg 0 to peg 1 with peg 2 as the spare,
    # matching the book's call compute_tower_hanoi_steps(num_rings, 0, 1, 2).
    transfer(n, 0, 1, 2)
    return moves


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 220–221)
# -------------------------------------------------
# Let T(n) be the number of moves for n rings. The recursion gives
#
#     T(n) = T(n - 1) + 1 + T(n - 1) = 1 + 2T(n - 1).
#
# The first T(n - 1) is the transfer of the top n - 1 rings from P1 to P3;
# the "1" is moving the largest ring; the second T(n - 1) is the transfer of
# those n - 1 rings from P3 to P2.
#
# The recurrence solves to T(n) = 2^n - 1. One way to see this is to unroll
# it repeatedly: T(n) = 1 + 2 + 4 + ... + 2^k T(n - k); continuing down to
# T(0) = 0 leaves the geometric sum 1 + 2 + ... + 2^(n-1) = 2^n - 1.
#
# Each move is printed (here: recorded) in O(1) time, so the time
# complexity is O(2^n).
#
# VARIANTS (pages 220–221; each stated in the book; no solution given)
# --------------------------------------------------------------------
# 1. Solve the same problem without using recursion.
# 2. Find the minimum number of operations subject to the constraint that
#    each operation must involve P3.
# 3. Find the minimum number of operations subject to the constraint that
#    each transfer must be from P1 to P2, P2 to P3, or P3 to P1.
# 4. Find the minimum number of operations subject to the constraint that a
#    ring can never be transferred directly from P1 to P2 (transfers from
#    P2 to P1 are allowed).
# 5. Find the minimum number of operations when the stacking constraint is
#    relaxed so that only the largest ring on a peg must be the lowest ring
#    on that peg; the remaining rings on the peg may be in any order (e.g.
#    the second-largest ring may sit above the third-largest).
# 6. You have 2n disks of n different sizes, two of each size. A larger disk
#    may not go on a smaller one, but a disk may go on top of another of
#    equal size. Compute the minimum number of moves to transfer the 2n
#    disks from P1 to P2.
# 7. You have 2n disks colored black or white. A white disk may not be
#    placed directly on top of a black disk. Compute the minimum number of
#    moves to transfer the 2n disks from P1 to P2.
# 8. Find the minimum number of operations if you have a fourth peg, P4.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Names: book `def compute_tower_hanoi(num_rings)` with nested
#   `def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg,
#   use_peg)`; file `def compute_tower_hanoi(n: int)` with nested
#   `def transfer(count, source, target, spare)`. Type hints are added in
#   the file and are not in the book.
# * Book has a module-level constant `NUM_PEGS = 3`; the file has none.
# * Book builds `pegs = [list(reversed(range(1, num_rings + 1)))] +
#   [[] for _ in range(1, NUM_PEGS)]` and performs
#   `pegs[to_peg].append(pegs[from_peg].pop())` for every move, simulating
#   the rings. The file does not keep any peg state; it records moves only.
# * Book records each move as a list `[from_peg, to_peg]`; the file records
#   a tuple `(source, target)`.
# * Book guards with `if num_rings_to_move > 0:`; the file uses an early
#   `if count == 0: return`. (For a negative n the book does nothing while
#   the file would recurse without end; for n >= 0 both behave the same.)
# * Recursive structure, peg roles and the initial call (0, 1, 2) match.


# Python executes this block only when this source file is run directly
# (for example with `python -m epi_python.chapter_15_recursion.
# pg_219_compute_tower_hanoi`). When pytest imports the file, this block is
# skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Small examples, each checked against the exact expected move list:
    # 0 rings need no moves; 1 ring needs one move; 2 rings need 3 moves;
    # 3 rings need 7 moves (2^n - 1, as the textbook's analysis predicts).
    # Each move (a, b) means "top ring of peg a goes to peg b"; peg 0 is the
    # source, peg 1 the destination and peg 2 the spare.
    #
    # `assert condition` stops the program with an AssertionError if the
    # condition is false. These are quick smoke checks; the pytest suite in
    # tests/ provides the thorough automated verification.
    observed = compute_tower_hanoi(0)
    print("compute_tower_hanoi:", observed)
    assert observed == []
    observed = compute_tower_hanoi(1)
    print("compute_tower_hanoi:", observed)
    assert observed == [(0, 1)]
    observed = compute_tower_hanoi(2)
    print("compute_tower_hanoi:", observed)
    assert observed == [(0, 2), (0, 1), (2, 1)]
    observed = compute_tower_hanoi(3)
    print("compute_tower_hanoi:", observed)
    assert observed == [(0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1)]
