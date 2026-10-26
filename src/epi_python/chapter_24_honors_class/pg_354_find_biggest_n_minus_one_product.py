"""EPI Python 24.4, textbook printed page 354: Compute the maximum product of all entries but one.

QUESTION: Choose n-1 entries whose product is largest, without division.

TEXTBOOK ALGORITHM: Compare products built from suffix/prefix arrays; book also has a sign-counting alternative.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_354_find_biggest_n_minus_one_product
Test: python -m pytest tests/chapter_24_honors_class/test_pg_354_find_biggest_n_minus_one_product.py -v
"""

# itertools.accumulate documentation: https://docs.python.org/3/library/itertools.html#itertools.accumulate
import itertools

# operator.mul documentation: https://docs.python.org/3/library/operator.html#operator.mul
import operator

# functools.reduce documentation: https://docs.python.org/3/library/functools.html#functools.reduce
import functools


def find_biggest_n_minus_one_product(a: list[int]) -> int:
    """Textbook prefix/suffix technique; multiply all but one element."""
    if len(a) < 2:
        raise ValueError('At least two numbers required')

    # accumulate with operator.mul computes successive cumulative products.
    suffix_products=list(reversed(list(itertools.accumulate(reversed(a),operator.mul))))
    prefix_product,max_product=1,float('-inf')
    for i in range(len(a)):
        suffix_product = suffix_products[i+1] if i+1<len(a) else 1
        max_product=max(max_product,prefix_product*suffix_product)
        prefix_product*=a[i]
    return max_product


def find_biggest_n_minus_one_product_by_sign(a: list[int]) -> int:
    """The sign-counting alternative from the following printed page."""
    if len(a) < 2:
        raise ValueError('At least two numbers required')
    number_of_negatives=0
    least_nonnegative_idx=least_negative_idx=greatest_negative_idx=None
    for i,value in enumerate(a):
        if value < 0:
            number_of_negatives+=1
            if least_negative_idx is None or a[least_negative_idx] < value:
                least_negative_idx=i
            if greatest_negative_idx is None or value < a[greatest_negative_idx]:
                greatest_negative_idx=i
        elif least_nonnegative_idx is None or value < a[least_nonnegative_idx]:
            least_nonnegative_idx=i
    idx_to_skip=(least_negative_idx if number_of_negatives%2
                 else least_nonnegative_idx if least_nonnegative_idx is not None
                 else greatest_negative_idx)

    # reduce repeatedly multiplies generator items, starting from 1.
    return functools.reduce(operator.mul,(v for i,v in enumerate(a) if i!=idx_to_skip),1)


if __name__=='__main__':
    for fn in (find_biggest_n_minus_one_product,find_biggest_n_minus_one_product_by_sign):
        print(fn.__name__,fn([3,2,5,4]))
        assert fn([3,2,5,4])==60
