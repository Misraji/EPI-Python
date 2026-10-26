"""EPI Python 24.27, textbook printed page 388: Measure with defective jugs.

QUESTION: Determine if a sum from uncertain-volume jugs can be guaranteed within [L,H].

TEXTBOOK ALGORITHM: Try each jug recursively and memoize ranges that cannot be satisfied.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_388_check_feasible
Test: python -m pytest tests/chapter_24_honors_class/test_pg_388_check_feasible.py -v
"""

# collections.namedtuple documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple


Jug=namedtuple('Jug',('low','high'))
VolumeRange=namedtuple('VolumeRange',('low','high'))


def check_feasible(jugs: list[Jug],lower: int,upper: int) -> bool:
    visited: set[VolumeRange]=set()
    def helper(l,h):
        state=VolumeRange(l,h)
        if l>h or state in visited or (l<0 and h<0):return False
        for jug in jugs:
            if l<=jug.low and jug.high<=h:
                return True
            if helper(l-jug.low,h-jug.high):
                return True
        visited.add(state)
        return False
    return helper(lower,upper)


if __name__=='__main__':
    choices=[Jug(230,240),Jug(290,310),Jug(500,515)]
    print('Feasible 2100..2300:',check_feasible(choices,2100,2300))
    assert check_feasible(choices,2100,2300)
