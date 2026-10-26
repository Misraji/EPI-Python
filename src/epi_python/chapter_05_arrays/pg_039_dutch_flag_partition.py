"""EPI Python — Exercise 5.1: The Dutch National Flag Problem

Chapter 5: Arrays
Textbook: pages 39–42 (printed page numbers; the problem is introduced at
the bottom of page 39, stated on page 40, and solved on pages 40–42).

PROBLEM (from the textbook)
---------------------------
"Write a program that takes an array A and an index i into A, and
rearranges the elements such that all elements less than A[i] (the
"pivot") appear first, followed by elements equal to the pivot, followed
by elements greater than the pivot."

Context and examples given with the problem:
  - Quicksort picks a pivot, reorders the array so that elements <= pivot
    come first, then sorts the two parts recursively. Implemented naively,
    it has large run times and deep call stacks on arrays with many
    duplicates, because the two parts may differ greatly in size. One fix
    is to reorder the array into three groups: less than, equal to, and
    greater than the pivot. This is "Dutch national flag partitioning",
    since the Dutch flag has three horizontal bands of different colors.
  - Figure 5.1: (a) an unpartitioned array of colored bars; (b) a valid
    three-way partitioning if black precedes white and white precedes gray
    (resembling the Dutch flag); (c) a valid partitioning if gray precedes
    black and black precedes white (resembling the Russian flag).
  - "Generalizing, suppose A = <0,1,2,0,2,1,1>, and the pivot index is 3.
    Then A[3] = 0, so <0,0,1,2,2,1,1> is a valid partitioning. For the same
    array, if the pivot index is 2, then A[2] = 2, so the arrays
    <0,1,0,1,1,2,2> as well as <0,0,1,1,1,2,2> are valid partitionings."

HINT (from the textbook)
------------------------
"Think about the partition step in quicksort."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
1. Extra-space approach. With O(n) additional storage the problem is easy:
   build three lists (less than, equal to, greater than the pivot) and
   then write them back into A. Time O(n), extra space O(n). The book
   gives no program for this.

2. In-place, quadratic approach. To avoid O(n) extra space, accept a
   slower running time. First stage: walk A from index 0 upward; at each
   index, search forward for an element smaller than the pivot and, as
   soon as one is found, swap it into the current position. That gathers
   every smaller element at the front. Second stage: the mirror image,
   moving larger elements to the back. The book prints this program
   (here `dutch_flag_partition_quadratic`).

   Extra space is O(1) but time is O(n^2). The book's bad case: i = n/2,
   every element before position i is greater than A[i], and every
   element after i is less than A[i]. The waste comes from restarting
   each search from the beginning; nothing stops us from resuming at the
   last location we advanced to (likewise for the second pass).

3. In-place, two linear passes. Make one pass that moves each smaller
   element to the front the moment it is seen (tracking the boundary
   `smaller`), then a second, backward pass that moves each larger
   element to the end (tracking `larger`). Each pass is a single loop.
   Time O(n), space O(1). The book prints this program (here
   `dutch_flag_partition_two_pass`).

4. Single pass, four regions. Classify elements as less / equal / greater
   in one pass, at the cost of a trickier implementation. Maintain four
   subarrays: bottom (less than pivot), middle (equal), unclassified, and
   top (greater). Initially everything is unclassified. Each step takes
   the first unclassified element and moves it into bottom, middle or
   top depending on how it compares with the pivot.

   The book's worked example: A = <-3,0,-1,1,1,?,?,?,4,2>, pivot 1, where
   ? marks unclassified entries. The first unclassified element is A[5]:
     - If A[5] < pivot (say -5): swap it with the first 1, giving
       <-3,0,-1,-5,1,1,?,?,4,2>.
     - If A[5] == pivot (1): leave it and advance to the next unclassified
       element, giving <-3,0,-1,1,1,1,?,?,4,2>.
     - If A[5] > pivot (say 3): swap it with the last unclassified
       element, giving <-3,0,-1,1,1,?,?,3,4,2>.
   In every case the unclassified region shrinks by one. The book prints
   this program (here `dutch_flag_partition`).

So the file contains all three printed programs as separate functions:
`dutch_flag_partition_quadratic`, `dutch_flag_partition_two_pass` and
`dutch_flag_partition`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    values=[3, 1, 2, 1, 3], pivot_index=1 (pivot 1)
        -> any arrangement of the form [1, 1, 2/3 ...] with every value
           > 1 after both 1s, e.g. [1, 1, 2, 3, 3] or [1, 1, 3, 2, 3].
Order *within* each group is not promised by any of the algorithms.
"""


