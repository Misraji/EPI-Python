"""EPI Python — Exercise 24.23: Implement Regular Expression Matching

Chapter 24: Honors Class
Textbook: pages 380–383 (printed page numbers; problem starts on 380,
solution on 381).

PROBLEM (from the textbook)
---------------------------
The book defines a simple subset of regular expressions by examples. A
regular expression is "a string made up of the following characters:
alphanumeric, . (dot), * (star), ^, and $." Examples of regular expressions:
a, aW, aW.9, aW.9*, aW.*9*, ^a, aW$, ^aW.9*$. Not every string is valid: "if
^ appears, it must be the first character, if $ appears, it must be the last
character, and star must follow an alphanumeric character or dot." Beyond
the base cases (a single alphanumeric character, dot, a single alphanumeric
character followed by a star, dot followed by star), regular expressions are
concatenations of shorter regular expressions.

Matching: "an alphanumeric character matches itself, dot matches any single
character, and star matches zero or more occurrences of the preceding
character." Without ^ and $ there is no anchor: "if the string contains any
substring matched by the regular expression, the regular expression matches
the string itself."

The book's examples (it underlines a matched substring; underlining cannot be
shown here):

* aW9 matches any string containing aW9: aW9, aW9bcW, ab8aW9, cc2aW9raW9z
  match; aW8, bcd8, xy do not.
* a.9. matches any string containing a length-4 substring whose first and
  third characters are a and 9: ab9w, ac9bcW, ab8a999, cc2aW9r match; az9,
  a989a, bac9 do not.
* aW*9 matches a substring starting with a, ending with 9, with zero or more
  Ws between: a9, aW9, aWW9b9cW, aU9aWW9, ab8aWWW9W9aa, cc2a9raW9zWW9ac
  match; aWWU9, baX9, aXW9Wa do not.
* a.*9 matches a substring starting with a, ending with 9, with zero or more
  characters between: a9, aZ9, aZW9b9cW, aU9a9, b8aWUW9W, cc2a9raU9z match;
  9UWaW8, b9aaaX, XUq8 do not.
* aW9*.b3 matches a substring of aW, zero or more 9s, any single character,
  then b3: ceaW999zb34b3az, ceaW9b34, pqaWzb38q match; ceaW98zb34,
  pqaW988b38q do not.

"If the regular expression begins with ^, that indicates the match must
begin at the start of the string. If the regular expression ends with $, the
match must end at the end of the string."

* ^aW.9 matches strings beginning with a, W, any character, 9: aW99zer,
  aWW9, aWP9GA match; baWx9, aW9, aWcc90 do not.
* aW.9$ matches strings whose last character is 9, third-last W and
  fourth-last a (second-last arbitrary): aWW9, aWW9abcaWz9, baaWX9,
  abcaWP9 match; aWW99, aW, aWcc90 do not.
* ^aW9$ is matched by aW9 and nothing else.

"Design an algorithm that takes a regular expression and a string, and checks
if the regular expression matches the string."

HINT (from the textbook)
------------------------
"Regular expressions are defined recursively."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Both the syntax (which strings are valid expressions) and the semantics (when
an expression matches) are recursive, which suggests matching by recursion.

Notation: s^k is the k-th suffix of s, i.e. s with its first k characters
deleted. For s = aWaW9W9, s^0 = aWaW9W9 and s^2 = aW9W9.

For an expression r and a string s:
* if r starts with ^, the rest of r must match a prefix of s;
* if r ends with $, some suffix of s must be matched by r without the $;
* with neither anchor, r matches s if it matches some substring of s.

A helper that tests whether r matches at the *beginning* of a string handles
four cases:

(1) a length-0 expression: trivially true;
(2) an expression starting with ^ or ending with $: ^ needs one call to the
    match function; a trailing $ needs a check that the string is used up;
(3) an expression starting with a starred item (e.g. a*wXY or .*Wa): walk
    along the string while its prefix keeps matching the starred character
    (or dot), testing at each step whether the remainder of the expression
    matches the remaining suffix (one recursive call per suffix);
(4) an expression starting with an alphanumeric character or dot: compare
    one character, then possibly recurse.

Worked example: r = ab.c*d and s = caeabbedeabacccde.
* s[0] = c, so r cannot match at the start of s. Try s^1: s[1] = a, so
  continue with s^1 and b.c*d, but s[2] != b, so that call fails.
* s^2 is ruled out immediately.
* s^3: s[3] = a, continue with s^4 and b.c*d; s[4] = b, continue with .c*d;
  dot matches s[5]; continue with c*d. Since s[6] = e, the only prefix of
  s^6 that c* can match is the empty one, and then d fails because
  s[6] != d.
* Skipping further failures, reach s^9; as before, proceed to s^12 and c*d.
  At offset 12, c* can match prefixes of length 0, 1, 2, 3. After the first
  three, the remaining d does not match; after the prefix ccc the rest of
  the string does continue with d, so the answer is true.

The book prints one program, implemented below as is_match with nested
is_match_here.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    is_match('^a.*z$', 'abcz')  -> True
"""


