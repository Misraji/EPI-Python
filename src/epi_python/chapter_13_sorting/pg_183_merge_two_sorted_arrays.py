"""EPI Python — Exercise 13.2: Merge Two Sorted Arrays

Chapter 13: Sorting
Textbook: pages 183–184 (printed page numbers; problem and solution start on 183).

PROBLEM (from the textbook)
---------------------------
"Suppose you are given two sorted arrays of integers. If one array has
enough empty entries at its end, it can be used to store the combined
entries of the two arrays in sorted order. For example, consider
<5,13,17,_,_,_,_,_> and <3,7,11,19>, where _ denotes an empty entry. Then
the combined sorted entries can be stored in the first array as
<3,5,7,11,13,17,19,_>."

"Write a program which takes as input two sorted arrays of integers, and
updates the first to the combined entries of the two arrays in sorted
order. Assume the first array has enough empty entries at its end to hold
the result."

HINT (from the textbook)
------------------------
"Avoid repeatedly moving entries."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
The difficulty is writing the result back into the FIRST array. With a
separate third array, one could walk both inputs in tandem and always copy
the smaller current entry into the output: O(m + n) time, where m and n are
the numbers of entries initially in the first and second arrays.

Doing the same forward merge inside the first array does not keep O(m + n):
whenever an entry of the second array is smaller than some entry of the
first, that first-array entry and everything after it must be shifted right
by one position. In the worst case every entry of the second array is
smaller than every entry of the first, giving O(mn) time.

The first array, however, has its spare space at the END. So fill it from
the end: the last element of the merged result goes to index m + n - 1, and
at each step the larger of the two largest unprocessed values is written to
the current write position.

Worked example from the book, A = <5,13,17,_,_,_,_,_>, B = <3,7,11,19>;
A evolves as:
    <5,13,17,_,_,_,19,_>
    <5,13,17,_,_,17,19,_>
    <5,13,17,_,13,17,19,_>
    <5,13,17,11,13,17,19,_>
    <5,13,7,11,13,17,19,_>
    <5,5,7,11,13,17,19,_>
    <3,5,7,11,13,17,19,_>

Why this is safe: an entry of the first array that has not yet been
processed is never overwritten. Even if every entry of the second array is
larger than every entry of the first, the second array's entries occupy
exactly indices m to m + n - 1, which do not overlap the first array's
original entries. The book notes the resemblance to Solution 6.4 (page 71),
which also fills values from the end.

The function below is the book's single implementation.
"""


# Type hints: `list[int | None]` means a list whose entries are ints or None
# (None stands for an empty slot); `-> None` says the function returns
# nothing and works by mutating A. `X | Y` in annotations is the union
# syntax (Python 3.10+). Python records annotations but does NOT enforce
# them at run time.
# Documentation: https://docs.python.org/3/library/typing.html
def merge_two_sorted_arrays(A: list[int | None], m: int,
                            B: list[int], n: int) -> None:
    """Merge the first m elements of A and first n elements of B into A.

    This is the textbook's implementation (fill from the end).
    The four-argument signature is retained from the textbook's printed
    listing on page 184. A must have at least m + n slots.
    """

    # Defensive argument check (not in the book). `raise ValueError(...)`
    # stops the function with an exception describing the bad input, rather
    # than silently writing outside A or reading past the end of B.
    # Documentation: https://docs.python.org/3/library/exceptions.html#ValueError
    if m < 0 or n < 0 or m + n > len(A) or n > len(B):
        raise ValueError("Invalid element counts or insufficient target capacity")

    # Tuple unpacking assigns three variables at once:
    #   a         -> index of the largest unprocessed entry of A,
    #   b         -> index of the largest unprocessed entry of B,
    #   write_idx -> next position of A to fill, starting at the very end
    #                of the merged result.
    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:

        # Place the larger of the two current maxima at write_idx.
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1

    # If B still has entries, copy them. If instead A has leftover entries,
    # they are already in their correct final positions, so nothing to do.
    # The tuple assignment decrements both indices in one statement.
    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1


# TEXTBOOK POST-SOLUTION DISCUSSION (page 184)
# --------------------------------------------
# Time: O(m + n). Additional space: O(1).
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def merge_two_sorted_arrays(A, m, B, n):` with no type hints and no
# argument validation. File: same name and parameter names, with type hints
# `A: list[int | None], m: int, B: list[int], n: int` and `-> None`, plus an
# added `if ... raise ValueError(...)` input check at the start. The merge
# loops themselves match the book's listing line for line.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # The book's example values: A = <5,13,17> followed by empty slots
    # (None here), merged with B = <3,7,11,19>. This list has exactly
    # m + n = 7 slots (the book's figure shows one extra empty slot).
    values = [5, 13, 17, None, None, None, None]
    merge_two_sorted_arrays(values, 3, [3, 7, 11, 19], 4)
    print("Merged:", values)

    # `assert` stops the program with an AssertionError if the condition is
    # false; a quick smoke check, with full tests in the tests/ folder.
    assert values == [3, 5, 7, 11, 13, 17, 19]
