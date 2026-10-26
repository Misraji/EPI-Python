"""EPI Python — Exercise 6.13: Find the First Occurrence of a Substring

Chapter 6: Strings
Textbook: pages 79–81 (printed page numbers; introduction on 79; problem,
hint, solution and most of the program on 80; end of the program and the
complexity on 81).

PROBLEM (from the textbook)
---------------------------
A good string search algorithm is fundamental to the performance of many
applications. Several clever algorithms have been proposed for string
search, each with its own trade-offs. As a result, there is no single
perfect answer. If someone asks you this question in an interview, the
best way to approach this problem would be to work through one good
algorithm in detail and discuss at a high level other algorithms.

Given two strings s (the "search string") and t (the "text"), find the
first occurrence of s in t.

HINT (from the textbook)
------------------------
Form a signature from a string.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: two nested loops — the outer one steps through t, the inner
one tests whether s occurs starting at the current index of t. The worst
case is expensive: if t is n 'a's and s is n/2 'a's followed by a 'b', there
are n/2 unsuccessful string comparisons, each taking n/2 + 1 character
comparisons, so the brute-force algorithm is O(n^2).

Why it is slow: it moves through t one character at a time and may do O(m)
work at each step, where m is the length of s.

Three string matching algorithms run in linear time: KMP, Boyer-Moore and
Rabin-Karp. Rabin-Karp is by far the simplest to understand and implement.

Rabin-Karp is close to brute force but drops the inner loop by using a
"fingerprint": with m the length of s, it computes hash codes of every
length-m substring of t (the fingerprints). Efficiency comes from an
incremental hash function — one where a string's hash code is an additive
function of its individual characters (often called a rolling hash). With
such a function, the hash of a sliding window of characters can be updated
very quickly at each shift.

Worked example from the book: strings over {A, C, G, T}; t = "GACGCCA",
s = "CGC". Give the letters codes A = 0, C = 1, G = 2, T = 3, and let the
hash of a string be the decimal number formed by its letters' codes.
    * hash(s) = 121.
    * The first three characters of t, "GAC", hash to 201, so s cannot
      start at position 0.
    * The next window, "ACG", is obtained from 201 by subtracting 200,
      multiplying by 10 and adding 2, giving 12: still no match.
    * Continuing, the window "CGC" is reached, whose hash, 121, is
      computed the same way. A matching hash is not yet proof — there may
      be a collision — so the substring is compared explicitly with s;
      here it does match.

For Rabin-Karp to run in linear time, the hash function must be good, so
that collisions (which force potentially time-consuming string equality
checks) are unlikely.

The book prints one program, rabin_karp(t, s); this file's
rabin_karp(text, pattern) implements the same rolling-hash algorithm with
a different base, a modulus, and some restructuring (see TEXTBOOK CODE
COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    rabin_karp('hello world', 'world') -> 6
    rabin_karp('abcabc', 'cab')        -> 2
    rabin_karp('abc', 'z')             -> -1  (not found)
    rabin_karp('abc', '')              -> 0   (empty pattern matches at 0)
"""


