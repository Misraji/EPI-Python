"""EPI Python 24.18, textbook printed page 374: Find an element that appears only once.

QUESTION: Find integer that appears once when all other values appear exactly three times.

TEXTBOOK ALGORITHM: Count each of 32 bit positions modulo three and convert 32-bit unsigned encoding back to signed.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_374_find_element_appears_once
Test: python -m pytest tests/chapter_24_honors_class/test_pg_374_find_element_appears_once.py -v
"""

def find_element_appears_once(a: list[int]) -> int:
    counts=[0]*32
    for value in a:
        for i in range(32):
            counts[i]+=(value>>i)&1
    result=sum(1<<i for i,c in enumerate(counts) if c%3)
    return result if result<2**31 else result-2**32


if __name__=='__main__':
    print('Unique integer:',find_element_appears_once([6,6,6,-3,7,7,7]))
    assert find_element_appears_once([6,6,6,-3,7,7,7])==-3
