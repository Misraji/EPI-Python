"""EPI Python — Exercise 15.6: Generate Strings of Matched Parens

Chapter 15: Recursion
Textbook: pages 227–228 (printed page numbers; problem and solution start on 227).

PROBLEM (from the textbook)
---------------------------
"Strings in which parens are matched are defined by the following three
rules:
  * The empty string, "", is a string in which parens are matched.
  * The addition of a leading left parens and a trailing right parens to a
    string in which parens are matched results in a string in which parens
    are matched. For example, since "(())()" is a string with matched
    parens, so is "((())())".
  * The concatenation of two strings in which parens are matched is itself
    a string in which parens are matched. For example, since "(())()" and
    "()" are strings with matched parens, so is "(())()()".
For example, the set of strings containing two pairs of matched parens is
{(()), ()()}, and the set of strings with three pairs of matched parens is
{((())), (()()), (())(), ()(()), ()()()}."

"Write a program that takes as input a number and returns all the strings
with that number of matched pairs of parens."

HINT (from the textbook)
------------------------
"Think about what the prefix of a string of matched parens must look like."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: enumerate all strings of 2k parentheses and test each one for
matched parens (Solution 8.3, page 102, specialized to one kind of
bracket). There are 2^(2k) such strings, a lower bound on that approach's
time. Even restricting to strings with equally many left and right parens
leaves C(2k, k) candidates.

Directed enumeration: some prefixes can never be completed (e.g. one
starting with ")"). So build strings one character at a time, keeping the
invariant that the current prefix CAN still be completed to a string with
k matched pairs. Given such a prefix shorter than 2k, there are two ways to
extend it:
* Add "(": allowed only if the number of left parens still needed is
  greater than 0.
* Add ")": allowed only if the number of left parens still needed is less
  than the number of right parens still needed (i.e. the prefix has an
  unmatched left paren).

Example, k = 2: the search visits "", "(", "((", "(()", "(())", "()",
"()(", "()()". Of these, "(())" and "()()" are complete and are added to
the result.

The book's program generate_balanced_parentheses(num_pairs) has a nested
directed_generate_balanced_parentheses(num_left_parens_needed,
num_right_parens_needed, valid_prefix, result=[]) that applies these two
rules and appends valid_prefix when no right parens are needed. This file
implements the same rules, counting parens USED instead of NEEDED (see
TEXTBOOK CODE COMPARISON).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    generate_balanced_parentheses(0) -> ['']      (only the empty string)
    generate_balanced_parentheses(1) -> ['()']
    generate_balanced_parentheses(2) -> ['(())', '()()']   (book's k = 2)
"""


def generate_balanced_parentheses(n: int) -> list[str]:
    """Return all strings of n matched pairs of parentheses.

    This is the textbook's directed recursive enumeration (book:
    generate_balanced_parentheses with nested
    directed_generate_balanced_parentheses), here with nested helper
    `visit(opened, closed, text)` that counts parens already used.
    """

    # Type hints (`n: int`, `-> list[str]`) document intended types only;
    # Python does not enforce them at run time.
    results=[]

    # Nested helper. `opened` / `closed` count the "(" and ")" already in
    # `text`, so the book's "left parens needed" is n - opened and "right
    # parens needed" is n - closed. Strings are immutable: `text+'('`
    # builds a NEW string, so each recursive call gets its own prefix and
    # nothing has to be undone afterwards. The helper appends to the
    # enclosing `results` list (no `nonlocal` needed; the name is not
    # rebound).
    def visit(opened: int,closed: int,text: str) -> None:

        # All n right parens are placed; since closed never exceeds opened
        # (and opened never exceeds n), the string is complete and matched.
        if closed == n:
            results.append(text)
            return

        # Able to insert '(' : fewer than n left parens used so far.
        if opened < n:
            visit(opened+1,closed,text+'(')

        # Able to insert ')' : there is an unmatched '(' in the prefix.
        if closed < opened:
            visit(opened,closed+1,text+')')
    visit(0,0,'')
    return results


# TEXTBOOK POST-SOLUTION DISCUSSION (page 228)
# --------------------------------------------
# The number C(k) of strings with k matched pairs grows very rapidly with
# k. The book states a recurrence for C(k + 1) as a sum over i = 0 .. k
# divided by (k + 1), which it says solves to (2k)!/((k!(k + 1)!)).
# [NEEDS PDF REVIEW: page 228, the summand of the recurrence for C(k + 1)
# is printed like a binomial "(k over i)"; confirm the exact formula.]
# (These counts are the Catalan numbers: 1, 1, 2, 5, 14, ... for
# k = 0, 1, 2, 3, 4.)
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Book nested helper `directed_generate_balanced_parentheses(
#   num_left_parens_needed, num_right_parens_needed, valid_prefix,
#   result=[])` counts parens still NEEDED, starting from
#   (num_pairs, num_pairs, ''); file `visit(opened, closed, text)` counts
#   parens USED, starting from (0, 0, '').
# * Book collects into a mutable default argument `result=[]` and returns
#   it from each call; the outer function returns the helper's result. File
#   uses an enclosing list `results` and the helper returns None.
# * Book checks the two extension rules first and then, at the end, appends
#   when `not num_right_parens_needed`; file checks completion first
#   (`if closed == n`) and returns early. The extension conditions
#   (`num_left_parens_needed > 0` / `num_left_parens_needed <
#   num_right_parens_needed`) are equivalent to `opened < n` /
#   `closed < opened`. Output order is the same.
# * Type hints added in the file; the book's "Able to insert" comments are
#   reproduced above.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Added examples n = 0 and n = 1, plus the book's own k = 2 example.
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, the pytest suite is thorough.
    observed = generate_balanced_parentheses(0)
    print("generate_balanced_parentheses:", observed)
    assert observed == ['']
    observed = generate_balanced_parentheses(1)
    print("generate_balanced_parentheses:", observed)
    assert observed == ['()']
    observed = generate_balanced_parentheses(2)
    print("generate_balanced_parentheses:", observed)
    assert observed == ['(())', '()()']
