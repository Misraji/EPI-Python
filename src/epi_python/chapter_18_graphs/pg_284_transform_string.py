"""EPI Python — Exercise 18.7: Transform One String to Another

Chapter 18: Graphs
Textbook: pages 284–286 (printed page numbers; problem on 284, hint,
solution, program, complexity and variant on 285, end of the variant on
286).

PROBLEM (from the textbook)
---------------------------
Let s and t be strings and D a dictionary, i.e., a set of strings. Define s
to produce t if there exists a sequence of strings from the dictionary
P = <s0, s1, ..., s(n-1)> such that the first string is s, the last string
is t, and adjacent strings have the same length and differ in exactly one
character. The sequence P is called a production sequence. For example, if
the dictionary is {bat, cot, dog, dag, dot, cat}, then <cat, cot, dot, dog>
is production sequence.

Given a dictionary D and two strings s and t, write a program to determine
if s produces t. Assume that all characters are lowercase alphabets. If s
does produce t, output the length of a shortest production sequence;
otherwise, output -1.

HINT (from the textbook)
------------------------
Treat strings as vertices in an undirected graph, with an edge between u and
v if and only if the corresponding strings differ in one character.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: explore every string one character away from s, then every
string two characters away, and so on. The trouble is that it explores many
strings that are not in the dictionary.

Better: focus on dictionary words and model the problem as a graph. Each
vertex is a dictionary string; an edge (u, v) means u and v differ in
exactly one character. "Differs in one character" is symmetric, so the
graph is undirected.

Book example: vertices {bat, cot, dog, dag, dot, cat}; edges
{(bat, cat), (cot, dot), (cot, cat), (dog, dag), (dog, dot)}.

A production sequence is just a path from s to t in this graph, so we need
a shortest path from s to t. In an undirected, unweighted graph shortest
paths are naturally computed with BFS.

The book's program transform_string(D, s, t) runs BFS over
(candidate_string, distance) pairs, generating neighbours by trying every
lowercase letter at every position, and marks strings visited by removing
them from D. This file's transform_string(start, target, dictionary)
follows the same BFS, with differences listed in TEXTBOOK CODE COMPARISON.

Note: the book's program returns the number of transformation STEPS (edges
on the path) — for cat -> cot -> dot -> dog that is 3 — and this file does
the same.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    start='cat', target='dog', dictionary={'cat','cog','cot','dog'} -> 3
        (cat -> cot -> cog -> dog)
    start='cat', target='cat', dictionary=set()                     -> 0
    start='cat', target='dog', dictionary={'dog'}                   -> -1
        (no intermediate words exist)
"""

# Python standard library: specialized container types.
# Module documentation: https://docs.python.org/3/library/collections.html
# deque API: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


# Type hints: two str arguments, a `set[str]` dictionary, and an int result.
# Python does not enforce annotations at run time.
def transform_string(start: str, target: str, dictionary: set[str]) -> int:
    """Minimum single-character substitutions through supplied dictionary words.

    The textbook's BFS solution (book: transform_string(D, s, t)). Returns
    -1 if target cannot be produced. The dictionary is NOT modified (the
    book's version removes words from D).
    """

    # Added shortcut (not in the book): zero steps if nothing must change.
    if start == target:
        return 0

    # Added shortcut: the last word of a production sequence must be in the
    # dictionary. `not in` on a set is an average O(1) hash lookup.
    if target not in dictionary:
        return -1

    # collections.deque: a double-ended queue with O(1) append() on the
    # right and popleft() on the left — the FIFO queue BFS needs. Each queue
    # item is a (word, distance-from-start) tuple.
    queue=deque([(start,0)])

    # A set literal holding the start word: words already discovered, so no
    # word is queued twice. (The book instead deletes words from D.)
    visited={start}
    while queue:

        # popleft() takes the oldest entry; unpack the tuple into two names.
        word,distance=queue.popleft()

        # Try every one-character change of `word` (book comment: "Tries all
        # possible transformations").
        for index in range(len(word)):

            # Iterating over a string yields its characters one at a time.
            # (The book uses string.ascii_lowercase, which is this same
            # 'abcdefghijklmnopqrstuvwxyz' string.)
            for letter in 'abcdefghijklmnopqrstuvwxyz':

                # Slicing: word[:index] is everything before position index,
                # word[index+1:] everything after it. Gluing letter between
                # them replaces exactly one character. Slices never raise
                # IndexError; they just return shorter (possibly empty)
                # strings.
                candidate=word[:index]+letter+word[index+1:]

                # BFS discovers vertices in order of distance, so the first
                # time target appears, distance + 1 is the minimum number of
                # steps.
                if candidate == target:
                    return distance+1

                # Only dictionary words not seen before become new vertices.
                if candidate in dictionary and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate,distance+1))

    # Book comment: cannot find a possible transformation.
    return -1


