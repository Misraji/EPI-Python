"""EPI Python — Exercise 5.11: Compute the Next Permutation

Chapter 5: Arrays
Textbook: pages 52–54 (printed page numbers; dictionary ordering is
introduced at the bottom of page 52, the problem and solution are on page
53, and the end of the program, complexity and variants are on page 54).

PROBLEM (from the textbook)
---------------------------
Context: "There exist exactly n! permutations of n elements. These can be
totally ordered using the dictionary ordering—define permutation p to
appear before permutation q if in the first place where p and q differ in
their array representations, starting from index 0, the corresponding
entry for p is less than that for q. For example, <2,0,1> < <2,1,0>. Note
that the permutation <0,1,2> is the smallest permutation under dictionary
ordering, and <2,1,0> is the largest permutation under dictionary
ordering."

"Write a program that takes as input a permutation, and returns the next
permutation under dictionary ordering. If the permutation is the last
permutation, return the empty array. For example, if the input is
<1,0,3,2> your function should return <1,2,0,3>. If the input is
<3,2,1,0>, return <>."

HINT (from the textbook)
------------------------
"Study concrete examples."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: generate every permutation of the same length, sort them in
dictionary order, and pick the one after the input. Besides its huge time
and space cost, generating all permutations of length n is itself a
nontrivial problem (the book points to Problem 15.3 on page 222).

Key insight: increase the permutation by as little as possible, a bit
like a car odometer ticking over, except that values cannot change, only
be reordered. The book develops the idea on <6,2,1,5,4,3,0>:

  - From the right, find the longest decreasing suffix: <5,4,3,0>. That
    suffix is already as large as it can be, so changing only it cannot
    give the next permutation.
  - Look at the entry e just before that suffix: here e = 1. (If there is
    no such entry, the whole permutation is decreasing, i.e. it is
    <n-1, n-2, ..., 2, 1, 0>, and there is no next permutation.)
  - e is smaller than some suffix entry (at least the one right after
    it). Swap e with the SMALLEST suffix entry s that is larger than e,
    to change the prefix (the part before the suffix) as little as
    possible. Here s = 3, and swapping gives <6,2,3,5,4,1,0>.
  - Not finished: the new prefix is the smallest possible among
    permutations greater than the input, but the suffix may not be
    smallest. Sorting the suffix ascending fixes that, giving <0,1,4,5>
    for the example (so the answer is <6,2,3,0,1,4,5>).
  - Optimization: no general sort is needed. The suffix was decreasing
    and remains decreasing after s is replaced by e, so simply reversing
    it sorts it ascending.

The general algorithm, as the book lists it:
  (1) Find k such that p[k] < p[k + 1] and the entries after index k are
      in decreasing order.
  (2) Find the smallest p[l] such that p[l] > p[k] (such an l must exist
      since p[k] < p[k + 1]).
  (3) Swap p[l] and p[k] (the sequence after position k stays in
      decreasing order).
  (4) Reverse the sequence after position k.

The book prints one program, `next_permutation(perm)`, which modifies its
argument; it corresponds to `next_permutation_in_place` here. The file's
`next_permutation` is a repository version that works on a copy.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []        -> []
    [1]       -> []           (only one permutation exists)
    [1, 2, 3] -> [1, 3, 2]
    [3, 2, 1] -> []           (already the largest)
"""



# `values: list[int]` and `-> list[int]` are type hints that document the
# intended types; Python does not enforce them at run time. `list[int]`
# requires Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def next_permutation(values: list[int]) -> list[int]:
    """Lexicographically next permutation, or [] if this is the last.

    Repository version of the textbook algorithm that leaves `values`
    unchanged by working on a copy (the book's program modifies its
    input; see `next_permutation_in_place`).
    """

    # `list.copy()` returns a new (shallow) list with the same elements.
    # Documentation: https://docs.python.org/3/tutorial/datastructures.html
    result = values.copy()

    # Step (1): scan from the right for the first entry smaller than the
    # entry after it. `pivot` is the book's "inversion_point" (k).
    pivot = len(result) - 2
    while pivot >= 0 and result[pivot] >= result[pivot + 1]:
        pivot -= 1

    # No such entry: the whole list is non-increasing, so it is the last
    # permutation. (This also covers lists of length 0 and 1.)
    if pivot < 0:
        return []

    # Step (2): the suffix after `pivot` is decreasing, so scanning from
    # the right, the first entry larger than result[pivot] is the
    # smallest such entry.
    swap = len(result) - 1
    while result[swap] <= result[pivot]:
        swap -= 1

    # Step (3): swap them using tuple packing/unpacking.
    result[pivot], result[swap] = result[swap], result[pivot]

    # Step (4): reverse the suffix. On the right, the slice
    # `result[pivot + 1:]` makes a temporary copy of the suffix, and the
    # built-in reversed() returns an iterator over that copy from last to
    # first. On the left, slice assignment replaces exactly that suffix of
    # `result` with the iterator's items.
    # Documentation: https://docs.python.org/3/library/functions.html#reversed
    # Documentation: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
    result[pivot + 1:] = reversed(result[pivot + 1:])
    return result



