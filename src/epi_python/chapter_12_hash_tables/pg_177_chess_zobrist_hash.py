"""EPI exercise 12.12, printed page 177: Implement a hash function for chess.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Implement a hash function for chess.
Method/complexity: Random lookup XOR per occupied square; O(board_squares) full hash, O(1) single-square update.
For the book's original explanation and variants, see:
    pg_177_exercise_12_12_implement_a_hash_function_for_chess.md

Run: python -m epi_python.chapter_12_hash_tables.pg_177_chess_zobrist_hash
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_177_chess_zobrist_hash.py -v
"""

# Random generates stable pseudorandom table keys when seeded reproducibly.
# Documentation: https://docs.python.org/3/library/random.html#random.Random
import random


class ChessHash:
    """Zobrist hash for chess-board piece positions, supporting constant-time updates."""
    PIECES = ("P","N","B","R","Q","K","p","n","b","r","q","k")

    def __init__(self, side: int = 8, seed: int = 7):
        if side <= 0:
            raise ValueError("Board side must be positive")
        self.side = side
        rng = random.Random(seed)
        self.table = {(row,col,piece): rng.getrandbits(64)
                      for row in range(side) for col in range(side)
                      for piece in self.PIECES}

    def hash_board(self, board: list[list[str | None]]) -> int:
        if len(board) != self.side or any(len(row) != self.side for row in board):
            raise ValueError("Unexpected board dimensions")
        result = 0
        for row in range(self.side):
            for col in range(self.side):
                piece = board[row][col]
                if piece is not None:
                    result ^= self.table[(row,col,piece)]
        return result

    def update(self, old_hash: int, row: int, col: int, old: str | None, new: str | None) -> int:
        if old is not None:
            old_hash ^= self.table[(row,col,old)]
        if new is not None:
            old_hash ^= self.table[(row,col,new)]
        return old_hash


def chess_board_hash(board: list[list[str | None]]) -> int:
    return ChessHash(len(board)).hash_board(board)


if __name__ == "__main__":
    hasher=ChessHash(2)
    board=[["K",None],[None,"k"]]
    initial=hasher.hash_board(board)
    print("chess Zobrist hash:", initial)
    assert hasher.update(initial,0,0,"K",None) == hasher.hash_board([[None,None],[None,"k"]])
