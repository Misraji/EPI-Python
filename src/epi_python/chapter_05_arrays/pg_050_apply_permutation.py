"""EPI Python — Exercise 5.10: Permute the Elements of an Array

Chapter 5: Arrays
Textbook: pages 50–52 (printed page numbers; the topic is introduced at
the bottom of page 50, the problem and first program are on page 51, and
the second program and variant are on page 52).

PROBLEM (from the textbook)
---------------------------
Context: "A permutation is a rearrangement of members of a sequence into a
new sequence. For example, there are 24 permutations of <a,b,c,d>; some of
these are <b,a,d,c>, <d,a,b,c>, and <a,d,b,c>."

"A permutation can be specified by an array P, where P[i] represents the
location of the element at i in the permutation. For example, the array
<2,0,1,3> represents the permutation that maps the element at location 0
to location 2, the element at location 1 to location 0, the element at
location 2 to location 1, and keep the element at location 3 unchanged. A
permutation can be applied to an array to reorder the array. For example,
the permutation <2,0,1,3> applied to A = <a,b,c,d> yields the array
<b,c,a,d>."

"Given an array A of n elements and a permutation P, apply P to A."

HINT (from the textbook)
------------------------
"Any permutation can be viewed as a set of cyclic permutations. For an
element in a cycle, how would you identify if it has been permuted?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
With extra storage it is easy: allocate a new array B of the same length,
set B[P[i]] = A[i] for every i, then copy B back into A. Time O(n), extra
space O(n).

To save space, break the permutation into simpler pieces processed one at
a time. Book example: permutation <3,2,1,0> applied to A = <α,b,c,δ>
(symbols as printed). Move the element at index 0 (α) to index 3 and the
element that was at index 3 (δ) to index 0. Then move the element at
index 1 (b) to index 2 and the one at index 2 (c) to index 1. Everything
has now moved as required, and the result is <δ,c,b,α>.

In general every permutation is a collection of independent cyclic
permutations, each of which shifts its elements by a fixed offset with
wrap-around. A single cycle can be carried out one element at a time with
constant extra storage, so applying the cycles one after another needs
only constant extra storage overall. The task becomes: identify the
disjoint cycles.

To find and apply the cycle containing entry i, keep following i -> P[i]
until returning to i. Afterwards we must find a cycle not yet applied;
storing one Boolean per element would make that easy (but uses O(n)
space). The book avoids that by using the sign bit of the permutation
entries: subtract n from P[i] once its move is done, so a negative P[i]
means "already performed".

Book walk-through applying <3,1,2,0>: start with entry 0, whose value is
3. Move A[0] to A[3], first saving the original A[3]; the permutation
becomes <-1,1,2,0>. Move (the saved) A[3] to A[0]. Since P[0] is negative,
the cycle starting at 0 is finished; the permutation is now
<-1,1,2,-4>. Next look at P[1]: it is not negative, so its cycle has not
been applied yet; continue in the same way.

The book prints this sign-marking program (here `apply_permutation`) and,
after discussing it, a second program that does not modify P (here
`apply_permutation_without_sign_marking`). The file also has
`apply_permutation_visited`, written for this repository, which uses the
Boolean-array idea the book mentions only in words.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    perm=[0, 1], values=[7, 8] -> [7, 8]   (identity permutation)
    perm=[],     values=[]     -> []
The `['a','b','c','d']` example in `__main__` is the book's <2,0,1,3>
example.
"""


# `perm: list[int]` etc. are type hints: they document intended types,
# but Python does not enforce them at run time. `list[int]` requires
# Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def apply_permutation(perm: list[int], values: list[int]) -> list[int]:
    """Textbook O(n) time, O(1) extra space using negative permutation marks.

    This is the book's first `apply_permutation(perm, A)` program. `values`
    is rearranged in place and returned; `perm` is temporarily modified
    and then restored.
    """

    # Length check added in this repository (not in the book).
    # Documentation: https://docs.python.org/3/library/exceptions.html#ValueError
    if len(values) != len(perm):
        raise ValueError("Permutation and input must have equal lengths")
    n = len(perm)
    for start in range(n):

        # Book comment: "Check if the element at index i has not been moved
        # by checking if perm[i] is nonnegative."
        current = start
        while perm[current] >= 0:
            destination = perm[current]

            # Swap via tuple packing/unpacking: the element waiting at
            # `start` goes to its destination, and the element displaced
            # from there is parked at `start` for the next step.
            values[start], values[destination] = values[destination], values[start]

            # Book comment: "Subtracts len(perm) from an entry in perm to
            # make it negative, which indicates the corresponding move has
            # been performed." Valid entries are 0..n-1, so after
            # subtracting n they lie in -n..-1 and can be restored exactly.
            perm[current] -= n
            current = destination

    # Book comment: "Restore perm."
    # `perm[:] = ...` is slice assignment: it replaces the contents of the
    # EXISTING list object (callers holding a reference see the change),
    # whereas `perm = ...` would just rebind the local name. The list
    # comprehension builds the restored values `entry + n`.
    # Slice assignment changes entries in the EXISTING permutation list,
    # preserving its identity and restoring all original nonnegative values.
    perm[:] = [entry + n for entry in perm]
    return values


