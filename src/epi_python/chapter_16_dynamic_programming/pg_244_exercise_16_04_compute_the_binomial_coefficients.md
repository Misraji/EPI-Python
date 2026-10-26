# Exercise 16.4: Compute the binomial coefficients

**Printed textbook page:** 244. **Reference transcription pages:** 244–244.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 244 (PDF page 258)

```text
number D monotoneif DUI < DU + 11,0 < i < lDl. Write a program which takes as input a positive
integer k and computes the number of decimal numbers of length k that are monotone.
Variant: Call a decimal number D, as defined above, strictly monotone if D[r] < DU + 11,0 < i < lDl.
Write a program which takes as input a positive integer k and computes the number of decirnal
numbers of length k that are strictly monotone.
16.4 Coupurr rHE BTNoMTAL coEFFICIENTS
The symbol (X) is tf,e short form for the expression #+ffi,fi 
It is the number of ways to choose
a k-element subset from an n-element set. It is not obvious that the expression defining ([) always
yields an integer. Furthermore, direct computation of ([) from this expression quickly results in the
numerator or denominator overflowing if integer types are used, even if the final result fits in a
32-bit integer. If floats are used, the expression may not yield a 32-bit integer.
Design an efficient algorithm for computing ([) which has the property that it never overflows if
the final result fits in the integer word size.
Hint: Write an equation.
Solution: Abrute-force approach would be to compute n(n-l)' ' '(n-k+l), then k(k- 1)' ' ' (3X2)(1),
and finally divide the former by the latter. As pointed out in the problem introduction, this can
lead to overflows, even when the final result fits in the integer word size.
It is tempting to proceed by pairing terms in the numerator and denominator that have conunon
factors and cancel them out. This approach is unsatisfactory because of the need to factor numbers,
which itself is challenging.
A better approach is to avoid multiplications and divisions entirely. Fundamentally, the binomial
coefficient counts the number of subsets of size k in a set of size n. We could enumerate k-sized
subsets of {0,1,,2,...,n- 1} sets using recursion, as in Solution 15.5 on Page226. The idea is as
follows. Consider the rth element in the initial set. A subset of size k will either contain this element,
or not contain it. This is the basis for a recursive enumeration-find all subsets of size k - L amongst
the first n - 1 elements and add the nth element into these sets, and then find all subsets of size k
amongst the first n - 1 elements. The union of these two subsets is all subsets of size k.
However, since all we care about is th e number of such subsets, we can do much better complexity-
wise. The recursive enumeration also implies that the binomial coefficient must satisfy the following
formula:
(;)=(';').ft-l)
This identity yields a straightforward recursion for ([). The base cases are (l) *a (6), both of
which are 1. The individual results from the subcalls are 32-bit integers and if ([) canbe represented
by a3}-bitinteger, they can too, so it is not possible for intermediate results to overflow.
Forexample,() = (l)*(t). Expanding(!),weget(1) = ()*(?).Expanding(l;,weget(]) = (i)*(?).
Note that (l) is a Uase case, retuming 1. Continuing this way, we get (l),which is 6 and (t), *tri.tr it
+,so(!) =6+4=10.
Naively implemented, the above recursion will have repeated subcalls with identical arguments
and exponential time complexity. This can be avoided by caching intermediate results.
def conpute-binomial-coefficient(n, k)
244
```
