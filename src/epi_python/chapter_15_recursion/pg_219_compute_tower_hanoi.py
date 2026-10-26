"""EPI 15.1: The Towers of Hanoi problem (printed page 219).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: The Towers of Hanoi problem
Method: Recursively move n-1 disks out of the way, move the base disk, then restore them on the destination.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_219_exercise_15_01_the_towers_of_hanoi_problem.md

Run independently:
    python -m epi_python.chapter_15_recursion.pg_219_compute_tower_hanoi
Run thorough tests:
    python -m pytest tests/chapter_15_recursion/test_pg_219_compute_tower_hanoi.py -v
"""

def compute_tower_hanoi(n: int) -> list[tuple[int, int]]:
    """List the source/destination peg moves for n Hanoi disks."""
    moves: list[tuple[int, int]] = []

    def transfer(count: int, source: int, target: int, spare: int) -> None:
        if count == 0:
            return
        transfer(count - 1, source, spare, target)
        moves.append((source, target))
        transfer(count - 1, spare, target, source)

    transfer(n, 0, 1, 2)
    return moves


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
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
