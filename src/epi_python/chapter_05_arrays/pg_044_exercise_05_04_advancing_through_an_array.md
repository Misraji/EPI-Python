# Exercise 5.4: Advancing through an array

**Printed textbook page:** 44. **Reference transcription pages:** 44–44.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 44 (PDF page 58)

```text
Write a program that takes two arrays representing integers, and retums an integer represent-
ing their product. For example, since 193707721.x -761838257287 = -147573952589676412927, if
the inputs are (1,9,3,7,0,7,7,2, 1) and <-7,6,L,8,3,8,2,5,7,2,8,7>, your function should refum
(-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7>.
Hint: Use arrays to simulate the grade-school multiplication algorithm.
Solution: As in Solution 5.2 on the preceding page, the possibility of overflow precludes us from
converting to the integer type.
Instead we can use the grade-school algorithm for multiplication which consists of multiplying
the first number by each digit of the second, and then adding all the resulting terms.
From a space perspective, it is better to incrementally add the terms rather than compute all of
them individually and then add them up. The number of digits required for the product is at most
n + m for n and m digit operands, so we use an array of size n + m for lhe result.
For example, when multiplying 123 with 987,wewould forn T x123 = 861, then we would form
8x123 x10=9840,whichwewouldaddto861toget10701. Thenwewouldform9xl23xl00=
7L0700, which we would add to 10701 to get the final result 727407. (All numbers shown are
represented using arrays of digits.)
def multiply(numl, num2):
sisn = -1 if (num1[0] < 0) r (num2[0] < 0) else 1
numl [0] , num2 [0] = abs (num1 [0] ) , abs (nun2 [0] )
result = [0] o (Ien(num1) + len(num2))
for i in reversed(range(len(num1))) 
:
for j in reversed(range(Ien(num2))) 
:
result[i + j + 1] +- numl[i] * num2[j]
resultti + jl += result[i + j + LJ // lo
result[i+j+1]%=10
# Renove the Teading zeroes,
result = resultlnext((i for i, x in enunerate(xesult)
if x != 0), len(result)):l or [0]
return Isign * resultt0]l + result[1:]
There are m paftral products, each with at most n + 1 digits. We perform O(1) operations on each
digit in each partial product, so the time complexity is O(nm).
5.4 AnvaNcrNc rrrRoucH AN ARRAY
In a particular board garne, a player has to try to advance through a sequence of positions. Each
position has a nonnegative integer associated with it, representing the maximum you can advance
from that position in one move. You begin at the first position, and win by getting to the last
position. For example,let A = (3,3,1.,0,2,0,1) represent the board garr.e, i.e., the lth entry in A is
the maximum we can advance from L Then the game can be won by the following sequence of
advances through A: take 1 step from A[0] to A[1], then 3 steps from A[1] to A[4], then 2 steps from
A[ ]toA[6],whichisthelastPosition.NotethatA[0] =3>1,,4[1] =3)3,andA[4] =2>2,soall
moves are valid. If A instead was (3, 2,0,0,2,0,1), it would not possible to advance past position 3,
so the game cannot be won.
44
```
