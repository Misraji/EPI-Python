"""EPI Python 24.29, textbook printed page 391: Determine the critical height.

QUESTION: Given c identical test cases and d drops, find maximum critical height determinable.

TEXTBOOK ALGORITHM: Use F(c,d)=F(c-1,d-1)+F(c,d-1)+1 memoized dynamic programming.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_391_get_height
Test: python -m pytest tests/chapter_24_honors_class/test_pg_391_get_height.py -v
"""

def get_height(cases: int,drops: int) -> int:
    table=[[-1]*(drops+1) for _ in range(cases+1)]
    def helper(c,d):
        if c==0 or d==0:return 0
        if c==1:return d
        if table[c][d]==-1:
            table[c][d]=helper(c,d-1)+helper(c-1,d-1)+1
        return table[c][d]
    return helper(cases,drops)


if __name__=='__main__':
    print('Two cases, five drops:',get_height(2,5))
    assert get_height(2,5)==15
