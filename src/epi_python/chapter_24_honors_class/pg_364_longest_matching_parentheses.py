"""EPI Python 24.11, textbook printed page 364: Compute the longest substring with matching parens.

QUESTION: Find length of longest contiguous substring of correctly matched parentheses.

TEXTBOOK ALGORITHM: Keep indices of unmatched opening parentheses and last unmatched closing parentheses.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_364_longest_matching_parentheses
Test: python -m pytest tests/chapter_24_honors_class/test_pg_364_longest_matching_parentheses.py -v
"""

def longest_matching_parentheses(s: str) -> int:
    max_length,end,left_parentheses_indices=0,-1,[]
    for i,c in enumerate(s):
        if c=='(':
            left_parentheses_indices.append(i)
        elif not left_parentheses_indices:
            end=i
        else:
            left_parentheses_indices.pop()
            start=left_parentheses_indices[-1] if left_parentheses_indices else end
            max_length=max(max_length,i-start)
    return max_length


if __name__=='__main__':
    print('Longest valid parentheses:',longest_matching_parentheses(')()())'))
    assert longest_matching_parentheses(')()())')==4
