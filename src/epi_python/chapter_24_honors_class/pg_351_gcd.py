"""EPI 24.1: Compute the greatest common divisor (printed page 351).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Compute the greatest common divisor
Method: Repeated remainders preserve the GCD and shrink the arguments. Uses nonnegative inputs after abs().

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_351_exercise_24_01_compute_the_greatest_common_divisor.md

Run independently:
    python -m epi_python.chapter_24_honors_class.pg_351_gcd
Run thorough tests:
    python -m pytest tests/chapter_24_honors_class/test_pg_351_gcd.py -v
"""

def gcd(x: int, y: int) -> int:
    """Greatest common divisor using the Euclidean remainder recurrence."""
    x, y = abs(x), abs(y)
    while y:
        x, y = y, x % y
    return x


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = gcd(0, 0)
    print("gcd:", observed)
    assert observed == 0
    observed = gcd(20, 8)
    print("gcd:", observed)
    assert observed == 4
    observed = gcd(17, 13)
    print("gcd:", observed)
    assert observed == 1
    observed = gcd(-12, 18)
    print("gcd:", observed)
    assert observed == 6
    observed = gcd(100, 10)
    print("gcd:", observed)
    assert observed == 10
