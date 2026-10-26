# Exercise 6.1: Interconvert strings and integers

**Printed textbook page:** 68. **Reference transcription pages:** 68–68.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 68 (PDF page 82)

```text
Similar to arrays, string
that use
sPace
solution, but subtler solutions that use the string itself to reduce space complexity to O(1).
Understand the implications of a string type which is immutable, e.9., the need to allocate a
new string when concatenating immutable strings. Know alternatives to immutable strings,
e.g., a list in Python.
Updating a mutable string from the front is slow, so see if it's possible to write values from the
back.
Table 6.1 : Top Tips for Strings
implementations of Python use tricks under-the-hood to avoid having to do this allocation, reducing
the complexrty to O(n).)
6.1, IurnncouvrRT sTRINGS AND INTEcERS
A string is a sequence of characters. A string may encode an integer, e.g., "123" encodes 123. In
this problem, you are to irnplement methods that take a string representing an integer and retum
the corresponding integer, and vice versa. Your code should handle negative integers. You cannot
use library functions like int in Python.
Implement an integer to string conversion function, and a string to integer conversison function,
For example, if the input to the first function is the integer 314,it should retum the string "31.4" and
if the input to the second function is the string "314" it should return the integer 314.
Hint: Build the result one digit at a time.
Solution: Let's consider the integer to string problem first. If the number to convert is a single
digit, i.e., it is between 0 and 9, the result is easy to compute: it is the string consisting of the single
character encoding that digit.
If the number has more than one digit, it is natural to perform the conversion digit-by-digit. The
key insight is that for any positive integer r, the least significant digit in the decimal representation
of r is r mod 10, and the remaining digits are x170. This approach computes the digits in reverse
order, e.g., if we begin wlth 423, we get 3 and are left with 42 to convert. Then we get 2, and are left
with 4 to convert. Finally, we get 4 and there are no digits to convert. The natural algorithm would
be to prepend digits to the partial result. However, adding a digit to the beginning of a string is
expensive, since all remaining digit have to be moved. A more time efficient approach is to add
each computed digit to the end, and then reverse the computed sequence.
If r is negative, we record that, negate x, and then add a '-'before reversing. If r is 0, our code
breaks out of the iteration without writing any digits, in which case we need to explicitly set a 0.
To convert from a string to an integer we recall the basic working of a positional number system.
A base-10 number dzddo encodes the number 102 x d2 + 101 x h + do. A brute-force algorithm then
is to begin with the rightmost digit, and iteratively add 10i x di to a cumulative sum. The efficient
way to compute 10'*1 is to use the existing value 10' and multiply that by 10.
A more elegant solution is to begin from the leftmost digit and with each succeeding digit,
multiply the partial result by 10 and add that digit. For example, to convert "374" to an integer, we
68
```
