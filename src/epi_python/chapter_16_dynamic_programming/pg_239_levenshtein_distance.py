"""EPI Python — Exercise 16.2: Compute the Levenshtein Distance

Chapter 16: Dynamic Programming
Textbook: pages 239–242 (printed page numbers; problem and solution start on 239).

PROBLEM (from the textbook)
---------------------------
"Spell checkers make suggestions for misspelled words. Given a misspelled
string, a spell checker should return words in the dictionary which are
close to the misspelled string.

In 1965, Vladimir Levenshtein defined the distance between two words as the
minimum number of "edits" it would take to transform the misspelled word
into a correct word, where a single edit is the insertion, deletion, or
substitution of a single character. For example, the Levenshtein distance
between "Saturday" and "Sundays" is 4—delete the first 'a' and 't',
substitute 'r' by 'n' and insert the trailing 's'."

"Write a program that takes two strings and computes the minimum number of
edits needed to transform the first string into the second string."

HINT (from the textbook)
------------------------
"Consider the same problem for prefixes of the two strings."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: enumerate all strings at distance 1, 2, 3, ... from the first
string until the second string turns up. The number of strings can explode:
if the first string is n 0s and the second is n 1s, all 2^n bit strings are
visited before reaching the second string.

Pruning idea: if the two strings end with the same character, that
character can be ignored. If they end differently, solve the problem for
the initial portions and then perform one final edit (an insertion,
deletion or substitution).

Let a and b be the lengths of A and B, and E(A[0, a-1], B[0, b-1]) their
Levenshtein distance (subarray notation is used for prefixes).
* If the last characters are equal:
      E(A[0,a-1], B[0,b-1]) = E(A[0,a-2], B[0,b-2]).
* Otherwise:
      E(A[0,a-1], B[0,b-1]) = 1 + min( E(A[0,a-2], B[0,b-2]),
                                       E(A[0,a-1], B[0,b-2]),
                                       E(A[0,a-2], B[0,b-1]) ).
  The three terms are the three ways of finishing:
  - transform A[0,a-2] into B[0,b-2], then SUBSTITUTE A's last character
    with B's last character;
  - transform A[0,a-1] into B[0,b-2], then ADD B's last character at the
    end;
  - transform A[0,a-2] into B[0,b-1], then DELETE A's last character.
These observations are intuitive; the book notes that their rigorous proof
(not given) rests on reordering the steps of an arbitrary optimum solution.

DP solves the recurrence efficiently by caching intermediate results on the
way to E(A[0,a-1], B[0,b-1]).

Figure 16.4 shows the E table for "Carthorse" and "Orchestra" (uppercase
and lowercase characters are different); the distance is 8:

           C  a  r  t  h  o  r  s  e
        0  1  2  3  4  5  6  7  8  9
     O  1  1  2  3  4  5  6  7  8  9
     r  2  2  2  2  3  4  5  6  7  8
     c  3  3  3  3  3  4  5  6  7  8
     h  4  4  4  4  4  3  4  5  6  7
     e  5  5  5  5  5  4  4  5  6  6
     s  6  6  6  6  6  5  5  5  5  6
     t  7  7  7  7  6  6  6  6  6  6
     r  8  8  8  7  7  7  7  6  7  7
     a  9  9  8  8  8  8  8  7  7  8

(The figure also draws arrows labelled sub/ins/del along one optimal edit
path.)

The book's program levenshtein_distance(A, B) is a memoized recursion with
nested compute_distance_between_prefixes(A_idx, B_idx) and a 2D cache
distance_between_prefixes filled with -1 -> `levenshtein_distance_memoized`
below. The file's `levenshtein_distance` is a bottom-up, two-row version
that is NOT printed in the book.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    ('', '')               -> 0
    ('cat', 'cat')         -> 0
    ('cat', 'cut')         -> 1   (substitute 'a' by 'u')
    ('kitten', 'sitting')  -> 3
    ('a', '')              -> 1   (delete 'a')
"""


def levenshtein_distance(first: str, second: str) -> int:
    """Edit distance by bottom-up DP, keeping only two rows of the E table.

    NOT a printed textbook implementation (the book's program is the
    memoized recursion below). Time O(len(first) * len(second)), extra space
    O(len(second)).
    """

    # Row 0 of the table: turning the empty prefix of `first` into the
    # first j characters of `second` takes j insertions.
    # list(range(k)) builds [0, 1, ..., k-1].
    # Type hints such as `first: str` are not enforced by Python.
    previous = list(range(len(second) + 1))

    # enumerate(iterable, start=1) yields (1, ch0), (2, ch1), ...: the row
    # number counts characters of `first` used so far, starting at 1.
    for row, left_character in enumerate(first, start=1):

        # Column 0: turning `row` characters into the empty string takes
        # `row` deletions. The rest of the row is filled below.
        current = [row] + [0] * len(second)
        for column, right_character in enumerate(second, start=1):

            # Conditional expression: cost 0 when the last characters match
            # (no edit needed for them), else 1 for a substitution.
            substitution = 0 if left_character == right_character else 1

            # min(a, b, c) returns the smallest argument. The three options:
            # delete from `first` (cell above), insert into it (cell to the
            # left), or match/substitute (diagonal cell).
            current[column] = min(
                previous[column] + 1,
                current[column - 1] + 1,
                previous[column - 1] + substitution,
            )

        # The finished row becomes the "previous" row; older rows are no
        # longer needed, which is what saves space.
        previous = current

    # `previous[-1]` is the last entry of the last row: the full distance.
    return previous[-1]



