"""EPI Python — Exercise 10.6: Compute the k Largest Elements in a Max-Heap

Chapter 10: Heaps
Textbook: pages 140–141 (printed page numbers; problem, solution and most of
the program on page 140, the program's end and complexity on page 141).

PROBLEM (from the textbook)
---------------------------
"A heap contains limited information about the ordering of elements, so
unlike a sorted array or a balanced BST, naive algorithms for computing the
k largest elements have a time complexity that depends linearly on the
number of elements in the collection.

Given a max-heap, represented as an array A, design an algorithm that
computes the k largest elements stored in the max-heap. You cannot modify
the heap. For example, if the heap is the one shown in Figure 10.1(a) on
Page 132, then the array representation is
<561, 314, 401, 28, 156, 359, 271, 11, 3>, the four largest elements are
561, 314, 401, and 359."

(The book prints no hint for this exercise.)

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: perform k extract-max operations on the heap: O(k log n) time
for a heap of n elements, but this modifies the heap, which is not allowed.

Selection: use a kth-smallest-element algorithm such as Solution 11.8
(page 153); its time is O(n) with near certainty, but it also modifies the
heap.

Using the heap's partial order: every parent is >= its children. So the root
A[0] is certainly among the k largest; indeed it is the largest. The second
largest must be the larger of the root's children A[1] and A[2], and the
search continues from there.

The set of "next candidates" needs fast insertion and fast extraction of
the maximum, i.e. another max-heap. The algorithm builds a candidate
max-heap of INDICES into A, ordered by the values they refer to, starting
with index 0 (for A[0]). It then performs k extract-max operations; after
extracting index i, it inserts i's children, the left child 2i + 1 and the
right child 2i + 2, whenever those indices exist in A.

The book's program is `k_largest_in_binary_heap(A, k)`; this file's
function of the same name implements the same algorithm (see the code
comparison at the end).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    k_largest_in_binary_heap([10, 9, 8, 3, 4, 1, 2], 3) -> [10, 9, 8]
    Book example: k_largest_in_binary_heap(
        [561, 314, 401, 28, 156, 359, 271, 11, 3], 4) -> [561, 401, 359, 314]
    (the same four elements the book lists, in extraction order)
"""

# Python standard library: heap queue (priority queue) algorithms on plain
# lists. heapq only provides MIN-heaps; storing negated values makes the
# largest original value come out first (a max-heap effect).
# Module documentation: https://docs.python.org/3/library/heapq.html
# heappop:  https://docs.python.org/3/library/heapq.html#heapq.heappop
# heappush: https://docs.python.org/3/library/heapq.html#heapq.heappush
import heapq


# Type hints (not enforced by Python): `max_heap` is a list of ints already
# in max-heap order (A[i] >= A[2i+1] and A[i] >= A[2i+2]); the result is a
# list of ints.
def k_largest_in_binary_heap(max_heap: list[int], k: int) -> list[int]:
    """Find k largest keys in a binary max-heap without modifying the heap.

    Implements the textbook's `k_largest_in_binary_heap` (pages 140–141).
    """

    # A chained comparison `0 <= k <= len(max_heap)` means
    # `0 <= k and k <= len(max_heap)`. Values of k outside that range are
    # rejected with ValueError.
    if not 0 <= k <= len(max_heap):
        raise ValueError("k must lie between zero and size")

    # `not k` is True when k == 0 (zero is falsy).
    if not k:
        return []

    # Candidate heap of (negated value, index) pairs, starting with the root.
    # Tuples compare component by component, so the negated value decides
    # the order (most negative = largest original value first) and the
    # index only breaks ties. A one-element list is already a valid heap.
    candidates = [(-max_heap[0], 0)]
    answer = []

    # `_` is the conventional name for a loop variable that is not used:
    # this loop simply runs k times.
    for _ in range(k):

        # heapq.heappop(heap) removes and returns the smallest entry, i.e.
        # the candidate with the LARGEST original value, in O(log k) time.
        # The pair is unpacked into two names.
        # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappop
        neg_value, index = heapq.heappop(candidates)

        # Negate again to recover the original value.
        answer.append(-neg_value)

        # The children of array index i in a binary heap are at 2i + 1
        # (left) and 2i + 2 (right). Only indices inside the array exist.
        for child in (2 * index + 1, 2 * index + 2):
            if child < len(max_heap):

                # heapq.heappush(heap, item) inserts while keeping heap
                # order. The input list `max_heap` is only read, never
                # modified, as the problem requires.
                # Documentation: https://docs.python.org/3/library/heapq.html#heapq.heappush
                heapq.heappush(candidates, (-max_heap[child], child))
    return answer


# TEXTBOOK POST-SOLUTION DISCUSSION (page 141)
# --------------------------------------------
# There are O(k) insertions and extract-max operations in total (each
# extraction adds at most two candidates), so the candidate heap holds O(k)
# entries and each operation costs O(log k): O(k log k) time and O(k)
# additional space. The original heap is not modified.
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def k_largest_in_binary_heap(A, k)` returns [] when `k <= 0`;
# builds `candidate_max_heap = []` and appends `(-A[0], 0)` (comments:
# stores (-value, index) pairs ordered by value, negated for a max-heap
# effect; "The largest element in A is at index 0."); each iteration reads
# `candidate_idx = candidate_max_heap[0][1]` before popping, appends
# `-heapq.heappop(candidate_max_heap)[0]`, then pushes the left child
# (`left_child_idx = 2 * candidate_idx + 1`) and the right child
# (`right_child_idx = 2 * candidate_idx + 2`) with two separate if
# statements.
# File: parameters renamed `max_heap: list[int], k: int` with
# `-> list[int]`; raises ValueError unless 0 <= k <= len(max_heap) (book:
# negative k returns [], and k > len(A) is not checked, so the book's
# heappop would raise IndexError on an exhausted candidate heap); the
# candidate list is created directly as `[(-max_heap[0], 0)]`; the popped
# pair is unpacked into `neg_value, index` instead of peeking at [0][1]
# first; the two children are handled by one loop over a tuple of indices;
# result list renamed `answer`. Same algorithm and output.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # [10, 9, 8, 3, 4, 1, 2] is a valid max-heap: every parent is at least
    # as large as its children. Its three largest values, in extraction
    # order, are 10, 9, 8.
    # `assert` stops the program with an AssertionError if the result
    # differs; pytest provides the thorough automated verification.
    heap = [10,9,8,3,4,1,2]
    print("top 3 heap:", k_largest_in_binary_heap(heap, 3))
    assert k_largest_in_binary_heap(heap, 3) == [10,9,8]
