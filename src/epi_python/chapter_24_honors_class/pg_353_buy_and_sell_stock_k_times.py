"""EPI Python 24.3, textbook printed page 353: Buy and sell a stock k times.

QUESTION: Compute maximum profit from at most k nonoverlapping stock buy-sell transactions.

TEXTBOOK ALGORITHM: Use the O(k*n) update of minimum effective purchase prices and maximum accumulated profits, iterating transaction counts backward.

The complete question, hints, solution development, and variants are in the
adjacent page-numbered reference Markdown, extracted from the supplied PDF.
This executable implementation restores syntax damaged by the PDF text layer;
minor type annotations, examples, and assertions are educational additions.

Run: python -m epi_python.chapter_24_honors_class.pg_353_buy_and_sell_stock_k_times
Test: python -m pytest tests/chapter_24_honors_class/test_pg_353_buy_and_sell_stock_k_times.py -v
"""

def buy_and_sell_stock_k_times(prices: list[float], k: int) -> float:
    if not k or not prices:
        return 0.0
    if 2*k>=len(prices):

        # zip pairs each day's price with the following day's price.
        return sum(max(0.0,b-a) for a,b in zip(prices[:-1],prices[1:]))
    min_prices=[float('inf')]*k
    max_profits=[0.0]*k
    for price in prices:

        # reversed walks transaction counts backward so each update uses the
        # previous day's values for the immediately preceding transaction.
        for i in reversed(range(k)):
            max_profits[i]=max(max_profits[i],price-min_prices[i])
            min_prices[i]=min(min_prices[i],price-(0 if i==0 else max_profits[i-1]))
    return max_profits[-1]


if __name__ == '__main__':
    values=[3,2,6,5,0,3]
    profit=buy_and_sell_stock_k_times(values,2)
    print('Maximum profit for two trades:',profit)
    assert profit==7
