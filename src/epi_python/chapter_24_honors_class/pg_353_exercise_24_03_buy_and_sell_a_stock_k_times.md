# Exercise 24.3: Buy and sell a stock k times

**Printed textbook page:** 353. **Reference transcription pages:** 353–353.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 353 (PDF page 367)

```text
Now we make a pass through A looking for the first index I such that A[] * i + 1.; this is the
smallest missing positive entry, which is 1 for our example.
def find-first_missing_positive (A) :
# Record which values are present by writing A[i] to jndex Atil - 1 if
# A[i] is betr*een 1 and 7en(A), inc-lusive. we save the value at index A[i]
# - 1 by swapping jt h'jth the entry at i. If etjJ is negative or greater
# than n, we just advance i.
for i in range(Len(A)):
while 1 <= A[i] <= len(A) and A[i] != AtA[i] - tl:
AtAtil - 11, Atil = A[i], AtAtil - 1l
# Second pass through A to search for the first 
jndex i such that A[i] 
!=
# i+1, indicating that i + 7 is absent. If a77 nunbers between 7 and
# 7en(A) are present, the snaTTest nissing positive is Len(A) + 1.
return next((i + 1 for i, a in enuDerate(A) if a != i + 1), len(A) + 1)
The time complexity is O(n), since we perform a constant amount of work per entry. Because we
reuse A, the space complexity is O(1).
24.3 Buy anp sELL A srocK k uurs $
This problem generalizes the buy and sell problem introduced on page 1
Write a Program to compute the maximum profit that can be made by buying and selling a share k
times over a given day range. Your program takes k and an array of daily stock prices as input.
Solution: Here is a straightforward algorithm. Iterate over 7 from 1 to k and iterate through A,
recording for each index I the best solution for Al},i] with / pairs. We store these solutions in an
auxiliary array of length n. The overall time complexity will be O(kn2); by reusing the arrays, we
can reduce the additional space complexity to O(n).
We can improve the time complexity to O(kn), and the additional space complexity to O(k) as
follows. Define ff to be the most money you can have if you must make i - 1 buy-sell transactions
prior to I and buy at i. Define S/ to be the maximum profit achievable with I buys and sells with the
ith sell taking place at l. Then the following mutual recurrence holds:
sl = Afil+maxBtu
Bj, = rnaxsi;l -a1q
The key to achieving an O(kn) time bound is the observation that computing B and S requires
computing rloX7.; Bil andrl€tX7a; Sl, 1. fhese two quantities can be computed in constant time for
each I and 7 with a conditional update. In code:
def buy-and-seI1-stock_k_times (prices , k) :
if not k:
return 0.0
elif 2 o k >= len(prices):
return sun(nar(0, b - a) for a, b in zip(prices[:-1], pricestl:l))
min-prices, max_profits = [ftoat('inf')] 
" k, [0] o k
for price in prices:
for i in reversed(list(range(k))) :
353
```
