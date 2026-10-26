# Exercise 16.10: Count the number of moves to climb stairs

**Printed textbook page:** 253. **Reference transcription pages:** 253–253.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 253 (PDF page 267)

```text
so as to minimize the first player's revenue. Therefore, R(a,b) satisfies the following equations:
mln
Clal +
Clbl + min
R(a + 2,b),
R(a+l,b-l)
R(a+1,b-7),
R(a,b - 2) ll
rta<b;
max
R(a,b) =
otherwise
In essence, the strategy is to minimize the maximum revenue the opponent can gain. The benefit of
this "min-max" recurrence for R(a,b), compared to our first formulation, is that it does not require
computing S(a + 1,b) and S(a,b - 1).
For the coins (10,25,5,1,10,5), the optimum revenue for the first player is 31. Some of subprob-
lems encountered include computing the optimum revenue for (10,25) (which is 25), (5,1) (which
is 5), and (5, 1, 10,5) (which is 15).
For the coins in Figure 16.11 on the facing page, the maximum revenue for the first player is
740q., i.e., whatever strategy the second player uses, the first player can guarantee a revenue of at
least 140c. In contrast, if both players always pick the more valuable of the two coins available to
them, the first player will get only 120C.
In the program below we solve for R using DP.
def maximum-revenue (coins) :
def compute-maximum_revenue-for-range(a, b)
if a > b:
# No coins left.
return 0
if maximum-revenue-for-rangeIa][b] == O:
max_revenue_a = coins[a] + nin(
compute-maxinum_revenue_for_range(a + 2, b),
compute-maximum_revenue_for_range(a + 1, b - 1))
max_revenue_b = coins[b] + nin(
compute-naximum-revenue-for_range(a + 1, b - l),
compute-maximum-revenue-for_range(a, b - 2))
maximum-revenue-for-range Ia] [b] = nar(rnax-revenue_a, max_revenue_b)
return maximum-revenue-for-range Ia] [b]
maximum-revenue-for-range = [[0] * Ien(coins) for _ in coinsl
return compute_maximum_revenue_for_range(0, len(coins) - 1)
There are O(n2) possible arguments for R(a, b), where n is the number of coins, and the time spent
to compute R from previously computed values is O(1). Hence, R can be computed in O(n2) time.
15.10 Couur rHE NUMBER oF MovES To cLrMB srArRS
You are climbing stairs. You can advance 1 to k steps at a time. Your destination is exactly n steps
up.
Write a program which takes as inputs n andk and retums the number of ways in which you can
get to your destination. For example, if n = 4 and k = 2, there are five ways in which to get to the
destination:
r four single stair advances,
0,
253
```
