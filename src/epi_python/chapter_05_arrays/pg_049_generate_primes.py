"""EPI Python — Exercise 5.9: Enumerate All Primes to n

Chapter 5: Arrays
Textbook: pages 49–50 (printed page numbers; problem and basic sieve on
page 49, complexity discussion and the improved sieve on page 50).

PROBLEM (from the textbook)
---------------------------
"A natural number is called a prime if it is bigger than 1 and has no
divisors other than 1 and itself."

"Write a program that takes an integer argument and returns all the
primes between 1 and that integer. For example, if the input is 18, you
should return <2,3,5,7,11,13,17>."

HINT (from the textbook)
------------------------
"Exclude the multiples of primes."

SOLUTION DEVELOPMENT (following the textbook)
---------------------------------------------
Brute force: for each i from 2 to n, test whether i is prime by "trial
division": divide i by every integer from 2 up to sqrt(i) and check for a
zero remainder. Testing beyond sqrt(i) is pointless, because a number
with a divisor other than 1 and itself also has one no larger than its
square root. Each test costs O(sqrt(n)), so the whole computation is
bounded by O(n * sqrt(n)) = O(n^(3/2)).

That approach treats each number independently and ignores that we want
ALL primes up to n. A better heuristic: whenever a number is found to be
prime, "sieve" it, i.e. remove all of its multiples from further
consideration.

Sieve details: a Boolean array marks candidates; entry i being true means
i might still be prime. Initially every number >= 2 is a candidate. Each
time a prime is identified it is appended to the result list. 2 is the
first prime; its multiples are marked false. The next true entry is 3,
which must be prime since nothing between 1 and 3 divides it; add it and
remove its multiples. Continue to the end of the array.

Book example with n = 10 (T = true, F = false; entries 0 and 1 start as
false because 0 and 1 are not prime):
  start:            <F,F,T,T,T,T,T,T,T,T,T>
  after sieving 2:  <F,F,T,T,F,T,F,T,F,T,F>
  after sieving 3:  <F,F,T,T,F,T,F,T,F,F,F>
The remaining true entries 5 and 7 are primes, and neither removes any
further entries.

The book prints this basic sieve (here `generate_primes_basic`), then, on
page 50, a faster and smaller variant (here `generate_primes_odd_only`);
see the POST-SOLUTION DISCUSSION below. The file also has
`generate_primes`, an additional sieve written for this repository.

ADDITIONAL EXAMPLES (added for learning; not printed in this exercise)
---------------------------------------------------------------------
    n = 0 or 1 -> []
    n = 2      -> [2]
    n = 10     -> [2, 3, 5, 7]
    n = 20     -> [2, 3, 5, 7, 11, 13, 17, 19]
"""



# `n: int` and `-> list[int]` are type hints. They document the intended
# types; Python does not check them at run time. `list[int]` requires
# Python 3.9 or newer.
# Documentation: https://docs.python.org/3/library/typing.html
def generate_primes(n: int) -> list[int]:
    """Return all primes less than or equal to n (sieve of Eratosthenes).

    Additional implementation written for this repository; not one of the
    book's two printed programs. It starts sieving at candidate * candidate
    (as the book's improved version does) and stops the outer loop once
    candidate^2 exceeds n, keeping all integers (not just odd ones).
    """
    if n < 2:
        return []

    # `[True] * (n + 1)` makes a list of n + 1 True values, one per integer
    # 0..n. Chained assignment `a = b = False` sets both entries.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    candidate = 2

    # Once candidate^2 > n, every composite <= n has already been crossed
    # out by a smaller prime factor.
    while candidate * candidate <= n:
        if is_prime[candidate]:

            # `range(start, stop, step)` yields start, start+step, ... below
            # stop: here the multiples candidate^2, candidate^2 + candidate,
            # ... up to n. Smaller multiples k*candidate (k < candidate) were
            # already removed by the smaller prime factors of k.
            for multiple in range(candidate * candidate, n + 1, candidate):
                is_prime[multiple] = False
        candidate += 1

    # List comprehension with a filter: keep each index whose flag is
    # True. `enumerate(seq)` yields (index, value) pairs.
    # Documentation: https://docs.python.org/3/library/functions.html#enumerate
    return [number for number, prime in enumerate(is_prime) if prime]



def generate_primes_basic(n: int) -> list[int]:
    """First PDF listing: Boolean table covering every integer 0..n.

    The book's basic sieve (its comment: "Given n, return all primes up to
    and including n.").
    """

    # Guard added in this repository; the book has no `n < 2` test in its
    # basic version.
    if n < 2:
        return []

    # Book comment: "is_prime[p] represents if p is prime or not.
    # Initially, set each to true, expecting 0 and 1. Then use sieving to
    # eliminate nonprimes." List `+` concatenates two lists; `[True] * k`
    # repeats True k times, giving n + 1 entries in total.
    candidates = [False, False] + [True] * (n - 1)
    primes = []
    for p in range(2, n+1):
        if candidates[p]:
            primes.append(p)

            # Book comment: "Sieve p's multiples." range(p, n + 1, p) yields
            # p, 2p, 3p, ... up to n.
            for multiple in range(p, n + 1, p):
                candidates[multiple] = False
    return primes


