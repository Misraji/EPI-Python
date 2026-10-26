"""EPI Python — Exercise 13.1: Compute the Intersection of Two Sorted Arrays

Chapter 13: Sorting
Textbook: pages 182–183 (printed page numbers; problem and solution start on 182).

PROBLEM (from the textbook)
---------------------------
"A natural implementation for a search engine is to retrieve documents that
match the set of words in a query by maintaining an inverted index. [...]
The most computationally intensive step of doing this is finding the
intersection of the sorted arrays."

"Write a program which takes as input two sorted arrays, and returns a new
array containing elements that are present in both of the input arrays. The
input arrays may have duplicate entries, but the returned array should be
free of duplicates. For example, the input is <2,3,3,5,5,6,7,7,8,12> and
<5,5,6,8,8,9,10,10>, your output should be <5,6,8>."

HINT (from the textbook)
------------------------
"Solve the problem if the input array lengths differ by orders of
magnitude. What if they are approximately equal?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Context: in an inverted index each web page has an integer document-ID, and
each word w maps to a sorted array of the IDs of pages containing w (the
order could be, e.g., descending page rank). A multi-word query intersects
the arrays for its words; that intersection is the expensive step.

Let m and n be the lengths of the two input arrays.

1. Brute force ("loop join"): walk over every element of one array and look
   for it among the elements of the other. Duplicates in the output are
   avoided by keeping an element of A only when it is the first entry or
   differs from the entry just before it. Testing membership with a linear
   scan of B makes this O(mn) time.

2. Binary search: since both arrays are sorted, iterate over the first array
   and use binary search (bisect.bisect_left) to test whether each element
   is in the second array. This costs O(m log n), where m is the length of
   the array iterated over. Choosing the SHORTER array for the outer loop
   helps further: if n is much smaller than m, n log(m) is much smaller than
   m log(n). This is the best approach when one array is much smaller than
   the other.

3. Simultaneous linear sweep: when the lengths are similar, the binary
   search approach fails to use the fact that BOTH arrays are sorted.
   Advance through both arrays together in increasing order:
   - if the current elements differ, the smaller one cannot be in the
     intersection, so skip past it;
   - if they are equal, add the value to the result (unless it duplicates
     the previous element) and advance in both arrays.

   Worked example from the book: A = <2,3,3,5,7,11>, B = <3,3,7,15,31>.
   - 2 vs 3: 2 cannot be in the intersection; advance in A.
   - 3 vs 3: common element, add 3; advance both.
   - 3 vs 3 again: 3 was already added (the previous element of A is also
     3), so advance both without adding.
   - 5 vs 7: eliminate 5; advance in A to its fourth element, 7.
   - 7 vs 7: add 7; advance both.
   - 11 vs 15: eliminate 11; A is exhausted, so the result is <3,7>.

This file implements approach 3 as `intersect_two_sorted_arrays` and
approach 2 as `intersect_two_sorted_arrays_bisect`. The brute-force listing
(approach 1) is not reproduced as a function in this file.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [], []                    -> []
    [1, 2, 2, 3], [2, 2, 3, 4] -> [2, 3]
    [1, 3], [2, 4]            -> []     (no common values)
    [1, 1], [1]               -> [1]    (duplicates collapse to one)
"""

# Python standard library: array bisection (binary search on sorted lists).
# Module documentation: https://docs.python.org/3/library/bisect.html
# bisect_left API: https://docs.python.org/3/library/bisect.html#bisect.bisect_left
from bisect import bisect_left


# Type hints such as `a: list[int]` and `-> list[int]` document that the
# parameters and return value are lists of integers. Python records these
# annotations but does NOT enforce them at run time.
# Documentation: https://docs.python.org/3/library/typing.html
def intersect_two_sorted_arrays(a: list[int], b: list[int]) -> list[int]:
    """Sorted intersection with each shared value appearing once.

    This is the textbook's third (final) implementation: a simultaneous
    linear sweep through both sorted arrays, O(m + n) time.
    """

    # A variable annotation (`name: type = value`) declares the intended
    # type of `result`; like all annotations it is not enforced.
    result: list[int] = []

    # Chained assignment: both indices start at 0.
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:

            # Duplicate suppression. An empty list is falsy, so
            # `not result` is True before anything has been added.
            # `result[-1]` is the last element appended (negative indices
            # count from the end). Because values are added in increasing
            # order, any repeat of a value must equal result[-1].
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:

            # a[i] is smaller than everything remaining in b, so it cannot
            # belong to the intersection; skip it.
            i += 1
        else:

            # Symmetric case: a[i] > b[j], so b[j] is eliminated.
            j += 1
    return result



