# Exercise 5.3: Multiply two arbitrary-precision integers

**Printed textbook page:** 43. **Reference transcription pages:** 43–43.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 43 (PDF page 57)

```text
5.2 INcnsMsl{r AN ARBTTRARy-pRECrsroN TNTEGER
Write a program which takes as input an array of digits encoding a nonnegative decimal integer
D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
langua ge that has finite-precision arithmetic.
Hlzf: Experiment with concrete examples.
Solution: A brute-force approach might be to convert the array of digits to the equivalent integel,
increment that, and then convert the resulting value back to an array of digits. For example, if the
array is <1.,2,9r, we would derive the integer 129, add one to get 130, then extract its digits to form
(1,3,0). lrVhen implemented in a language that imposes a limit on the range of values an integer
type can take, this approach will fail on inputs that encode integers outside of that range.
We can avoid overflow issues by operating directly on the array of digits. Specifically, we mimic
the grade-school algorithm for adding integers, which entails adding digits starting from the least
significant digit, and propagate carries. If the result has an additional digit, e.g., 99 + 1. = 100, there
is not enough storage in the array for the result-we need three digits to represent 100, but the input
has only two digits.
For the given example, we would update 9 to 0 with a carry-out of 1. We update 2 to 3 (because
of the carry-in). There is no carry-out, so we stop-the result is (1,3,0).
def plus-one (A) :
A[-1] += r
for i in reversed(range(1, Ien(A))):
if Atil != 10:
break
Atil = 6
AIi - 1] += 1
if Atol == 10:
# There is a carry-out, so we need one more digit to store the resu-It
# A slick way to do this is to append a 0 at the end of the array,
# and update the fjrst entry to 1.
A[0] = 1
A. append (0)
return A
The time complexity isO(n), where n is the length of A.
Variant: Write a program which takes as input two strings s and f of bits encodingbinary numbers
B, and 81, respectively, and refurns a new string of bits representing the number B, + Bs.
5.3 Mur,rrpry rwo ARBTTRARy-pREcrsroN TNTEGERS
Certain applications require arbitrary precision arithmetic. One way to achieve this is to use arrays
to represent integers, e.9., with one digit per array entry with the most significant digit appearing
first, and a negative leading digit denoting a negative integer. For example, <1,9,3,7,0,7,7,2,1>
represents 193707721 and (-7,6,1.,8,3,8,2,5,7,2,8,7> represents -761838257287.
43
```
