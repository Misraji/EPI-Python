"""EPI Python — Exercise 24.4: Compute the Maximum Product of All Entries but One

Chapter 24: Honors Class
Textbook: pages 354–356 (printed page numbers; problem and first program on
354–355, second program on 355, its analysis and the variants on 356).

PROBLEM (from the textbook)
---------------------------
Suppose you are given an array A of integers, and are asked to find the
largest product that can be made by multiplying all but one of the entries
in A. (You cannot use an entry more than once.) For example, if
A = <3, 2, 5, 4>, the result is 3 x 5 x 4 = 60, if A = <3, 2, -1, 4>, the
result is 3 x 2 x 4 = 24, and if A = <3, 2, -1, 4, -1, 6>, the result is
3 x -1 x 4 x -1 x 6 = 72.

[The book then explains the division and brute-force approaches; see
SOLUTION DEVELOPMENT.]

Given an array A of length n whose entries are integers, compute the
largest product that can be made using n - 1 entries in A. You cannot use
an entry more than once. Array entries may be positive, negative, or 0.
Your algorithm cannot use the division operator, explicitly or implicitly.

HINT (from the textbook)
------------------------
Consider the products of the first i - 1 and the last n - i elements.
Alternatively, count the number of negative entries and zero entries.

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Context before the formal statement: one approach forms the product P of
all elements and takes the maximum of P / A[i] over all i — n - 1
multiplications plus n divisions. If finite-precision concerns rule out
division, the brute force computes each of the n products of n - 1
elements separately, each needing n - 2 multiplications: O(n^2) time.

Solution 1 (prefix/suffix products):
  * Brute force computes P / A[i] by multiplying the entries before i with
    those after i, n(n - 2) multiplications in total.
  * There is heavy overlap: the product of the entries before i + 1 is A[i]
    times the product of the entries before i. So all prefix products can
    be found with n - 1 multiplications, and likewise all suffix products,
    stored in a prefix array and a suffix array. The answer is the largest
    prefix x suffix product.
  * Slightly less space: build only the suffix-product array, then sweep
    forward keeping the prefix product in one variable, multiplying it by
    the matching suffix product and updating the maximum.
  This is `find_biggest_n_minus_one_product` below. It runs in O(n) time
  and O(n) space (one array of length n).

Solution 2 (sign counting, O(n) time and O(1) extra space). Insights:
  * With no negative entries, the best product omits the smallest element
    (true whether there are zero, one, or more 0 entries).
  * With an odd number of negatives, regardless of zeros and positives,
    omit the negative entry with the smallest absolute value, i.e. the
    least negative entry.
  * With an even number of negatives and at least one nonnegative entry,
    again omit the smallest nonnegative element (correct even with zeros).
  * With an even number of negatives and no nonnegative entries, the result
    must be negative; to make it as large as possible, omit the entry of
    largest magnitude, i.e. the greatest negative entry.
  This gives a two-stage algorithm: first determine which scenario applies
  (e.g. is the number of negatives even?), then do the multiplication. In
  this file it is `find_biggest_n_minus_one_product_by_sign`.

Both textbook programs appear below as separate functions.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
The __main__ block reuses the book's first example, <3, 2, 5, 4> -> 60.
This file's functions also raise ValueError when given fewer than two
numbers (an addition not in the book).
"""

# Python standard library: iterator building blocks.
# Module documentation: https://docs.python.org/3/library/itertools.html
# accumulate API: https://docs.python.org/3/library/itertools.html#itertools.accumulate
import itertools

# Python standard library: functions corresponding to Python's operators.
# Module documentation: https://docs.python.org/3/library/operator.html
# mul API: https://docs.python.org/3/library/operator.html#operator.mul
import operator

# Python standard library: higher-order functions and operations on callables.
# Module documentation: https://docs.python.org/3/library/functools.html
# reduce API: https://docs.python.org/3/library/functools.html#functools.reduce
import functools


def find_biggest_n_minus_one_product(a: list[int]) -> int:
    """Textbook solution 1: suffix-product array plus a running prefix product.

    Type hints (`a: list[int]`, `-> int`) document intent; Python does not
    enforce them at run time.
    """

    # Added guard (not in the book): with fewer than two numbers there is no
    # meaningful "all but one" product. `raise` stops the function with the
    # given exception.
    if len(a) < 2:
        raise ValueError('At least two numbers required')

    # Builds suffix products.
    #
    # itertools.accumulate(iterable, func) lazily yields running results:
    # the first item, then func(previous_result, next_item), and so on.
    # Without func it adds; operator.mul (a function equivalent to `x * y`)
    # makes it a running product.
    #
    # reversed(a) iterates a from the end, so accumulate yields
    # a[-1], a[-1]*a[-2], ..., i.e. the suffix products from the back.
    # list(...) materializes them, the outer reversed(...) puts them back in
    # front-to-back order, and the final list(...) makes an indexable list:
    # suffix_products[i] is the product of a[i:].
    suffix_products=list(reversed(list(itertools.accumulate(reversed(a),operator.mul))))

    # Finds the biggest product of (n - 1) numbers.
    #
    # Tuple assignment sets two names at once. float('-inf') is negative
    # infinity, smaller than every number, so the first comparison always
    # replaces it.
    prefix_product,max_product=1,float('-inf')
    for i in range(len(a)):

        # Product of the entries after i. Conditional expression
        # `X if cond else Y`: for the last index there are no later entries,
        # so the empty product 1 is used.
        suffix_product = suffix_products[i+1] if i+1<len(a) else 1

        # prefix_product is the product of a[:i]; times suffix_product it is
        # the product of every entry except a[i].
        max_product=max(max_product,prefix_product*suffix_product)

        # `*=` multiplies in place: extend the prefix to include a[i].
        prefix_product*=a[i]
    return max_product