# Type hints: `regex: str, s: str` and `-> bool` document the expected
# types; Python does not enforce annotations at run time.
def is_match(regex: str,s: str) -> bool:
    """Return True if `regex` matches `s` (the book's subset of regexes).

    This is the textbook's single implementation: a recursive matcher
    anchored at the start of a string (is_match_here) plus an outer search
    over all starting positions when there is no leading ^.
    """

    # Nested helper: does `regex` match some prefix of `s`?
    def is_match_here(regex: str,s: str) -> bool:

        # Case (1): an empty regex matches every string (empty prefix).
        # `not regex` is True for the empty string.
        if not regex:return True

        # Case (2): reached the end of regex and its last char is '$': the
        # match succeeds only if the string has been used up.
        if regex=='$':return not s

        # Case (3): a starred item, e.g. 'a*...' or '.*...'.
        if len(regex)>=2 and regex[1]=='*':

            # Try every number i of characters consumed by the star,
            # starting with zero. regex[2:] and s[i:] are slices: the regex
            # after 'x*' and the string after its first i characters.
            i=0
            while i<=len(s):
                if is_match_here(regex[2:],s[i:]):return True

                # Stop if the string is exhausted or if s[i] can't be
                # absorbed by the star. `x not in ('.', s[i])` is True when
                # regex[0] is neither a dot nor equal to s[i].
                if i==len(s) or regex[0] not in ('.',s[i]):break
                i+=1
            return False

        # Case (4): regex begins with a single-character match. `s and ...`
        # short-circuits: an empty s yields '' (falsy), so s[0] is never read
        # on an empty string. bool(...) converts that '' to False so the
        # function always returns a real bool.
        return bool(s and regex[0] in ('.',s[0]) and is_match_here(regex[1:],s[1:]))

    # Case (2): regex starts with '^': must match at the start of s.
    # str.startswith(prefix) returns True if the string begins with prefix
    # (and safely returns False for an empty regex).
    # Docs: https://docs.python.org/3/library/stdtypes.html#str.startswith
    if regex.startswith('^'):
        return is_match_here(regex[1:],s)

    # Unanchored: try every starting position, including len(s) (the empty
    # suffix, needed e.g. for regex 'a*'). any() returns True as soon as one
    # item of the generator expression is true, so it stops early; for an
    # empty iterable it returns False.
    # Docs: https://docs.python.org/3/library/functions.html#any
    return any(is_match_here(regex,s[i:]) for i in range(len(s)+1))


# TEXTBOOK POST-SOLUTION DISCUSSION (page 383)
# --------------------------------------------
# Write C(x, k) for k copies of the string x concatenated. For the regular
# expression C(a.*, k) and the string C(ab, k - 1), the algorithm above runs
# in time exponential in k. The book says a more precise bound on the time
# complexity cannot be given.
#
# VARIANTS
# --------
# * Solve the same problem for regular expressions without the ^ and $
#   operators. (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Signatures: book `def is_match(regex, s)` and nested
#   `def is_match_here(regex, s)`; file adds `str`/`bool` type hints to
#   both.
# * Case (3): book starts with `i = 1` and loops
#   `while i <= len(s) and regex[0] in ('.', s[i - 1]):` testing
#   `is_match_here(regex[2:], s[i:])`, and only after the loop tests the
#   zero-occurrence case with `return is_match_here(regex[2:], s)`
#   (comment "See '*' matches zero character in s[:len(s)]"). File starts
#   at `i=0` (zero occurrences tried first), uses an explicit `break`
#   when the string ends or the character does not match, and returns
#   False after the loop. Same set of suffixes is tried, in a different
#   order.
# * Leading '^': book tests `if regex[0] == '^':` (which would raise
#   IndexError for an empty regex); file uses `regex.startswith('^')`.
# * Cases (1), (2) for '$', (4) and the final `any(...)` line match the
#   book (the file omits the book's case comments from the code but they
#   are reflected in the comments above).


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: anchored at both ends, 'a', any characters, then 'z'.
    print('Regex match:',is_match('^a.*z$','abcz'))

    # `assert` stops with an AssertionError if the condition is false; a
    # quick smoke check. pytest provides the more thorough verification.
    assert is_match('^a.*z$','abcz')