# NOTE ON TYPE HINTS used throughout this file:
# `pivot_index: int` and `values: list[int]` are annotations. They document
# the intended types (an int index, a list of ints) and are read by tools
# such as type checkers and IDEs, but Python itself does NOT enforce them
# at run time. `-> int` / `-> list[int]` annotate the return value.
# `list[int]` (a built-in generic) needs Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def _validate_pivot(pivot_index: int, values: list[int]) -> int:
    """Return the pivot value, rejecting out-of-range pivot indices.

    Helper added in this repository; it is not part of the textbook. The
    book's programs simply read A[pivot_index].
    """

    # `0 <= pivot_index < len(values)` is a chained comparison: Python
    # evaluates it as `0 <= pivot_index and pivot_index < len(values)`.
    # Negative indices are rejected deliberately, even though plain
    # indexing would accept them (values[-1] is the last element).
    if not 0 <= pivot_index < len(values):

        # `raise` signals an error. IndexError is the built-in exception
        # Python itself uses for out-of-range sequence indices.
        # Documentation: https://docs.python.org/3/library/exceptions.html#IndexError
        raise IndexError("Invalid pivot index")
    return values[pivot_index]


def dutch_flag_partition_quadratic(pivot_index: int, values: list[int]) -> list[int]:
    """Textbook's first in-place program: two passes with nested searches.

    O(n^2) time, O(1) extra space. The list is rearranged in place and
    also returned for convenience.
    """
    pivot = _validate_pivot(pivot_index, values)

    # First pass (book comment: "group elements smaller than pivot").
    # For each position i, look further right for an element smaller than
    # the pivot (book comment: "Look for a smaller element") and swap it
    # into position i. The inner search restarts from i + 1 every time,
    # which is what makes this version quadratic.
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[j] < pivot:

                # `a, b = b, a` swaps two entries: the right-hand side
                # builds a tuple of the two current values first, then
                # unpacks it into the two targets, so no temporary
                # variable is needed.
                values[i], values[j] = values[j], values[i]

                # `break` exits only the inner `for j` loop.
                break

    # Second pass (book comment: "group elements larger than pivot").
    # `reversed(range(n))` yields n-1, n-2, ..., 0 without building a list:
    # reversed() returns an iterator that walks a sequence backwards.
    # Documentation: https://docs.python.org/3/library/functions.html#reversed
    for i in reversed(range(len(values))):

        # Once we reach an element less than the pivot we are inside the
        # prefix built by the first pass, so the work is finished.
        if values[i] < pivot:
            break

        # Book comment: "Look for a larger element. Stop when we reach an
        # element less than pivot, since first pass has moved them to the
        # start of A." Search leftward from i - 1 for an element greater
        # than the pivot and swap it into position i.
        for j in reversed(range(i)):
            if values[j] > pivot:
                values[i], values[j] = values[j], values[i]
                break
    return values


def dutch_flag_partition_two_pass(pivot_index: int, values: list[int]) -> list[int]:
    """Textbook's second in-place program: one linear scan per pass.

    O(n) time, O(1) extra space. The list is rearranged in place and also
    returned for convenience.
    """
    pivot = _validate_pivot(pivot_index, values)

    # Book comment: "First pass: group elements smaller than pivot."
    # Invariant: values[:smaller] holds exactly the smaller elements seen
    # so far; each newly found smaller element is swapped to index
    # `smaller`, and the boundary advances by one.
    smaller = 0

    for i in range(len(values)):
        if values[i] < pivot:

            # Tuple-unpacking swap (see the comment in the quadratic
            # version): exchange values[i] and values[smaller].
            values[i], values[smaller] = values[smaller], values[i]
            smaller += 1
    larger = len(values) - 1

    # Book comment: "Second pass: group elements larger than pivot."
    # `reversed(range(smaller, len(values)))` visits len(values)-1 down to
    # `smaller`. Starting the range at `smaller` skips the prefix of
    # smaller elements produced by the first pass (the book instead scans
    # from the end and `break`s at the first element less than the pivot;
    # see TEXTBOOK CODE COMPARISON below). Each larger element is swapped
    # to index `larger`, which then moves one step left.
    for i in reversed(range(smaller, len(values))):
        if values[i] > pivot:
            values[i], values[larger] = values[larger], values[i]
            larger -= 1
    return values


def dutch_flag_partition(pivot_index: int, values: list[int]) -> list[int]:
    """Textbook's final program: one-pass, three-way partitioning.

    O(n) time, O(1) extra space. The list is rearranged in place and also
    returned for convenience.
    """
    pivot = _validate_pivot(pivot_index, values)

    # Book comments: "Keep the following invariants during partitioning:
    #   bottom group: A[:smaller].
    #   middle group: A[smaller:equal].
    #   unclassified group: A[equal:larger].
    #   top group: A[larger:]."
    # (A[a:b] is slice notation for indices a up to, not including, b.)
    #
    # `x, y, z = 0, 0, n` assigns three names at once by tuple unpacking.
    smaller, equal, larger = 0, 0, len(values)

    # Book comment: "Keep iterating as long as there is an unclassified
    # element." values[equal] is always the next unclassified element.
    while equal < larger:
        if values[equal] < pivot:

            # The incoming element belongs in bottom: swap it with the
            # first element of middle (or with itself if middle is empty),
            # then grow bottom and advance past the classified element.
            values[smaller], values[equal] = values[equal], values[smaller]
            smaller += 1
            equal += 1
        elif values[equal] == pivot:

            # Already in the right place: middle simply grows by one.
            equal += 1
        else:

            # Book comment: "A[equal] > pivot." Grow top leftward by one
            # and swap the incoming element into that slot. Do not
            # increment `equal`: the element moved in from the right has
            # not been classified yet.
            larger -= 1
            values[equal], values[larger] = values[larger], values[equal]
    return values


