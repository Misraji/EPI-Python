"""EPI Python — Exercise 24.11: Compute the Longest Substring with Matching Parens

Chapter 24: Honors Class
Textbook: pages 364–365 (printed page numbers; problem, solution and most of
the program on 364; the program ends, with analysis and variant, on 365).

PROBLEM (from the textbook)
---------------------------
Problem 8.3 on Page 102 defines matched strings of parens, brackets, and
braces. This problem is restricted to strings of parens. Specifically, this
problem is concerned with a long substrings of matched parens. As an
example, if s is "((())()(()(", then "(())()" is a longest substring of
matched parens.

Write a program that takes as input a string made up of the characters
'(' and ')', and returns the size of a maximum length substring in which
the parens are matched.

HINT (from the textbook)
------------------------
Start with a brute-force algorithm and then refine it by considering cases
in which you can advance more quickly.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: run the matching algorithm from Solution 8.3 (Page 102) on
every substring. There are C(n, 2) = n(n - 1)/2 substrings and the check is
O(n), so the total is O(n^3), with n the string length.

Observation 1: if a prefix fails the matched test because of an unmatched
right paren, no extension of that prefix can be matched. So for each i,
find the longest matched substring starting at index i — an O(n^2)
algorithm.

Observation 2: if a substring ends in an unmatched right paren, but all of
its prefixes ending in right parens are matched, then no nonempty suffix of
that prefix can begin a matched string, since any such suffix has fewer
left parens. So as soon as a prefix has an unmatched right paren, restart
with the character after it. Store the indices of left parens on a stack;
when a right paren is processed and the prefix is still matched, the index
on top of the stack (after popping) gives the start boundary used to update
the longest matched length for this prefix.

Worked example from the book, "((())()(()(" (push on '(' and pop on ')';
the first stack element is the bottom):
  * Before the first pop the stack is <0, 1, 2>; matched length 3 - 1 = 2.
  * Before the second pop it is <0, 1>; matched length 4 - 0 = 4.
  * Before the third pop it is <0, 5>; matched length 6 - 0 = 6.
  * Before the last pop it is <0, 7, 8>; matched length 9 - 7 = 2.
The answer is 6.

The book prints one program, `longest_matching_parentheses(s)`, which this
file implements.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    ')()())' -> 4   (the substring '()()')
"""


def longest_matching_parentheses(s: str) -> int:
    """Textbook implementation: stack of left-paren indices plus a boundary.

    `end` is the index of the last unmatched ')' (initially -1, i.e. before
    the string), which bounds matched substrings on the left once the stack
    empties. Type hints (`s: str`, `-> int`) are not enforced by Python.
    """

    # Tuple assignment initializes three variables; the list serves as a
    # stack (append pushes onto the end, pop removes from the end).
    max_length,end,left_parentheses_indices=0,-1,[]

    # enumerate(s) yields (index, character) pairs: (0, s[0]), (1, s[1]), ...
    # https://docs.python.org/3/library/functions.html#enumerate
    for i,c in enumerate(s):
        if c=='(':
            left_parentheses_indices.append(i)

        # An empty list is falsy: a ')' with no '(' to match is unmatched,
        # so no matched substring can extend across it; remember its index.
        elif not left_parentheses_indices:
            end=i
        else:

            # list.pop() with no argument removes and returns the LAST item,
            # here the matching '(' index (its return value is not needed).
            # https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
            left_parentheses_indices.pop()

            # Conditional expression `X if cond else Y`. The matched
            # substring ending at i starts just after the nearest unmatched
            # '(' still on the stack (top = index -1), or just after the last
            # unmatched ')' if the stack is empty.
            start=left_parentheses_indices[-1] if left_parentheses_indices else end
            max_length=max(max_length,i-start)
    return max_length


# TEXTBOOK POST-SOLUTION DISCUSSION (page 365)
# --------------------------------------------
# Time: O(n). Space: O(n) (the stack can hold up to n indices).
#
# VARIANTS
# 1. Solve the same problem using only O(1) space. (stated in the book; no
#    solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# book: `def longest_matching_parentheses(s)`; the `start = (...)`
#   conditional expression is written in parentheses across two lines.
# file: same name and parameter, type hints `s: str` and `-> int` added; the
#   conditional is on one line without parentheses. The code matches the
#   book's listing otherwise.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # ')()())': the leading and trailing ')' are unmatched; '()()' in the
    # middle has length 4.
    # `assert` raises AssertionError if the result differs; the tests/
    # folder holds the thorough pytest suite.
    print('Longest valid parentheses:',longest_matching_parentheses(')()())'))
    assert longest_matching_parentheses(')()())')==4
