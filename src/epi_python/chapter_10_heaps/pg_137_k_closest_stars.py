"""EPI exercise 10.4, printed page 137: Compute the k closest stars.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Compute the k closest stars.
Method/complexity: Keep k entries in heap; O(n log k) time, O(k) auxiliary space.
For the book's original explanation and variants, see:
    pg_137_exercise_10_04_compute_the_k_closest_stars.md

Run: python -m epi_python.chapter_10_heaps.pg_137_k_closest_stars
Test: python -m pytest tests/chapter_10_heaps/test_pg_137_k_closest_stars.py -v
"""

# heapq.nsmallest iterates over arbitrary data with a bounded heap.
# Documentation: https://docs.python.org/3/library/heapq.html#heapq.nsmallest
import heapq


def find_closest_k_stars(stars: list[tuple[float, float, float]], k: int) -> list[tuple[float, float, float]]:
    """Return up to k stars nearest origin, ordered by Euclidean distance."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    # Comparing squared distances avoids a needless square root.
    return heapq.nsmallest(k, stars, key=lambda p: p[0]**2 + p[1]**2 + p[2]**2)


if __name__ == "__main__":
    stars = [(2.,0.,0.), (0.,0.,1.), (3.,3.,0.)]
    print("closest stars:", find_closest_k_stars(stars, 2))
    assert find_closest_k_stars(stars, 2) == [(0.,0.,1.), (2.,0.,0.)]
