"""EPI Python — Exercise 24.25: Count Inversions

Chapter 24: Honors Class
Textbook: pages 385–386 (printed page numbers; problem and solution start
on 385).

PROBLEM (from the textbook)
---------------------------
"Let A be an array of integers. Call the pair of indices (i, j) inverted if
i < j and A[i] > A[j]. For example, if A = <4,1,2,3>, then the pair of
indices (0,3) is inverted. Intuitively, the number of inverted pairs in an
array is a measure of how unsorted it is.

Design an efficient algorithm that takes an array of integers and returns
the number of inverted pairs of indices."

HINT (from the textbook)
------------------------
"Let A and B be arrays. How would you count the number of inversions where
one element is from A and the other from B in the array consisting of
elements from A and B?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: examine every pair (i, j) with i < j: O(n^2) for an array of
length n.

Why that is wasteful: when checking whether an array is sorted, nobody
compares each element with all later elements; comparing with the next
element suffices because "greater than or equal" is transitive. This
suggests sorting can speed up the counting. For instance, if the second half
were sorted, then for an element of the first half a binary search in the
second half would locate it, and the second-half elements before that
position are exactly those inverted with it.

Divide and conquer: suppose the inversions inside the left half L and the
right half R have been counted. The remaining inversions have one element in
L and one in R. Once L and R are sorted these are easy to count: for indices
i in L and j in R, if L[i] > R[j] then L[i] > R[j'] for every j' < j as well.

Worked example: A = <3,6,4,2,5,1>, so L = <3,6,4> and R = <2,5,1>; sorted,
L = <3,4,6> and R = <1,2,5>. The inversion counts inside L and inside R are 1
and 2. Merging the sorted halves:
* 1 < 3, so 3, 4, 6 are all inverted with 1: add |L| - 0 = 3;
* 2 < 3, so again 3, 4, 6 are inverted with 2: add |L| - 0 = 3;
* 3 is then processed: 5 > 3, so no inversion is added;
* 4 is processed: 5 > 4, no inversion is added;
* 5 is processed: 5 < 6, add |L| - 2 = 1 (2 being the index of 6).
Cross inversions total 3 + 3 + 1 = 7; adding the 1 and 2 from L and R gives
the answer 10.

The book prints one program (merge sort that counts while merging); it
corresponds to count_inversions below.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
None: the __main__ block uses the book's example <3,6,4,2,5,1> -> 10.
"""


# Type hints: `a: list[int]` and `-> int` document expected types; Python
# does not enforce annotations at run time.
def count_inversions(a: list[int]) -> int:
    """Return the number of inverted index pairs in `a`.

    This is the textbook's single implementation (merge sort that counts
    cross inversions during each merge). Note: like the book's program, it
    sorts the list `a` in place as a side effect.
    """

    # Returns the number of inversions in a[start:end] and leaves that
    # slice sorted (the book's comment: "Return the number of inversions in
    # A[start:end]").
    def merge_sort_count(start,end):

        # Zero or one element: no inversions.
        if end-start<=1:return 0

        # `//` is floor (integer) division, giving the split index.
        mid=(start+end)//2

        # Inversions inside each half; after these calls both halves are
        # sorted.
        inv=merge_sort_count(start,mid)+merge_sort_count(mid,end)

        # Merge the sorted halves a[start:mid] and a[mid:end]. Tuple
        # unpacking initializes both cursors at once.
        i,j=start,mid
        merged=[]
        while i<mid and j<end:
            if a[i]<=a[j]:

                # `;` separates two simple statements on one line.
                merged.append(a[i]);i+=1
            else:

                # a[i:mid] are the inversions of a[j] (book's comment): all
                # remaining left elements are larger than a[j], and there are
                # mid - i of them. Using `<=` above means equal values are
                # not counted, matching the strict A[i] > A[j] definition.
                merged.append(a[j]);inv+=mid-i;j+=1

        # Updates a with the merged result (book's comment). Slice
        # assignment `a[start:end] = ...` replaces that part of the list in
        # place. At most one of a[i:mid] and a[j:end] is nonempty; it holds
        # the leftover, already sorted, elements. `+` concatenates lists.
        a[start:end]=merged+a[i:mid]+a[j:end]
        return inv
    return merge_sort_count(0,len(a))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 386)
# --------------------------------------------
# The book states the recurrence for the time as T(n) = O(n) + 2T(n - 1)
# and says it solves to O(n log n), n being the array length. (The
# recurrence for halving, which yields O(n log n), is T(n) = O(n) + 2T(n/2);
# the printed "n - 1" appears to be a typo in the book.)
# [NEEDS PDF REVIEW: page 386, recurrence printed as 2T(n - 1)]
#
# VARIANTS
# --------
# * Runners numbered 0 to n - 1 race on a straight one-way road to a common
#   finish line. Speeds are distinct constants and starting distances from
#   the finish line differ: runner i has speed s_i and starts at distance
#   d_i. Each runner stops at the finish line; the race ends when all have
#   finished. How many times does one runner pass another?
#   (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Signature: book `def count_inversions(A)`; file renames the parameter
#   to `a` and adds type hints `list[int]` / `-> int`.
# * Structure: the book has two nested functions,
#   `count_subarray_inversions(start, end)` and, nested inside it,
#   `merge_sort_and_count_inversions_across_subarrays(start, mid, end)`.
#   The file merges both into one nested function
#   `merge_sort_count(start, end)` that recurses and then merges inline.
# * Names: book's `sorted_A`, `left_start`, `right_start`,
#   `inversion_count` become `merged`, `i`, `j`, `inv`.
# * Order of statements in the else-branch: book counts
#   `inversion_count += mid - left_start` before appending; file appends
#   first. Same result.
# * The final slice assignment and the overall algorithm match the book.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # The book's worked example <3,6,4,2,5,1>, which has 10 inversions.
    # (count_inversions sorts `data` in place as a side effect.)
    data=[3,6,4,2,5,1]
    print('Inversions:',count_inversions(data))

    # `assert` stops with an AssertionError if the condition is false. A
    # fresh list is passed because `data` is now sorted. pytest provides
    # the more thorough verification.
    assert count_inversions([3,6,4,2,5,1])==10
