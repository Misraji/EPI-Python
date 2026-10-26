"""EPI 14.7: Enumerate numbers of the form a + b sqrt(2) (printed page 207).

Problem: Enumerate numbers of the form a + b sqrt(2). The problem, examples, discussion, and variants
appear in the PDF and its corresponding page-numbered reference Markdown.

Approach: O(k) two-index algorithm, also discussed in the textbook as an improvement over balanced-BST enumeration.

Python study exercise based on the textbook algorithm. Some type hints,
data structures, and demonstrations have been adapted for direct execution.
"""

# TEXTBOOK PROBLEM (exercise 14.7, printed page 207):
# Generate the first k smallest numbers of the form a + b * sqrt(2).
# HINT: Merge the two increasing sequences formed by adding 1 and sqrt(2).

# math.sqrt returns the square root as a float.
# https://docs.python.org/3/library/math.html#math.sqrt
from math import sqrt


def generate_first_k_a_b_sqrt2(k: int) -> list[float]:
    """Generate the first k distinct increasing values of a + b*sqrt(2)."""
    if k < 0:
        raise ValueError('k must be nonnegative')
    if not k:
        return []
    values=[0.0]
    i=j=0
    for _ in range(1,k):
        increment_one=values[i]+1.0
        increment_sqrt=values[j]+sqrt(2)
        candidate=min(increment_one,increment_sqrt)
        values.append(candidate)
        # Floating-point roundoff may make mathematically identical candidates
        # differ in the last few bits. Advance both streams on near-equality.
        epsilon = 1e-12
        if increment_one <= increment_sqrt + epsilon:
            i += 1
        if increment_sqrt <= increment_one + epsilon:
            j += 1
    return values


if __name__ == '__main__':
    result=generate_first_k_a_b_sqrt2(5)
    print('First five a + b*sqrt(2) values:',result)
    assert result==sorted(result) and len(result)==5
