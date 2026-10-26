# Exercise 4.5: Compute x times y without arithmetical operators

**Printed textbook page:** 29. **Reference transcription pages:** 29–30.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 29 (PDF page 43)

```text
Hint: Start with the least significant bit.
Solution: Abrute-force approach mightbe to try all integers x-1.,x +1.,x -2,x+2,..., stopping
as soon as we encounter one with the same weight at x. This performs very poorly on some inputs.
One way to see this is to consider the case where x = 23 = 8. The only numbers with a weight of
1 are powers of 2. Thus, the algorithm will try the following sequence: 7,9,6,L0,5,11,4, stopping
at 4 (since its weight is the same as 8's weight). The algorithm tries 23-1 numbers smaller than 8,
namely, 7,6,5,4, and 23-1 - 1 numbers greater than 8, namely, 9,10,11. This example generalizes.
Suppose x = 230. The power of 2 nearest to 230 is 22e. Therefore this computation will evaluate the
weight of all integers between 230 and 22e andbetween 230 and 230 a 22e - 1, i.e., over one billion
integers.
Heuristically, it is natural to focus on the LSB of the input, specifically, to swap the LSB with
rightmost bit that differs from it. This yields the correct result for some inputs, e.g., for (10)2 it
returns (01)2, which is the closest possible, Howevel, more experimentation shows this heuristic
does not work generally. For example, for (111)2 (7 in decimal) it retums (1i10)2 which is 14 in
decimal; however, (1011)2 (11 in decimal) has the same weight, and is closer to (111)2.
A little math leads to the correct approach. Suppose we flip the bit at index k1 and flip the bit
at index k2, kl > k2. Then the absolute value of the difference between the original integer and the
new one is 2k1 - 2k2. To minimize this, we should make k1 as small as possible andklas close to kL.
Since we must preserve the weight, the bit at index k1 has to be different from the bit in k2,
otherwise the flips lead to an integer with different weight. This means the smallest k1 is the
rightmost bit that's different from the LSB, and k2 must be the very next bit. In summary, the correct
approach is to swap the two rightmost consecutive bits that differ.
de:f closest-int-sane-bit-count (x) :
NUll-UNSIGNED-BITS = 64
for i in range(NUU-UNSIGNED-BITS - 1):
if (x >> i) & 1 != (x >> (i + 1)) & 1:
x ^= (1 << i) I (1 << (i + 1)) # Swaps bit-i 
and bit-(i 
+ 1)
return x
# Raise error if all bits of x are 0 or 1
raise ValueError('A1l bits are 0 or 1')
The time complexity is O(n), where n is the integer width.
Variank Solve the same problem in O(1) time and space.
4.5 Colrrruru x x y wrrHour ARITHMETTcAL opERAToRs
Sometimes the processors used in ultra low-power devices such as hearing aids do not have
dedicated hardware for performing multiplication. A program that needs to perform multiplication
must do so explicitly using lower-level primitives.
Write a program that multiplies two nonnegative integers. The only operators you are allowed to
use are
. assi8nment,
e thebitwise operators ,r, rr, l, &, -, ^ and
29
```

#### Printed page 30 (PDF page 44)

```text
. equality checks and Boolean combinations thereof.
You may use loops and functions that you write yourself. These constraints i*ply, for example,
that you cannot use increment or decrement, or test if r < y.
Hint: Add using bitwise operations; multiply using shift-and-add.
Solution: A brute-force approach would be to perform repeated addition, i.e., initialize the result
to 0 and then add x to it y times. For example, to form 5 x 3, we would start with 0 and repeatedly
add 5, i.e., form 0 + 5,5 + 5,10 + 5. The time complexity is very high-as much asO(2"), where n is
the number of bits in the input, and it still leaves open the problem of adding numbers without the
presence of an add instruction.
The algorithm taught in grade-school for decimal multiplication does not use repeated
addition-it uses shift and add to achieve a much better time complexity. We can do the same
with binary numbers-to multiply x and y we initialize the result to 0 and iterate through the bits
of x, adding 2ky to the result if the kth bit of r is 1.
The value 2ky cmrbe computed by left-shiftin g yby k. Since we cannot use add directly, we must
implement it. We apply the grade-school algorithm for addition to the binary case, i.e., compute
the sum bit-by-bit, and "rippling" the carry along.
As an example, we show how to multiply 13 = (1101)2 and 9 = (1001)z using the algorithm
described above. In the first iteration, since the LSB of 13 is 1, we set the result to (1001)2. The
second bit of (1101)2 is 0, so we move on to the third bit. This bit is 1, so we shift (1001)2 to the
left by 2 to obtain (100100)2, which we add to (1001)2 to get (101101)2. The fourth and final bit of
(1101)2 is 1, so we shift (1001)2 to the left by 3 to obtain (1001000)2, which we add to (101101)2 to get
(1110101)2 ='1.\7.
Each addition is itself performed bit-by-bit. For example, when adding (101101)2 and (1001000)2,
the LSB of the result is 1 (since exactly one of the two LSBs of the operands is 1). The next bit is 0
(since both the next bits of the operands are 0). The next bit is 1 (since exactly one of the next bits of
the operands is 1). The next bit is 0 (since both the next bits of the operands are 1). We also "carry" a
1 to the next position. The next bit is 1 (since the carry-in is L and both the next bits of the operands
are 0). The remaining bits are assigned similarly.
def multiply (x , y) :
def add(a, b):
running-sum, carryin, k, temp-a, temp-b = 0,0, 1, a, b
while temp-a or temp-b:
ak, bk = a & k, b & k
carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
running-sum l= ak ^ bk ^ carryin
carryin, k, temp-a, temp-b = (carryout << 1, k << 1, temp-a >> 1,
temp-b >> 1)
return running-sum I carryin
running-sum = 0
while x: # Examines each bit of x.
if x & 1:
running-sum = add(running-sum, y)
x, y = x >> 1, y << 1
return running-sum
30
```
