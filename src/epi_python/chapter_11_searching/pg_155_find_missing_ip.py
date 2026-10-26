"""EPI Python — Exercise 11.9: Find the Missing IP Address

Chapter 11: Searching
Textbook: pages 155–156 (printed page numbers; problem and first ideas on
155, the two-pass method, program and storage remark on 156).

PROBLEM (from the textbook)
---------------------------
"The storage capacity of hard drives dwarfs that of RAM. This can lead to
interesting space-time trade-offs.

Suppose you were given a file containing roughly one billion IP addresses,
each of which is a 32-bit quantity. How would you programmatically find an
IP address that is not in the file? Assume you have unlimited drive space
but only a few megabytes of RAM at your disposal."

HINT (from the textbook)
------------------------
"Can you be sure there is an address which is not in the file?"

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Treat the file as a list of 32-bit integers.

1. Sort and scan: sort the file, then look for a gap between consecutive
   values. O(n log n) time for n entries, and with little RAM the sort must
   use disk as storage, which is very slow in practice.

2. Largest + 1: does not work in general -- if the largest entry is
   255.255.255.255 (the highest possible address), adding one overflows.
   Smallest - 1 has the same problem. (The book notes this would be a good
   heuristic in practice.)

3. Hash table: insert every address, then try 0.0.0.0, 0.0.0.1, ... until
   one is missing from the table. This needs at least 4 gigabytes of RAM
   for the data. (Book footnote: a hash table carries extra overhead -- the
   table itself and the next-fields of the collision chains -- roughly
   6 gigabytes on a 32-bit machine.)

4. Bit array: one bit per possible address, 2^32 bits all starting at 0;
   set the bit for each address in the file, then look for a 0 bit. There
   are 2^32 (about 4 x 10^9) possible addresses, so some bit must remain 0.
   This is an order of magnitude smaller, but 2^32 / 8 bytes is half a
   gigabyte, still far above the memory limit.

5. Multiple passes, one bit at a time: since the input is a file, it can be
   read more than once. Count how many addresses start with bit 1 and how
   many with bit 0. Some address is absent, so at least one count is below
   2^31. Say an absent address must start with 0: from then on consider only
   file addresses starting with 0 and repeat on the second bit, and so on.
   This takes 32 passes and only two integer counters.

6. Counting on groups of bits (the book's final method): with more memory
   available, count the addresses by their leading 16 bits using an array
   of 2^16 integers (each fits in 32 bits). Each address's 16 most
   significant bits index into the array, and that count is incremented.
   Because the file has fewer than 2^32 numbers, some entry is below 2^16,
   so at least one address with those upper 16 bits is missing. A second
   pass looks only at addresses whose top 16 bits match that bucket, and a
   bit array of size 2^16 records which lower 16-bit values occur; any
   unset position gives a missing address.

This file implements method 6:
  * find_missing_ip -- the two-pass bucket method generalised to a
    configurable address width (address_bits) and bucket width
    (prefix_bits), so tests can use small address spaces.
  * find_missing_ip_32bit -- the book's full-size setting: 32-bit addresses
    and 16-bit buckets, delegating to find_missing_ip.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    8-bit addresses 0..255 except 42, 4-bit buckets -> 42
    32-bit addresses [0, 1, 2, 4]                   -> 3
"""


