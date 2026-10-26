"""EPI Python — Exercise 24.33: The Heavy Hitter Problem

Chapter 24: Honors Class
Textbook: pages 399–400 (printed page numbers; problem and solution start
on 399).

PROBLEM (from the textbook)
---------------------------
Context: this generalizes Problem 17.5 (page 266). In practice one may want
not just a majority token but every token whose count exceeds, say, 1% of the
total. With limited memory this cannot be done in a single pass, but with two
passes over the sequence the common tokens can be identified.

"You are reading a sequence of strings separated by whitespace. You are
allowed to read the sequence twice. Devise an algorithm that uses O(k)
memory to identify the words that occur more than n/k times, where n is the
length of the sequence."

HINT (from the textbook)
------------------------
"Maintain a list of k candidates."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
This generalizes the majority-element solution of Problem 17.5. Instead of
discarding two distinct words at a time, discard k distinct words at a time.
Every word that occurred more than 1/k of the time in the sequence before a
discard still occurs more than 1/k of the time in what remains. To carry this
out, keep a hash table of the current candidates and their counts: add each
word, and whenever the table holds k distinct words, decrement every count
by one and drop the words whose count reaches zero.

The book prints one program; search_frequent_items below follows it.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    k = 3, words a b a c a b a  (n = 7, n/k = 2.33)  -> ['a']  (a occurs 4 times;
                                                     b occurs 2 times, not > 2.33)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# Counter API: https://docs.python.org/3/library/collections.html#collections.Counter
import collections


# Type hints: `k: int`; `stream` is unannotated (any re-iterable of
# strings); `-> list[str]` is the list of heavy hitters. Annotations are not
# enforced at run time.
def search_frequent_items(k: int, stream) -> list[str]:
    """stream must support *two independent iterations* (e.g. a list).

    This is the textbook's single implementation: a first pass keeps at
    most k - 1 candidates by discarding k distinct words at a time; a second
    pass counts the candidates exactly. Returns the words occurring more
    than n/k times. (A one-shot iterator such as a generator or file would
    be exhausted after the first pass.)
    """

    # Added guard (not in the book): with k <= 1, n/k >= n, so no word can
    # occur more than n/k times; also, k == 1 would empty the table at
    # every step.
    if k <= 1:
        return []

    # collections.Counter() starts as an empty dictionary-like object whose
    # missing keys read as 0, so `table[word] += 1` works for a new word.
    # It maps each candidate word to its current (reduced) count.
    table = collections.Counter()

    # Count the number of strings (book's comment).
    n = 0
    for word in stream:
        table[word] += 1
        n += 1

        # Detecting k items in table: at least one of them has count exactly
        # one; discard those k items by one each (book's comments).
        if len(table) == k:

            # list(table) snapshots the keys first. (Changing values while
            # iterating a dict is allowed; adding or removing keys is not.)
            for candidate in list(table):
                table[candidate] -= 1

            # Unary plus on a Counter returns a new Counter containing only
            # entries with positive counts, removing the zeros so the table
            # again holds fewer than k words.
            table = +table

    # Resets table for the following counting (book's comment): keep the
    # candidate keys but restart their counts at 0.
    for candidate in table:
        table[candidate] = 0

    # Reads the stream again and counts the occurrences of each candidate
    # word (book's comments). `word in table` tests key membership; it does
    # not create a key, so non-candidates are not counted.
    for word in stream:
        if word in table:
            table[word] += 1

    # Selects the words which occur > n / k times (book's comment). The list
    # comprehension filters table.items(), which yields (key, value) pairs.
    # `/` is true division, so n / k may be fractional.
    return [word for word, count in table.items() if count > n / k]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 400)
# --------------------------------------------
# The code might look like O(nk) time, since the outer loop runs n times and
# the inner decrement loop can take k steps. But each word occurrence can be
# erased only once, so the total time spent erasing is O(n), and the other
# steps of the outer loop are O(1). Total time: O(n).
#
# The first pass produces a set S of at most k words, a superset of the
# words occurring more than n/k times. A second pass counts how often each
# word in S really occurs, and the words of S that occur more than n/k times
# are returned.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Signature: book `def search_frequent_items(k, stream)`; file adds
#   `k: int` and `-> list[str]` type hints.
# * Added: `if k <= 1: return []` guard.
# * Names: book's loop variables `buf` and `it` (and `value` in the final
#   comprehension) become `word`, `candidate` and `count`.
# * Decrement loop: book `for it in table:`; file iterates over
#   `list(table)`, a snapshot of the keys. Same effect.
# * Otherwise matches the book, including `table = +table`.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Added example: a list can be iterated twice, as required.
    words = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
    print('Frequent words:', search_frequent_items(3, words))

    # `assert` stops with an AssertionError if the condition is false; a
    # quick smoke check. pytest provides the more thorough verification.
    assert search_frequent_items(3, words) == ['a']
