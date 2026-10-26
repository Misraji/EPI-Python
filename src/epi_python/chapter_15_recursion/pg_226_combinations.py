"""EPI Python — Exercise 15.5: Generate All Subsets of Size k

Chapter 15: Recursion
Textbook: pages 226–227 (printed page numbers; problem and solution start on 226).

PROBLEM (from the textbook)
---------------------------
"There are a number of testing applications in which it is required to
compute all subsets of a given size for a specified set."

"Write a program which computes all size k subsets of {1, 2, ..., n},
where k and n are program inputs. For example, if k = 2 and n = 5, then
the result is the following:
{{1,2}, {1,3}, {1,4}, {1,5}, {2,3}, {2,4}, {2,5}, {3,4}, {3,5}, {4,5}}"

HINT (from the textbook)
------------------------
"Think of the right function signature."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: compute every subset of {1, ..., n} (conveniently, with
Solution 15.4 on the preceding page) and keep those of size k. That costs
O(n * 2^n) regardless of k; when k is much smaller than n, or nearly n, it
builds many subsets that can never have the right size.

Focused approach by case analysis: a size-k subset either does not contain
1 or does contain 1.
* Without 1: all size-k subsets of {2, 3, ..., n}.
* With 1: all size-(k-1) subsets of {2, 3, ..., n}, each with 1 added.

Example from the book: n = 4, k = 2. Compute all size-2 subsets of
{2,3,4} and all size-1 subsets of {2,3,4}, add 1 to each of the latter,
and take the union:
    {{2,3}, {2,4}, {3,4}} union {{1,2}, {1,3}, {1,4}}.

The book's program combinations(n, k) uses a nested
directed_combinations(offset, partial_combination): when the partial
combination has k elements it is recorded; otherwise, with
num_remaining = k - len(partial_combination) still needed, it tries each
next value i from offset upward, but only while
num_remaining <= n - i + 1 (enough values remain to finish), recursing on
(i + 1, partial_combination + [i]). This file implements the same
recursion (without that pruning test; see TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    combinations(0, 0) -> [[]]                       (one empty subset)
    combinations(3, 0) -> [[]]
    combinations(3, 2) -> [[1, 2], [1, 3], [2, 3]]
    combinations(2, 3) -> []                         (k > n: no subsets)
"""


def combinations(n: int, k: int) -> list[list[int]]:
    """Return all k-element subsets of {1, ..., n}, each in increasing order.

    This is the textbook's recursive implementation (combinations with
    nested directed_combinations), here with nested helper `visit` that
    mutates one partial list with append/pop.
    """

    # Type hints (`n: int`, `-> list[list[int]]`) document intended types
    # only; Python does not enforce them at run time.
    result=[]

    # Nested helper: `next_value` is the smallest value still allowed (the
    # book's `offset`), so values are always chosen in increasing order and
    # each subset is produced exactly once. It mutates the enclosing
    # `result` list; no `nonlocal` is needed since the name is not rebound.
    def visit(next_value: int, partial: list[int]) -> None:

        # A complete size-k subset: store a COPY, because `partial` is the
        # one shared list that later append/pop calls keep changing.
        if len(partial) == k:
            result.append(partial.copy())
            return

        # Try each remaining candidate. range(next_value, n+1) stops BEFORE
        # n+1, so it includes n. Unlike the book, there is no test that
        # enough values remain; branches that cannot reach size k simply
        # run out of values and record nothing.
        for value in range(next_value,n+1):

            # Choose `value`, generate all completions using larger values,
            # then pop() (remove the last item) to undo the choice.
            partial.append(value)
            visit(value+1,partial)
            partial.pop()
    visit(1,[])
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 227)
# --------------------------------------------
# Time complexity: O(n * C(n, k)), where C(n, k) is "n choose k". The
# argument is analogous to the one for the recursive power-set enumeration
# (Solution 15.4, page 225).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Book nested helper `directed_combinations(offset, partial_combination)`;
#   file `visit(next_value: int, partial: list[int])`. Type hints added.
# * Book loop: `i = offset; while i <= n and num_remaining <= n - i + 1:
#   ...; i += 1`, with `num_remaining = k - len(partial_combination)`. This
#   prunes candidates when too few values remain. File: `for value in
#   range(next_value, n+1)` with NO pruning test (same output, but it
#   explores dead-end branches).
# * Book passes a new list `partial_combination + [i]` to each call and
#   stores `list(partial_combination)`; file mutates one list with
#   `append`/`pop` and stores `partial.copy()`.
# * Book's comment "Generate remaining combinations over {offset, ..., n - 1}
#   of size num_remaining." has no counterpart in the original file.
# * Initial call `(1, [])` matches.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples: k = 0 (one empty subset, even when n = 0), an
    # ordinary case, and k > n (no subsets at all).
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite is thorough.
    observed = combinations(0, 0)
    print("combinations:", observed)
    assert observed == [[]]
    observed = combinations(3, 0)
    print("combinations:", observed)
    assert observed == [[]]
    observed = combinations(3, 2)
    print("combinations:", observed)
    assert observed == [[1, 2], [1, 3], [2, 3]]
    observed = combinations(2, 3)
    print("combinations:", observed)
    assert observed == []
