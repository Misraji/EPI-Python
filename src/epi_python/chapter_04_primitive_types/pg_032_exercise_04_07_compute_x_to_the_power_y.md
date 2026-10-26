# Exercise 4.7: Compute x to the power y

**Printed textbook page:** 32. **Reference transcription pages:** 32–32.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 32 (PDF page 46)

```text
4.7 Coupurn.x/
Write a program that takes a double x and an integer y and retums x/. You can ignore overflow and
underflow.
Hint: Exploll mathematical properties of exponentiation.
Solution: First, assume y is nonnegative. The brute-force algorithm is to form 12 = r X x, then
f = x2 x r, and so on. This approach takes y - 1 multiplications, which is O(2"), where n is number
of bits needed to represent y.
The key to efficiency is to try and get more work done with each multiplication, thereby using
fewer multiplications to accomplish the same result. For example, to compute 1.121, instead of
starting with 1.1 and multiplying by 1.1 20 times, we could multiply 1.1 by 1..').2 = "1..21.10 times for
a total of 11 multiplications (one to compute 1.12, and 10 additional multiplications by 1.21), We
can do still better by computing7.13,1.1a, etc.
When y is a power of 2, the approach that uses fewest multiplications is iterated squaring,
i.e., formhg x,x2,1x212 = xa,(#)z = x8,.... To develop an algorithm that works for generaly,
it is instructive to look at the binary representation of y, as well as properties of exponentiation,
specifically Yvo+lt = xYo ' xYl.
We begin with some small concrete instances, first assumin g that y is nonnegative. For example,
a(1010):-a(10i)z+(101)z-/101)zyr(101)z.Similarly,a(101)z-y(100)z+(1)z-r(100)2r*-y$O)zXr(10)rXr.
Generalizing, if the least significant bit of y is 0, the result is @vlz1z' otherwise, it is r x @vlzr'.
This gives us a recursive algorithm for computing rv when y is nonnegative.
The only change when y is negative is replacing xby l.lx and y by -y. ln the implementation
below we replace the recursion with a while loop to avoid the overhead of function calls.
def power (x , y) :
result, power = 1.0, Y
ify<0:
power,x=-power,1.0/x
while power:
if power & 1:
result o= x
x r power = x * x, power >> 1
return result
The number of multiplications is at most twice the index of y's MSB, implying an O(rz) time
complexity.
4.8 RsvEnsr DrGIrs
Write a program which takes an integer and returns the integer corresponding to the digits of the
input written in reverse order. For example, the reverse of 42is 24, and the reverse of -314 is -413.
Hint: How would you solve the same problem if the input is presented as a string?
Solution: The brute-force approach is to convert the input to a string, and then compute the reverse
from the string by traversing it from back to front. For example, (1100)2 is the decimal number 12,
and the answer for (1100)2 can be computed by traversing the string t'72" kr reverse order.
32
```
