"""EPI 6.13: Find the first occurrence of a substring — printed page 79.

Educational reconstruction; not a verified verbatim textbook transcription.
Question: Find the first occurrence of a substring
Algorithm: Rabin–Karp polynomial rolling hash, with an exact substring comparison to resolve rare hash collisions.
Read the corresponding `pg_079_exercise_...md` file for the extracted
book's problem, worked explanations and variants. OCR is unverified.

Run: python -m epi_python.chapter_06_strings.pg_079_rabin_karp
Test: python -m pytest tests/chapter_06_strings/test_pg_079_rabin_karp.py -v
"""

def rabin_karp(text: str, pattern: str) -> int:
    """Find first pattern position with a polynomial rolling-hash search."""
    if not pattern:
        return 0
    m = len(pattern)
    if m > len(text):
        return -1
    base = 256
    modulus = 1_000_000_007
    power = pow(base, m - 1, modulus)
    target_hash = 0
    current_hash = 0
    for i in range(m):
        target_hash = (target_hash * base + ord(pattern[i])) % modulus
        current_hash = (current_hash * base + ord(text[i])) % modulus
    for start in range(len(text) - m + 1):
        if target_hash == current_hash and text[start:start + m] == pattern:
            return start
        if start + m < len(text):
            current_hash = (
                (current_hash - ord(text[start]) * power) * base
                + ord(text[start + m])
            ) % modulus
    return -1


if __name__ == "__main__":
    # Demonstrations check representative input/output behavior.
    observed = rabin_karp('hello world', 'world')
    print("rabin_karp:", observed)
    assert observed == 6
    observed = rabin_karp('abcabc', 'cab')
    print("rabin_karp:", observed)
    assert observed == 2
    observed = rabin_karp('abc', 'z')
    print("rabin_karp:", observed)
    assert observed == -1
    observed = rabin_karp('abc', '')
    print("rabin_karp:", observed)
    assert observed == 0
