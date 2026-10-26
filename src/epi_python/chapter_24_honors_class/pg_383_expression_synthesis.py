"""EPI Python — Exercise 24.24: Synthesize an Expression

Chapter 24: Honors Class
Textbook: pages 383–385 (printed page numbers; problem and solution start
on 383).

PROBLEM (from the textbook)
---------------------------
Context: for an expression of the form (3 o 1 o 4 o 1 o 5), where each o is
an operator such as +, -, x, /, the value depends on the operators chosen:
14 if all are +, 60 if all are x, and 22 for (3 - 1 + 4 x 1 x 5). Choosing
operators to reach a given value is hard in general: with only + and - and a
target of 0, the NP-complete problem of partitioning a set of integers into
two subsets of equal sum reduces directly to it.

"Write a program that takes an array of digits and a target value, and
returns true if it is possible to intersperse multiplies (x) and adds (+)
with the digits of the array such that the resulting expression evaluates to
the target value. For example, if the array is <1,2,3,2,5,3,7,8,5,9> and the
target value is 995, then the target value can be realized by the expression
123 + 2 + 5 x 3 x 7 + 85 x 9, so your program should return true."

HINT (from the textbook)
------------------------
"Build the assignment incrementally."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Let A be the digit array (length n) and k the target. Between each adjacent
pair A[i], A[i + 1] we may put x, +, or nothing (the digits join into a
longer number). The n - 1 choices can be encoded as an array of length
n - 1 over three values (x, +, and "no operator").

Brute force: enumerate all 3^(n-1) such arrays, evaluate the resulting
expression (O(n) each) and stop as soon as one evaluates to k. Time:
O(n x 3^n).

A more focused enumeration builds the assignment incrementally: the first
operator can come after the first, second, third, ... digit, and can be +
or x. Pruning heuristic for +: since the largest value obtainable from the
remaining digits is the number they form with no operators, a + is only
worth trying if the value of the operators chosen so far plus the number
formed by all remaining digits is at least the target. Example: for
<1,2,3,4,5>, target 1107 can never be reached if the first operator is a +
after the 3, because 123 + 45 < 1107.

The book prints one program (a recursive search with operand and operator
stacks, evaluating x before +, with the + pruning test). This file's
expression_synthesis follows the same recursive search but omits the
pruning test (see the code comparison).

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    digits [1, 2, 3], target 7  -> True   (1 + 2 x 3)
"""


# Type hints: `digits: list[int]`, `target: int`, `-> bool`. They document
# expected types; Python does not enforce annotations at run time.
def expression_synthesis(digits: list[int],target: int) -> bool:
    """Return True if + and x can be inserted among digits to hit target.

    This follows the textbook's recursive search (operands and operators
    kept on two stacks; no-operator, then x, then + tried in that order)
    without the textbook's pruning test before trying +.
    """

    # Annotated assignments: `name: type = value`. `list[str]` means "a list
    # of strings". These stacks hold the numbers and operators chosen so far
    # (operators[j] sits between operands[j] and operands[j + 1]). The book
    # creates them with `operands, operators = [], []`.
    operands: list[int]=[]
    operators: list[str]=[]

    # Evaluate the current expression with x before +: multiply into the
    # last term, start a new term on +, and finally add up the terms.
    def evaluate() -> int:
        terms=[]

        # iter(operands) returns an iterator over the list; each next(...)
        # call returns the following element (raising StopIteration if none
        # remain, which cannot happen here: there is always one more operand
        # than operators). This lets the loop over operators pull the
        # matching right-hand operand.
        # Docs: https://docs.python.org/3/library/functions.html#iter
        #       https://docs.python.org/3/library/functions.html#next
        iterator=iter(operands)
        terms.append(next(iterator))

        # Evaluates '*' first (book's comment).
        for operator in operators:
            value=next(iterator)
            if operator=='*':

                # terms[-1] is the last element; `*=` multiplies it in place.
                terms[-1]*=value
            else:
                terms.append(value)

        # Evaluates '+' second: sum() adds all items of an iterable.
        # Docs: https://docs.python.org/3/library/functions.html#sum
        return sum(terms)

    # search(remaining, current_term): `remaining` are the digits not yet
    # used; `current_term` is the number being formed by joining digits
    # since the last operator.
    def search(remaining: list[int],current_term: int) -> bool:

        # Added base case (not in the book): no digits left. Recursive calls
        # never pass an empty list (the len(remaining)==1 case stops first)
        # and the guard at the bottom rejects empty input, so this is a
        # safety net only.
        if not remaining:
            operands.append(current_term)
            found=evaluate()==target
            operands.pop()
            return found

        # Append the next digit to the number being formed.
        current_term=current_term*10+remaining[0]

        # Last digit: the expression is complete, so evaluate it (the book's
        # "Found a match" check). list.pop() removes the last element,
        # restoring the stack for the caller (the book uses del operands[-1]).
        if len(remaining)==1:
            operands.append(current_term)
            found=evaluate()==target
            operands.pop()
            return found

        # No operator: keep extending current_term. remaining[1:] is a slice
        # (a copy) holding all digits after the first.
        if search(remaining[1:],current_term):
            return True

        # Tries multiplication operator '*'.
        operands.append(current_term)
        operators.append('*')
        if search(remaining[1:],0):
            return True

        # Tries addition operator '+': swap the operator, keeping the same
        # operand on the stack. (The book first checks whether + is
        # feasible; this file tries + unconditionally.)
        operators.pop()
        operators.append('+')
        if search(remaining[1:],0):
            return True

        # Undo this level's changes before returning to the caller.
        operators.pop()
        operands.pop()
        return False

    # Added guard (not in the book): an empty digit list cannot form an
    # expression. (A one-line `if` puts its body right after the colon.)
    if not digits:return False
    return search(digits,0)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 385)
# --------------------------------------------
# The pruning heuristics help on some inputs, but no better worst-case
# time bound than the original O(n 3^n) can be proved.
#
# VARIANTS
# --------
# The book states no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# * Names: book `expression_synthesis(digits, target)` with nested
#   `directed_expression_synthesis(digits, current_term)`; file adds type
#   hints and names the nested function `search(remaining, current_term)`.
# * Placement: in the book, `evaluate()` is nested inside
#   `directed_expression_synthesis`; in the file it is nested directly in
#   `expression_synthesis`. Book's names `intermediate_operands`,
#   `operand_it`, `oper`, `product` become `terms`, `iterator`,
#   `operator`, and an in-place `terms[-1]*=value`.
# * Stacks: book `operands, operators = [], []` at the end; file declares
#   annotated `operands: list[int]=[]`, `operators: list[str]=[]` at the
#   start.
# * Missing pruning: the book checks
#   `if target - evaluate() <= functools.reduce(lambda val, d: val * 10 + d,
#   digits[1:], 0):` before trying '+'. The file has no such test and no
#   `functools` import, so it explores more branches (results unchanged).
# * Stack handling: the book pops operand and operator after '*', then
#   pushes the operand again for '+'; the file only swaps the operator
#   (`operators.pop()` then `append('+')`), and uses `.pop()` where the
#   book uses `del x[-1]`.
# * Added code: an `if not remaining:` base case inside `search`, and
#   `if not digits:return False` before the initial call.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Added example: 1 + 2 x 3 = 7.
    print('Expression can make 7:',expression_synthesis([1,2,3],7))

    # `assert` stops with an AssertionError if the condition is false; a
    # quick smoke check. pytest provides the more thorough verification.
    assert expression_synthesis([1,2,3],7)
