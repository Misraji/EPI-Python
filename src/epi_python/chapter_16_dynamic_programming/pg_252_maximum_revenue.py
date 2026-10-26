"""EPI Python 16.9, textbook printed page 252: Pick up coins for maximum gain.

QUESTION: Maximize first-player revenue in the take-the-left-or-right-end coins game with optimal opposition.

TEXTBOOK ALGORITHM: Memoize the two-end minimax recurrence printed in EPI.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_16_dynamic_programming.pg_252_maximum_revenue
Test: python -m pytest tests/chapter_16_dynamic_programming/test_pg_252_maximum_revenue.py -v
"""

def maximum_revenue(coins: list[int]) -> int:
    if not coins:
        return 0
    maximum_revenue_for_range = [[0] * len(coins) for _ in coins]

    def compute_maximum_revenue_for_range(a: int,b: int) -> int:
        if a > b:
            return 0
        if maximum_revenue_for_range[a][b] == 0:
            max_revenue_a = coins[a] + min(
                compute_maximum_revenue_for_range(a+2,b),
                compute_maximum_revenue_for_range(a+1,b-1))
            max_revenue_b = coins[b] + min(
                compute_maximum_revenue_for_range(a+1,b-1),
                compute_maximum_revenue_for_range(a,b-2))
            maximum_revenue_for_range[a][b] = max(max_revenue_a,max_revenue_b)
        return maximum_revenue_for_range[a][b]

    return compute_maximum_revenue_for_range(0,len(coins)-1)


if __name__ == '__main__':
    print('Optimal first-player winnings:',maximum_revenue([10,25,5,1,10,5]))
    assert maximum_revenue([10,25,5,1,10,5]) == 31
