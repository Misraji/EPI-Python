# Exercise 24.2: Find the first missing positive entry

**Printed textbook page:** 352. **Reference transcription pages:** 352–352.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 352 (PDF page 366)

```text
larger and return the GCD of the resulting pair. Multiplication by 2 is trivially implemented with a
single left shift. Division by 2 is done with a single right shift.
def gcd (x , y) :
if x > y:
return gcd(y, x)
elif x == 0:
return y
elif not x & 1 and not y & 1: # x and y are even
return gcd(x >> 1, y >> 1) << 1
elif not x & I and y & 1: # x is even, y js odd.
return gcd(x >> 1, y)
elif x & I and not y & 1: # x is odd, y is even.
return gcd(x, y >> 1)
return gcd(x, y - x) # Both x and y are odd'
Note that the last step leads to a recursive call with one even and one odd number. Consequently, in
every two calls, we reduce the combined bit length of the two numbers by at least one, meaning that
the time complexity is proportional to the sum of the number of bits in x and y,i.e.,O(logx+logy)).
24.2 Frrrro rHs FrRST MIssINc posITIvE rurnv $
Let A be an aray of length rz. Design an algorithm to find the smallest positive integer which is not
presentinA. Youdonotneedtopreservethecontentsof A. ForexamPle,1f /= \3,5,4,-1,5,1,-1>,
the smallest positive integer not present in A is 2.
Hint: First, find an upper bound for x.
Solution: A brute-force approach is to sort A and iterate through it looking for the first gap in the
entries after we see an entry equal to 0. The time complexity is that of sorting, i.e., O(nlogn).
Since all we want is the smallest positive number in A, we explore other algorithms that do not
rely on sorting. We could store the entries in A in a hash table S (Chapter 12), and then iterate
through the positive integers 7,2,3,.. . looking for the first one that is not in S. The time complexity
is O(n) to create S, and then O(n) to perform the lookups, since we must find a missing entry by the
time we get to fl + 1 as there are only n entries. Therefore the time complexity rs O(n). The space
complexity is O(n), e.g., if the entries from A are all distinct positive integers.
The problem statement gives us a hint which we can use to reduce the space complexity. Instead
of using an extemal hash table to store the set of positive integers, we can use A itself. Specifically,
if A contains k between 1. au,;rd n, we set Alk - l|to k. (We use k - 1 because we need to use all n
entries, including the entry at index 0, which will be used to record the presence of L.) Note that
we need to save the presence of the existing entry in A[k - 1] if it is between 1 and n. Because A
contains n entries, the smallest positive number that is missing in A cannot be greater than n + 1.
For example,let A - <3,4,0,2), n = 4. we begin by recording the presence of 3 by writing it in
Al3 - 1); we save the current entry at index 2 by writing it to A[0]. Now A = (0,4,3,2]. Since 0 is
outside the range of interest, we advance to A[1], i.e., 4, which is within the range of interest. We
write 4 in A[4 - 1], and save the value at that location to index 1, and A becomes (0,2,3,4). The
value at A[1] already indicates thata2is present, so we advance. The same holds for Al2l and A[3].
352
```