def find_missing_ip(addresses, address_bits: int = 16, prefix_bits: int = 8) -> int:
    """Find a missing address using two passes over a replayable integer iterable.

    This is the textbook's find_missing_element two-pass method,
    generalised to configurable bit widths and re-reading the input through
    a factory function instead of itertools.tee.

    `addresses` has no type hint: it may be a replayable iterable of ints
    (list, tuple, range) or a zero-argument function returning a fresh
    iterator each time it is called. `address_bits: int = 16` and
    `prefix_bits: int = 8` are parameters with defaults; `-> int` is the
    return type. Python does not enforce type hints.
    """

    # Chained comparison: all three inequalities must hold. The bucket
    # prefix must be shorter than the address, and at most 32 bits are
    # allowed (the IP address size).
    # ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    if not (1 <= prefix_bits < address_bits <= 32):
        raise ValueError("Need 1 <= prefix_bits < address_bits <= 32")
    # The test version supports a replayable iterable (list/tuple/range).
    # For file input, pass a factory that reopens the data source each pass.
    #
    # callable(obj) is True if obj can be called like a function. If the
    # caller passed a factory, use it directly. Otherwise wrap the iterable
    # in a `lambda` -- a small anonymous function -- that calls iter() to
    # get a fresh iterator each time. Either way, `produce()` starts a new
    # pass over the data. This replaces the book's itertools.tee copy.
    # callable: https://docs.python.org/3/library/functions.html#callable
    # iter: https://docs.python.org/3/library/functions.html#iter
    # lambda: https://docs.python.org/3/reference/expressions.html#lambda
    produce = addresses if callable(addresses) else lambda: iter(addresses)
    suffix_bits = address_bits - prefix_bits

    # `1 << n` shifts 1 left by n bits, i.e. computes 2**n. There are
    # 2**prefix_bits buckets, and each bucket can hold 2**suffix_bits
    # distinct addresses (its "capacity").
    bucket_count = 1 << prefix_bits
    bucket_capacity = 1 << suffix_bits

    # `[0] * n` builds a list of n zeros: one counter per bucket.
    counts = [0] * bucket_count

    # Pass 1: count addresses per leading-bits bucket.
    for address in produce():
        if not 0 <= address < (1 << address_bits):
            raise ValueError("Address out of configured address space")

        # `address >> suffix_bits` shifts right, discarding the low suffix
        # bits and leaving the high prefix bits: the bucket number (the
        # book's `x >> 16`). Python ints are unbounded and nonnegative here,
        # so no sign issues arise.
        counts[address >> suffix_bits] += 1

    # Book's comment: look for a bucket that contains fewer than its
    # capacity of elements.
    #
    # `(i for i, count in enumerate(counts) if count < bucket_capacity)` is
    # a generator expression: it lazily yields each bucket index whose count
    # is too small. enumerate() pairs each count with its index. next(gen,
    # None) returns the first yielded value, or the default None if there is
    # none (instead of raising StopIteration as the book's next() would).
    # next: https://docs.python.org/3/library/functions.html#next
    # enumerate: https://docs.python.org/3/library/functions.html#enumerate
    bucket = next((i for i, count in enumerate(counts) if count < bucket_capacity), None)
    if bucket is None:
        raise ValueError("No missing address")

    # bytearray(n) creates a mutable sequence of n zero bytes. It serves as
    # the bit array of size 2**suffix_bits (one byte per flag, which is
    # simpler than packing bits).
    # bytearray: https://docs.python.org/3/library/stdtypes.html#bytearray
    seen = bytearray(bucket_capacity)

    # Pass 2: book's comment -- find all addresses whose leading bits equal
    # the chosen bucket, and record the presence of their low bits.
    for address in produce():
        if address >> suffix_bits == bucket:

            # `&` is bitwise AND. bucket_capacity - 1 is a mask of
            # suffix_bits ones (e.g. 0b1111), so this keeps only the low
            # bits -- the book's `((1 << 16) - 1) & x`.
            seen[address & (bucket_capacity - 1)] = 1

    # Book's comment: at least one of the low-bit combinations is absent;
    # find it. bytearray.index(0) returns the position of the first 0 byte.
    # bytes.index: https://docs.python.org/3/library/stdtypes.html#bytes.index
    suffix = seen.index(0)

    # Reassemble the address: shift the bucket back into the high bits and
    # combine with the low bits using `|` (bitwise OR). `<<` binds more
    # tightly than `|`, so this is (bucket << suffix_bits) | suffix.
    return bucket << suffix_bits | suffix



def find_missing_ip_32bit(addresses) -> int:
    """Full-size PDF exercise: 32-bit address space, using 16-bit buckets.

    The same two-pass method as the scaled testing function, requiring
    65,536 16-bit prefix counts and a 65,536-byte suffix bitmap.
    Supply a replayable iterable or a factory that opens the source twice.

    This corresponds directly to the textbook's parameters (1 << 16 buckets,
    16 low bits per bucket). Not a separate book function.
    """

    # Keyword arguments (`name=value`) make the chosen widths explicit.
    return find_missing_ip(addresses,address_bits=32,prefix_bits=16)


# TEXTBOOK POST-SOLUTION DISCUSSION (page 156)
# --------------------------------------------
# The storage is dominated by the count array, i.e., 2^16 integer entries.
# (The second-pass bit array has 2^16 entries as well.) Each pass reads the
# whole file once, so the method uses two passes, O(n) time overall.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# Book: `def find_missing_element(stream):` with constants
#   `NUM_BUCKET = 1 << 16` and `BUCKET_CAPACITY = 1 << 16`, a counter list,
#   `stream, stream_copy = itertools.tee(stream)` to read the stream twice
#   (so the book imports itertools), `upper_part_x = x >> 16`,
#   `candidate_bucket = next(i for i, c in enumerate(counter) if c <
#   BUCKET_CAPACITY)`, a `candidates = [0] * BUCKET_CAPACITY` list filled
#   with `lower_part_x = ((1 << 16) - 1) & x`, and a final loop
#   `for i, v in enumerate(candidates): if v == 0: return
#   (candidate_bucket << 16) | i`.
# File: function renamed `find_missing_ip` and generalised with
#   `address_bits` / `prefix_bits` parameters (defaults 16 / 8, not the
#   book's 32 / 16); no itertools.tee -- the input is re-read through a
#   `produce` factory (callable or `lambda: iter(addresses)`); adds input
#   validation (ValueError for bad widths, out-of-range addresses, and when
#   no bucket has room) that the book lacks; `bytearray` replaces the
#   `candidates` list; `seen.index(0)` replaces the final enumerate loop;
#   names changed (counter -> counts, candidate_bucket -> bucket, etc.).
#   Extra helper `find_missing_ip_32bit` (not in the book) calls it with the
#   book's 32-bit / 16-bit settings.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # A list comprehension builds every 8-bit value 0..255 except 42.
    # With 8-bit addresses and 4-bit buckets, the bucket 42 >> 4 == 2 holds
    # only 15 of its 16 values, so the second pass finds 42.
    #
    # `assert` stops the program with an AssertionError if the condition is
    # false; these are quick smoke checks, while pytest provides the more
    # thorough automated verification.
    addresses = [i for i in range(256) if i != 42]
    print("missing IP:", find_missing_ip(addresses, 8, 4))
    assert find_missing_ip(addresses, 8, 4) == 42

    # Exercise's actual 32-bit address domain, with small test input.
    # The input is given as a factory (`lambda: iter([...])`), so each of
    # the two passes gets a fresh iterator -- the way a file would be
    # reopened for each pass.
    assert find_missing_ip_32bit(lambda: iter([0,1,2,4])) == 3