# TEXTBOOK POST-SOLUTION DISCUSSION (page 285)
# --------------------------------------------
# Let d be the number of words in the dictionary: that is the number of
# vertices. In the worst case there are O(d^2) edges. BFS takes
# O(d + d^2) = O(d^2) time. If the string length n is less than d, each
# vertex has at most O(n) outgoing edges, giving an O(nd) bound.
#
# VARIANTS
# --------
# Variant (stated in the book; no solution given): An addition chain
# exponentiation program for computing x^n is a finite sequence
# <x, x^i1, x^i2, ..., x^n> where each element after the first is either the
# square of some previous element or the product of any two previous
# elements. For example, the term x^15 can be computed by the following two
# addition chain exponentiation programs:
#     P1 = <x, x^2 = (x)^2, x^4 = (x^2)^2, x^8 = (x^4)^2, x^12 = x^8 x^4,
#           x^14 = x^12 x^2, x^15 = x^14 x>
#     P2 = <x, x^2 = (x)^2, x^3 = x^2 x, x^5 = x^3 x^2, x^10 = (x^5)^2,
#           x^15 = x^10 x^5>
# It is not obvious, but the second program, P2, is the shortest addition
# chain exponentiation program for computing x^15. Given a positive integer
# n, how would you compute a shortest addition chain exponentiation program
# to evaluate x^n?


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Signature: book `def transform_string(D, s, t):` (dictionary FIRST);
#   file `def transform_string(start: str, target: str, dictionary:
#   set[str]) -> int:` (dictionary LAST, parameters renamed, type hints).
#   Calls written for the book's argument order will not work here.
# - Queue items: book uses a namedtuple `StringWithDistance(candidate_string,
#   distance)` defined inside the function; file uses plain (word,
#   distance) tuples.
# - Visited tracking: book removes words from D (`D.remove(s)`, then
#   `D.remove(cand)`), so D is modified and `D.remove(s)` raises KeyError
#   if s is not in D; file keeps a separate `visited` set and leaves the
#   dictionary untouched (start need not be in the dictionary).
# - Target test: book checks `f.candidate_string == t` when a string is
#   DEQUEUED and returns `f.distance`; file checks `candidate == target`
#   when a candidate is GENERATED and returns `distance + 1`. Same answer,
#   found earlier.
# - Additions in the file: early `return 0` when start == target and early
#   `return -1` when target is not in the dictionary.
# - Alphabet: book `import string` and `string.ascii_lowercase`; file uses
#   the literal 'abcdefghijklmnopqrstuvwxyz' (no `string` import).
#   Imports: book `collections.deque`; file `from collections import
#   deque`.
# - The book's comments ("Uses BFS to find the least steps of
#   transformation", "Marks s as visited by erasing it in D", "Returns if
#   we find a match", "Number of steps reaches t", "Tries all possible
#   transformations of f.candidate_string", "Iterates through 'a' ~ 'z'",
#   "Cannot find a possible transformations") are reflected in the new
#   comments rather than reproduced verbatim.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Demonstrations check representative input/output behavior (added
    # examples): a three-step transformation, the trivial case, and an
    # impossible case.
    #
    # `assert` raises AssertionError if its condition is False; these are
    # quick smoke checks, pytest does the thorough testing.
    observed = transform_string('cat', 'dog', {'cat', 'cog', 'cot', 'dog'})
    print("transform_string:", observed)
    assert observed == 3
    observed = transform_string('cat', 'cat', set())
    print("transform_string:", observed)
    assert observed == 0
    observed = transform_string('cat', 'dog', {'dog'})
    print("transform_string:", observed)
    assert observed == -1
