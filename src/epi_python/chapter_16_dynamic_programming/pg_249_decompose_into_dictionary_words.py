"""EPI Python — Exercise 16.7: The Bedbathandbeyond.com Problem

Chapter 16: Dynamic Programming
Textbook: pages 249–251 (printed page numbers; problem and solution start on 249).

PROBLEM (from the textbook)
---------------------------
"Suppose you are designing a search engine. In addition to getting keywords
from a page's content, you would like to get keywords from Uniform Resource
Locators (URLs). For example, bedbathandbeyond.com yields the keywords
"bed, bath, beyond, bat, hand": the first two coming from the decomposition
"bed bath beyond" and the latter two coming from the decomposition "bed bat
hand beyond"."

"Given a dictionary, i.e., a set of strings, and a name, design an
efficient algorithm that checks whether the name is the concatenation of a
sequence of dictionary words. If such a concatenation exists, return it. A
dictionary word may appear more than once in the sequence. For example,
"a", "man", "a", "plan", "a", "canal" is a valid sequence for
"amanaplanacanal"."

HINT (from the textbook)
------------------------
"Solve the generalized problem, i.e., determine for each prefix of the name
whether it is the concatenation of dictionary words."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Natural recursion: find dictionary words that begin the name and solve the
rest recursively. Naively this is very slow on some inputs: if the name is
N repetitions of "AB" followed by "C" and the dictionary is "A", "B", "AB",
the time is exponential in N. E.g. for "ABABC" the substring "ABC" is
solved twice (once after "A", "B" and once after "AB").

Fix: cache intermediate results. The cache keys are prefixes of the
string; each value is a Boolean saying whether that prefix splits into
dictionary words. Checking whether a string is a word is easy: keep the
dictionary in a hash table. A prefix has a valid decomposition exactly when
it is itself a dictionary word, or some shorter prefix has a valid
decomposition and the remaining piece (current prefix minus shorter
prefix) is a dictionary word.

Example, "amanaplanacanal":
1. "a" is decomposable ("a" is a word);
2. "am" is decomposable ("am" is a word);
3. "ama" is decomposable ("a" is decomposable and "am" is a word) [as
   printed in the book];
4. "aman" is decomposable ("am" is decomposable and "an" is a word).
Skipping ahead:
5. "amanapl" is not decomposable (none of "l", "pl", "apl", ... is a word);
6. "amanapla" is not decomposable (the only word ending it is "a", and
   "amanapl" is not decomposable).
[NEEDS PDF REVIEW: page 250, step (3.) — "ama" = "a" + "ma" or "am" + "a";
the book's stated reason ("a" decomposable and "am" a word) does not
match the split; confirm the printed wording.]

This tells WHETHER a string splits into words but not WHICH words. A
little bookkeeping fixes that: for each decomposable prefix, record the
length of the last dictionary word in its decomposition. The book's program
decompose_into_dictionary_words(domain, dictionary) does this with an array
last_length and then walks backwards to rebuild the words. This file
implements the same program.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    domain 'bedbathandbeyond', dictionary {'bed','bath','and','beyond'}
        -> ['bed', 'bath', 'and', 'beyond']
"""


def decompose_into_dictionary_words(domain: str, dictionary: set[str]) -> list[str]:
    """Return one split of `domain` into dictionary words, or [] if none.

    This is the textbook's DP implementation. An empty `domain` returns []
    (a guard not in the book).
    """

    # Type hints (`set[str]`: a set of strings, `-> list[str]`) document
    # intended types only; Python does not enforce them. Any container
    # supporting `in` works for `dictionary`; a set (hash table) makes each
    # lookup O(1) on average, plus the cost of hashing the substring.
    if not domain:
        return []

    # When the algorithm finishes, last_length[i] != -1 indicates that
    # domain[:i + 1] has a valid decomposition, and the length of the last
    # word in that decomposition is last_length[i]. -1 means "no
    # decomposition".
    last_length = [-1] * len(domain)
    for i in range(len(domain)):

        # If domain[:i + 1] (the prefix ending at index i; slices exclude
        # their end index) is itself a dictionary word, its last word is the
        # whole prefix, of length i + 1.
        if domain[:i+1] in dictionary:
            last_length[i] = i+1

        # Otherwise look for j < i such that domain[:j + 1] has a valid
        # decomposition and domain[j + 1:i + 1] is a dictionary word; if
        # found, that word's length is i - j. `break` leaves the inner loop
        # at the first such j (one decomposition is enough).
        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and domain[j+1:i+1] in dictionary:
                    last_length[i] = i-j
                    break
    decompositions: list[str] = []

    # `last_length[-1]` is the entry for the whole string (negative indices
    # count from the end). If it is not -1, domain can be assembled from
    # dictionary words.
    if last_length[-1] != -1:

        # Walk backwards: the last word ends at `index` and has length
        # last_length[index]; then jump to the end of the previous word.
        index = len(domain)-1
        while index >= 0:
            decompositions.append(domain[index+1-last_length[index]:index+1])
            index -= last_length[index]

        # Slicing [::-1] (step -1) returns a reversed copy of the list; the
        # words were found back-to-front.
        decompositions = decompositions[::-1]
    return decompositions


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 250–251)
# -------------------------------------------------
# Let n be the length of the input string s. For each k < n the algorithm
# checks, for each j < k, whether s[j + 1, k] is a dictionary word; each
# check costs O(k - j). So the time is O(n^3).
#
# Improvement: let W be the length of the longest dictionary word. j only
# needs to range from k - W to k - 1 without losing decompositions, giving
# O(n^2 W) time.
#
# To get ALL decompositions, store every j that gives a correct break at
# each position. The number of decompositions can be exponential, as the
# string "itsitsitsits..." illustrates.
#
# VARIANTS (stated in the book; no solution given)
# ------------------------------------------------
# Palindromic decompositions were described in Problem 15.7 (page 228).
# Every string s has at least one palindromic decomposition — the trivial
# one into single characters (e.g. for s = "0204451881": "0", "2", "0",
# "4", "4", "5", "1", "8", "8", "1"). The minimum decomposition of s is
# "020", "44", "5", "1881". How would you compute a palindromic
# decomposition of a string s that uses a minimum number of substrings?


# TEXTBOOK CODE COMPARISON
# ------------------------
# * File adds the guard `if not domain: return []` (the book would raise
#   IndexError at `last_length[-1]` for an empty string) and type hints.
# * Book variable `idx`; file `index`. Book's `decompositions = []` has no
#   annotation; file `decompositions: list[str] = []`.
# * Otherwise the code matches the book's listing; the book's comments are
#   reproduced above.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':

    # Added example based on the book's motivating URL. `{...}` with
    # comma-separated strings is a set literal.
    # `assert` stops the program with an AssertionError if the condition is
    # false; this is a quick smoke check, the pytest suite is thorough.
    words = {'bed','bath','and','beyond'}
    result = decompose_into_dictionary_words('bedbathandbeyond',words)
    print(result)
    assert result == ['bed','bath','and','beyond']
