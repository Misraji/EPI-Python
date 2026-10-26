"""EPI 5.7: Buy and sell a stock twice — printed page 47.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Buy and sell a stock twice
Algorithm: Prefix best single-transaction profits and suffix profits combine into two transactions.
Read the corresponding `pg_047_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_05_arrays.pg_047_buy_and_sell_stock_twice
Test: python -m pytest tests/chapter_05_arrays/test_pg_047_buy_and_sell_stock_twice.py -v
"""

def buy_and_sell_stock_twice(prices: list[float]) -> float:
    """Best total gain from at most two non-overlapping transactions."""
    if not prices:
        return 0.0
    lowest = float('inf')
    first_best = 0.0
    left_profits = []
    for p in prices:
        lowest = min(lowest, p)
        first_best = max(first_best, p - lowest)
        left_profits.append(first_best)
    highest = float('-inf')
    second_best = 0.0
    best_total = 0.0
    for i in range(len(prices) - 1, -1, -1):
        highest = max(highest, prices[i])
        second_best = max(second_best, highest - prices[i])
        best_total = max(best_total, left_profits[i] + second_best)
    return best_total


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = buy_and_sell_stock_twice([])
    print("buy_and_sell_stock_twice:", observed)
    assert observed == 0.0
    observed = buy_and_sell_stock_twice([1, 5])
    print("buy_and_sell_stock_twice:", observed)
    assert observed == 4.0
    observed = buy_and_sell_stock_twice([1, 5, 2, 10])
    print("buy_and_sell_stock_twice:", observed)
    assert observed == 12.0
    observed = buy_and_sell_stock_twice([5, 4, 3, 2])
    print("buy_and_sell_stock_twice:", observed)
    assert observed == 0.0
