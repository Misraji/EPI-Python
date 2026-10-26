"""EPI Python — Exercise 12.7: Find Smallest Subarray Sequentially Covering All Values

Chapter 12: Hash Tables
Textbook: pages 171–172 (printed page numbers; problem and solution start
on 171, the key recurrence, program and complexity on 172).

PROBLEM (from the textbook)
---------------------------
"In Problem 12.6 on Page 168 we did not differentiate between the order in
which keywords appeared. If the digest has to include the keywords in the
order in which they appear in the search textbox, we may get a different
digest. For example, for the search keywords "Union" and "save", in that
order, the digest would be "Union, and is not either to save".

Write a program that takes two arrays of strings, and return the indices of
the starting and ending index of a shortest subarray of the first array
(the "paragraph" array) that "sequentially covers", i.e., contains all the
strings in the second array (the "keywords" array), in the order in which
they appear in the keywords array. You can assume all keywords are
distinct. For example, let the paragraph array be <apple, banana, cat,
apple>, and the keywords array be <banana, apple>. The paragraph subarray
starting at index 0 and ending at index 1 does not fulfill the
specification, even though it contains all the keywords, since they do not
appear in the specified order. On the other hand, the subarray starting at
index 1 and ending at index 3 does fulfill the specification."

HINT (from the textbook)
------------------------
"For each index in the paragraph array, compute the shortest subarray
ending at that index which fulfills the specification."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: consider every subarray of the paragraph. To test whether one
sequentially covers the keywords, find the first occurrence of the first
keyword -- later occurrences of it never help -- then the first occurrence
of the second keyword AFTER that, and so on; earlier occurrences of the
second keyword can never be in the right order. That test is O(n) for a
paragraph of length n, and there are O(n^2) subarrays, so O(n^3) overall.

O(n^2): the brute force repeats work. Instead, for each start index,
compute the shortest subarray starting there that sequentially covers the
keywords, by moving forward from the start and ticking off the keywords in
order.

O(n): this still repeats work, because the earliest keyword occurrences
can be reused as the scan moves through the paragraph. Two auxiliary hash
tables are kept:
  * keyword -> its most recent occurrence in the paragraph so far;
  * keyword -> the length of the shortest subarray that ends at that most
    recent occurrence and sequentially covers all keywords up to and
    including it.
These let the answer for the first k keywords be built from the answer for
the first k - 1 keywords.

Recurrence: when the ith paragraph string is the jth keyword, set its most
recent occurrence to i. The shortest subarray ending at i that sequentially
covers the first j keywords is the shortest subarray ending at the most
recent occurrence of keyword j - 1, extended by the elements from that
occurrence up to i. (Keyword 0 alone gives a subarray of length 1.) When
j is the last keyword, the resulting subarray is a candidate answer.

The implementation below, find_smallest_sequentially_covering_subset,
follows this method (using lists indexed by keyword position, as the book
also does).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    values=["a","b","x","c","a","b","c"], query=["a","b","c"] -> (4, 6)
    query=[]                                                 -> (0, -1)
                                                  (empty window; added)
    a query word never appearing in order                    -> None
    query with a repeated word                -> raises ValueError (added)
"""


