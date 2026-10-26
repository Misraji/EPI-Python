# Exercise 11.7: Find the min and max simultaneously

**Printed textbook page:** 152. **Reference transcription pages:** 152–152.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 152 (PDF page 166)

```text
return True
elif Alrowl[col] < x:
row+=L 
#Elininate
else: 
#Afrow][coL]>x.
col-=L 
#ETininate
return False
this row,
thi s co-I urnn
Ineachiteration,weremovearoworacolumn/whichmeansweinspectatmost m+n- 1 elements,
yielding anO(m + n) time complexity.
11.7 FrNo rHr MrN AND MAx srMULTANEousLy
Given Errr array of comparable objects, you c.u:r find either the min or the max of the elements in the
array with n - 1 comparisons, where r is the length of the array.
Comparing elements may be expensive, e.9., a comparison may involve a number of nested
calls or the elements being compared may be long strings. Therefore, it is natural to ask if both the
min and the max canbe computed with less than the 2(n-l) comparisons required to compute the
min and the max independently.
Design an algorithm to find the min and max elements in an array. For example , if A : <3,2,5,1,,2,4>,
you should retum 1 for the min and 5 for the max.
Hint:Usethefactthata<bandb<cimpliesa<ctoreducethenumberofcomparesusedbythebrute-force
approach.
Solution: The brute-force approach is to compute the min and the max independently, i.e., with
2(n - 7) comparisons. We can reduce the number of comparisons by 1 by first computing the min
and then skipping the comparison with it when computing the max.
One way to think of this problem is that we are searching for the strongest and weakest players
in a group of players, assuming players are totally ordered. There is no point in looking at any
player who won a game when we want to find the weakest player. The better approach is to play
n/2 matches between disjoint pairs of players. The strongest player will come from the nl2 winners
and the weakest player will come from the nl2losers.
Following the above analogy, we partition the array into min candidates and max candidates
by comparing successive pairs-this will give us nlT candidates for min and nl2 candidates for
max at the cost of nl2 comparisons. It takes nlL- 1. comparisons to find the min from the min
candidates and nlZ - 1 comparisons to find the max from the max candidates, yielding a total of
3n12 - 2 comparisons.
Naively implemented, the above algorithm need O(n)storage. Howeveq, we can implement it
in streaming fashion, by maintaining candidate min and max as we process successive pairs. Note
that this entails three comparisons for each pair.
For the given example, we begin by comparing 3 and 2. Since 3 > 2, we set min to 2 and max to
3, Next we compare 5 and 1. Since 5 > 1, we compare 5 with the current max, namely 3, and update
max to 5. We compare 1 with the current min, namely 2, and update min to 1. Then we compare 2
and 4. Since 4 > 2,we compare 4 with the current max, namely 5. Since 4 < 5, we do not update
max. We compare 2 with the current min, namely 1 Since 2> L,we do not update min.
llinllax = collections.namedtuple('llinl,lax', ('smaIlest','largest'))
152
```
