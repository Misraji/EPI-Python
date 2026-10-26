"""EPI Python — Exercise 5.5: Delete Duplicates from a Sorted Array

Chapter 5: Arrays
Textbook: pages 45–46 (printed page numbers; problem on page 45, solution
and variants on page 46).

PROBLEM (from the textbook)
---------------------------
"This problem is concerned with deleting repeated elements from a sorted
array. For example, for the array <2,3,5,5,7,11,11,11,13>, then after
deletion, the array is <2,3,5,7,11,13,0,0,0>. After deleting repeated
elements, there are 6 valid entries. There are no requirements as to the
values stored beyond the last valid element."

"Write a program which takes as input a sorted array and updates it so
that all duplicates have been removed and the remaining elements have been
shifted left to fill the emptied indices. Return the number of valid
elements. Many languages have library functions for performing this
operation—you cannot use these functions."

HINT (from the textbook)
------------------------
"There is an O(n) time and O(1) space solution."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Let A be the array and n its length.

1. With O(n) extra space: scan A, use a hash table to recognise values not
   seen before, append each new value to a separate list, and finally copy
   that list back into A.

2. Brute force with O(1) extra space: scan A, and whenever A[i] equals
   A[i + 1], shift every element from position i + 2 onward one place to
   the left. If all entries are equal, the shifts cost
   (n - 1) + (n - 2) + ... + 2 + 1, which is O(n^2).

3. Better: cut down the shifting. Because A is sorted, equal values sit
   next to each other, so no auxiliary structure is needed to tell
   whether a value is new: just compare with the last value kept. Move
   one element at a time (not a whole subarray), and move each element at
   most once.

Book walk-through on <2,3,5,5,7,11,11,11,13>: when A[3] is processed, it is
compared with A[2]; both are 5, so it is skipped and we move on to A[4].
A[4] = 7 is new, so it is copied into the first vacant slot, A[3]. The
array becomes <2,3,5,7,7,11,11,11,13>, the first vacant slot is now A[4],
and the scan continues at A[5].

The book prints one program, implemented here as `delete_duplicates`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [1, 1, 2, 2, 3] -> returns 3; valid prefix [1, 2, 3]
    [4, 4, 4]       -> returns 1; valid prefix [4]
    []              -> returns 0
"""


# `sorted_array: list[int]` and `-> int` are type hints documenting the
# expected argument and return types. Python does not enforce them at run
# time. `list[int]` requires Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def delete_duplicates(sorted_array: list[int]) -> int:
    """Textbook `delete_duplicates(A)`: compact in place, return the count.

    Book comment above the function: "Returns the number of valid entries
    after deletion."
    """

    # An empty list is falsy, so `not sorted_array` is True for [].
    if not sorted_array:
        return 0

    # `write` is the first vacant position. The first element is always
    # kept, so writing starts at index 1.
    write = 1
    for read in range(1,len(sorted_array)):
        if sorted_array[read] != sorted_array[write-1]:
            # Only compare with the most recent *retained* value, which may
            # be far behind `read` after discarding repeated items.
            sorted_array[write] = sorted_array[read]
            write += 1

    # `write` now equals the number of valid (distinct) entries at the
    # front of the list. Anything after them is left over and meaningless.
    return write


# TEXTBOOK POST-SOLUTION DISCUSSION (page 46)
# ------------------------------------------
# The time complexity is O(n). The space complexity is O(1): only two
# extra variables (the read and write indices) are needed.
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Implement a function
# which takes as input an array and a key, and updates the array so that
# all occurrences of the key have been removed and the remaining elements
# have been shifted left to fill the emptied indices. Return the number of
# remaining elements. There are no requirements as to the values stored
# beyond the last valid element.
#
# Variant 2 (stated in the book; no solution given): Write a program which
# takes as input a sorted array A of integers and a positive integer m,
# and updates A so that if x appears m times in A it appears exactly
# min(2, m) times in A. The update must be done in one pass, and no
# additional storage may be allocated.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def delete_duplicates(A)`; file: parameter renamed
#   `sorted_array`, type hints added.
# - Book variables `write_index` and `i`; file: `write` and `read`.
# - Book test `A[write_index - 1] != A[i]`; file writes the same
#   comparison with the operands swapped (`sorted_array[read] !=
#   sorted_array[write-1]`). Otherwise the code matches the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (input list, expected valid prefix). These are added
    # for learning: repeated pairs, all-equal values, and an empty list.
    for original,expected in (([1,1,2,2,3],[1,2,3]),([4,4,4],[4]),([],[])):

        # `list.copy()` returns a new (shallow) list, so the in-place update
        # does not disturb `original`, which is printed below.
        # Documentation: https://docs.python.org/3/tutorial/datastructures.html
        values = original.copy()
        valid_length = delete_duplicates(values)

        # `values[:valid_length]` is a slice: the first valid_length items.
        # An f-string (prefix f) evaluates each {expression} and inserts
        # its text into the string.
        # Documentation: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
        print(f"unique prefix of {original}: {values[:valid_length]}")

        # `assert` stops the program with an AssertionError if the condition
        # is false. These are quick smoke checks; pytest provides the more
        # thorough automated verification.
        assert values[:valid_length] == expected
