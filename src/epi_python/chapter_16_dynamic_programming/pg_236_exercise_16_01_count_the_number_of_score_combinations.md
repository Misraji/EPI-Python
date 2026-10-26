# Exercise 16.1: Count the number of score combinations

**Printed textbook page:** 236. **Reference transcription pages:** 236–238.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 236 (PDF page 250)

```text
sum for A is the maximum of I + r, the answer for L, and the answer for R. The time complexity
analysis is similar to that for quicksort, and the time complexity is O(nlogn). Because of off-by-one
errors, it takes some time to get the program just right.
Now we will solve this problem by using DP. A natural thought is to assume we have the
solution for the subarray Al},n - 21. However, even if we knew the largest sum subarray for
subarray AIO,n - 2], it does not help us solve the problem for Al},n - 1]. Instead we need to know
the subarray amongst all subarrays Al},i\, i < n - 1, with the smallest subarray sum. The desired
value is S[n - 1] minus this subarray's sum. We compute this value by iterating through the array.
For each index f, the maximum subarray sum ending at i is equal to S[] - rrdnrsr S[k]. During the
iteration, we track the minimum S[k] we have seen so far and compute the maximum subarray
sum for each index. The time spent per index is constant, leading to an O(n) time and O(1) space
solution. It is legal for all array entries to be negative, or the array to be empty. The algorithm
handles these input cases correctly.
def find-maximum-subarray (A) :
min-sum=max-sum=0
for running-sum in itertools. accumulate (A) :
min-sum = nin(min-sum, running-sum)
max-sum = nar(max-sum, running-sum - min-sum)
return max-sum
Dyn amic pro gr amming b o o t c amp
The programs presented in the introduction for computing the Fibonacci numbers and the maximum
subarray sum are good illustrations of DP.
1,6,1, CouNr rrrE NUMBER oF scoRE coMBrNATroNs
In an American football Bame, a play can lead to 2 points (safety), 3 points (field goal), or 7 points
(touchdown, assuming the extra point). Many different combinations of 2,3, and 7 point plays can
make up a final score. For example, four combinations of plays yield a score of 12:
o 6safeties (2x6=12),
o 3 safeties and 2 field goals (2 x 3 + 3 x2 = 72),
o 1 safety,l field goal and l touchdown (2 x 1+ 3 x 1 +7 x1= 12), and
o 4fieldgoals(3x4=12).
Write a program that takes a final score and scores for individual plays, and retums the number of
combinations of plays that result in the final score.
Hlrf: Count the number of combinations in which there are 0 zus plays, then 1 ars plays, etc.
Solution: We can gain some intuition by considering small scores. For example, a 9 point score can
be achieved in the following ways:
o scoring 7 points, followed by a2 point play,
o scoring 6 points, followed by a 3 point play, and
o scoring 2 points, followed by a7 point play.
Generalizing, an s point score can be achieved by an s - 2 point score, followed by a 2 point play, an
s-3pointscore,followedbya3pohtplay,orans-Tpointscore,followedbyaTpointplay.This
gives us a mechanism for recursively enumerating all possible scoring sequences which lead to a
given score. Note that different sequences may lead to the same score combination, e.9., a 2 point
236
```

#### Printed page 237 (PDF page 251)

```text
Consider usmS
you
to make choices to arrive at
DP is applicable when you can construct a solution to the given instance from solutions to
subinstances of smaller problems of the same kind.
In addition to optimization problems, DP is also applicable to counting and decision prob-
lems-any problem where you can express a solution recursively in terms of the same compu-
tation on smaller instances.
Although conceptually DP involves recursion, often for efficiency the cache is built "bottom-
ttp", i.e., iteratively. .
When DP is implemented recursively the cache is typically a dynamic data structure such
as a hash table or a BST; when it is implemented iteratively the cache is usually a one- or
multi-dimensional array.
To save space/ cache space may be recycled once it is known that a set of entries will not be
looked up again.
Sometimes, recursion may out-perform a bottom-up DP solution, e.g., when the solution is
found early or subproblems can be pruned through bounding.
A common mistake in solving DP problems is trying to think of the recursive case by splitting the
Proble-m into two equal halves, a /a quicksort, i.e., solve the subproblems for subarrays All,lill
and AIL|J + 1,,nf and combine the results. However, in most cases, these two subproblems are
not sufficient to solve the original problem.
DP is based on combining solutions to subproblems to yield a solution to the original problem.
However, for some problems DP will not work. For example, if you need to compute the longest
path from City 1 to City 2 without repeating an intermediate city, and this longest path passes
through City 3, then the subpaths from City 1 to City 3 and City 3 to City 2 may not be
longest
Table 16.1 : Top Tips for Dynamic Programming
playfollowedbyaTpointplayandaTpointplayfollowedbya2pointplaybothleadtoafinal
score of 9. A brute-force approach might be to enumerate these sequences, and count the distinct
combinations within these sequences, e.g., by sorting each sequence and inserting into a hash table.
The time complexity is very high, since there may be a very large number of scoring sequences.
Since all we care about are the combinations, a better approach is to focus on the number of
combinations for each possible number of plays of a single type.
For example, if the final score is 12 and we are only allowed 2 point plays, there is exactly one
way to get 12. Now suppose we are allowed both 2 and 3 point plays. Since all we care about
are combinations, assume the 2 point plays come before the 3 point plays. We could have zero 2
point plays, for which there is one combination of 3 point plays, one 2 point play, for which there
no combination of 3 point plays (since 3 does not evenly divide 12 - 2, two 2 point plays, for which
there no combination of 3 point plays (since 3 does not evenly 12 - 2 x 2), three 2 point plays, for
which there is one combination of 3 point plays (since 3 evenly divides 12 - 2 x 3), etc. To count
combinations when we add 7 point plays to the mix, we add the number of combinations of 2 and
3 that lead to 12 and to S-these are the only scores from which 7 point plays can lead to 12.
Naively implemented, for the general case, i.e., individual play scores are W[0], Wlll, . . . ,WIn -
1], and s the final score, the approach outlined above has exponential complexity because it repeat-
237
```