def levenshtein_distance_memoized(first: str, second: str) -> int:
    """Textbook implementation: memoized recursion over prefix end indices.

    Book: levenshtein_distance(A, B) with nested
    compute_distance_between_prefixes(A_idx, B_idx). distance(i, j) is the
    edit distance between first[:i+1] and second[:j+1].
    """
    rows = len(first)
    columns = len(second)

    # A sentinel of -1 distinguishes an uncomputed answer from cost 0.
    # The list comprehension makes an independent row for each index of
    # `first` (`[[-1]*columns]*rows` would share one row object).
    cache = [[-1] * columns for _ in range(rows)]

    # Nested recursive helper reading the enclosing `cache`, `first` and
    # `second`. Only cache items are assigned, so no `nonlocal` is needed.
    def distance(i: int, j: int) -> int:

        # `first` prefix is empty, so add all of second[:j+1] (j+1 chars).
        if i < 0:
            return j + 1

        # `second` prefix is empty, so delete all of first[:i+1].
        if j < 0:
            return i + 1

        # Already computed: reuse the cached value (the DP step).
        if cache[i][j] >= 0:
            return cache[i][j]

        # Equal last characters: ignore them.
        if first[i] == second[j]:
            result = distance(i - 1, j - 1)
        else:

            # 1 + the cheapest of: delete first's last character, add
            # second's last character, substitute the last character.
            result = 1 + min(
                distance(i - 1, j),
                distance(i, j - 1),
                distance(i - 1, j - 1),
            )
        cache[i][j] = result
        return result

    return distance(rows - 1, columns - 1)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 241)
# --------------------------------------------
# Once E(A[0,k], B[0,l]) is known for all k < a and l < b, computing
# E(A[0,a-1], B[0,b-1]) takes O(1) time. Hence the algorithm runs in O(ab)
# time. The implementation uses O(ab) space (the 2D cache).
#
# VARIANTS (each stated in the book; no solution given)
# ----------------------------------------------------
# 1. Compute the Levenshtein distance using O(min(a, b)) space and O(ab)
#    time.
# 2. Given A and B as above, compute a longest sequence of characters that
#    is a subsequence of both A and B. For example, for the strings of
#    Figure 16.4 the longest common subsequence is <r, h, s>.
# 3. Given a string A, compute the minimum number of characters you need to
#    delete from A to make the resulting string a palindrome.
# 4. Given a string A and a regular expression r, what is the string in the
#    language of r that is closest to A? Distance is the Levenshtein
#    distance above.
# 5. A string t is an interleaving of strings s1 and s2 if the characters
#    of s1 and s2 can be interleaved, keeping the left-to-right order of
#    each, to obtain t. For example, for s1 = "gtaa" and s2 = "atc",
#    "gattaca" and "gtataac" are interleavings of s1 and s2 but "gatacta"
#    is not. Design an algorithm that takes s1, s2 and t and determines
#    whether t is an interleaving of s1 and s2.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * `levenshtein_distance` (two rolling rows, bottom-up) is NOT the book's
#   program even though it carries the book's function name; it is an
#   added space-saving version using O(len(second)) space (close to, but not
#   exactly, variant 1's O(min(a, b))).
# * The book's program is `levenshtein_distance_memoized` here. Book
#   parameters `A`, `B`; file `first`, `second`. Book helper
#   `compute_distance_between_prefixes(A_idx, B_idx)` and cache
#   `distance_between_prefixes = [[-1] * len(B) for _ in A]`; file helper
#   `distance(i, j)` and `cache = [[-1] * columns for _ in range(rows)]`.
# * Book stores into the cache inside each branch and names the three
#   options `substitute_last`, `add_last`, `delete_last` (min in that
#   order); file computes `result` and orders the min arguments as delete,
#   add, substitute (same minimum). Book's comments ("A is empty so add all
#   of B's characters." / "B is empty so delete all of A's characters.")
#   are reflected above. Type hints added.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples for the bottom-up version (empty strings, identical
    # strings, one substitution, the classic kitten/sitting = 3, one
    # deletion), then the textbook memoized version on kitten/sitting.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite is thorough.
    observed = levenshtein_distance('', '')
    print("levenshtein_distance:", observed)
    assert observed == 0
    observed = levenshtein_distance('cat', 'cat')
    print("levenshtein_distance:", observed)
    assert observed == 0
    observed = levenshtein_distance('cat', 'cut')
    print("levenshtein_distance:", observed)
    assert observed == 1
    observed = levenshtein_distance('kitten', 'sitting')
    print("levenshtein_distance:", observed)
    assert observed == 3
    observed = levenshtein_distance('a', '')
    print("levenshtein_distance:", observed)
    assert observed == 1
    assert levenshtein_distance_memoized("kitten", "sitting") == 3
    print("Textbook memoized edit distance: passed")
