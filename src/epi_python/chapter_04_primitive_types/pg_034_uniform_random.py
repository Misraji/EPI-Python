"""EPI Python — Exercise 4.10: Generate Uniform Random Numbers

Chapter 4: Primitive Types
Textbook: pages 34–35 (printed page numbers; problem, solution and the
start of the program are on 34; the rest of the program and the complexity
analysis are at the top of 35).

PROBLEM (from the textbook)
---------------------------
This problem is motivated by the following scenario. Six friends have to
select a designated driver using a single unbiased coin. The process should
be fair to everyone.

How would you implement a random number generator that generates a random
integer i between a and b, inclusive, given a random number generator that
produces zero or one with equal probability? All values in [a, b] should be
equally likely.

HINT (from the textbook)
------------------------
How would you mimic a three-sided coin with a two-sided coin?

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
A random integer from 0 to 2**i - 1 inclusive is easy: generate i random
bits and put them side by side. With two calls the outcome is one of
(00)_2, (01)_2, (10)_2, (11)_2, which stand for 0, 1, 2, 3, all equally
likely.

General case: generating a number in [a, b] is the same as generating one
in [0, b - a] and adding a. If b - a happens to equal 2**i - 1 for some i,
the previous paragraph solves it directly.

Otherwise, find the smallest number of the form 2**i - 1 that is larger than
b - a, and generate an i-bit number. If it lies in [0, b - a], return it;
all such values are equally likely. If not, throw it away and try again with
i fresh random bits, repeating until a value lands in range.

Book's dice example (a number from 1 to 6): since 2**2 - 1 < (6 - 1) <=
2**3 - 1, make three calls to the bit generator. If the result is one of
(000)_2, (001)_2, (010)_2, (011)_2, (100)_2, (101)_2, return 1 plus that
value; each of 1..6 is equally likely. If the result is (110)_2 or (111)_2,
make three more calls. The chance of having to retry is 2/8, under one
half. Tries are independent, so needing many tries quickly becomes
unlikely: failing 10 times in a row has probability (2/8)**10, less than one
in a million.

The book gives one program, implemented below as `uniform_random`.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    uniform_random(4, 9, bits) for a seeded bit source: five draws, each an
    integer in 4..9 (six equally likely outcomes, like the dice example).
"""

# Python standard library: pseudo-random number generators.
# Module documentation: https://docs.python.org/3/library/random.html
# getrandbits: https://docs.python.org/3/library/random.html#random.getrandbits
# Random class: https://docs.python.org/3/library/random.html#random.Random
import random


# Type hints (`lower_bound: int`, `-> int`) document intended types; Python
# does not enforce them. `bit_source=None` is an optional parameter with no
# hint: it should be a function taking no arguments and returning 0 or 1
# (the book's `zero_one_random()`). Passing one makes results reproducible.
def uniform_random(lower_bound: int, upper_bound: int, bit_source=None) -> int:
    """Uniformly select an integer in [lower_bound, upper_bound].

    Textbook implementation (rejection sampling from random bits), with an
    added injectable bit source and an added bounds check.
    """
    if lower_bound > upper_bound:

        # ValueError is the built-in exception for an unacceptable value.
        # https://docs.python.org/3/library/exceptions.html#ValueError
        raise ValueError("Lower bound must not exceed upper bound")
    if bit_source is None:

        # `lambda: expression` creates a small anonymous function; here one
        # with no parameters whose body is the single expression after the
        # colon. Calling bit_source() therefore calls random.getrandbits(1).
        #
        # random.getrandbits(k) returns a nonnegative int made of k random
        # bits; with k = 1 it returns 0 or 1 with equal probability. It uses
        # the module's shared generator, so results differ from run to run.
        # This plays the role of the book's zero_one_random().
        bit_source = lambda: random.getrandbits(1)

    # The number of possible outcomes, t = b - a + 1 in the book's analysis.
    count = upper_bound - lower_bound + 1

    # `while True` loops until a `return` exits: each pass is one "try".
    while True:
        result = 0

        # int.bit_length() returns how many binary digits are needed to write
        # the number (0 -> 0, 5 = 0b101 -> 3). (count - 1).bit_length() is
        # the smallest i with 2**i >= count, the same i the book reaches with
        # its `while (1 << i) < number_of_outcomes` loop.
        # https://docs.python.org/3/library/stdtypes.html#int.bit_length
        # `_` is the conventional name for an unused loop variable.
        for _ in range((count - 1).bit_length()):

            # `result << 1` shifts the bits so far one place left; `|` (OR)
            # puts the new random bit in the freed lowest position. This
            # concatenates the random bits into an i-bit number.
            result = (result << 1) | bit_source()

        # Accept only values in 0..count-1, each equally likely; otherwise
        # reject and draw a fresh set of bits.
        if result < count:
            return lower_bound + result


# TEXTBOOK POST-SOLUTION DISCUSSION (page 35)
# -------------------------------------------
# Let t = b - a + 1. A single try succeeds with probability t / 2**i. Since
# 2**i is the smallest power of 2 that is >= t, it is less than 2t (look at
# t and 2t in binary to see this). So t / 2**i > t / 2t = 1/2, and a try
# fails with probability 1 - t / 2**i < 1/2.
#
# Tries are independent, so the chance of needing more than k tries is at
# most 1 / 2**k. The expected number of tries is therefore at most
# 1 + 2(1/2)**1 + 3(1/2)**2 + ..., a convergent series, so it is O(1).
#
# Each try makes ceil(log(b - a + 1)) calls to the 0/1 generator. If one
# call takes O(1) time, the time complexity is O(log(b - a + 1)).
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Book: `def uniform_random(lower_bound, upper_bound)` calling a provided
#   `zero_one_random()`. File: adds type hints and a third parameter
#   `bit_source=None`, defaulting to `random.getrandbits(1)` via a lambda
#   (the book has no import).
# - Book: `number_of_outcomes`, and a bit-counting loop
#   `result, i = 0, 0; while (1 << i) < number_of_outcomes: ...; i += 1`.
#   File: `count`, and `for _ in range((count - 1).bit_length())` (same
#   number of bits).
# - Book: `if result < number_of_outcomes: break` then, after the loop,
#   `return result + lower_bound`. File: returns directly inside the loop.
# - File adds a ValueError check for lower_bound > upper_bound.
# - Book's comment "zero_one_random() is the provided random number
#   generator." is reflected in the comments above.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":

    # random.Random(seed) creates an independent generator object. With a
    # fixed seed (42) it produces the same sequence on every run, which
    # makes the printed examples reproducible.
    # https://docs.python.org/3/library/random.html#random.Random
    generator = random.Random(42)

    # Draw five numbers in [4, 9] (six outcomes, like a die roll shifted).
    for _ in range(5):

        # The lambda wraps the seeded generator as a no-argument 0/1 source.
        sample = uniform_random(4, 9, lambda: generator.getrandbits(1))

        # f-string: each expression in {} is evaluated and inserted.
        # https://docs.python.org/3/reference/lexical_analysis.html#f-strings
        print(f"uniform_random(4, 9) = {sample}")

        # `assert` stops the program with an AssertionError if the condition
        # is false; `4 <= sample <= 9` is a chained comparison. This only
        # checks the range; pytest does the thorough (statistical) testing.
        assert 4 <= sample <= 9
