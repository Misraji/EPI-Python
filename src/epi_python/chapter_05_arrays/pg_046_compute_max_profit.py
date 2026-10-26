"""EPI 5.6: Buy and sell a stock once (printed page 46).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Buy and sell a stock once
Method: Track lowest price seen so far, then compute best selling profit at each new price. Time O(n), space O(1).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_046_exercise_05_06_buy_and_sell_a_stock_once.md

Run independently:
    python -m epi_python.chapter_05_arrays.pg_046_compute_max_profit
Run thorough tests:
    python -m pytest tests/chapter_05_arrays/test_pg_046_compute_max_profit.py -v
"""

def compute_max_profit(prices: list[float]) -> float:
    """Largest profit obtainable by one buy followed by one sell."""
    min_seen = float("inf")
    max_profit = 0.0
    for price in prices:
        min_seen = min(min_seen, price)
        max_profit = max(max_profit, price - min_seen)
    return max_profit


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = compute_max_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
    print("compute_max_profit:", observed)
    assert observed == 30.0
    observed = compute_max_profit([5, 4, 3])
    print("compute_max_profit:", observed)
    assert observed == 0.0
    observed = compute_max_profit([])
    print("compute_max_profit:", observed)
    assert observed == 0.0
    observed = compute_max_profit([1, 5])
    print("compute_max_profit:", observed)
    assert observed == 4.0
