"""EPI Python — Exercise 8.2: Evaluate RPN Expressions

Chapter 8: Stacks and Queues
Textbook: page 101 (printed page number; problem, solution and variant are
all on page 101).

PROBLEM (from the textbook)
---------------------------
"A string is said to be an arithmetical expression in Reverse Polish
notation (RPN) if:
(1.) It is a single digit or a sequence of digits, prefixed with an option
     -, e.g., "6", "123", "-42".
(2.) It is of the form "A, B, o" where A and B are RPN expressions and o is
     one of +, -, ×, /.
For example, the following strings satisfy these rules: "1729",
"3, 4, +, 2, ×, 1, +", "1, 1, +, -2, ×", "-641, 6, /, 28, /".

An RPN expression can be evaluated uniquely to an integer, which is
determined recursively. The base case corresponds to Rule (1.), which is an
integer expressed in base-10 positional system. Rule (2.) corresponds to the
recursive case, and the RPNs are evaluated in the natural way, e.g., if A
evaluates to 2 and B evaluates to 3, then "A, B, ×" evaluates to 6.

Write a program that takes an arithmetical expression in RPN and returns the
number that the expression evaluates to."

(The book writes the multiplication operator as × in the prose; its program,
and this file, use the character '*'.)

HINT (from the textbook)
------------------------
"Process subexpressions, keeping values in a stack. How should operators be
handled?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Worked example: "3,4,+,2,×,1,+" is the RPN form of (3 + 4) × 2 + 1. Scanning
left to right by hand: note 3, then 4; the + combines them into 7, which is
noted in their place (3 and 4 are never looked at again); × with 2 gives 14;
finally + with 1 gives the answer 15.

Key observation: partial results must be remembered, and each operator is
applied to the most recently remembered partial results. Partial results are
therefore added and removed in last-in, first-out order, so a stack is the
natural structure: push each number; on an operator, pop two values, apply
the operator, and push the result. At the end the single remaining value is
the answer. The book's program `evaluate` implements this with a dictionary
mapping each operator symbol to a lambda; this file's `evaluate_rpn`
implements the same algorithm with an if/elif chain.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    '3,4,+'      -> 7
    '3,4,+,2,*'  -> 14
    '6,3,/,2,-'  -> 0
    '-7,3,/'     -> -2   (division truncates toward zero, see below)
"""


def evaluate_rpn(expression: str) -> int:
    """Evaluate integer RPN tokens separated by commas.

    Implements the textbook's `evaluate` algorithm (page 101), using an
    if/elif chain instead of the book's operator dictionary.
    """

    # `stack: list[int] = []` is an annotated assignment: the type hint says
    # the list will hold ints. Python records the hint but never enforces it.
    # The list's end is the top of the stack of partial results.
    stack: list[int] = []

    # str.split(",") cuts the string at every comma and returns a list of
    # the pieces (tokens), e.g. "3,4,+".split(",") -> ['3', '4', '+'].
    # Spaces are NOT removed, so the input must not contain spaces.
    # Documentation: https://docs.python.org/3/library/stdtypes.html#str.split
    for token in expression.split(","):

        # `{...}` here is a set literal; `in` on a set is a fast membership
        # test. A token that is one of the four operator symbols is an
        # operator; anything else is treated as a number.
        if token in {"+", "-", "*", "/"}:

            # The operand pushed LAST is the right-hand operand, so it is
            # popped first. The order matters for - and /.
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:

                # `/` is true division and always produces a float, e.g.
                # -7 / 3 -> -2.333... ; int() then drops the fractional part,
                # truncating toward zero (-2). This differs from floor
                # division `//`, which rounds toward negative infinity
                # (-7 // 3 == -3). The book uses the same int(x / y) form.
                # For very large ints the float step can lose precision.
                # int(): https://docs.python.org/3/library/functions.html#int
                stack.append(int(left / right))
        else:

            # int(token) parses a decimal string, including a leading minus
            # sign: int("-42") -> -42. It raises ValueError on bad input.
            stack.append(int(token))

    # The final result is the value on top of the stack (index -1).
    return stack[-1]


# TEXTBOOK POST-SOLUTION DISCUSSION (page 101)
# --------------------------------------------
# Each character of the input string involves O(1) work, so the time
# complexity is O(n), where n is the length of the string.
#
# VARIANTS
# Variant (stated in the book; no solution given): solve the same problem for
# expressions in Polish notation, that is, when "A, B, o" in Rule (2.) is
# replaced by "o, A, B".


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def evaluate(RPN_expression)` with a local list
# `intermediate_results`, a constant `DELIMITER = ','`, and a dictionary
# `OPERATORS` mapping '+', '-', '*', '/' to two-argument lambdas
# (`lambda y, x: ...`, written so that the first pop supplies y and the
# second supplies x); an operator token is handled in one statement:
# `intermediate_results.append(OPERATORS[token](intermediate_results.pop(),
# intermediate_results.pop()))`.
# File: function renamed `evaluate_rpn(expression: str) -> int`; list
# renamed `stack` with a `list[int]` hint; the delimiter is the literal ","
# instead of a named constant; the operator dictionary and lambdas are
# replaced by a set-membership test plus an if/elif chain, with explicit
# locals `right` and `left` for the two pops. The arithmetic (including
# `int(x / y)` truncating division) and the final `return ...[-1]` are the
# same. The book's comment `# token is a number.` is not in the file.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # Run a few self-contained examples before exploring the pytest suite.
    # They show addition, a longer expression, operand order for / and -,
    # and division of a negative number truncating toward zero.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, pytest does the thorough testing.
    observed = evaluate_rpn('3,4,+')
    print("evaluate_rpn:", observed)
    assert observed == 7
    observed = evaluate_rpn('3,4,+,2,*')
    print("evaluate_rpn:", observed)
    assert observed == 14
    observed = evaluate_rpn('6,3,/,2,-')
    print("evaluate_rpn:", observed)
    assert observed == 0
    observed = evaluate_rpn('-7,3,/')
    print("evaluate_rpn:", observed)
    assert observed == -2