def intersect_two_sorted_arrays_bisect(a: list[int], b: list[int]) -> list[int]:
    """PDF's binary-search approach; iterate over shorter sorted input.

    This is the textbook's second implementation (binary search for each
    element of one array in the other), combined with the book's remark
    that the shorter array should drive the outer loop.
    For a much shorter array A and long array B, this can be faster
    than a full two-pointer sweep: O(len(A)*log(len(B))).
    """

    # Tuple packing/unpacking swaps the two names in one statement, so that
    # `a` is always the shorter list (the book's suggested optimization).
    if len(a)>len(b):
        a,b=b,a
    result=[]
    for value in a:

        # Skip a value equal to the last one recorded: since `a` is sorted,
        # repeated values are adjacent and must appear only once in output.
        # (If the repeated value was NOT found in b, it is simply searched
        # for again, which is harmless.)
        if result and result[-1]==value:
            continue

        # bisect_left(b, value) performs a binary search in the sorted list
        # b and returns the FIRST (leftmost) index at which value could be
        # inserted while keeping b sorted. It runs in O(log len(b)) time and
        # does not modify b. If value occurs in b, that index points at its
        # first occurrence. An equality check is still required: a missing
        # item also has an insertion position, possibly len(b) (past the
        # end), which is why `pos < len(b)` is tested first.
        # Documentation: https://docs.python.org/3/library/bisect.html#bisect.bisect_left
        pos=bisect_left(b,value)
        if pos<len(b) and b[pos]==value:
            result.append(value)
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 182–183)
# -------------------------------------------------
# - Brute-force loop join: O(mn) time.
# - Binary-search version: O(m log n), m being the length of the array that
#   is iterated over; iterate over the shorter array, because when n is much
#   smaller than m, n log(m) is much smaller than m log(n). Best when one
#   array is much smaller than the other.
# - Linear sweep: O(1) time is spent per input element, so the whole
#   algorithm is O(m + n). Best when the array lengths are similar.
#
# VARIANTS
# --------
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# The book prints three listings, all named `intersect_two_sorted_arrays(A, B)`
# with no type hints.
# - Brute force (book: one-line list comprehension using `enumerate` and
#   `a in B`): NOT present in this file.
# - Binary search (book: nested helper `is_present(k)` calling
#   `bisect.bisect_left(B, k)`, with a list comprehension that keeps
#   `a` when `i == 0 or a != A[i - 1]` and `is_present(a)`): file renames it
#   `intersect_two_sorted_arrays_bisect(a: list[int], b: list[int])`, uses
#   `from bisect import bisect_left` instead of `import bisect`, replaces the
#   comprehension and helper with an explicit loop, deduplicates by comparing
#   with `result[-1]` (and `continue`) rather than `A[i - 1]`, and adds a swap
#   so the shorter list is iterated (the book only recommends this in prose;
#   its listing does not swap).
# - Linear sweep (book: variables `i, j, intersection_A_B = 0, 0, []`,
#   deduplicates with `if i == 0 or A[i] != A[i - 1]`, advances with
#   `i, j = i + 1, j + 1`, comment `# A[i] > B[j].` on the else): file
#   uses lowercase parameters `a`, `b` with type hints, names the output
#   `result`, deduplicates with `not result or result[-1] != a[i]`, and
#   increments `i` and `j` in separate statements. Behaviour is the same.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Run a few self-contained examples before exploring the pytest suite.
    # The first four (added for learning) exercise the linear-sweep version:
    # empty inputs, duplicates on both sides, no overlap, and a repeated
    # value collapsing to a single output entry.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false. These are quick smoke checks; pytest provides the more
    # thorough automated verification in the separate tests/ folder.
    observed = intersect_two_sorted_arrays([], [])
    print("intersect_two_sorted_arrays:", observed)
    assert observed == []
    observed = intersect_two_sorted_arrays([1, 2, 2, 3], [2, 2, 3, 4])
    print("intersect_two_sorted_arrays:", observed)
    assert observed == [2, 3]
    observed = intersect_two_sorted_arrays([1, 3], [2, 4])
    print("intersect_two_sorted_arrays:", observed)
    assert observed == []
    observed = intersect_two_sorted_arrays([1, 1], [1])
    print("intersect_two_sorted_arrays:", observed)
    assert observed == [1]

    # The book's worked example A = <2,3,3,5,7,11>, B = <3,3,7,15,31>,
    # whose intersection is <3,7>, run through the binary-search version.
    print('PDF binary-search intersection:',intersect_two_sorted_arrays_bisect([2,3,3,5,7,11],[3,3,7,15,31]))
    assert intersect_two_sorted_arrays_bisect([2,3,3,5,7,11],[3,3,7,15,31])==[3,7]
