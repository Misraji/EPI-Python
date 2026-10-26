# Exercise 4.4: Find a closest integer with the same weight

**Printed textbook page:** 28. **Reference transcription pages:** 28–28.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 28 (PDF page 42)

```text
The time complexity is O(1), independent of the word size.
4.3 Rrvrxsn utrs
Write a program that takes a 64-bit unsigned integer and retums the 64-bit unsigned integer con-
sisting of the bits of the input in reverse order. For example, if the input is (1110000000000001), the
output should be (1000000000000111).
Hint:Use a lookup table.
Solution: If we need to perform this operation just once, there is a simple brute-force algorithm:
iterate through the 32 least significant bits of the input, and swap each with the corresponding most
significant bit, using, for example, the approach in Solution 4.2 on the preceding page.
To implement reverse when the operation is tobe performed repeatedly, we look more carefully
at the structure of the input, with an eye towards using a cache. Let the input consist of the four L6-
bit integers Ut,Az,At,/0, with y3 holding the most significant bits. Then the 16 least significant bits
in the reverse come from /a. Tobe precise, thesebits appear in the reverse order in which they do in
As. For example, if y3 is (1110000000000001), then the 16 LSBs of the result are (1000000000000111).
Similar to computing parity (Problem 4.1 on Page 24), a very fast way to reverse bits for L6-bit
integer when we are performing many reverses is to build an array-based lookup-table A such that
for every 16-bit integer y, Alyi holds the bit-reversal of y. We can then form the reverse of x with
the reverse of ys in the most significant bit positions, followed by the reverse of y1, followed by the
reverse of yz, followed by the reverse of ys.
We illustrate the approach with 8-bit integers and 2-bit lookup table keys. The table is rev =
((00),(10),(01),(11)). If the input is (10010011), its reverse is rev(11),rev(00),rev(01),rev(10), i.e.,
(11001001).
def reverse-bits (x) :
HASK-SIZE = 16
BIT-}IASK = 0xFFFF
returN (PRECOI{PUTED-REVERSEIx & BIT-}IASK] << (3 * }IASK-SIZE)
I PRECOUPUTED-REVERSE[(X >> IIASK-SIZE) & BIT-}IASK] <<
(2 * IIASK-SIZE) |
PRECO}IPUTED-REVERSE [(X >> (2 * }IASK-SIZE)) & BIT-}IASK] << I'IASK-SIZE
I PRECoIPUTED-REVERSE[(x >> (3 * ]IASK-SIZE)) & BIT-uASKl)
The time complexity is identical to that for Solution 4.1 on Page 24, i.e., O(nlL), for n-bit integers
and L-bit cache keys.
4.4 FrNp e cLosEST TNTEGER wrrH THE sAME wErcHT
Define the weight of a nonnegative integer r to be the number of bits that are set to 1 in its binary
representation. For example, since 92 in base-2 equals (1011100)2, the weight of 92is 4.
Write a program which takes as input a nonnegative integer x and retums a number y which is not
equal to r, but has the same weight as x and their difference,ly - rl, is as small as possible. You can
assume.r is not 0, or all 1s. For example, if x = 6, you should return 5. You can assume the integer
fits in 64 bits.
28
```
