"""EPI 5.9: Enumerate all primes to n (printed page 49).

ORIGIN: Educational reconstruction based on the supplied EPI exercise.
NOT a verified line-for-line transcription of the textbook's Python snippet.

Question: Enumerate all primes to n
Method: Cross off all multiples starting with each prime square. Time O(n log log n), space O(n).

For the PDF text layer of the original problem, solution exposition, variants,
and complexity discussion, read the companion Markdown document:
    pg_049_exercise_05_09_enumerate_all_primes_to_n.md

Run independently:
    python -m epi_python.chapter_05_arrays.pg_049_generate_primes
Run thorough tests:
    python -m pytest tests/chapter_05_arrays/test_pg_049_generate_primes.py -v
"""

def generate_primes(n: int) -> list[int]:
    """Return all primes less than or equal to n (sieve of Eratosthenes)."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    candidate = 2
    while candidate * candidate <= n:
        if is_prime[candidate]:
            for multiple in range(candidate * candidate, n + 1, candidate):
                is_prime[multiple] = False
        candidate += 1
    return [number for number, prime in enumerate(is_prime) if prime]


if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    observed = generate_primes(0)
    print("generate_primes:", observed)
    assert observed == []
    observed = generate_primes(1)
    print("generate_primes:", observed)
    assert observed == []
    observed = generate_primes(2)
    print("generate_primes:", observed)
    assert observed == [2]
    observed = generate_primes(10)
    print("generate_primes:", observed)
    assert observed == [2, 3, 5, 7]
    observed = generate_primes(20)
    print("generate_primes:", observed)
    assert observed == [2, 3, 5, 7, 11, 13, 17, 19]