def generate_primes_odd_only(n: int) -> list[int]:
    """Second PDF listing: omit all even candidates except prime 2.

    Slot i represents odd integer 2*i+3. Thus p*p maps to index
    `(p*p-3)//2`, equivalent to the book's `2*i*i+6*i+3` formula.
    """
    if n < 2:
        return []

    # `//` is floor division (rounds toward negative infinity). The count
    # of odd numbers 3, 5, ..., <= n is (n - 3) // 2 + 1; for n = 2 this
    # is (-1) // 2 + 1 = -1 + 1 = 0, so no odd slots exist.
    count = (n-3)//2 + 1
    candidate = [True]*count

    # Book comment: "Stores the primes from 1 to n." 2 is added up front
    # because even numbers are not represented in the table.
    primes = [2]

    # Book comments: "is_prime[i] represents (2i + 3) is prime or not.
    # Initially set each to true. Then use sieving to eliminate nonprimes."
    for i in range(count):
        if candidate[i]:
            p = 2*i+3
            primes.append(p)

            # Book comments: "Sieving from p^2, where p^2 = (4i^2 + 12i + 9).
            # The index in is_prime is (2i^2 + 6i + 3) because is_prime[i]
            # represents 2i + 3." Stepping the index by p moves 2p in value,
            # i.e. through the odd multiples p^2, p^2 + 2p, ... only.
            # The book also notes: "we need to use long for j because p^2
            # might overflow." That concern is for fixed-width integer
            # languages; Python ints have unbounded size.
            for j in range(2*i*i + 6*i + 3, count, p):
                candidate[j] = False
    return primes


# TEXTBOOK POST-SOLUTION DISCUSSION (page 50)
# ------------------------------------------
# The sieve was preferred over trial division on heuristic grounds. Its
# cost: sifting out the multiples of p takes time proportional to n/p, so
# the total is O(n/2 + n/3 + n/5 + n/7 + n/11 + ...). Although not
# obvious, this sum tends asymptotically to n log log n, giving an
# O(n log log n) time bound. The space is dominated by the Boolean array,
# O(n).
#
# The O(n^(3/2)) bound for trial division came from an O(sqrt(n)) bound
# per test. Because most numbers are not prime, the test usually exits
# early, so trial division is actually faster than that on average: its
# known complexity is O(n^(3/2) / (log n)^2). The sieve is still superior.
#
# Two improvements lead to the second program:
#   - Sieve p's multiples starting from p^2 instead of p, because every
#     number k*p with k < p has already been removed.
#   - Halve the storage by not representing even numbers.
# The improved program has the same asymptotic time and space complexity
# as the basic sieve.
#
# VARIANTS
# --------
# The book gives no variants for this exercise.


# TEXTBOOK CODE COMPARISON
# ------------------------
# - Both book programs are named `generate_primes(n)`. The file names the
#   basic one `generate_primes_basic` and the improved one
#   `generate_primes_odd_only`; the name `generate_primes` is used for a
#   third sieve that is NOT in the book (full table, `while c*c <= n`
#   outer loop, starts at c*c, result built by a list comprehension with
#   enumerate). Type hints added to all three.
# - Basic sieve: book list is `is_prime`, inner loop variable `i`; file
#   uses `candidates` and `multiple`, and adds an `if n < 2: return []`
#   guard the book's basic version lacks. Otherwise matches.
# - Improved sieve: book names `size` and `is_prime`; file uses `count`
#   and `candidate`. Book writes `2 * i**2 + 6 * i + 3` and `i * 2 + 3`;
#   file `2*i*i + 6*i + 3` and `2*i+3`. Otherwise matches.


# Python executes this block only when this source file is run directly.
# When pytest imports the file, this block is skipped automatically.
# Documentation: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    # Run a few self-contained examples before exploring the pytest suite.
    #
    # These n values are added for learning (boundary cases 0, 1, 2 and
    # small ranges). print() with several arguments separates them with a
    # space. `assert` stops the program with an AssertionError if a
    # condition is false; pytest provides the more thorough verification.
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

    # Cross-check: both textbook sieves and the extra sieve agree.
    # `a == b == c` is a chained comparison meaning `a == b and b == c`.
    for n in (0, 2, 10, 20, 50):
        textbook_basic = generate_primes_basic(n)
        textbook_odd_only = generate_primes_odd_only(n)
        print("Textbook sieves for", n, ":", textbook_odd_only)
        assert textbook_basic == textbook_odd_only == generate_primes(n)
