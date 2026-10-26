"""EPI Python — Exercise 12.6: Find the Smallest Subarray Covering All Values

Chapter 12: Hash Tables
Textbook: pages 168–171 (printed page numbers; problem and solution start
on 168, worked example and first program on 169, second program on 170,
variants at the top of 171).

PROBLEM (from the textbook)
---------------------------
"When you type keywords in a search engine, the search engine will return
results, and each result contains a digest of the web page, i.e., a
highlighting within that page of the keywords that you searched for. For
example, a search for the keywords "Union" and "save" on a page with the
text of the Emancipation Proclamation should return the result shown in
Figure 12.1."

    My paramount object in this struggle is to [save the Union], and is
    not either to save or to destroy slavery. If I could save the Union
    without freeing any slave I would do it, and if I could save it by
    freeing all the slaves I would do it; and if I could save it by
    freeing some and leaving others alone I would also do that.
    (Figure 12.1: Search result with digest in boldface and search
    keywords underlined. Here the bold digest is shown in [brackets];
    "save" and "Union" inside it are the underlined keywords.)

"The digest for this page is the text in boldface, with the keywords
underlined for emphasis. It is the shortest substring of the page which
contains all the keywords in the search. The problem of computing the
digest is abstracted as follows.

Write a program which takes an array of strings and a set of strings, and
return the indices of the starting and ending index of a shortest subarray
of the given array that "covers" the set, i.e., contains all strings in the
set."

HINT (from the textbook)
------------------------
"What is the maximum number of minimal subarrays that can cover the query?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: try every subarray and test whether it contains all strings of
the set. An array of length n has O(n^2) subarrays, and each test is O(n)
using a hash table to record which strings are present, so O(n^3) overall.

O(n^2): grow subarrays incrementally. For each start i, extend the
subarray one element at a time in order of increasing length and stop as
soon as the set is covered. A hash table records which set strings are
still uncovered, and each one-element extension updates it in O(1).

O(n): reuse work between consecutive starts. Suppose the smallest
subarray starting at i that covers the set ends at j. Subarrays starting at
i + 1 and ending before j cannot cover the set, so there is no point
looking at them. When moving to i + 1, either the set is still covered, or
j must be advanced until it is covered again. Each step advances one of i
or j, which gives O(n) time (the sliding-window / two-pointer technique).

Book's worked example: array <apple, banana, apple, apple, dog, cat, apple,
dog, banana, apple, cat, dog> (indices 0..11), set {banana, cat}.
  * The smallest covering subarray starting at 0 ends at 5.
  * Advance the start to 1: index 0 was not in the set, so it still ends
    at 5.
  * Advance to 2: the set is no longer covered, so the end moves from 5 to
    8; the subarray 2..8 covers the set.
  * The start advances 2 -> 3 -> 4 -> 5 while the set remains covered.
  * At start 6 coverage is lost, so the end advances until 10.
  * The start can advance to 8 and still cover the set; after moving past
    8 the set cannot be covered.
  * The shortest covering subarray is from 8 to 10.

Streaming alternative (the book's second program, see the post-solution
notes): avoids keeping subarrays in memory.

This file implements only the first (sliding-window) program, as
smallest_subarray_covering_set. The book's second, streaming program
(find_smallest_subarray_covering_subset, with a doubly linked list) is NOT
implemented in this file; see TEXTBOOK CODE COMPARISON.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    values=["a","x","b","a","c","b"], required={"a","b","c"} -> (2, 4)
    required=set()                                           -> (0, -1)
                                                    (empty window; added)
    a required word missing from values                      -> None
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# Counter API: https://docs.python.org/3/library/collections.html#collections.Counter
#
# `from collections import Counter` imports just that one name, so the code
# can write Counter(...) instead of collections.Counter(...).
from collections import Counter


def smallest_subarray_covering_set(values: list[str], required: set[str]) -> tuple[int, int] | None:
    """Return inclusive (start,end) of shortest window containing all required keys.

    This is the textbook's find_smallest_subarray_covering_set (the first,
    sliding-window program). It returns None when no window covers the set
    (the book returns Subarray(-1, -1)).

    Type hints: `list[str]`, `set[str]`, and `tuple[int, int] | None` ("a
    pair of ints, or None"; the `|` syntax needs Python 3.10+). Python does
    not enforce annotations.
    """

    # An empty set is covered by the empty window; (0, -1) represents an
    # empty inclusive range. (Special case added in this file.)
    if not required:
        return (0, -1)

    # Counter(iterable) maps each item to its count. Built from a SET, every
    # required word starts with count 1 -- "one copy still needed". Counts
    # fall as words enter the window and may go negative when a word appears
    # several times inside it; they rise again as words leave. Reading a
    # missing key from a Counter returns 0 rather than raising KeyError.
    # (The `in need` tests below still only match required words, because
    # reading a key does not insert it.)
    need = Counter(required)

    # How many distinct required words are not yet in the window.
    still_missing = len(required)
    left = 0
    best = None

    # enumerate() yields (index, value) pairs; `right` is the window's
    # inclusive right end and advances one step per iteration.
    # enumerate: https://docs.python.org/3/library/functions.html#enumerate
    for right, value in enumerate(values):
        if value in need:

            # The first copy of a still-needed word reduces the number of
            # missing words; extra copies only make its count negative.
            if need[value] > 0:
                still_missing -= 1
            need[value] -= 1

        # Book's comment: keep advancing left until the window no longer
        # contains all keywords. Each time it is covering, it is a candidate
        # answer.
        while still_missing == 0:

            # `best is None` handles the first window found; otherwise keep
            # the strictly shorter window (ties keep the earlier one).
            # best[1] - best[0] is the stored window's end minus start.
            if best is None or right - left < best[1] - best[0]:
                best = (left, right)

            # Remove values[left] from the window. If it was the last copy
            # of a required word, that word becomes missing again.
            outgoing = values[left]
            if outgoing in need:
                need[outgoing] += 1
                if need[outgoing] > 0:
                    still_missing += 1
            left += 1
    return best


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 169–171)
# -------------------------------------------------
# Complexity of the sliding-window program: O(n), where n is the array's
# length, because each of the two indices advances at most n - 1 times and
# each advance costs O(1). Extra space is proportional to the number of
# keywords.
#
# Drawback: the subarrays must be kept in memory (the program indexes back
# into the array with `left`). A streaming algorithm is possible by
# tracking the latest occurrence of each query keyword while processing A:
#   * a doubly linked list L stores the last occurrence (index) of each
#     keyword in Q, and a hash table H maps each keyword to its node in L;
#   * when a word of Q is seen, its old node is removed from L (found via H),
#     a new node holding the current index is appended to the end of L, and
#     H is updated;
#   * L is thereby ordered by position in A, so when L holds all n_Q
#     keywords, the current index minus the index in L's first node is the
#     length of a covering subarray ending here; if it beats the current
#     best, the best is updated.
# This streaming version is still O(n). The book prints it as
# find_smallest_subarray_covering_subset(stream, query_strings), with
# nested classes DoublyLinkedListNode and LinkedList (methods __len__,
# insert_after, remove). It is not implemented in this file.
#
# VARIANTS
# --------
# Variant 1 (stated in the book; no solution given): Given an array A, find
#   a shortest subarray A[i, j] such that each distinct value present in A
#   is also present in the subarray.
#
# Variant 2 (stated in the book; no solution given): Given an array A,
#   rearrange the elements so that the shortest subarray containing all the
#   distinct values in A has maximum possible length.
#
# Variant 3 (stated in the book; no solution given): Given an array A and a
#   positive integer k, rearrange the elements so that no two equal
#   elements are k or less apart.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book, first program: defines
#   `Subarray = collections.namedtuple('Subarray', ('start', 'end'))` and
#   `def find_smallest_subarray_covering_set(paragraph, keywords):` with
#   `keywords_to_cover = collections.Counter(keywords)`,
#   `result = Subarray(-1, -1)`, `remaining_to_cover = len(keywords)`; in the
#   loop it decrements first and then tests `>= 0`; the window test is
#   `result == (-1, -1) or right - left < result[1] - result[0]`; the
#   outgoing word is `pl`; returns `result` (Subarray(-1, -1) if none).
# File: imports `from collections import Counter`; function renamed
#   `smallest_subarray_covering_set`; parameters `values: list[str]`,
#   `required: set[str]` with return hint `tuple[int, int] | None`; no
#   Subarray namedtuple -- returns a plain tuple, or None when nothing
#   covers the set (book: (-1, -1)); adds `(0, -1)` for an empty required
#   set; membership is tested against the Counter (`in need`) rather than
#   the keyword set; tests `need[value] > 0` BEFORE decrementing (same
#   effect as the book's decrement-then-`>= 0`); variables renamed
#   (`need`, `still_missing`, `best`, `outgoing`).
# Book, second program: `find_smallest_subarray_covering_subset(stream,
#   query_strings)` (streaming, doubly linked list) is MISSING from this
#   file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # In ["a","x","b","a","c","b"] the shortest window holding a, b and c
    # is indices 2..4 ("b","a","c"). `{"a","b","c"}` is a set literal.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, while pytest provides the more
    # thorough automated verification.
    words=["a","x","b","a","c","b"]
    print("covering window:", smallest_subarray_covering_set(words,{"a","b","c"}))
    assert smallest_subarray_covering_set(words,{"a","b","c"}) == (2,4)
