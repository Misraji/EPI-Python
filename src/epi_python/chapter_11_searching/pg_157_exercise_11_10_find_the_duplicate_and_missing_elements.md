# Exercise 11.10: Find the duplicate and missing elements

**Printed textbook page:** 157. **Reference transcription pages:** 157–158.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 157 (PDF page 171)

```text
11.10 FrNo rsE DUpLTcATE AND MrssrNG ELEMENTs
If an array contains rz - 1 integers, each between 0 and n - 1, inclusive, and all numbers in the array
are distinct, then it must be the case that exactly one number between 0 and n - 1 is absent.
We can determine the missing number n O(n) time and O(1) space by computing the sum of the
elements in the array. Since the sum of all the numbers from 0 to n - 7, inclusive, i" W, we can
subtract the sum of the numbers in the array from 9 
,"get the missing number.
Forexample,ifthearrayis<5,3,0,1,2),thenn=6.Wesubtract(5+3+0+1+2) =11 from
9 = t5, and the result,4, is the missing number.
Similarly, if the array contains n + 1 integers, each between 0 and n - 1, inclusive, with exactly
one element appearing twice, the duplicated integer will be equal to the sum of the elements of the
. 
(n-7),n
array mmUS :--.
Altematively, for the first problem, we can compute the missing number by computing the XOR
of all the integers from 0 to n - 1., inclusive, and XORing that with the XOR of all the elements in the
array. Every element in the array, except for the missing element, cancels out with an integer from
the first set. Therefore, the resulting XOR equals the missing element. The same approach works
for the problem of finding the duplicated element. For example, the array <5,3,0,1,2) represented
in binary is ((101)2, (0L1)2, (000)2, (001)2, (010)2). The XOR of these entries is (101)2. The XOR of all
numbers from 0 to 5, inclusive, is (001)2. The XOR of (101)z and (00L)z is (100)2 = 4, which is the
missing number.
We now tum to a related, though harder, problem.
You are given an array of z integers, each between 0 and n - 1., inclusive. Exactly one element
aPpears twice, implying that exactly one number between 0 and n - 1 is missing from the array.
How would you compute the duplicate and missing numbers?
Hlrfr Consider performing multiple passes through the array.
Solution: A brute-force approach is to use a hash table to store the entries in the array. The number
added twice is the duplicate. After having built the hash table, we can test for the missing element
by iterating through the numbers from 0 to n - L, inclusive, stopping when a number is not present
in the hash table. The time complexity and space complexity are O(n). We can improve the space
complexity to O(1) by sorting the array, subsequent to which finding duplicate and missing values
is trivial. Howeveq, the time complexity increases to O(nlogn).
We can improve on the space complexity by focusing on a collective property of the numbers in
the array, rather than the individual numbers. For example, let f be the element appearing twice,
and m be the missing number. The sum of the numbers from O to n - 1., inclusive, i" W, so the
sum of the elements in the array is exactly * 
* t - m. Thisgives us an equation in f and m,but
we need one more independent equation to solve for them.
We could use €ul equation for the product of the elements in the afiay, ot for the sum of the
squares of the elements in the array, This is not a good idea in practice because it results in very
large integers.
The introduction to this problem showed how to find a missing number from an arcay of n - 2
distinct numbers between 0 and n - 1 using XOR. Applying the same idea to the current problem,
i.e., computing the XOR of all the numbers from 0 to n - 7, inclusive, and the entries in the array,
yields rz @ f. This does not seem very helpful at first glance, since we wantm and f. However, since
1,57
```

#### Printed page 158 (PDF page 172)

```text
m I t, there must be some bit in m @ f that is set to 1, i.e., m and f differ in that bit. For example, the
XOR of (01101)2 and (11100)2 is (10001)2. The 1s in the XOR are exactly the bits where (01101)2 and
(11100)z differ.
This fact allows us to focus on a subset of numbers from 0 to n - L where we can guarantee
exactly one of m and f is present. Suppose we know m and f differ in the kth bit. We compute the
XOR of the numbers from 0 to n - 7 in which the kth bit is 1, and the entries in the array in which the
kth bit is 1. Let this XOR be h-by the logic described in the problem statement, h must be one of m
or f . We can make another pass through A to determine if ft is the duplicate or the missing element.
For example, for the array (5,3,0,3,1,2), the duplicate entry f is 3 and the missing entry m is
4. Represented in binary the array is ((101)2, (011)2, (000)2, (011)2, (001)2, (010)2). The XOR of these
entries is (110)2. The XOR of the numbers from 0 to 5, inclusive, is (001)2. The XOR of (110)2 and
(001)2 is (111)2. This tells we can focus our attention on entries where the least significant bit is
1. We compute the XOR of all numbers between 0 and 5 in which this bit is 1, i.e., (001)2, (011)2,
and (101)2, and all entries in the array in which this bit is 1, i.e., (101)2, Q11)2,(011)2, and (001)2.
The XOR of these seven values is (01L)2. This implies that (011)z = 3 is either the missing or the
duplicate entry. Another pass through the array shows that it is the duplicate entry. We can then
find the missing entry by forming the XOR of (011)2 with all entries in the array, and XORing that
result with the XOR of all numbers from 0 to 5, which yields (100)2, i.e., 4.
Dupl i cateAndlli s sing = collections . namedtuple (' Dupl i cateAndlli s sing',
('duplicate','missing'))
def find-duplicate-missing (A) :
# Conpute the XOR of a71 nurnbers fron 0 to lAl - 1 and a-11 entries in A
miss-X0R-dup = functools.reduce(lanbda v, i: v ^ i[0] ^ i[1],
enunerate(A), 0)
# We need to find a bit that 's set to 1 in niss-XOR-dup. Such a bit aust
# exist if there is a single rnissing number and a single duplicated number
# in A.
# The bit-fiddling assignment below sets a17 of bjts jn differ-bit
# to 0 ercept for the least significant bit in miss-.f,oR-dup that's I.
differ-bit, niss-or-dup = miss-XoR-dup & (-(miss-XoR-dup - 1)), 0
for i , a in enumerate (A) :
# Focus on entries and nurnbers in which the differ-bit-th bit is L
if i & differ-bit:
miss-or-duP a= i
if a & differ-bit:
miss-or-duP ^= 3
# niss-or-dup is either the njssing vaTue or the duplicated entry.
if miss-or-dup in A:
# niss-or-dup is the duplicate.
return DuplicateAndl{issing (mi ss-or-dup, mi ss-or-dup ^ mi ss-XoR-dup)
# niss-or-dup is the nissing value.
r€turn Dupli.cateAndl{issing (mi ss-or-dup ^ miss-XoR-dup, miss-or-dup)
The time complexity isO(n) and the space complexity is O(i)
158
```
