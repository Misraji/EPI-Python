"""EPI Python — Exercise 8.3: Test a String over "{,},(,),[,]" for Well-Formedness

Chapter 8: Stacks and Queues
Textbook: page 102 (printed page number; problem, solution and complexity
are all on page 102).

PROBLEM (from the textbook)
---------------------------
"A string over the characters "{,},(,),[,]" is said to be well-formed if the
different types of brackets match in the correct order.

For example, "([]){()}" is well-formed, as is "[()[]{()()}]". However, "{)",
"()", and "[()[]{()()" are not well-formed,

Write a program that tests if a string made up of the characters '(', ')',
'[', ']', "{" and "}" is well-formed."

NOTE ON A PROBABLE BOOK MISPRINT: the second "not well-formed" example is
printed as "()" (confirmed on a high-resolution render of page 102), but
"()" is in fact well-formed. It is reproduced as printed; treat it as a
misprint in the book.

HINT (from the textbook)
------------------------
"Which left parenthesis does a right parenthesis match with?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Parentheses only: consider strings made of '(' and ')' alone, such as
"()(())". In a well-formed string every ')' pairs with the nearest
still-unmatched '(' to its left. So, reading left to right, remember each
'(' as it appears and match each ')' against a remembered one. With only one
kind of bracket, a simple counter of unmatched '(' characters is enough.

General case: the same idea works, but the unmatched left characters
('(', '[', '{') must themselves be stored, not just counted. Three separate
counters would not work, since they cannot tell which kind of bracket was
opened most recently. A stack fits exactly: it holds the unmatched left
characters with the most recent at the top.

Rules:
  * When a right character arrives and the stack is empty, or its top is a
    left character of a different kind, that right character has no match
    and the string is not well-formed.
    Example: for "(()][)", at the first ']' the top of the stack is '(',
    so the answer is "not well-formed".
    Counter-example: for "(()[])", at the first ']' the top is '[', so
    processing continues.
  * After all characters are processed, a nonempty stack means some left
    characters were never closed, so the string is not well-formed.

The book's program `is_well_formed(s)` implements this; this file's
`is_well_formed` implements the same stack algorithm.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    ''        -> True  (nothing to match)
    '()[]{}'  -> True
    '([{}])'  -> True
    '([)]'    -> False (']' would close '(' )
"""


def is_well_formed(brackets: str) -> bool:
    """Return whether (), [], and {} brackets are correctly nested.

    Implements the textbook's `is_well_formed` stack algorithm (page 102).
    """

    # A dictionary mapping each RIGHT character to the LEFT character that
    # it must close. Looking up
    # matching[')'] gives '(' so a popped left character can be compared
    # against the expected one. (The book's dictionary goes the other way:
    # left -> right.)
    matching = {')': '(', ']':'[', '}':'{'}

    # A plain Python list used as a stack of unmatched left characters;
    # append pushes onto the end (the top) and pop removes from the end.
    stack = []
    for character in brackets:

        # `character in '([{'` on a string tests whether the one-character
        # string occurs inside '([{', i.e. whether it is a left character.
        if character in '([{':
            stack.append(character)

        # `in` on a dict tests the KEYS, so this asks whether the character
        # is a right character.
        elif character in matching:

            # `or` short-circuits: if the stack is empty (`not stack` is
            # True) the pop is never evaluated, avoiding an IndexError from
            # popping an empty list. Otherwise list.pop() removes the most
            # recent left character, which must be the one this right
            # character closes.
            if not stack or stack.pop() != matching[character]:
                return False

        # Any other character is silently ignored by this version (the book
        # assumes the input contains brackets only).

    # An empty list is falsy, so `not stack` is True exactly when every left
    # character was matched.
    return not stack


# TEXTBOOK POST-SOLUTION DISCUSSION (page 102)
# --------------------------------------------
# Each character requires only O(1) work, so the time complexity is O(n),
# where n is the length of the string. (The stack can hold up to n
# characters in the worst case, e.g. a string of only left brackets.)
#
# VARIANTS
# The textbook gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def is_well_formed(s)`; `left_chars, lookup = [], {'(': ')',
# '{': '}', '[': ']'}` (left -> right mapping). Loop: if `c in lookup`
# (a left character) push it; `elif not left_chars or
# lookup[left_chars.pop()] != c:` return False (book comment: "Unmatched
# right char or mismatched chars."); finally `return not left_chars`.
# File: parameter renamed `brackets: str` with `-> bool` hint; the dictionary
# `matching` maps right -> left instead; the stack is a separate variable
# `stack`; left characters are recognised with `character in '([{'`, and the
# comparison is `stack.pop() != matching[character]`.
# Behavioural difference on inputs outside the problem's alphabet: the book
# treats every non-left character as a right character (so any other
# character returns False), whereas the file's `elif character in matching`
# ignores characters that are not brackets. For strings made only of the six
# bracket characters both give the same answers.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Demonstrations check representative input/output behavior: the empty
    # string, sequential pairs, nested pairs, and interleaved (crossed)
    # brackets, which are not well-formed.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, pytest does the thorough testing.
    observed = is_well_formed('')
    print("is_well_formed:", observed)
    assert observed == True
    observed = is_well_formed('()[]{}')
    print("is_well_formed:", observed)
    assert observed == True
    observed = is_well_formed('([{}])')
    print("is_well_formed:", observed)
    assert observed == True
    observed = is_well_formed('([)]')
    print("is_well_formed:", observed)
    assert observed == False
