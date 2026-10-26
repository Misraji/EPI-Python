"""EPI Python — Exercise 17.5: Find the Majority Element

Chapter 17: Greedy Algorithms and Invariants
Textbook: pages 266–267 (printed page numbers; problem, solution and the
start of the program on 266; rest of program and discussion on 267).

PROBLEM (from the textbook)
---------------------------
Several applications require identification of elements in a sequence
which occur more than a specified fraction of the total number of elements
in the sequence. For example, we may want to identify the users using
excessive network bandwidth or IP addresses originating the most Hypertext
Transfer Protocol (HTTP) requests. Here we consider a simplified version of
this problem.

You are reading a sequence of strings. You know a priori that more than
half the strings are repetitions of a single string (the "majority
element") but the positions where the majority element occurs are unknown.
Write a program that makes a single pass over the sequence and identifies
the majority element. For example, if the input is
<b, a, c, a, a, b, a, a, c, a>, then a is the majority element (it appears
in 6 out of the 10 places).

HINT (from the textbook)
------------------------
Take advantage of the existence of a majority element to perform
elimination.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: count every distinct element in a hash table. O(n) time, but
also O(n) space, where n is the number of elements.

Randomized sampling can find a majority element with high probability using
less storage, but it is not exact.

Better idea: split the entries into two groups, those equal to the
majority element and those that are not. The first group is known to be
larger. If two DIFFERENT entries are seen, at most one of them can be the
majority element, so discarding both keeps the difference between the
group sizes the same; the majority of the remaining entries is unchanged.

Algorithm: keep a candidate and a count, starting with the first entry.
For each further entry: if it equals the candidate, increment the count;
otherwise decrement it. When the count reaches zero, the next entry becomes
the new candidate.

Mathematical justification: let the majority element occur m times among n
entries, so m/n > 1/2. Of the two distinct discarded entries, at most one is
the majority element, so afterwards the ratio of remaining majority
elements to remaining elements is either m/(n - 2) (neither discarded entry
was the majority) or (m - 1)/(n - 2) (one was). It is simple to verify that
if m/n > 1/2, then both m/(n - 2) > 1/2 and (m - 1)/(n - 2) > 1/2.

Book worked example: <b, a, c, a, a, b, a, a, c, a>. The candidate starts
as b. Next, a differs, so the count drops to 0; the next element c becomes
the candidate with count 1. Then a differs, count back to 0. The next
element a becomes the candidate; the following b decrements the count to 0.
The next element, a, becomes the candidate again and keeps a nonzero count
until the end.

The book's program is majority_search(input_stream), which returns the
candidate. This file's majority_search uses the same voting loop but also
adds a verifying count (see TEXTBOOK CODE COMPARISON below).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []               -> None (no elements)
    ['a', 'a', 'b']  -> 'a'
    ['a', 'b']       -> None (no strict majority; the file verifies this)
    ['z']            -> 'z'
"""


# Type hints: `values: list[str]` and the return type `str | None` (the
# `X | Y` union syntax, Python 3.10+) document that the function returns a
# string or None. Python does not enforce annotations at run time.
def majority_search(values: list[str]) -> str | None:
    """Return a majority element appearing more than half the time, if any.

    The voting loop is the textbook's majority_search; the final
    verification pass (returning None when there is no strict majority)
    is an addition reflecting the book's post-solution remark.
    """

    # candidate: the current guess for the majority element.
    # count: how many unmatched copies of candidate we are holding.
    candidate=None
    count=0
    for value in values:

        # Count zero means every earlier entry has been cancelled against a
        # different one, so start afresh with this entry as candidate.
        if count == 0:
            candidate=value
            count=1
        elif value == candidate:
            count+=1
        else:

            # A different entry: "discard" it together with one copy of the
            # candidate, which keeps the majority unchanged.
            count-=1

    # Verification pass (not in the book's program; the book says such a
    # second pass could be used when a majority is not guaranteed).
    #
    # `is not None` tests identity with the None object; it is the
    # recommended way to check for None. list.count(x) scans the whole list
    # and returns how many items equal x (O(n) time). `//` is floor
    # division, so count > len // 2 means "strictly more than half".
    if candidate is not None and values.count(candidate)>len(values)//2:
        return candidate
    return None


# TEXTBOOK POST-SOLUTION DISCUSSION (page 267)
# --------------------------------------------
# O(1) time is spent per entry, so the time complexity is O(n); the
# additional space complexity is O(1).
#
# The book's code assumes that a majority word exists. If no word has a
# strict majority, it still returns some word from the stream, with no
# meaningful guarantee about how common that word is. A second pass could
# check whether the returned word really is a majority. Similar ideas can
# identify words appearing more than n/k times in the sequence (book
# Problem 24.33 on page 399).
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def majority_search(input_stream):` iterating `for it in
#   input_stream`, with variables `candidate, candidate_count = None, 0`;
#   on count zero it does `candidate, candidate_count = it,
#   candidate_count + 1`; it simply `return candidate`.
# - File: parameter renamed `values: list[str]`, return hint `str | None`,
#   loop variable `value`, counter `count`, separate assignment statements,
#   and `count=1` instead of `candidate_count + 1` (equivalent since the
#   count is 0 there).
# - Behaviour difference: the file adds a verification step with
#   `values.count(candidate)` and returns None when there is no strict
#   majority; the book returns the candidate unconditionally. The file's
#   version therefore needs a second pass and a list (not a one-pass
#   stream), unlike the book's single-pass requirement.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Demonstrations check representative input/output behavior: empty
    # input, a clear majority, a tie (no majority -> None, because of the
    # file's verification step) and a single element.
    #
    # `assert` raises AssertionError if its condition is False; these are
    # quick smoke checks, pytest does the thorough testing.
    observed = majority_search([])
    print("majority_search:", observed)
    assert observed == None
    observed = majority_search(['a', 'a', 'b'])
    print("majority_search:", observed)
    assert observed == 'a'
    observed = majority_search(['a', 'b'])
    print("majority_search:", observed)
    assert observed == None
    observed = majority_search(['z'])
    print("majority_search:", observed)
    assert observed == 'z'
