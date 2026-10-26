"""EPI exercise 11.9, printed page 155: Find the missing IP address.

EDUCATIONAL RECONSTRUCTION — not a verbatim verified code transcription.
Problem: Find the missing IP address.
Method/complexity: Two passes, O(n + 2^prefix + 2^suffix) time, bounded count/bitmap storage.
For the book's original explanation and variants, see:
    pg_155_exercise_11_09_find_the_missing_ip_address.md

Run: python -m epi_python.chapter_11_searching.pg_155_find_missing_ip
Test: python -m pytest tests/chapter_11_searching/test_pg_155_find_missing_ip.py -v
"""

def find_missing_ip(addresses, address_bits: int = 16, prefix_bits: int = 8) -> int:
    """Find a missing address using two passes over a replayable integer iterable."""
    if not (1 <= prefix_bits < address_bits <= 32):
        raise ValueError("Need 1 <= prefix_bits < address_bits <= 32")
    # The test version supports a replayable iterable (list/tuple/range).
    # For file input, pass a factory that reopens the data source each pass.
    produce = addresses if callable(addresses) else lambda: iter(addresses)
    suffix_bits = address_bits - prefix_bits
    bucket_count = 1 << prefix_bits
    bucket_capacity = 1 << suffix_bits
    counts = [0] * bucket_count
    for address in produce():
        if not 0 <= address < (1 << address_bits):
            raise ValueError("Address out of configured address space")
        counts[address >> suffix_bits] += 1
    bucket = next((i for i, count in enumerate(counts) if count < bucket_capacity), None)
    if bucket is None:
        raise ValueError("No missing address")
    seen = bytearray(bucket_capacity)
    for address in produce():
        if address >> suffix_bits == bucket:
            seen[address & (bucket_capacity - 1)] = 1
    suffix = seen.index(0)
    return bucket << suffix_bits | suffix


if __name__ == "__main__":
    addresses = [i for i in range(256) if i != 42]
    print("missing IP:", find_missing_ip(addresses, 8, 4))
    assert find_missing_ip(addresses, 8, 4) == 42