def find_smallest_sequentially_covering_subset(values: list[str], query: list[str]) -> tuple[int, int] | None:
    """Find shortest subarray containing query words in order, with gaps allowed.

    This is the textbook's find_smallest_sequentially_covering_subset (the
    only implementation given). It returns a plain tuple, or None when no
    subarray qualifies (the book returns Subarray(-1, -1)).

    Type hints: `list[str]` arguments; `tuple[int, int] | None` means "a
    pair of ints, or None" (`|` syntax needs Python 3.10+). Python does not
    enforce annotations.
    """

    # No keywords: the empty window (0, -1) trivially covers them. (Added in
    # this file.)
    if not query:
        return (0, -1)

    # set(query) removes duplicates; if its size differs from the list's
    # size, some keyword repeats. The book simply assumes distinct keywords;
    # this file checks it and raises an exception.
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if len(set(query)) != len(query):
        raise ValueError("This educational version expects distinct query words")

    # Book's comment: map each keyword to its index in the keywords array.
    # `{word: i for i, word in enumerate(query)}` is a dict comprehension;
    # enumerate() yields (position, word) pairs.
    # enumerate: https://docs.python.org/3/library/functions.html#enumerate
    query_index = {word: i for i, word in enumerate(query)}

    # Book's comment: since keywords are uniquely identified by their index,
    # those indices can be used to look up in an array (list) instead of a
    # hash table. `[-1] * k` builds a list of k copies of -1 ("not seen").
    latest = [-1] * len(query)

    # Book's comment: for each keyword (by index), the length of the
    # shortest subarray ending at its most recent occurrence that
    # sequentially covers all keywords up to that one. float('inf') (positive
    # infinity) means "no such subarray yet".
    # float: https://docs.python.org/3/library/functions.html#float
    shortest = [float('inf')] * len(query)
    result = None
    for i, word in enumerate(values):

        # dict.get(key) returns the value, or None if the key is absent --
        # so non-keywords give None instead of raising KeyError.
        # dict.get: https://docs.python.org/3/library/stdtypes.html#dict.get
        j = query_index.get(word)

        # `continue` skips to the next loop iteration.
        if j is None:
            continue

        # First keyword: the subarray consisting of just this word.
        if j == 0:
            shortest[j] = 1

        # Later keyword, and the previous keyword has a covering subarray:
        # extend that subarray from the previous keyword's latest position
        # (latest[j - 1]) up to i. That adds i - latest[j - 1] elements.
        elif shortest[j - 1] != float('inf'):
            shortest[j] = shortest[j - 1] + i - latest[j - 1]
        latest[j] = i

        # Book's comment: last keyword, check for an improved subarray.
        if j == len(query) - 1 and shortest[j] != float('inf'):

            # int() turns the stored length into an int (it is an int once
            # set, but the list started out holding floats). The subarray of
            # that length ending at i starts at i - length + 1.
            start = i - int(shortest[j]) + 1

            # Keep it if it is the first answer or strictly shorter.
            if result is None or i - start < result[1] - result[0]:
                result = (start, i)
    return result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 172)
# --------------------------------------------
# Each paragraph entry costs a constant number of lookups and updates, so
# the time complexity is O(n), where n is the length of the paragraph array.
# The additional space is dominated by the three tables (keyword -> index,
# latest occurrence, shortest length), i.e., O(m) for m keywords.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: defines `Subarray = collections.namedtuple('Subarray', ('start',
#   'end'))` and `def find_smallest_sequentially_covering_subset(paragraph,
#   keywords):` with `keyword_to_idx`, `latest_occurrence`,
#   `shortest_subarray_length` and a separate `shortest_distance =
#   float('inf')` holding the best length found; inside the loop it tests
#   `if p in keyword_to_idx:`, computes a `distance_to_previous_keyword`
#   temporary, and for the last keyword updates when
#   `shortest_subarray_length[-1] < shortest_distance`, setting
#   `result = Subarray(i - shortest_distance + 1, i)`. Returns
#   Subarray(-1, -1) if nothing qualifies.
# File: no Subarray namedtuple -- returns a plain tuple or None; parameters
#   renamed `values: list[str]`, `query: list[str]` with a return hint;
#   adds `(0, -1)` for an empty query and a ValueError for repeated
#   keywords (book assumes distinct); variable names shortened
#   (`query_index`, `latest`, `shortest`, `j`); uses `dict.get` plus
#   `continue` instead of an `in` test; no `distance_to_previous_keyword`
#   temporary; no `shortest_distance` variable -- the best is compared via
#   the stored result's end minus start (equivalent strict comparison).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Both indices 0..3 ("a","b","x","c") and 4..6 ("a","b","c") contain
    # a, b, c in order; the second is shorter, so (4, 6) is expected.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, while pytest provides the more
    # thorough automated verification.
    words=["a","b","x","c","a","b","c"]
    print("ordered cover:", find_smallest_sequentially_covering_subset(words,["a","b","c"]))
    assert find_smallest_sequentially_covering_subset(words,["a","b","c"]) == (4,6)