# `text: str`, `pattern: str` and `-> int` are type hints: they document
# the expected argument and return types. Python does not check or enforce
# them at run time; tools such as mypy can.
# Annotations: https://docs.python.org/3/glossary.html#term-annotation
def rabin_karp(text: str, pattern: str) -> int:
    """Find first pattern position with a polynomial rolling-hash search.

    This is the textbook's Rabin-Karp algorithm (rabin_karp(t, s)),
    using base 256 and a prime modulus instead of the book's base 26 with
    unbounded integers. Returns -1 if the pattern does not occur.
    """
    # An empty pattern occurs at position 0 (as with str.find).
    if not pattern:
        return 0
    m = len(pattern)

    # A pattern longer than the text cannot be a substring of it.
    if m > len(text):
        return -1

    # The hash of a length-m string c0 c1 ... c(m-1) is the polynomial
    # c0*base^(m-1) + c1*base^(m-2) + ... + c(m-1), taken modulo
    # `modulus`. Base 256 covers all byte-sized character codes. Reducing
    # modulo a large prime keeps the numbers small (Python ints never
    # overflow, but huge ints make arithmetic slower).
    # Underscores in a numeric literal (1_000_000_007) are only visual
    # digit separators; the value is 1000000007.
    # Numeric literals: https://docs.python.org/3/reference/lexical_analysis.html#integer-literals
    base = 256
    modulus = 1_000_000_007

    # pow(base, exp, mod) with three arguments computes
    # (base ** exp) % mod efficiently, without building the huge
    # intermediate power. base^(m-1) is the weight of the leftmost
    # character in a window, needed to remove it when the window slides.
    # Docs: https://docs.python.org/3/library/functions.html#pow
    power = pow(base, m - 1, modulus)
    target_hash = 0
    current_hash = 0

    # Hash codes for s and for the first length-m substring of t, built
    # left to right ("multiply by base and add the next code").
    # ord(c) returns the integer code point of a character, used as the
    # character's numeric code.
    # ord: https://docs.python.org/3/library/functions.html#ord
    for i in range(m):
        target_hash = (target_hash * base + ord(pattern[i])) % modulus
        current_hash = (current_hash * base + ord(text[i])) % modulus

    # One iteration per window start: 0 .. len(text) - m.
    for start in range(len(text) - m + 1):

        # Check that the two substrings are actually equal, to protect
        # against hash collisions (a book comment, adapted). `and`
        # short-circuits: the slice comparison runs only when the hashes
        # agree. text[start:start + m] is a new string holding the
        # current window.
        if target_hash == current_hash and text[start:start + m] == pattern:
            return start

        # Use the rolling hash to compute the next window's hash (book
        # comment, adapted): subtract the outgoing character's
        # contribution, shift by multiplying with base, add the incoming
        # character. Skipped after the last window.
        if start + m < len(text):

            # The subtraction can make the intermediate value negative.
            # Python's `%` with a positive modulus always returns a
            # result in 0..modulus-1 (the sign follows the divisor), so
            # the hash stays non-negative without extra adjustment.
            # Docs: https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
            current_hash = (
                (current_hash - ord(text[start]) * power) * base
                + ord(text[start + m])
            ) % modulus

    # s is not a substring of t (book comment).
    return -1


# TEXTBOOK POST-SOLUTION DISCUSSION (page 81)
# -------------------------------------------
# With a good hash function the time complexity is O(m + n), independent
# of the inputs s and t, where m is the length of s and n is the length
# of t.
#
# VARIANTS
# --------
# The book lists no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def rabin_karp(t, s)` (text first, then search string);
#   returns -1 when `len(s) > len(t)` ("s is not a substring of t");
#   `BASE = 26`; computes `t_hash` and `s_hash` with
#   `functools.reduce(lambda h, c: h * BASE + ord(c), ..., 0)` over
#   `t[:len(s)]` and `s`; `power_s = BASE**max(len(s) - 1, 0)`; no
#   modulus (relies on Python's unbounded integers); then
#   `for i in range(len(s), len(t))`: if the hashes match and
#   `t[i - len(s):i] == s` it returns `i - len(s)`, otherwise it rolls the
#   hash with `t_hash -= ord(t[i - len(s)]) * power_s` and
#   `t_hash = t_hash * BASE + ord(t[i])`; after the loop a separate check
#   tries `t[-len(s):]` and returns `len(t) - len(s)`; finally returns -1.
#   The book uses functools (import not shown in this file).
# file: `rabin_karp(text: str, pattern: str) -> int` (type hints added;
#   parameters renamed, same order); adds an explicit `if not pattern:
#   return 0` (the book's code also returns 0 for an empty s: the first
#   loop iteration compares two empty strings); base 256 instead of 26, and all hashes are reduced
#   modulo the prime 1_000_000_007, with `pow(base, m - 1, modulus)` for
#   the leading power; initial hashes computed with a for loop instead of
#   functools.reduce; the loop runs over window starts
#   `range(len(text) - m + 1)` and checks the window before rolling, so
#   the book's separate final-window check is unnecessary; the roll is a
#   single expression with `% modulus`. Same results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples: a match at the end, a match in the middle, no match,
    # and an empty pattern. The comprehensive test suite remains in the
    # separate tests/ folder.
    observed = rabin_karp('hello world', 'world')

    # print() with several arguments writes them separated by a space.
    print("rabin_karp:", observed)

    # `assert` stops the program with an AssertionError if the condition
    # is false. These are quick smoke checks; pytest provides the more
    # thorough automated verification.
    assert observed == 6
    observed = rabin_karp('abcabc', 'cab')
    print("rabin_karp:", observed)
    assert observed == 2
    observed = rabin_karp('abc', 'z')
    print("rabin_karp:", observed)
    assert observed == -1
    observed = rabin_karp('abc', '')
    print("rabin_karp:", observed)
    assert observed == 0
