"""EPI Python — Exercise 12.5: Find the Nearest Repeated Entries in an Array

Chapter 12: Hash Tables
Textbook: pages 167–168 (printed page numbers; problem, solution and the
start of the program on 167, end of program and complexity on 168).

PROBLEM (from the textbook)
---------------------------
"People do not like reading text in which a word is used multiple times in
a short paragraph. You are to write a program which helps identify such a
problem.

Write a program which takes as input an array and finds the distance
between a closest pair of equal entries. For example, if s = <"All",
"work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun",
"and", "no", "results">, then the second and third occurrences of "no" is
the closest pair."

HINT (from the textbook)
------------------------
"Each entry in the array is a candidate."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: examine every pair of entries; when two are equal, check
whether their distance beats the smallest distance seen so far. O(n^2) time
for an array of length n.

Improvement 1: when looking at an entry, only entries with the same value
matter, not every other entry. A hash table could map each value to the set
of indices where it occurs, and then each such set could be scanned.

Improvement 2 (the book's choice): when processing an entry, only the
closest PREVIOUS equal entry matters. So while scanning the array, keep a
hash table from each value seen so far to the latest index at which it
appeared. For the current element, the table gives the most recent earlier
index holding the same value, and the distance between them is a candidate
answer.

Book's example: in s above, when the element at index 9 ("no") is
processed, the table says the most recent previous "no" is at index 7, so
the closest-pair distance seen so far is updated to 2.

The implementation below, find_nearest_repetition, follows this idea.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    []              -> -1 (no entries, so no repeated pair)
    ['a', 'b', 'a'] -> 2
    ['a', 'a', 'b'] -> 1
    ['a', 'b']      -> -1 (all entries distinct)
"""


def find_nearest_repetition(words: list[str]) -> int:
    """Return shortest index gap between equal words; -1 if all distinct.

    This is the textbook's find_nearest_repetition (the only implementation
    given).

    Type hints: `list[str]` and `-> int` document the expected argument and
    return types; Python does not enforce them.
    """

    # `{}` is an empty dict: the hash table from each word to the latest
    # index where it was seen.
    last_seen={}

    # float('inf') is positive infinity: larger than every number, so the
    # first real distance found will replace it via min(). It also serves as
    # a "nothing found yet" marker.
    # float: https://docs.python.org/3/library/functions.html#float
    nearest=float('inf')

    # enumerate(words) yields (index, word) pairs, so the loop gets each
    # position along with its word.
    # enumerate: https://docs.python.org/3/library/functions.html#enumerate
    for index,word in enumerate(words):

        # A repeat: compare its distance to the previous occurrence with the
        # best so far. min() returns the smaller of its arguments.
        # min: https://docs.python.org/3/library/functions.html#min
        if word in last_seen:
            nearest=min(nearest,index-last_seen[word])

        # Always record this index as the word's latest position, so the
        # next occurrence is measured from here (the closest previous one).
        last_seen[word]=index

    # Conditional expression `X if condition else Y`: if no repeat was ever
    # found, nearest is still infinity and -1 is returned. Otherwise int()
    # converts the value to a plain int (it already is one once a distance
    # has been found, since min() then returns an int index difference).
    # int: https://docs.python.org/3/library/functions.html#int
    return int(nearest) if nearest != float('inf') else -1


# TEXTBOOK POST-SOLUTION DISCUSSION (page 168)
# --------------------------------------------
# Time complexity O(n), since a constant amount of work is done per entry.
# Space complexity O(d), where d is the number of distinct entries in the
# array (the size of the hash table).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def find_nearest_repetition(paragraph):` initialising
#   `word_to_latest_index, nearest_repeated_distance = {}, float('inf')`,
#   looping `for i, word in enumerate(paragraph):`, storing
#   `latest_equal_word = word_to_latest_index[word]` before taking `min`,
#   and returning `nearest_repeated_distance if nearest_repeated_distance
#   != float('inf') else -1`.
# File: parameter renamed `words: list[str]`, return hint `-> int` added;
#   variables renamed (`last_seen`, `nearest`, `index`) and initialised in
#   separate statements; no `latest_equal_word` temporary; the result is
#   wrapped in `int(...)`. Same algorithm.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Demonstrations check representative input/output behavior: an empty
    # list, a repeat two apart, adjacent repeats, and no repeats at all.
    #
    # `assert` stops the program with an AssertionError if a result is
    # different from the expected value. These are quick smoke checks;
    # pytest provides the more thorough automated verification.
    observed = find_nearest_repetition([])
    print("find_nearest_repetition:", observed)
    assert observed == -1
    observed = find_nearest_repetition(['a', 'b', 'a'])
    print("find_nearest_repetition:", observed)
    assert observed == 2
    observed = find_nearest_repetition(['a', 'a', 'b'])
    print("find_nearest_repetition:", observed)
    assert observed == 1
    observed = find_nearest_repetition(['a', 'b'])
    print("find_nearest_repetition:", observed)
    assert observed == -1
