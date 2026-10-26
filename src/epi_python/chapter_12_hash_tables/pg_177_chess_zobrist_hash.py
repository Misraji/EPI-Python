"""EPI Python — Exercise 12.12: Implement a Hash Function for Chess

Chapter 12: Hash Tables
Textbook: pages 177–179 (printed page numbers; problem on 177, Figure 12.2,
hint and solution on 178, worked 2 x 2 example and variant on 179).

PROBLEM (from the textbook)
---------------------------
"The state of a game of chess is determined by what piece is present on
each square, as illustrated in Figure 12.2 on the following page. Each
square may be empty, or have one of six classes of pieces; each piece may
be black or white. Thus ceil(log(1 + 6 x 2)) = 4 bits suffice per square,
which means that a total of 64 x 4 = 256 bits can represent the state of
the chessboard. (The actual state of the game is slightly more complex, as
it needs to capture which side is to move, castling rights, en passant,
etc., but we will use the simpler model for this question.)

Chess playing computers need to store sets of states, e.g., to determine if
a particular state has been evaluated before, or is known to be a winning
state. To reduce storage, it is natural to apply a hash function to the 256
bits of state, and ignore collisions. The hash code can be computed by a
conventional hash function for strings. However, since the computer
repeatedly explores nearby states, it is advantageous to consider hash
functions that can be efficiently computed based on incremental changes to
the board.

Design a hash function for chess game states. Your function should take a
state and the hash code for that state, and a move, and efficiently compute
the hash code for the updated state."

    (Figure 12.2: Chessboard corresponding to the fastest checkmate, Fool's
    Mate -- the position after 1. f3, e5 2. g4, Qh4. The diagram itself is
    an image and is not reproduced here.)

HINT (from the textbook)
------------------------
"XOR is associative, commutative, and fast to compute. Additionally,
a XOR a = 0."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
A straightforward hash: treat the board as 64 base-13 digits, one per
square (squares numbered 0 to 63). Each digit encodes the square's state:
blank, white pawn, white rook, ..., white king, black pawn, ..., black
king. The hash is sum over i = 0..63 of c_i * p^i, where c_i is the digit
for square i and p is a prime (the book refers to page 159 for details).

This hash can be updated incrementally to some extent. For example, if a
black knight is captured by a white bishop, the new code is obtained by
subtracting the terms for the knight's and bishop's original squares, then
adding a term for a blank at the bishop's original square and a term for
the bishop at the knight's square.

A hash that is much faster to update (Zobrist hashing): create a random
64-bit integer code for each of the 13 states each of the 64 squares can be
in -- 13 x 64 = 832 random constants. The board's hash code is the XOR of
the codes for the state of every square. Updates are very fast: for the
capture above, XOR in the codes for black knight on i1, white bishop on i2,
white bishop on i1, and blank on i2. (XOR-ing a code a second time removes
it, because a XOR a = 0.)

Incremental updates of the first hash need terms such as p^i, which are
more expensive than an XOR, so the second hash is preferred. At most 4
word-level XORs are needed per move -- for a capture or a castling.

Book's worked example: a simpler game on a 2 x 2 board with at most two
pieces, P and Q, and at most one piece per position. The positions are
(0,0), (0,1), (1,0), (1,1), with these random 7-bit codes:
    (0,0): blank 1100111, P 1011000, Q 1100010
    (0,1): blank 1111100, P 1000001, Q 0001111
    (1,0): blank 1100101, P 1101101, Q 0011101
    (1,1): blank 0100001, P 0101100, Q 1001011
State with P at (0,0), Q at (1,1) and the other positions blank:
    1011000 XOR 1111100 XOR 1100101 XOR 1001011 = 0001010.
If Q moves to (0,1), XOR the current code with 1001011 (removes Q from
(1,1)), 0100001 (adds blank at (1,1)), 1111100 (removes blank from (0,1)),
and 0001111 (adds Q at (0,1)). Whatever the board size and number of
pieces, this takes four XORs.

The book prints NO Python program for this exercise. The ChessHash class
below is this repository's own Zobrist-hash implementation of the idea
(with no codes for blank squares; see the comparison section).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
On a 2 x 2 board with "K" at (0,0) and "k" at (1,1): removing "K" with
update(initial, 0, 0, "K", None) gives the same hash as hashing the board
[[None, None], [None, "k"]] from scratch.
"""

# Python standard library: pseudo-random number generators.
# Module documentation: https://docs.python.org/3/library/random.html
# random.Random: https://docs.python.org/3/library/random.html#random.Random
# Random.getrandbits: https://docs.python.org/3/library/random.html#random.getrandbits
import random