def find_biggest_n_minus_one_product_by_sign(a: list[int]) -> int:
    """Textbook solution 2: count negatives, choose the entry to skip, multiply.

    Uses O(1) extra space. The book gives this program the same name as
    solution 1; this file renames it so both can coexist.
    """

    # Added guard (not in the book).
    if len(a) < 2:
        raise ValueError('At least two numbers required')
    number_of_negatives=0

    # Chained assignment: all three names are bound to None, meaning
    # "no such entry seen yet".
    least_nonnegative_idx=least_negative_idx=greatest_negative_idx=None

    # Identify the least negative, greatest negative, and least nonnegative
    # entries.
    #
    # enumerate(a) yields (index, value) pairs.
    # https://docs.python.org/3/library/functions.html#enumerate
    for i,value in enumerate(a):
        if value < 0:
            number_of_negatives+=1

            # `x is None` tests identity with the None object (the
            # recommended way to test for None). `or` short-circuits, so the
            # index is not used while it is still None.
            # "Least negative" = closest to zero = largest negative value.
            if least_negative_idx is None or a[least_negative_idx] < value:
                least_negative_idx=i

            # "Greatest negative" = largest magnitude = smallest value.
            if greatest_negative_idx is None or value < a[greatest_negative_idx]:
                greatest_negative_idx=i

        # value >= 0.
        elif least_nonnegative_idx is None or value < a[least_nonnegative_idx]:
            least_nonnegative_idx=i

    # Nested conditional expressions, read left to right:
    #   odd count of negatives  -> skip the least negative entry;
    #   otherwise, if a nonnegative entry exists -> skip the smallest one;
    #   otherwise (all negative, even count) -> skip the greatest negative.
    # `number_of_negatives%2` is 1 (truthy) when odd and 0 (falsy) when even.
    idx_to_skip=(least_negative_idx if number_of_negatives%2
                 else least_nonnegative_idx if least_nonnegative_idx is not None
                 else greatest_negative_idx)

    # functools.reduce(function, iterable, initial) combines items left to
    # right: starting from 1, it computes 1 * v0, then (1 * v0) * v1, etc.,
    # producing the product. Passing the initial value 1 also makes an
    # empty input give 1 instead of raising TypeError.
    #
    # The second argument is a generator expression (in parentheses). It
    # yields every value whose index is not idx_to_skip, one at a time; the
    # book notes a generator is used rather than a list comprehension to
    # avoid extra space.
    return functools.reduce(operator.mul,(v for i,v in enumerate(a) if i!=idx_to_skip),1)


# TEXTBOOK POST-SOLUTION DISCUSSION (pages 355–356)
# -------------------------------------------------
# Solution 1: O(n) time; O(n) space for the single suffix-product array.
#
# Solution 2: one traversal with constant work per entry, a nested
# conditional, then a second traversal with constant work per entry:
# O(n) + O(1) + O(n) = O(n) time. Additional space is O(1), for the local
# variables.
#
# VARIANTS
# 1. Let A be as above. Compute an array B where B[i] is the product of all
#    elements in A except A[i]. You cannot use division. Your time
#    complexity should be O(n), and you can only use O(1) additional space.
#    (stated in the book; no solution given)
# 2. Let A be as above. Compute the maximum over the product of all triples
#    of distinct elements of A. (stated in the book; no solution given)


# TEXTBOOK CODE COMPARISON
# ------------------------
# Solution 1 — book: `def find_biggest_n_minus_one_product(A)`; same suffix
#   product expression with itertools.accumulate and operator.mul; same loop.
#   file: parameter renamed `a: list[int]`, return hint `-> int` added; an
#   added `if len(a) < 2: raise ValueError(...)` guard; otherwise the same
#   statements.
# Solution 2 — book: also named `find_biggest_n_minus_one_product(A)`; loop
#   variable `a`; nonnegative branch written as `else:` containing a nested
#   `if`; final line `functools.reduce(lambda product, a: product * a, (a for
#   i, a in enumerate(A) if i != idx_to_skip), 1)`.
#   file: renamed `find_biggest_n_minus_one_product_by_sign(a: list[int]) ->
#   int`; added ValueError guard; loop variable renamed `value`; the
#   `else: if` became `elif`; reduce uses `operator.mul` instead of the
#   lambda. Same algorithm and results.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__=='__main__':

    # Run both textbook implementations on the book's first example,
    # <3, 2, 5, 4>, whose best product (omitting 2) is 60.
    #
    # Functions are objects: the tuple holds the two functions themselves,
    # and `fn.__name__` is the attribute holding a function's name, printed
    # to show which version produced each result.
    # `assert` raises AssertionError if a result differs; the tests/ folder
    # holds the thorough pytest suite.
    for fn in (find_biggest_n_minus_one_product,find_biggest_n_minus_one_product_by_sign):
        print(fn.__name__,fn([3,2,5,4]))
        assert fn([3,2,5,4])==60
