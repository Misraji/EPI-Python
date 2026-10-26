# Exercise 5.9: Enumerate all primes to n

**Printed textbook page:** 49. **Reference transcription pages:** 49–49.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 49 (PDF page 63)

```text
for i in range(Ien(A)):
A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)
This approach has time complexity O(n), which is the same as the approach based on median
finding. However, it is much easier to implement and operates in an online fashion, i.e., it never
needs to store more than two elements in memory or read a previous element. It nicely illustrates
algorithm design by iterative refinement of a brute-force solution.
5,9 ENuurnarn ALL PRTMES To 7t
A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.
Write a program that takes an integer argument and retums all the primes between 1 and that
integer. For example, if the input is 18, you should retum <2,3,5,7,77,13,\7>.
Hlnf; Exclude the multiples of primes.
Solution: The natural brute-force algorithm is to iterate over all I from 2to n,where n is the input to
the program. For each l, we test if I is prime; if so we add it to the result. We can use "trial-division"
to test if I is prime, i.e.,by dividing I by each integer from 2 to the square root of l, and checking
if the remainder is 0. (There is no need to test beyond the square root of l, since if i has a divisor
other than 1 and itself, it must also have a divisor that is no greater than its square root.) Since each
test has time complexity O(1fi;, the time complexity of the entire computation is upper bounded
by O(n x li), i.e., O(nz tz1.
Intuitively, the brute-force algorithm tests each number from 1 to rz independently, and does not
exploit the fact that we need to compute all primes from 1 to n. Heuristically, a better approach is
to compute the primes and when a number is identified as a prime, to "sieve" it,i.e., remove all its
multiples from fu ture consideration,
We use a Boolean array to encode the candidates, i.e., if the lth entry in the array is true, then I
is potentially a prime. Initially, every number greater than or equal to 2 is a candidate. Whenever
we determine a number is a prime, we will add it to the result, which is an array. The first prime
is 2. We add it to the result. None of its multiples can be primes, so remove all its multiples from
the candidate set by writing false in the corresponding locations. The next location set to true is 3.
It must be a prime since nothing smaller than it and greater than 1 is a divisor of it. As before, we
add it to result and remove its multiples from the candidate array. We continue till we get to the
end of the array of candidates.
As an example, rt n = 1O the candidate array is initialized to (I, F, T,T,T,T,T,T,T,T,T>,where T
is true and F is false. (Entries 0 and 1 are false, since 0 and 1 are not primes.) We begin with index 2.
Since the corresponding entry is one, we add 2 to the list of primes, and sieve out its multiples. The
arrayisnow(I, I,T,T,F,T,F,T,F,T,F). Thenextnonzeroentryis3,soweaddittothelistof 
prirnes,
and sieve out its multiples. The array is now <F,F,T,T,F,T,F,T,F,F,F>. The next nonzero entries are
5 and7, and neither of them can be used to sieve out more entries.
# Given n, retllrn all prines up to and incTuding n.
def generate-primes (n) :
Primes = []
# is_prine[p] represents if p is prime or not. InitiaTTy, set each to
# true, expecting 0 and 1. IIen use sieving to e-limjnate nonprines.
49
```
