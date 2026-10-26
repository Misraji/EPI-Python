"""Independent tests for EPI 12.12.

pytest parameterization: https://docs.pytest.org/en/stable/how-to/parametrize.html
"""

# pytest enables one test function to run over several examples.
# Documentation: https://docs.pytest.org/en/stable/
import pytest

# Standard library: copies mutable inputs so tests do not share state.
# Documentation: https://docs.python.org/3/library/copy.html
import copy

from epi_python.chapter_12_hash_tables.pg_177_chess_zobrist_hash import chess_board_hash

@pytest.mark.parametrize(("args", "expected"), [
    (([[None]],), 0),
])
def test_examples(args, expected):
    """Verify representative and boundary conditions independently."""
    assert chess_board_hash(*copy.deepcopy(args)) == expected

from epi_python.chapter_12_hash_tables.pg_177_chess_zobrist_hash import ChessHash


def test_incremental_hash_matches_full_recompute():
    hasher=ChessHash(3)
    before=[[None,"p",None],[None,None,None],[None,None,"K"]]
    initial=hasher.hash_board(before)
    after=[[None,None,None],[None,"p",None],[None,None,"K"]]
    updated=hasher.update(hasher.update(initial,0,1,"p",None),1,1,None,"p")
    assert updated == hasher.hash_board(after)
