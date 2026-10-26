# Exercise 4.9: Check if a decimal integer is a palindrome

**Printed textbook page:** 33. **Reference transcription pages:** 33–33.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 33 (PDF page 47)

```text
Closer analysis shows that we can avoid having to form a string. Consider the input 1132. The
first digit of the result is 2, which we can obtain by taking the input mod 10. The remaining digits of
the result are the reverse of 1,1,32110 = 113. Generalizing, let the input be k. If k > 0, then k mod 10
is the most significant digit of the result and the subsequent digits are the reverse of -!. Continuing
with the example, we iteratively update the result and the input as 2 and 1,1,3, then 23 and 11, then
231 and L, then 2311.
For general k, we record its sign, solve the problem for lkl, and apply the sign to the result.
def reverse (x) :
result, x-remaining = 0, abs(x)
rhile x-remaining:
result = result * 10 + x_remaining % l0
x-remaining //= L0
return -result if x < 0 else result
The time complexity is O(n), where zl is the number of digits in k.
4,9 CHscT IF A DECIMAL INTEGER IS A PALINDRoME
A palindromic string is one which reads the same forwards and backwards, e.g., "redivider". In this
problem, you are to write a program which determines if the decimal representation of an integer is a
palindromic string. For example, your program should return true for the inputs 0,1",7,17,727,333,
a:nd21.4744741.2, arrd false for the inputs -'1,12,100, and 2147483647.
Write a Program that takes an integer and determines if that integer's representation as a decimal
string is a palindrome.
Hint: lt's easy to come up with a simple expression that extracts the least significant digit. Can you find a
simple expression for the most significant digit?
Solution: First note that if the input is negative, then its representation as a decimal string cannot
be palindromic, since itbegins with a -.
A brute-force approach would be to convert the input to a string and then iterate through the
string, pairwise comparing digits starting from the least significant digit and the most significant
digit, and working inwards, stopping if there is a mismatch. The time and space complexity are
O(n),where n is the number of digits in the input.
We can avoid the O(n) space complexity used by the string representation by directly extracting
the digits from the input. The number of digits, n, in the input's string representation is the log
(base 10) of the input value, r. To be precise, n = llogro xJ + 1.. Therefore, the least significant digit
is r mod 10, and the most significant digit is xll}n-t.In the program below, we iteratively compare
the most and least significant digits, and then remove them from the input. For example, if the
input is '1.51751., we would compare the leading and trailing digits, 1 and 1. Since these are equal,
we update the value to 5175. The leading and trailing digits are equal, so we update to 17. Now
the leading and trailing are unequal, so we return false. If instead the number was157751, the final
compare would be of 7 with7, so we would retum true.
def is-palindrome-number (x)
ifx<=0:
JJ
```
