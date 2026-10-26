# Exercise 4.2: Swap bits

**Printed textbook page:** 27. **Reference transcription pages:** 27–27.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 27 (PDF page 41)

```text
Varianh Write expressions that use bitwise operators, equality checks, and Boolean operators to do
the following in O(1) time.
o Right propagate the rightmost set bit in x, e.9., tums (01010000)2 to (01011111)2.
o Compute r mod a power of two, e.9., retums 13 for77 mod 64.
o Testif risapower of 2,i.e.,evaluatestotrue forx=1.,2,4,8,...,falseforallothervalues.
4.2 Sm.p nIrs
There are a number of ways in which bit manipulations can be accelerated. For example, as
described on Page 23, the expression r & (x - 1) clears the lowest set bit in x, and x & -(x - 1) extracts
thelowestsetbitof r. Hereareafewexamples: 16&(16-1) = 0,11&(11-1)= 10,20ftQ0-l) =16,
16&-(16 - 1) = 16, 11&-(11 - 1) = 1, and 208.-(20 - l) = 4.
MSB 
LSB
(a) The 8-bit integer 73 can be viewed as anay of bits,
with the LSB being at index 0.
MSB 
LSB
(b) The result of swapping the bits at indices 1 and 6, with
the LSB being at index 0. The conesponding integer is 11.
Figure 4.1 : Example of swapping a pair ot bits.
A 64-bit integer can be viewed as an array of 64bits, with the bit at index 0 corresponding to the
least significant bit (LSB), and the bit at index 63 corresponding to the most significant bit (MSB).
Implement code that takes as input a 64-bit integer and swaps the bits at indices i and j. Figure 4.1
illustrates bit swapping for an 8-bit integer.
Hinf; When is the swap necessary?
Solution: A brute-force approach would be to use bitmasks to extract the ith and ith bits, saving
them to local variables. Consequently, write the saved ith bit to index I and the saved lth bit to
index i, using a combination of bitmasks and bitwise operations.
The brute-force approach works generally, e.g., if we were swapping objects stored in an array.
Howeveq, since a bit can only take two values, we czrn do a little better. Specifically, we first test if
the bits to be swapped differ. If they do not, the swap does not change the integer. If the bits are
diffurent, swapping them is the same as flipping their individual values. For example in Figure 4.1,
since the bits at Index 1 and Lndex 6 diffe{, flipping each bit has the effect of a swap.
In the code below we use standard bit-fiddling idioms for testing and flipping bits. Overall, the
resulting code is slightly more succinct and efficient than the brute force approach.
def swap-bits(x, i, j):
# Extract the i-tfi 
and j-th bjts, and see jf they differ.
if (x >> i) & r != (x >> j) A r:
# i-th and j-th bits differ. 
We wi77 swap then by flipping their val.ues
# Select the bits to flip with bit_nask. Since x^I = 0 when x = I and 1
# when x = 0, we can perforn the flip 
X1R.
bit-mask - (1 << i) I (1 << j)
x r= bit_mask
return x
0
1
0
0
1
0
0
1
0
0
0
0
1
0
1
1
27
```