#### Printed page 238 (PDF page 252)

```text
1
0
0
0
edly solves the same problems. We can use DP to reduce its complexity. Let the 2D array Alilljl
store the number of score combinations that result in a total of 7, using individual plays of scores
W[0], W[1], ...,Wli - 11. For example, Atll[12] is the number of ways in which we can achieve a
total of 12 points, using 2 and/or 3 point plays. Then A[ + 1][] is simply Alillil (no WU + 1l point
plays used to get to fl, plus Ali)U - lV[, + 1]l (one Wft + 1l point play), plus Alilli - 2Wli + 1ll (two
W[i + 1]point plays), etc.
The algorithm directly based on the above discussion consists of three nested loops. The first
loop is over the total range of scores, and the second loop is over scores for individual plays. For a
giveni and i, thethird loop iteratesoveratmostT/W[]+ l values. (Forexample,if j=10,i=1,
and WUI = 3, then the third loop examines A[0][10],A[0][7],,4[0][4],4[0][1].) Therefore number of
iterations for the third loop is bounded by s. Hence, the overall time complexity is O(sns) = O(s2n)
(first loop is to n, second is to s, third is bounded by s).
Looking more carefully at the computation for the row A[ + 1], it becomes apparent that it is
not as efficient as it could be. As an example, suppose we are working with 2 and 3 point plays.
Suppose we are done with 2 point plays. Let A[0] be the row holding the result for just 2 point
plays, i.e., A[0][l] is the number of combinations of 2 point plays that result in a final score of
i. Th" number of score combinations to get a final score of 12 when we include 3 point plays in
addition to 2 point plays is At0lt0l + A[0][3] + A[0][6] + A[0][9] + ,4[0][12]. The number of score
combinations to get a final score of 15 when we include 3 point plays in addition to 2 point plays
is A[0][0] + A[0][3] + A[0][5] + A[0][9] + A[0][12] + A[0][15]. Clearly this repeats computation-
etOlt0l + A[0][3] + A[0][6] + A[0][9] + ,4[0][12] was computed when considering the final score of
12.
Note that ,4[1][15] = ,4[0][15] + A[1][12]. Therefore a better way to fill in A[1] is as follows:
AIlltOl = A[0][0],A[1][1] = A[0][1],,a[1][2] = A[0][2],A[1][3] = A[0][3] + A[1][0],A[1][4] = A[0][4] +
A[1][1],A[1][5] = A[0][5] + A[1][2],. . . . Observe that A[1]Ul takes O(1) time to compute-it's just
AtOlt,l + A[1]U - 31, See Figure 1.6.3 for an example table.
0
)7,
45
10
:
11
11
01
ta
JJ
1
2
2
7
0
1
2
89
10 11 L2
,
213
2,3,7
1
1
1
J
4
0
2
3
1
Figure 16.3: DP table lor 2,3,7 point plays (rows) and final scores from 0 to L2 (columns). As an example, tor 2,3,7
point plays and a total ol 9, the entry is the sum of the entry lor 2,3 point plays and a total of 9 (no7 point plays) and
the entry lor 2,3,7 point plays and a total ol 2 (one additional 7 point play).
The code below implements the generalization of this approach
def nun-combinations-for-finaI-score(final-score, individual-p1ay-scores)
# One way to reach 0.
num_combinations-for-score = [t1] + [0] * final-score
for - in individual-play-scoresl
for i in range(len(individual-play-scores)) 
:
for j in range(l, final-score + 1)l
without-this-play = (num-combinations-for-scoreti - lltjl
if i >= 1 else 0)
with-this-pIay = 1
238
```
