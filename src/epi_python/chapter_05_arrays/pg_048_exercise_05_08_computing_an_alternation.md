# Exercise 5.8: Computing an alternation

**Printed textbook page:** 48. **Reference transcription pages:** 48–48.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 48 (PDF page 62)

```text
backwards, the most profit that can be made with a single buy and sell on or after Day i is
fr' = (7,7,7,7,7,7,2,2,0). To combine these two, we compute Mlil = f[, - 1] + Bfil, where F[-1]
is taken to be 0 (since the second buy must happen strictly after the first sell). This yields M =
<7,7,7,9,9,70,5,8,6), i.e., the maximum profit is 1"0.
def buy-and-sel1-stock-twice (prices) :
max-total-profit, min-price-so-far = 0.0, float('inf')
first-buy-sell-profits = [0] o len(prices)
# Forward phase. For each day, we record maxinum profit if we sel-l on that
# day.
for i, price in enuuerate(prices):
min-price-so-far = uin(min-price-so-far, price)
max-total-profit = nax(max_total_profit, price - min-price_so_far)
first-buy-se1l-profits Ii] = max-total-profit
# Backward phase. For each day, find the naxinun profit if we nake the
# second buy on that day.
nax-price-so-far = float(' -inf ')
for i, price in reversed(Iist(enutrerate(prices[1:], 
1))):
max-price-so-far = nar(max-price-so-far, price)
nax-totaI-profit 
= uax(
max-total-profit,
max_price-so_far - price + first-buy-seIl-profitsti 
- 1l)
return max-total-profit
The time complexity is O(n), and the additional space complexity is O(n), which is the space used
to store the best solutions for the subarrays.
Variant: Solve the same problem in O(n) time and O(1) space.
5.8 CoupurrNc AN ALTERNATToN
Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array
BhavingthepropertythatB[0] < B[1] >Bl2) < B[3] >8141< B[5] >....
Hint: Can you solve the problem by making local changes to A?
Solution: One straightforward solution is to sort A and interleave the bottom and top halves
of the sorted array. Altematively, we could sort A and then swap the elements at the pairs
(Al1,l,Al2l),(A131,A14D,.... Both these approaches have the same time complexity as sorting/
namely O(nlogn).
You will soon realize that it is not necessary to sort A to achieve the desired configuration-
you could simply rearrange the elements around the median, and then perform the interleaving.
Median finding can be performed in time O(r), as per Solution 11 .8 on Page 153, which is the overall
time complexity of this approach.
Finally, you may notice that the desired ordering is very local, and realize that it is not necessary
to find the median. Iterating through the array and swapping A[i] and AU + 1l when i is even and
Alil > Ali + 1l or I is odd and A[4 < Ali + 1] achieves the desired configuration. In code:
def rearrange (A)
48
```