# TEXTBOOK POST-SOLUTION DISCUSSION (page 42)
# ------------------------------------------
# Every iteration of the final program shrinks the unclassified group by
# one, and each iteration does O(1) work, so the time complexity is O(n).
# The extra space is O(1): only three integer indices.
#
# (Complexities of the earlier programs, given in the development: the
# nested-search version is O(n^2) time / O(1) space; the two linear passes
# are O(n) time / O(1) space; the three-list idea is O(n) time / O(n)
# space.)
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Assuming keys take
# one of three values, reorder the array so that all objects with the
# same key appear together. The order of the subarrays does not matter;
# for example, both Figure 5.1(b) and Figure 5.1(c) are valid answers for
# Figure 5.1(a). Use O(1) additional space and O(n) time.
#
# Variant 2 (stated in the book; no solution given): Given an array A of
# n objects whose keys take one of four values, reorder the array so that
# all objects with the same key appear together. Use O(1) additional space
# and O(n) time.
#
# Variant 3 (stated in the book; no solution given): Given an array A of
# n objects with Boolean-valued keys, reorder the array so that objects
# with key false appear first. Use O(1) additional space and O(n) time.
#
# Variant 4 (stated in the book; no solution given): Same as Variant 3,
# but the relative ordering of the objects with key true must not change.
# Use O(1) additional space and O(n) time.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - All three book programs are named `dutch_flag_partition(pivot_index, A)`
#   in the book; the file renames the first two
#   `dutch_flag_partition_quadratic` and `dutch_flag_partition_two_pass`
#   so all three can coexist, and keeps `dutch_flag_partition` for the
#   final one. Parameter `A` is renamed `values`; type hints were added.
# - Each book listing starts with `RED, WHITE, BLUE = range(3)`; the file
#   does not define these constants.
# - The book reads `pivot = A[pivot_index]` directly; the file calls the
#   added helper `_validate_pivot`, which raises IndexError for an index
#   outside 0..len-1 (including negative indices). Not in the book.
# - The book's functions return None (they only modify A); every file
#   version also ends with `return values`.
# - Quadratic version: same loop structure as the book.
# - Two-pass version: the book's second pass is
#   `for i in reversed(range(len(A))): if A[i] < pivot: break / elif
#   A[i] > pivot: swap; larger -= 1`. The file instead iterates
#   `reversed(range(smaller, len(values)))` with no `break` and no
#   `< pivot` test. Restructured statement; same intent.
# - Final version: the book advances with the single statement
#   `smaller, equal = smaller + 1, equal + 1`; the file uses two separate
#   `+= 1` statements.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (original list, pivot index). The second one is the
    # book's A = <0,1,2,0,2,1,1> with pivot index 3 (pivot value 0); the
    # first one is added for learning.
    examples = (([3, 1, 2, 1, 3], 1), ([0, 1, 2, 0, 2, 1, 1], 3))
    for original, pivot_index in examples:
        pivot = original[pivot_index]

        # Functions are ordinary objects in Python, so they can be placed
        # in a tuple and looped over; `algorithm(...)` calls each in turn.
        for algorithm in (
            dutch_flag_partition_quadratic,
            dutch_flag_partition_two_pass,
            dutch_flag_partition,
        ):
            result = algorithm(pivot_index, original.copy())
            # `list.copy()` returns a shallow independent copy of the list.
            # Documentation: https://docs.python.org/3/tutorial/datastructures.html
            # Each algorithm mutates its argument, so every one receives a
            # fresh copy and `original` stays unchanged for comparison.

            # Map each value to its group number: 0 = less than the pivot,
            # 1 = equal, 2 = greater. Comparisons produce booleans, and
            # `True + True == 2` because bool is a subclass of int
            # (True == 1, False == 0).
            # Documentation: https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
            categories = [(v > pivot) + (v >= pivot) for v in result]

            # An f-string (prefix f) evaluates the expressions inside {}
            # and inserts their text. `algorithm.__name__` is the
            # function's name as a string.
            # Documentation: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
            print(f"{algorithm.__name__}: {result}")

            # `assert` stops the program with an AssertionError if the
            # condition is false. These are quick smoke checks; pytest
            # provides the more thorough automated verification.
            # sorted() returns a new sorted list
            # (https://docs.python.org/3/library/functions.html#sorted):
            # the first check says the result is a rearrangement of the
            # input; the second says the group numbers never decrease,
            # i.e. less < equal < greater from left to right.
            assert sorted(result) == sorted(original)
            assert categories == sorted(categories)
    print("All three textbook partition implementations passed.")