def apply_permutation_without_sign_marking(perm: list[int], values: list[int]) -> list[int]:
    """Textbook second method: process a cycle only from its minimum index.

    This is the book's second `apply_permutation(perm, A)` program. It
    never modifies `perm`, at the cost of O(n^2) time in the worst case.
    """
    if len(values) != len(perm):
        raise ValueError("Permutation and input must have equal lengths")

    # A function defined inside another function. It can read `perm` and
    # `values` from the enclosing function (a closure), so they need not
    # be passed as parameters. It mutates the list `values` but never
    # rebinds the name, so no `nonlocal` declaration is required.
    # Documentation: https://docs.python.org/3/reference/executionmodel.html#resolution-of-names
    def permute_cycle(start: int) -> None:

        # Apply one cycle: carry `saved` (the element that must move next)
        # around the cycle, dropping it at each destination and picking up
        # the element that was there.
        current, saved = start, values[start]
        while True:
            destination = perm[current]

            # Tuple assignment: the right side (saved, values[destination])
            # is evaluated first, so this stores `saved` into the slot and
            # simultaneously picks up the slot's previous element.
            values[destination], saved = saved, values[destination]
            current = destination

            # Back at the start: the whole cycle has been applied.
            if current == start:
                break

    for start in range(len(values)):

        # Book comment: "Traverses the cycle to see if i is the minimum
        # element." Walk the cycle from perm[start]; meeting a smaller
        # index means this cycle was handled from that smaller index.
        current = perm[start]
        while current != start:
            if current < start:
                break
            current = perm[current]
        else:
            # `while ... else` executes its else only when no `break`
            # occurred. That proves `start` is minimal in this cycle.
            # Documentation: https://docs.python.org/3/tutorial/controlflow.html#else-clauses-on-loops
            permute_cycle(start)
    return values


def apply_permutation_visited(perm: list[int], values: list[int]) -> list[int]:
    """Previous repository reconstruction (not in the PDF): O(n) visited bits.

    The book describes this Boolean-array idea in words ("allocate an array
    of n Booleans indicating whether the element at index i has been
    processed") but prints no program for it.
    """
    if len(values) != len(perm):
        raise ValueError("Permutation and input must have equal lengths")

    # One flag per position, all False initially.
    visited = [False] * len(values)
    for start in range(len(values)):

        # `continue` skips to the next loop iteration: this position's
        # cycle has already been applied.
        if visited[start]:
            continue
        position, saved = start, values[start]
        while not visited[position]:
            visited[position] = True
            dest = perm[position]

            # Drop `saved` at its destination and pick up the element that
            # was there (tuple assignment evaluates the right side first).
            values[dest], saved = saved, values[dest]
            position = dest
    return values


# TEXTBOOK POST-SOLUTION DISCUSSION (page 52)
# ------------------------------------------
# The sign-marking program applies the permutation in O(n) time. Its space
# complexity is O(1), assuming we are allowed to modify the sign bit of
# the permutation entries temporarily.
#
# If the sign bit is not available, one can allocate n Booleans recording
# whether index i has been processed (O(n) space). Alternatively, O(n)
# storage can be avoided by scanning left to right and applying a cycle
# only when the current position is the leftmost position in that cycle
# (the second program). Checking whether a position is the leftmost one
# requires traversing the cycle again, which raises the run time to
# O(n^2).
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): Given an array A of
# integers representing a permutation, update A to represent the inverse
# permutation using only constant additional storage.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book program 1: `def apply_permutation(perm, A)`; file keeps the name,
#   renames `A` -> `values`, `i` -> `start`, `next` -> `current`,
#   `temp` -> `destination`, adds type hints, a length-check ValueError,
#   caches `n = len(perm)`, and adds `return values` (book returns None).
#   Book's swap `A[i], A[perm[next]] = A[perm[next]], A[i]` uses the
#   precomputed `destination`. Restore line matches
#   (`perm[:] = [a + len(perm) for a in perm]`).
# - Book program 2 (also named `apply_permutation(perm, A)`): file name
#   `apply_permutation_without_sign_marking`. Book's inner helper is
#   `cyclic_permutation(start, perm, A)` using `next_i`/`next_temp`
#   temporaries; file's inner `permute_cycle(start)` reads `perm`/`values`
#   from the enclosing scope and swaps with one tuple assignment. The
#   leftmost-index test with `while ... else` matches (variable `j` ->
#   `current`). Length check and `return values` added.
# - `apply_permutation_visited` is not printed in the book (only described
#   in prose).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Each example is (permutation, array, expected result). The first is
    # the book's <2,0,1,3> applied to <a,b,c,d>; the other two are added
    # (identity permutation and empty input).
    examples = (([2,0,1,3],['a','b','c','d'],['b','c','a','d']),
                ([0,1],[7,8],[7,8]),([],[],[]))
    for perm,values,expected in examples:

        # Functions are objects, so they can be listed in a tuple and
        # called in turn.
        for algorithm in (apply_permutation, apply_permutation_without_sign_marking,
                          apply_permutation_visited):

            # `list.copy()` gives each algorithm fresh lists, since all of
            # them mutate their arguments.
            permutation_copy, array_copy = perm.copy(), values.copy()
            observed = algorithm(permutation_copy, array_copy)

            # f-string: `{...}` expressions are evaluated and inserted;
            # `algorithm.__name__` is the function's name.
            # Documentation: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
            print(f"{algorithm.__name__}: {observed}")

            # `assert` stops the program with an AssertionError if a
            # condition is false. The second check confirms that `perm`
            # ends up unchanged (restored, in the sign-marking version).
            # pytest provides the more thorough automated verification.
            assert observed == expected
            assert permutation_copy == perm
