# Exercise 24.4: Compute the maximum product of all entries but one

**Printed textbook page:** 354. **Reference transcription pages:** 354–355.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 354 (PDF page 368)

```text
max-profitsIi] = Ear(max-profitslil, price - min-pricesIi])
min-prices Ii] = nin(min-prices Ii] ,
price - (0 if i == 0 else nax-profitsti - 1l))
return max-profits [- 1]
Varianh Write a program that determines the maximum profit that can be obtained when you can
buy and sell a single share an unlimited number of times, subject to the constraint that a buy must
occur more than one day after the previous sell.
24.4 Colrpurs rHE MAXIMUM rRoDUCT oF ALL ENTRIES nut oNr $
Suppose you are given an arcay A of integers, and are asked to find the largest product that can be
made by multiplying all but one of the entries in A. (You cannot use an entry more than once.) For
example,ifA=(3,2,5,4>,theresultis3x5x4=60,ifA-<3,2,-1,4),theresultis3x2x4=24,
and if A - <3,2, -1,, 4, -1,, 6>, the result is 3 x -1 x 4 x -L x 6 = 72.
One approach is to form the product P of all the elements, and then find the maxirnum of PlAlil
over all1. This takes n - 1 multiplications (to form P) and n divisions (to compute each P/A[r]).
Suppose because of finite precision considerations we cannot use a division-based approach; we
can only use multiplications. The brute-force solution entails computing all n products of n - L
elements; each such product takes n - 2 multiplications, i.e., O(nz) time complexity.
Given an array A of length n whose entries are integers, compute the largest product that can be
made using n - 1 entries in z{. You carurot use an entry more than once. Array entries may be
positive, negative, or 0. Your algorithm cannot use the division operator, explicitly or implicitly.
Hinf; Consider the products of the first I - 1 and the last n - I elements. Altematively, count the number of
negative entries and zero entries.
Solution: The brute-force approach to compute P lAlilisto multiplying the entries appearingbefore
I with those that appear after L This leads to n(n - 2) multiplications, since for each term P/A[i] we
need n - 2 multiplications.
Note that there is substantial overlap in computation when computing PlAli) arrdPlAli + 11. ln
particular, the product of the entries appearing before I + 1 is A[l] times the product of the entries
appearing before l. We can compute all products of entries before I with n - 1 multiplications, and
all products of entries after i with n - 1 multiplications, and store these values in an array of prefix
products, and an array of suffix products. The desired result then is the maximum prefix-suffix
product. A slightly more space efficient approach is to build the suffix product array and then
iterate forward through the array, using a single variable to compute the prefix products. This
prefix product is multiplied with the corresponding suffix product and the maximum prefix-suffix
product is updated if required.
def find-biggest-n-minus-one-product (A) :
# BuiTds suffix products.
suffix-products = list(
reversed(Iist (itertools. accumulate (reversed(A), operator. mu1))) )
# Finds the biggest product of (n - 1) nunbers
prefix-product, max-product = 1, float('-inf')
354
```

#### Printed page 355 (PDF page 369)

```text
:for i in range(1en(A)):
suffix-product = suffix_products[i + 1] if i + 1 < ten(A) else 1
max-product = nar(max_product, prefix_product * suffix_product)
prefix-product *= AIi]
return max-product
The time comPlexity is O(n); the space complexity is O(n), since the solution uses a single array of
length n.
We now solve this problem n O(n) time and O(1) additional storage. The insight comes from
the fact that if there are no negative entries, the maximum product comes from using all but the
smallest element. (Note that this result is correct if the number of 0 entries is zero, one/ or more.)
If the number of negative entries is odd, regardless of how many 0 entries and positive entries,
the maximum product uses all entries except for the negative entry with the smallest absolute value,
i.e., the least negative entry.
Going furthet, if the number of negative entries is even, the maximum product again uses all
but the smallest nonnegative element, assuming the number of nonnegative entries is greater than
zero. (This is correct, even in the presence of 0 entries.)
If the number of negative entries is even, and there are no nonnegative entries, the result must
be negative. Since we want the largest product, we leave out the entry whose magnitude is largest,
i.e., the greatest negative entry.
This analysis yields a two-stage algorithm. First, determine the applicable scenario, e.g., are
there an even number of negative entries? Consequently, perform the actual multiplication to get
the result.
def find-biggest-n-minus-one_product (A) :
number-of-negatives = 0
least-nonnegative_idx = least_negative_idx = greatest_negative_idx = None
# Identify the Ieast negative, greatest negative, and Ieast nonnegative
# entries.
for i, a in enunerate(A):
ifa<0:
number-of-negatives += 1
if least-negative_idx is None or AIleast_negative_idx] < a:
least-negative-idx = i
if greatest_negative_idx is None or a < AIgreatest_negative_idx]:
greatest-negative_idx = i
else: #a>=0,
if least-nonnegative_idx is None or a < AIleast_nonnegative_idx]:
least-nonnegative-idx = i
idx-to-skip - (least_negative_idx
if number-of-negatives % 2 else Ieast_nonnegative_idx if
least_nonnegative_idx is not None else greatest_negative_idx)
return functool s . reduce (
Ianbda product, a: product * a,
# Use a generator rather than list comprefiension to
# avoid extra space.
(a for i, a in enunerate(A) if i t= idx_to_skip),
r)
355
```
