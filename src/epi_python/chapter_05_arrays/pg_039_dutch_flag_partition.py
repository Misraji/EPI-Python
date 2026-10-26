"""EPI exercise 5.1, printed page 39: The Dutch national flag problem.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: The Dutch national flag problem.
Method/complexity: Dutch three-way partition; O(n) time, O(1) extra space.
For the book's original explanation and variants, see:
    pg_039_exercise_05_01_the_dutch_national_flag_problem.md

Run: python -m epi_python.chapter_05_arrays.pg_039_dutch_flag_partition
Test: python -m pytest tests/chapter_05_arrays/test_pg_039_dutch_flag_partition.py -v
"""

def dutch_flag_partition(pivot_index: int, values: list[int]) -> list[int]:
    """Partition in place into < pivot, == pivot, > pivot."""
    if not 0 <= pivot_index < len(values):
        raise IndexError("Invalid pivot index")
    pivot = values[pivot_index]
    smaller, equal, larger = 0, 0, len(values)
    while equal < larger:
        if values[equal] < pivot:
            values[smaller], values[equal] = values[equal], values[smaller]
            smaller += 1
            equal += 1
        elif values[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            values[equal], values[larger] = values[larger], values[equal]
    return values


if __name__ == "__main__":
    values = [3, 1, 2, 1, 3]
    print("partition:", dutch_flag_partition(1, values))
    assert values[:2] == [1, 1]
