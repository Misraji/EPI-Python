"""EPI Python — Exercise 11.2: Search a Sorted Array for Entry Equal to Its Index

Chapter 11: Searching
Textbook: pages 146–147 (printed page numbers; problem and solution start
on 146, end of the program, complexity and variant on 147).

PROBLEM (from the textbook)
---------------------------
"Design an efficient algorithm that takes a sorted array of distinct
integers, and returns an index i such that the element at index i equals i.
For example, when the input is <-2, 0, 2, 3, 6, 7, 9> your algorithm should
return 2 or 3."

HINT (from the textbook)
------------------------
"Reduce this problem to ordinary binary search."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: loop over the array and test whether the entry at position i
equals i. That costs O(n) time for an array of length n.

The brute-force loop ignores two facts about the array A: it is sorted, and
its entries are distinct. Because the entries are distinct integers, each
one is at least 1 larger than the one before it, so the difference
A[i] - i can only stay the same or grow as i increases. Consequences:
  * If A[j] > j, no index after j can satisfy A[i] == i.
  * If A[j] < j, for the same reason no index before j can satisfy it.

These two observations already give a binary-search-style algorithm. The
book points out a slightly simpler way to view it: imagine a secondary
array B with B[i] = A[i] - i. B is sorted, so the task is just ordinary
binary search for 0 in B. B never has to be built; wherever B[i] would be
read, compute A[i] - i instead.

Book's example: for A = <-2, 0, 2, 3, 6, 7, 9>, the secondary array is
B = <-2, -1, 0, 0, 2, 2, 3>. A binary search for 0 in B returns index 2
or index 3, both of which are correct answers.

The implementation below, search_entry_equal_to_index, follows this idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    [-2, 0, 2, 5] -> 2
    [1, 2, 3]     -> -1 (every entry is larger than its index)
    []            -> -1 (empty array)
    [0]           -> 0
"""


def search_entry_equal_to_index(sorted_distinct: list[int]) -> int:
    """Find any index i with a[i] == i, or return -1.

    This is the textbook's search_entry_equal_to_its_index (the only
    implementation given), written by comparing A[mid] with mid directly
    instead of first computing the difference A[mid] - mid.

    Type hints: `list[int]` and `-> int` document the expected argument and
    return types; Python does not check them at run time.
    """

    # Tuple unpacking sets both ends of the candidate range in one line.
    # For an empty list right is -1, so the loop is skipped and -1 returned.
    left,right = 0,len(sorted_distinct)-1
    while left <= right:

        # `//` is floor division, giving an int index between left and right.
        middle=(left+right)//2

        # Equivalent to the book's test "difference == 0", where
        # difference = A[mid] - mid (the imaginary B[mid]).
        if sorted_distinct[middle] == middle:
            return middle

        # A[mid] > mid means B[mid] > 0: since B never decreases, every
        # later index also has A[i] > i, so search only the left part.
        if sorted_distinct[middle] > middle:
            right = middle-1

        # A[mid] < mid means B[mid] < 0: no earlier index can work, so
        # search only the right part.
        else:
            left = middle+1
    return -1


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 146–147)
# -------------------------------------------------
# Time complexity: the same as binary search, O(log n), where n is the
# length of A. Extra space is O(1) because B is never materialised.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Solve the same problem
#   when A is sorted but may contain duplicates. (Note: with duplicates,
#   A[i] - i is no longer guaranteed to be nondecreasing, so the pruning
#   argument above does not apply.)


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def search_entry_equal_to_its_index(A):` computes
#   `difference = A[mid] - mid` (comment: "A[mid] == mid if and only if
#   difference == 0.") and branches with if / elif / else on
#   `difference == 0`, `difference > 0` and `# difference < 0.`.
# File: function renamed `search_entry_equal_to_index`; parameter renamed
#   `sorted_distinct: list[int]`, return hint `-> int` added; `mid` renamed
#   `middle`; no `difference` variable -- the tests compare
#   `sorted_distinct[middle]` with `middle` directly, using `if` / `if` /
#   `else` instead of `if` / `elif` / `else` (the first branch returns, so
#   the behaviour is the same).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior: a normal
    # hit, an array with no fixed point, an empty array, and a one-element
    # array whose only entry matches.
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value. These are quick smoke checks;
    # pytest provides the more thorough automated verification.
    observed = search_entry_equal_to_index([-2, 0, 2, 5])
    print("search_entry_equal_to_index:", observed)
    assert observed == 2
    observed = search_entry_equal_to_index([1, 2, 3])
    print("search_entry_equal_to_index:", observed)
    assert observed == -1
    observed = search_entry_equal_to_index([])
    print("search_entry_equal_to_index:", observed)
    assert observed == -1
    observed = search_entry_equal_to_index([0])
    print("search_entry_equal_to_index:", observed)
    assert observed == 0
