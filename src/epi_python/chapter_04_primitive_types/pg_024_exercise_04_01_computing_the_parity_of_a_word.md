# Exercise 4.1: Computing the parity of a word

**Printed textbook page:** 24. **Reference transcription pages:** 24–26.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 24 (PDF page 38)

```text
Be very comfortable with the bitwise operators, particularly XOR.
Understand how to use masks and create them in an machine independent way,
Know fast ways to clear the lowermost set bit (and by extension, set the lowermost 0, get its
index, etc.)
Understand signedness and its implications to shifting.
Consider using a cache to accelerate operations by using it to brute-force small inputs.
Be aware that commutativity and associativity can be used to perform operations in parallel
and reorder operations.
Table 4.1 : Top Tips for Primitive Types
o The key methods for numeric types are abs(-34.5), math. ceil(2. 17), math. floor(3. 14),
min(x, -4), max(3 .t4, y), 
pow(2 .7L, 3.14) (altemately, 2.71 ** 3.14), and
math. sqrt (22 5).
o Know how to interconvert integers and strings, e.g., str(421 , int('42'), floats and strings,
e.g., str(3. 14), float(' 3. 14').
r Unlike integers, floats are not infinite precision, and it's convenient to refer to infinity as
float('inf ') and float('-inf '). These values are comparable to integers, and can be used
to create psuedo max-int and pseudo min-int.
o When comparing floating point values consider using math.iscloseO-it is robust, e.g.,
when comparing very large values, and can handle both absolute and relative differences.
o The key methods in random are random.randrange(28), random.randint(8,1.6),
randon. randomO, random. shuffle (A), and random. choice(A).
4.7 Cot'lpuuNc rlrE pARITy oF A woRD
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. For
example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
single bit errors in data storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word.
How would you compute the parity of a very large number of 64-bit words?
Hint: lJse a lookup table, but don't use 264 entries!
Solution: The brute-force algorithm iteratively tests the value of each bit while tracking the number
of 1s seen so far. Since we only care if the number of 1s is even or odd, we can store the number
mod 2.
def parity(x):
result = 0
while x:
resulta=x&1
24
```

#### Printed page 25 (PDF page 39)

```text
x>>=l
return result
The time complexity isO(n), where n is the word size.
We will now describe several algorithms for parity computation that are superior to the brute-
force algorithm.
The first improvement is based on erasing the lowest set bit in a word in a single operation,
thereby improving performance in the best- and average-cases. Here is a great bit-fiddling trick
which you should commit to memory: r &(x * 1) equals x with its lowest set bit erased. (Here
&isthebitwise-ANDoperator.) 1 Forexample, if x= (00101100)2,thenx-1= (00101017)y,
so x &(x - 1) = (00101100)2&(00101011)2 = (00101000)2. This fact can be used to reduce the time
complexity. Let k be the number of bits set to 1 in a particular word. (For example, for 10001010,
k = 3.) Then time complexity of the algorithm below is O(k).
def parity(x)
result = 0
rhile x:
result ^= I
x &= x - 1 # Drops the -lowest set bit of x
return result
We now consider a qualitatively different approach. The problem statement refers to computing
the parity for a very large number of words. \Atrhen you have to perform a large number of parity
computations, and, more generally, any kind of bit fiddling computations, two keys to performance
are processing multiple bits at a time and caching results in an array-based lookup table.
First we demonstrate caching. Clearly, we cannot cache the parity of every 64-bit integer-we
would need 2e bits of storage, which is of the order of two exabytes. However, when computing
the parity of a collection of bits, it does not matter how we group those bits, i.e., the computation is
associative. Therefore, we can compute the parity of a 64-bit integer by grouping its bits into four
nonoverlapping 16 bit subwords, computing the parity of each subwords, and then computing the
parity of these four subresults. We choose 16 since 216 = 65536 is relatively small, which makes it
feasible to cache the parity of all 16-bit words using an array. Furthernore, since 16 evenly divides
64, the code is simpler than if we were, for example, to use 10 bit subwords.
We illustrate the approach with a lookup table for 2-bit words. The cache is (0,1,1,0)-these
are the parities of (00), (01), (10), (11), respectively. To compute the parity of (11001010) we would
compute the parities of (11), (00), (10), (10). By table lookup we see these are 0,0,1.,1., respectively,
so the final result is the parity of 0,0, 1, 1 which is 0.
To lookup the parity of the first two bits in (11101010), we right shift by 6, to get (00000011), and
use this as an index into the cache. To lookup the parity of the next two bits, i.e., (10), we right shift
by 4, to get (10) in the two least-significant bit places. The right shift does not remove the leading
(11)-it results in (00001110). We cannot index the cache with this, it leads to an out-of-bounds
access. To get the last two bits after the right shift by 4, we bitwise-AND (00001110) with (0000001 1)
(this is the "mask" used to extract the last 2 bits). The result is (00000010). Similar masking is
needed for the two other 2-bit lookups.
lAnother key bit-fiddling trick: r & -(r - 1) isolates the lowest bit that is 1 in x; here - is the bitwise complement
operator.
25
```

