"""EPI Python 24.24, textbook printed page 383: Synthesize an expression.

QUESTION: Can concatenating digits, with inserted + and * operators, produce the target value?

TEXTBOOK ALGORITHM: Recursively enumerate concat/multiply/add choices; evaluate multiplication before addition as in the PDF.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_383_expression_synthesis
Test: python -m pytest tests/chapter_24_honors_class/test_pg_383_expression_synthesis.py -v
"""

def expression_synthesis(digits: list[int],target: int) -> bool:
    operands: list[int]=[]
    operators: list[str]=[]

    def evaluate() -> int:
        terms=[]
        iterator=iter(operands)
        terms.append(next(iterator))
        for operator in operators:
            value=next(iterator)
            if operator=='*':
                terms[-1]*=value
            else:
                terms.append(value)
        return sum(terms)

    def search(remaining: list[int],current_term: int) -> bool:
        if not remaining:
            operands.append(current_term)
            found=evaluate()==target
            operands.pop()
            return found
        current_term=current_term*10+remaining[0]
        if len(remaining)==1:
            operands.append(current_term)
            found=evaluate()==target
            operands.pop()
            return found
        if search(remaining[1:],current_term):
            return True
        operands.append(current_term)
        operators.append('*')
        if search(remaining[1:],0):
            return True
        operators.pop()
        operators.append('+')
        if search(remaining[1:],0):
            return True
        operators.pop()
        operands.pop()
        return False

    if not digits:return False
    return search(digits,0)


if __name__=='__main__':
    print('Expression can make 7:',expression_synthesis([1,2,3],7))
    assert expression_synthesis([1,2,3],7)
