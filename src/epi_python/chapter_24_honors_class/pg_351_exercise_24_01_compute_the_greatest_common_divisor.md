# Exercise 24.1: Compute the greatest common divisor

**Printed textbook page:** 351. **Reference transcription pages:** 351–351.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 351 (PDF page 365)

```text
o brute-force solutions, including dynamic programming, which have exponential time com-
plexity, may be acceptable, if the instances encountered are small, or if the specific parameter
that the complexity is exponential in is small;
o search algorithms, such as backtracking, branch-and-bound, and hill-climbing, which prune
much of the complexity of a brute-force search;
o approximation algorithms which return a solution that is provably close to optimum;
o heuristics based on insight, conunon case analysis, and careful tuning that may solve the
problem reasonably well;
o parallel algorithms, wherein a large number of computers can work on subparts simultane-
ously.
24.1, Coururr rHE GREATEST coMMoN otvtson $
The greatest common divisor (GCD) of nonnegative integers x and y is the largest integer d such
that d divides r evenly, and d divides y evenly, i.e., r mod d = 0 andy mod d = O. (Il/hen both x
and y arc 0, take their GCD to be 0.)
Design an efficient algorithm for computing the GCD of two nonnegative integers without using
multiplication, division or the modulus operators.
Hint: Use case analysis: both even; both odd; one even and one odd.
Solution: The straightforward algorithm is based on recursion. If x = y, GCD(x,y) = ri otherwise,
assume without loss of generality, that x > y. Then GCD(A y) is the GCD(r - y,y).
The recursive algorithm based on the above does not use multiplication, division or modulus,
but for some inputs it is very slow. As an example, if the input is x = 2n, A = 2, the algorithm
makes 2'-1 recursive calls. The time complexify can be improved by observing that the repeated
subtraction amounts to division, i.e., when x > y,GCD(x,y) = GCD(y,x mod y), but this approach
uses integer division which was explicitly disallowed in the problem statement.
Here is a fast solution, which is also based on recursion, but does not use general multiplication
or division. lnstead it uses case-analysis, specifically, the cases of one, two, or none of the numbers
being even.
An example is illustrative. Suppose we were to compute the GCD of 24 and 300. Instead
of repeatedly subtracting 24 fuorn 300, we can observe that since both are even, the result is 2 x
GCD(12,150). Dividingby 2 is a right shift by 1., so we do not need a general division operation.
Since 12 and 150 are both even, GCD(12,150) = 2 x GCD(6,75). Since 75 is odd, the GCD of 6 and
75 is the same as the GCD of 3 and 75, since 2 carurot divide 75. The GCD of 3 and75 is the GCD
of 3 and 75 - 3 = 72. Repeatedly applying the same logic, GCD(3,72) = GCD(3,36) = GCD(3, 18) =
GCD(3,9) = GCD(3,6) = GCD(3,3) = 3. This implies GCD(24,300) = 2 x 2x3 = 12.
More generally, the base case is when the two arguments are equal, in which case the GCD is
that value, e.g., GCD(12,1,2) = 12, or one of the arguments is zero, irr which case the other is the
GCD, e.g., GCD(0,6) = 6.
Otherr,rrise, we check if none, one/ or both numbers are even. If both are even, we compute the
GCD of the halves of the original numbers, and retum that result times 2; if exactly one is even, we
half it, and retum the GCD of the resultingpai; if both are odd, we subtract the smaller from the
351
```