#### Printed page 26 (PDF page 40)

```text
def parity(x):
IIASK-SIZE = 16
BIT-I'IASK = 0xFFFF
return (PRECOI{PUTED-PARITY[x >> (3 * ]IASK-SIZE)l ^
PREC0IIPUTED-PARITY[(x >> (2 * ]IASK-SIZE)) & BIT-l'tASKl ^
PRECOHPUTED-PARITY [(x >> I{ASK-SIZE)
& BIT-IIASKl ^ PRECOMPUTED-PARITYIx & BIT-]IASKl)
The time complexity is a function of the size of the keys used to index the lookup table. Let L be
the width of the words for which we cache the results, and n the word size. Since there are nlL
terms, the time complexity is O(nlL), assuming word-level operations, such as shifting, take O(1)
time. (This does not include the time for initialization of the lookup table.)
We can improve on the O(n) worst-case time complexity of the previous algorithms by exploiting
some simple properties of parity. Specifically, the XOR of two bits is defined to be 0 if both bits are
0 or both bits are 1; otherwise it is 1. XOR has the property of being associative, i.e., it does not
matter how we group bits, as well as commutative, i.e., the order in which we perform the XORs
does not change the result. The XOR of a group of bits is its parity. We can exploit this fact to use
the CPU's word-level XOR instruction to process multiple bits at a tirne.
For example, the parity of (b6,boz,. .. ,b3,bz, b1, bs) equals the parity of the XOR of
(boyboz,. . . ,by) and (b31, bn,. .., b6). The XOR of these two 32-bit values can be computed with a
single shift and a shgle 32-bit XOR instruction. We repeat the same operation on32-,16-,8-, 4-,
2-, and 1-bit operands to get the final result. Note that the leading bits are not meaningful, and we
have to explicitly extract the result from the least-significant bit.
We illustrate the approach with an 8-bit word. The parity of (11010111) is the stune as the parity
of (1101) XORed with (0111), i.e., of (1010). This in tum is the same as the parity of (10) XORed with
(10), i.e., of (00). The final result is the XOR of (0) with (0), i.e.,0, Note that the first XOR yields
(11011010), and only the last 4 bits are relevant going forward. The second XOR yields (11101100),
and only the last 2 bits are relevant. The third XOR yields (10011010). The last bit is the result, and
to extract it we have to bitwise-AND with (00000001).
def parity(x):
x^=x>>32
x^=x>>16
x ^= x >> 8
x ^= x >> 4
x^=x>>2
x^=x>>1
return x & 0x1
The time complexity is O(logn), where n is the word size.
Note that we can combine caching with word-level operations, €.9.2 by doing a lookup in the
XOR-based approach once we get to 16 bits.
The actual runtimes depend on the input data, e.g., the refinement of the brute-force algorithm
is very fast on sparse inputs. However, for random inputs, the refinement of the brute-force is
roughly 20h faster than the brute-force algorithm. The table-based approach is four times faster
still, and using associativity reduces run time by another factor of two.
26
```
