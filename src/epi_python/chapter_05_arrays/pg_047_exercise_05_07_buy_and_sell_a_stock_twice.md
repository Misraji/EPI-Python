# Exercise 5.7: Buy and sell a stock twice

**Printed textbook page:** 47. **Reference transcription pages:** 47–47.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 47 (PDF page 61)

```text
Write a program that takes an array denoting the daily stock price, and retums the maximum profit
that could be made by buying and then selling one share of that stock. There is no need to buy if
no profit is possible.
Hint:ldentifying the minimum and maximum is not enough since the minimum may appear after the maximum
height. Focus on valid differences.
Solution: We developed several algorithms for this problem in the introduction. Specifically, on
Page2we showed how to compute the maximum profitby computing the difference of the current
entry with the minimum value seen so far as we iterate through the array.
For example, the array of minimum values seen so far for the given example is
<310,370,275,275,2@,260,260,230,230,230>. The maximum profit that can be made by selling
on each specific day is the difference of the current price and the minimum seen so far, i.e.,
<0,5,0,20,0,10,30,0,25,20). The maximum profit overall is 30, corresponding to buying 260 and
selling for 290.
def buy-and-se11-stock-once (prices) :
min-price-so-far , nax_profit = float ('inf') 
, 0.0
for price in prices:
max-profit-se1l-today - price - min-price-so_far
max_profit = nar(max_profit, max_profit_se11_today)
min-price_so-far = nin(min-price-so-far, 
price)
r€turn max-profit
The time complexity is O(n) and the space complexity is O(1), where n is the length of the array.
Variant: Write a program that takes an array of integers and finds the length of a longest subarray
all of whose entries are equal.
5.7 Bw arun sELL A srocK TwrcE
The max difference problem, introduced on Page 1, formalizes the maximum profit that can be
made by buying and then selling a single share over a given day range.
Write a program that computes the maximum profit that can be made by buying and selling a share
at most twice. The second buy must be made on another date after the first sale.
Hint: What do you need to know about the first I elements when processing the (l + 1)th element?
Solution: The brute-force algorithm which examines all possible combinations of buy-sell-buy-
sell days has complexity O(na). The complexity can be improved to O(nz) by applying the O(n)
algorithm to each pair of subarays formed by splittingA.
The inefficiency in the above approaches comes from not taking advantage of previous com-
putations. Suppose we record the best solution for Al0, j), f between 1, and n - 1, inclusive. Now
we can do a reverse iteration, computing the best solution for a single buy-and-sell for Afj,n - 11, j
between I andn-1,, inclusive. For each day, we combine this result with the result from the forward
iteration for the previous day-this yields the maximum profit if we buy and sell once before the
current day and once at or after the current day.
For example/ suppose the input array is <12,11.,1.3,9,12,8,14,1,3,15). Then the most profit that
can be made with a single buy and sell by Day I (inclusive) is | = (0,0,2,2,3,3,6,6,7). Working
47
```