class ChessHash:
    """Zobrist hash for chess-board piece positions, supporting constant-time updates.

    Repository implementation of the textbook's XOR (Zobrist) hashing idea;
    the textbook gives no code for this exercise.
    """

    # A class attribute (shared by all instances): the 12 piece symbols,
    # using the common convention of uppercase for white and lowercase for
    # black (P pawn, N knight, B bishop, R rook, Q queen, K king). This is a
    # tuple, an immutable sequence.
    PIECES = ("P","N","B","R","Q","K","p","n","b","r","q","k")

    # Constructor. `side: int = 8` and `seed: int = 7` are parameters with
    # default values (a standard 8 x 8 board, and a fixed seed). Type hints
    # are not enforced by Python.
    def __init__(self, side: int = 8, seed: int = 7):

        # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
        if side <= 0:
            raise ValueError("Board side must be positive")
        self.side = side

        # random.Random(seed) creates an independent pseudo-random generator.
        # Seeding it makes the "random" codes identical on every run, so the
        # same board always hashes to the same value across program runs.
        rng = random.Random(seed)

        # A dict comprehension with three nested `for` clauses (rows, then
        # columns, then pieces) builds one entry per (row, col, piece)
        # triple -- 8 * 8 * 12 = 768 for a standard board. The tuple key
        # works because tuples of ints and strings are hashable.
        #
        # rng.getrandbits(64) returns a random nonnegative int with 64
        # random bits: the per-square, per-piece code from the book. Blank
        # squares get no code; they simply contribute nothing to the XOR.
        self.table = {(row,col,piece): rng.getrandbits(64)
                      for row in range(side) for col in range(side)
                      for piece in self.PIECES}

    def hash_board(self, board: list[list[str | None]]) -> int:
        """Hash a whole board from scratch by XOR-ing every occupied square's code.

        `list[list[str | None]]` means a list of rows, each holding piece
        strings or None for an empty square.
        """

        # any() is True if some row has the wrong length; it stops at the
        # first such row. The `or` checks the row count first.
        # any: https://docs.python.org/3/library/functions.html#any
        if len(board) != self.side or any(len(row) != self.side for row in board):
            raise ValueError("Unexpected board dimensions")
        result = 0
        for row in range(self.side):
            for col in range(self.side):
                piece = board[row][col]
                if piece is not None:

                    # `^=` XORs the square's code into the running hash.
                    # XOR is associative and commutative, so the order of
                    # squares does not matter (the hint).
                    result ^= self.table[(row,col,piece)]
        return result

    def update(self, old_hash: int, row: int, col: int, old: str | None, new: str | None) -> int:
        """Return the hash after one square changes from `old` to `new`.

        A move is two such updates (the source square becomes None and the
        target square gets the piece; a capture also replaces the target's
        old piece), so each update is O(1).
        """

        # XOR-ing the old piece's code again removes it, since a ^ a == 0.
        # The parameter `old_hash` is just a local int here; rebinding it
        # does not affect the caller's variable.
        if old is not None:
            old_hash ^= self.table[(row,col,old)]

        # XOR-ing the new piece's code adds it.
        if new is not None:
            old_hash ^= self.table[(row,col,new)]
        return old_hash


def chess_board_hash(board: list[list[str | None]]) -> int:
    """Hash a square board with a fresh ChessHash sized to it (default seed).

    Convenience helper added in this repository; not in the textbook.
    """
    return ChessHash(len(board)).hash_board(board)


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 178–179)
# -------------------------------------------------
# The book's discussion after its worked example is that, regardless of
# board size and number of pieces, a move needs only four XORs to update the
# hash (at most 4 word-level XORs for a capture or castling in chess). The
# initial hash of a whole board touches every square once. No other
# complexity analysis is given.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): How can you include
#   castling rights and en passant information in the state?


# TEXTBOOK CODE COMPARISON
# ------------------------
# The book prints no program for this exercise, so all code here is the
# repository's own: class `ChessHash` (with `hash_board` and `update`) and
# helper `chess_board_hash`. Differences from the book's described scheme:
# the book assigns a random code to each of 13 states per square
# (including "blank"), so moving a piece XORs out/in blank codes too; this
# file has codes only for the 12 pieces and treats blank as contributing 0,
# so `update` performs at most two XORs per square change. The board size
# is configurable (`side`), codes are 64-bit from a seeded random.Random,
# and pieces are identified by single-letter symbols.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # A 2 x 2 board (as in the book's small example) with a white king at
    # (0,0) and a black king at (1,1). Removing the white king incrementally
    # with update() must give the same hash as hashing the resulting board
    # from scratch -- the key property of an incremental hash.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, while pytest provides the more
    # thorough automated verification.
    hasher=ChessHash(2)
    board=[["K",None],[None,"k"]]
    initial=hasher.hash_board(board)
    print("chess Zobrist hash:", initial)
    assert hasher.update(initial,0,0,"K",None) == hasher.hash_board([[None,None],[None,"k"]])
