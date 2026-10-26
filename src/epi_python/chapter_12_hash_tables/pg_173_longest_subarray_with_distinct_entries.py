"""EPI Python — Exercise 12.8: Find the Longest Subarray with Distinct Entries

Chapter 12: Hash Tables
Textbook: pages 173–174 (printed page numbers; problem, solution and
program on 173, complexity at the top of 174).

PROBLEM (from the textbook)
---------------------------
"Write a program that takes an array and returns the length of a longest
subarray with the property that all its elements are distinct. For
example, if the array is <f, s, f, e, t, w, e, n, w, e> then a longest
subarray all of whose elements are distinct is <s, f, e, t, w>."

HINT (from the textbook)
------------------------
"What should you do if the subarray from indices i to j satisfies the
property, but the subarray from i to j + 1 does not?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: for every subarray, use a hash table to test whether all its
elements are distinct. There are O(n^2) subarrays with average length O(n),
so O(n^3) time for an array of length n.

O(n^2): if a subarray contains a duplicate, so does every array that
contains it. So for a fixed starting index, grow the subarray one element
at a time, adding elements to a hash table, and stop at the first
duplicate -- no longer duplicate-free subarray can begin at that index.
This is O(n) per start index.

O(n): reuse previous work while scanning. Suppose the longest
duplicate-free subarray ending at some index is known. The longest one
ending at the NEXT index is:
  * the previous subarray extended by the next element, if that element
    does not occur in the previous subarray;
  * otherwise, the subarray that starts just after the most recent
    occurrence of that element and ends at the next index.
All that is needed for this case analysis is a hash table of the most
recent occurrence of each element, plus the longest duplicate-free subarray
ending at the current element.

Book's worked example, <f, s, f, e, t, w, e, n, w, e>:
  * At index 2, the longest duplicate-free subarray ending at index 1 is
    0..1. The table shows the element at index 2, f, occurs in it, so the
    longest subarray ending at index 2 becomes 1..2.
  * Indices 3 to 5 bring in new elements.
  * Index 6 holds e again, which lies inside the longest subarray ending
    at index 5 (at index 3), so the longest subarray ending at index 6
    starts at index 4.

The implementation below, longest_subarray_with_distinct_entries, follows
this idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []              -> 0
    [1, 2, 3]       -> 3 (all distinct)
    [1, 2, 1, 3, 4] -> 4 ([2, 1, 3, 4])
    [1, 1, 1]       -> 1
"""


def longest_subarray_with_distinct_entries(values: list[int]) -> int:
    """Length of the longest contiguous subarray with no repeated values.

    This is the textbook's longest_subarray_with_distinct_entries (the only
    implementation given), rewritten in an equivalent sliding-window form.

    Type hints: `list[int]` and `-> int` document the expected types; Python
    does not enforce them.
    """

    # Book's comment: records the most recent occurrence of each entry.
    # `{}` is an empty dict (hash table): value -> latest index.
    last_seen={}

    # `begin` is the start index of the longest duplicate-free subarray
    # ending at the current position; `best` is the longest length so far.
    begin=0
    best=0

    # enumerate() yields (index, value) pairs; `end` is the current index.
    # enumerate: https://docs.python.org/3/library/functions.html#enumerate
    for end,value in enumerate(values):

        # A repeat. If its previous occurrence lies inside the current
        # window (index >= begin), the window must start just after it.
        # max() keeps begin from moving backwards when the previous
        # occurrence is older than the window.
        # max: https://docs.python.org/3/library/functions.html#max
        if value in last_seen:
            begin=max(begin,last_seen[value]+1)
        last_seen[value]=end

        # The window begin..end (inclusive) has end - begin + 1 elements.
        best=max(best,end-begin+1)
    return best


# TEXTBOOK POST-SOLUTION DISCUSSION (page 174)
# --------------------------------------------
# Time complexity O(n), since a constant number of operations is performed
# per element. Extra space is proportional to the number of distinct
# values stored in the hash table.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def longest_subarray_with_distinct_entries(A):` with
#   `most_recent_occurrence = {}` and
#   `longest_dup_free_subarray_start_idx = result = 0`. It defers updating
#   the result until a duplicate is seen (comment "Defer updating dup_idx
#   until we see a duplicate."): when `dup_idx >= start_idx` it sets
#   `result = max(result, i - start_idx)` and moves the start to
#   `dup_idx + 1`; it finally returns
#   `max(result, len(A) - longest_dup_free_subarray_start_idx)`.
# File: parameter renamed `values: list[int]` with return hint `-> int`;
#   variables renamed (`last_seen`, `begin`, `best`, `end`); instead of
#   the conditional `if dup_idx >= start` jump, it uses
#   `begin = max(begin, last_seen[value] + 1)`, and it updates `best` on
#   every iteration with `end - begin + 1`, so no final `max(..., len(A) -
#   start)` step is needed. Same result.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior: an empty
    # list, an all-distinct list, a repeat that forces the window to move,
    # and a list of identical values.
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value. These are quick smoke checks;
    # pytest provides the more thorough automated verification.
    observed = longest_subarray_with_distinct_entries([])
    print("longest_subarray_with_distinct_entries:", observed)
    assert observed == 0
    observed = longest_subarray_with_distinct_entries([1, 2, 3])
    print("longest_subarray_with_distinct_entries:", observed)
    assert observed == 3
    observed = longest_subarray_with_distinct_entries([1, 2, 1, 3, 4])
    print("longest_subarray_with_distinct_entries:", observed)
    assert observed == 4
    observed = longest_subarray_with_distinct_entries([1, 1, 1])
    print("longest_subarray_with_distinct_entries:", observed)
    assert observed == 1
