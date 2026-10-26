# Exercise 6.2: Base conversion

**Printed textbook page:** 69. **Reference transcription pages:** 69–69.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 69 (PDF page 83)

```text
initialthepartialresultrto0. Inthefirstiteration,r=3,intheseconditerationr=3x10+1=31,
and in the third iteration r = 3'L x 10 + 4 = 314, which is the final result.
Negative numbers are handled by recording the sign and negating the result.
def int-to-string (x) :
is-negative = False
ifx<0:
x, is-negative = -x, True
s = tl
Yhile True:
s.append(chr(ord('0') + x X 10))
x //= L0
ifx==0:
break
# Adds the negative sign back if is_negative
return ('-'if 
is_negative else ") + ".join(reversed(s))
def string-to-int (s) :
return functools. reduce(
lanbda running_sum, c: running_sum * 10 + string. digits. index (c) ,
s[s[0] 
:1, 0) " (-1 if s[0] == '-' else 1)
6.2 Besr coNvrnsroN
In the decimal number system, the position of a digit is used to signify the power of 10 that digit
istobemultipliedwith. Forexample, "Sl4" denotesthenumber3xl00+1x10+4x1. The
base b number system generalizes the decimal number system: the string "Ak1gk_z . . . a1.a0", where
0 < ai < b, denotes inbase-b the integer asxb0 -t fixbl + a2Xb2 +...+ a1-1 x*-1 .
Write a program that performs base conversion. The input is a string, an integer b1, and another
integer b2. The string represents an integer in base br. The output should be the string representing
the integer in base 02. Assume 2 < bt,b2 < 16. Use " N' to represent L0, "B" for 1.L,.. ., and "F" fot
15. (For example, if the string is "61.5", h is 7 and bz is 13, then the result should be "1A7", since
6x72 +1x7 + 5 = 1x 132 +70xL3+7.)
Hint: rNhatbase can you easily convert to and from?
Solution: A brute-force approach might be to convert the input to a unary representation, and then
group the Ls as multiples of b2, bl, b), etc. For example, (102\ = (11111111111)1. To convert to
base 4, there are two groups of 4 and with three 1s remaining, so the result is (23)a. This approach
is hard to implement, and has terrible time and space complexity.
The insight to a good algorithm is the fact that all languages have an integer type, which
suPPorts arithmetical operations like multiply, add, divide, modulus, etc. These operations make
the conversion much easier. Specifically, we can convert a string in base b1 to integer type using
a sequence of multiply and adds. Then we convert that integer type to a string in base b2 using
a sequence of modulus and division operations. For example, for the string is "615",bt = 7 and
bz = 13, then the integer value, expressed in decimal, is 305. The least significant digit of the result
is 305 mod 13 = 7, and we continue with 306i 13 = 23. The next digit is 23 mod 13 = 10, which we
69
```
