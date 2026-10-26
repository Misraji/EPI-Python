"""EPI Python 24.6, textbook printed page 357: Rotate an array.

QUESTION: Rotate an array right by i elements, using O(1) auxiliary space.

TEXTBOOK ALGORITHM: The printed source includes a cycle-permutation solution, a triple-reverse solution, and a naive slicing alternative.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_357_rotate_array
Test: python -m pytest tests/chapter_24_honors_class/test_pg_357_rotate_array.py -v
"""

# math.gcd documentation: https://docs.python.org/3/library/math.html#math.gcd
import math


def rotate_array_cycles(rotate_amount: int,a: list[int]) -> None:
    if not a:
        return
    rotate_amount%=len(a)
    if rotate_amount==0:
        return
    num_cycles=math.gcd(len(a),rotate_amount)
    cycle_length=len(a)//num_cycles
    for offset in range(num_cycles):
        temp=a[offset]
        for i in range(1,cycle_length):
            idx=(offset+i*rotate_amount)%len(a)
            a[idx],temp=temp,a[idx]
        a[offset]=temp


def rotate_array(rotate_amount: int,a: list[int]) -> None:
    """The book's simpler triple-reverse algorithm."""
    if not a:
        return
    i=rotate_amount%len(a)
    def reverse(begin: int,end: int) -> None:
        while begin<end:
            a[begin],a[end]=a[end],a[begin]
            begin,end=begin+1,end-1
    reverse(0,len(a)-1)
    reverse(0,i-1)
    reverse(i,len(a)-1)


def rotate_array_naive(i: int,a: list[int]) -> None:
    """The book's concise O(n)-extra-storage list-slice alternative."""
    if a:
        i%=len(a)
        a[:]=a[-i:]+a[:-i] if i else a[:]


if __name__=='__main__':
    for fn in (rotate_array_cycles,rotate_array,rotate_array_naive):
        a=[1,2,3,4,5]
        fn(2,a)
        print(fn.__name__,a)
        assert a==[4,5,1,2,3]
