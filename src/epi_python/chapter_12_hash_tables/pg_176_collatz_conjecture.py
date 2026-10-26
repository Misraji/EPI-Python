"""EPI exercise 12.11, printed page 176: Test the Collatz conjecture.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Test the Collatz conjecture.
Method/complexity: Memoize already-proven trajectories; experimental verification, not a mathematical proof.
For the book's original explanation and variants, see:
    pg_176_exercise_12_11_test_the_collatz_conjecture.md

Run: python -m epi_python.chapter_12_hash_tables.pg_176_collatz_conjecture
Test: python -m pytest tests/chapter_12_hash_tables/test_pg_176_collatz_conjecture.py -v
"""

def collatz_holds_to(n: int) -> bool:
    """Verify all starts from 1..n; remember proven positive intermediate values."""
    if n < 1:
        raise ValueError("n must be positive")
    verified = {1}
    for start in range(2, n + 1):
        current = start
        path = set()
        while current not in verified:
            if current in path:
                return False
            path.add(current)
            if current & 1:
                current = 3 * current + 1
            else:
                current //= 2
        verified.update(path)
    return True


if __name__ == "__main__":
    print("Collatz validated to 1000:", collatz_holds_to(1000))
    assert collatz_holds_to(1000)