def next_permutation_in_place(permutation: list[int]) -> list[int]:
    """Textbook variant modifies the input rather than copying it.

    This is the book's `next_permutation(perm)` program. It returns the
    same (modified) list, or [] for the last permutation (in which case
    the input is left unchanged).
    """

    # Book comment: "Find the first entry from the right that is smaller
    # than the entry immediately after it."
    pivot = len(permutation) - 2
    while pivot >= 0 and permutation[pivot] >= permutation[pivot+1]:
        pivot -= 1

    # Book comment on its `return []`: "perm is the last permutation."
    if pivot < 0:
        return []

    # Book comment: "Swap the smallest entry after index inversion_point
    # that is greater than perm[inversion_point]. Since entries in perm are
    # decreasing after inversion_point, if we search in reverse order, the
    # first entry that is greater than perm[inversion_point] is the entry
    # to swap with."
    # `range(len - 1, pivot, -1)` counts down from the last index to
    # pivot + 1 (start, stop exclusive, step -1).
    for j in range(len(permutation)-1, pivot, -1):
        if permutation[j] > permutation[pivot]:
            permutation[j], permutation[pivot] = permutation[pivot], permutation[j]
            break

    # Book comment: "Entries in perm must appear in decreasing order after
    # inversion_point, so we simply reverse these entries to get the
    # smallest dictionary order."
    # The right-hand slice makes a temporary copy of the suffix;
    # `reversed` then reads that copy backward, and slice assignment
    # replaces only the suffix of the original list (the list object
    # itself stays the same).
    # Documentation: https://docs.python.org/3/library/functions.html#reversed
    permutation[pivot+1:] = reversed(permutation[pivot+1:])
    return permutation


# TEXTBOOK POST-SOLUTION DISCUSSION (page 54)
# ------------------------------------------
# Each step is a single pass over (part of) the array, so the time
# complexity is O(n). Only a few local variables are used, so the
# additional space complexity is O(1) (for the book's in-place program).
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Compute the kth
# permutation under dictionary ordering, starting from the identity
# permutation (which is the first permutation in dictionary ordering).
#
# Variant 2 (stated in the book; no solution given): Given a permutation
# p, return the permutation corresponding to the previous permutation of
# p under dictionary ordering.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def next_permutation(perm)`, variables `inversion_point` and
#   `i`, test `if inversion_point == -1`, swap loop
#   `for i in reversed(range(inversion_point + 1, len(perm)))`.
# - `next_permutation_in_place(permutation)` is the book's program with
#   renamed parameter/variables (`pivot`, `j`), `if pivot < 0`, the swap
#   loop written as `range(len(permutation)-1, pivot, -1)`, and type hints.
# - `next_permutation(values)` (same name as the book's function) is a
#   repository version that copies the input first and finds the swap
#   index with a `while` loop instead of a `for`/`break`. It does not
#   modify the caller's list.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    #
    # The first four examples are added for learning. print() with several
    # arguments separates them with a space. `assert` stops the program
    # with an AssertionError if a condition is false; pytest provides the
    # more thorough automated verification.
    observed = next_permutation([])
    print("next_permutation:", observed)
    assert observed == []
    observed = next_permutation([1])
    print("next_permutation:", observed)
    assert observed == []
    observed = next_permutation([1, 2, 3])
    print("next_permutation:", observed)
    assert observed == [1, 3, 2]
    observed = next_permutation([3, 2, 1])
    print("next_permutation:", observed)
    assert observed == []

    # The book's example <1,0,3,2> -> <1,2,0,3>. id() returns an integer
    # identifying an object; comparing ids shows the textbook version
    # changed the very same list rather than building a new one.
    # Documentation: https://docs.python.org/3/library/functions.html#id
    sample = [1, 0, 3, 2]
    sample_id = id(sample)
    assert next_permutation_in_place(sample) == [1, 2, 0, 3]
    print("Textbook next permutation:", sample)
    assert id(sample) == sample_id
