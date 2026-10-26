"""EPI 15.6: Generate strings of matched parens — printed page 227.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Generate strings of matched parens
Algorithm: A valid prefix cannot contain more closing than opening parentheses; extend only allowed prefixes.
Read the corresponding `pg_227_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_15_recursion.pg_227_generate_balanced_parentheses
Test: python -m pytest tests/chapter_15_recursion/test_pg_227_generate_balanced_parentheses.py -v
"""

def generate_balanced_parentheses(n: int) -> list[str]:
    """Enumerate valid balanced parenthesis strings with n pairs."""
    results=[]
    def visit(opened: int,closed: int,text: str) -> None:
        if closed == n:
            results.append(text)
            return
        if opened < n:
            visit(opened+1,closed,text+'(')
        if closed < opened:
            visit(opened,closed+1,text+')')
    visit(0,0,'')
    return results


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = generate_balanced_parentheses(0)
    print("generate_balanced_parentheses:", observed)
    assert observed == ['']
    observed = generate_balanced_parentheses(1)
    print("generate_balanced_parentheses:", observed)
    assert observed == ['()']
    observed = generate_balanced_parentheses(2)
    print("generate_balanced_parentheses:", observed)
    assert observed == ['(())', '()()']
