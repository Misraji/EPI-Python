"""EPI 8.2: Evaluate RPN expressions (printed page 101).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Evaluate RPN expressions
Method: Use a stack, consuming operands before pushing each operator result; division truncates toward zero.

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_101_exercise_08_02_evaluate_rpn_expressions.md

Run independently:
    python -m epi_python.chapter_08_stacks_and_queues.pg_101_evaluate_rpn
Run thorough tests:
    python -m pytest tests/chapter_08_stacks_and_queues/test_pg_101_evaluate_rpn.py -v
"""

def evaluate_rpn(expression: str) -> int:
    """Evaluate integer reverse Polish notation tokens separated by commas."""
    stack: list[int] = []
    for token in expression.split(","):
        if token in {"+", "-", "*", "/"}:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(int(left / right))
        else:
            stack.append(int(token))
    return stack[-1]


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
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
