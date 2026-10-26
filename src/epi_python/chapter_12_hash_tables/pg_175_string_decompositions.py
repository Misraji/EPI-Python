"""EPI Python — Exercise 12.10: Compute All String Decompositions

Chapter 12: Hash Tables
Textbook: pages 175–176 (printed page numbers; problem, solution and the
start of the program on 175, end of program and complexity on 176).

PROBLEM (from the textbook)
---------------------------
"This problem is concerned with taking a string (the "sentence" string) and
a set of strings (the "words"), and finding the substrings of the sentence
which are the concatenation of all the words (in any order). For example,
if the sentence string is "amanaplanacanal" and the set of words is
{"can", "apl", "ana"}, "aplanacan" is a substring of the sentence that is
the concatenation of all words.

Write a program which takes as input a string (the "sentence") and an array
of strings (the "words"), and returns the starting indices of substrings of
the sentence string which are the concatenation of all the strings in the
words array. Each string must appear exactly once, and their ordering is
immaterial. Assume all strings in the words array have equal length. It is
possible for the words array to contain duplicates."

HINT (from the textbook)
------------------------
"Exploit the fact that the words have the same length."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
First consider a smaller question: is a given string exactly a
concatenation of the strings in words? In general this can be solved
recursively -- find a word that is a prefix of the string, then recurse on
the remaining suffix with the remaining words.

When every word has the same length n, at most one distinct word can be a
prefix of the string. So simply check whether the first n characters are
one of the words. If not, the string cannot be such a concatenation. If
they are, remove that word from the collection and continue with the rest
of the string and the remaining words.

To find all qualifying substrings of the sentence, apply this check
starting from every index of the sentence.

The implementation below, find_all_substrings, follows this idea, but
compares the whole window's word counts at once (see the comparison
section).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    s="barfoothefoobarman", words=["foo", "bar"] -> [0, 9]
        ("barfoo" starts at 0, "foobar" starts at 9)
    words=[]                                     -> [] (guard added)
    words of different lengths                   -> raises ValueError
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# Counter API: https://docs.python.org/3/library/collections.html#collections.Counter
#
# `from collections import Counter` imports just that one name, so the code
# can write Counter(...) instead of collections.Counter(...).
from collections import Counter


def find_all_substrings(s: str, words: list[str]) -> list[int]:
    """Return starts where equal-length dictionary words concatenate in any order.

    This is the textbook's find_all_substrings (the only implementation
    given), restructured: each candidate window is cut into word-sized
    pieces whose Counter is compared with the words' Counter, instead of
    the book's nested match_all_words_in_dict helper with early exit.

    Type hints: `s: str`, `words: list[str]`, `-> list[int]`; Python does
    not enforce annotations.
    """

    # No words, or empty words: nothing sensible to match, so return an
    # empty list. `or` evaluates words[0] only if `words` is non-empty.
    # (Guard added in this file.)
    if not words or not words[0]:
        return []
    width = len(words[0])

    # any(iterable) is True if at least one item is truthy; it stops at the
    # first True. The generator expression yields True for each word whose
    # length differs from the first. The book only assumes equal lengths;
    # this file checks it.
    # any: https://docs.python.org/3/library/functions.html#any
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if any(len(word) != width for word in words):
        raise ValueError("All dictionary words must have equal length")

    # Counter(words) maps each word to how many times it must appear. Using
    # counts (not a set) handles duplicate words, which the problem allows.
    target = Counter(words)

    # Every match covers exactly len(words) words of `width` characters.
    span = width * len(words)
    found = []

    # Candidate starting indices: every start whose window fits inside s.
    # If s is shorter than span, the range is empty and [] is returned.
    # range: https://docs.python.org/3/library/stdtypes.html#range
    for start in range(len(s) - span + 1):

        # A list comprehension cutting the window into consecutive pieces.
        # range(start, start + span, width) steps by `width`, and the slice
        # s[i:i+width] copies that many characters starting at i.
        pieces = [s[i:i+width] for i in range(start,start+span,width)]

        # Two Counters compare equal when they hold the same items with the
        # same counts -- i.e. the pieces are exactly the words, each used the
        # required number of times, in any order.
        if Counter(pieces) == target:
            found.append(start)
    return found


# TEXTBOOK POST-SOLUTION DISCUSSION (page 176)
# --------------------------------------------
# Let m be the number of words, n the length of each word, and N the length
# of the sentence. For a fixed start i, checking whether the length-nm
# substring at i is a concatenation of all the words costs O(nm), assuming a
# hash table holds the words. So the overall time is O(Nnm). In practice
# individual checks are usually much faster, because a check can stop as
# soon as a mismatch is found. (This file's version always builds the whole
# window's Counter, so it does not stop early.)
#
# The fact that all words have the same length makes the problem easier,
# both for complexity and implementation: testing whether a substring
# equals a concatenation of the words becomes straightforward.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def find_all_substrings(s, words):` containing a nested helper
#   `def match_all_words_in_dict(start):` that builds a
#   `curr_string_to_freq = collections.Counter()` word by word, returns
#   False as soon as a word is not in `word_to_freq` (count 0) or occurs too
#   many times ("curr_word occurs too many times for a match to be
#   possible."), and True otherwise. The outer function sets
#   `word_to_freq = collections.Counter(words)`, `unit_size =
#   len(words[0])`, and returns a list comprehension over
#   `range(len(s) - unit_size * len(words) + 1)` filtered by the helper.
# File: imports `from collections import Counter`; type hints added; adds
#   guards for empty input and a ValueError for unequal word lengths (book
#   assumes equal lengths); no nested helper and no early exit -- each
#   window is sliced into a `pieces` list and `Counter(pieces) == target` is
#   tested; an explicit loop with `found.append` replaces the book's list
#   comprehension; names changed (`width`, `target`, `span`).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # "barfoo" at index 0 and "foobar" at index 9 are both concatenations of
    # "foo" and "bar"; order does not matter.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, while pytest provides the more
    # thorough automated verification.
    print("word concatenations:", find_all_substrings("barfoothefoobarman",["foo","bar"]))
    assert find_all_substrings("barfoothefoobarman",["foo","bar"]) == [0,9]
