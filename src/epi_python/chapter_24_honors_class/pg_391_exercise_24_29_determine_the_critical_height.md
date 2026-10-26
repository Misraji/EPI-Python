# Exercise 24.29: Determine the critical height

**Printed textbook page:** 391. **Reference transcription pages:** 391–392.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 391 (PDF page 405)

```text
Altematively, the maximum subarray that cycles around can be determined by computing the
minimum subarray-the remaining elements yield a subarray that cycles around. (One or both of
the first and last elements may not be included in this subarray, but that is fine.) This approach uses
O(1) space andO(n) time; code for it is given below.
def max-subarray-sum-in*circular (A) :
def f ind_opt imum-subarray_u s in g_c omp ( c omp )
till=overall=0
for a in A:
tiIl = cornP(a, a + till)
overall = comp(overa1l, till)
return overall
# Finds the max in non-circu-Iar case and circul.ar case.
return nar(
find-optimum_subarray_using_comp(nar), # Non-circular case,
sun(A) - find_optimum_subarray_using_comp(nin)) # Circujar case
24.29 DErrnMrNs rHE cRrrrcAI, Hucrrr @
You need to test the design of a protective case. Specifically, the case can protect the enclosed device
from a fall from up to some number of floors, and you want to determine what that number of
floors is. You can assume the following:
o All cases have identical physical properties. In particular, if one breaks when falling from a
particular level, all of them will break when falling from that level.
o A case that survives a fall can be used again, and a broken case must be discarded.
o If a case breaks when dropped, then it would break if dropped from a higher floo1, and if a
case survives a fall, then it would survive a shorter fall.
It is not ruled out that the first-floor windows break cases, nor is it ruled out that cases can survive
the 36th-floor windows.
You know that there exists a floor such that the case will break if it is dropped from any floor at
or above that floor, will remain intact if dropped from a lower floor. The ground floor is numbered
zero, and it is given that the case will not break if dropped from the ground floor.
An additional constraint is that you can perform only a fixed number of dropsbefore thebuilding
supervisor stops you.
Note that if we have a single case and are allowed only 5 drops, then the highest we can measure
to is 5 floors, testing from 1, 2, 3, 4, and 5. We cannot skip a floor, since the case may break
immediately aJter the skipped floor, and we would have no way to know if the critical floor was
the last one tested or a skipped floor. If the case does not break, we know it is able to last to a fifth
floor drop.
If we have two cases and are allowed 5 drops, we can do better. For example, we could test by
dropping from floors 2, 4, 6, 8, 9. lf a case breaks on the first four drops, we have narrowed the
critical floor to that floor or the one below it. We can test the one below it with the second case. If
the case breaks on the fifth drop, we know the critical floor is 9. If the case does not break, we know
it is able to last to a ninth floor drop. Clearly having two cases is better than one.
391
```

#### Printed page 392 (PDF page 406)

```text
Given c cases and a maximum of d allowable drops, what is the maximum number of floors that
you can test in the worst-case?
Hint: Write a recurrence relation.
Solution: Let F(c, d) be the maximum number of floors we can test with c identical cases and at
mostddrops.WeknowthatE(1.,d)=d.SupposeweknowthevalueofF(i,j)foralli<candj<d.
Ifwearegivenc+lcasesandddropswecanstartatfloorF(c,d-1)+landdropacase.
If the case breaks, then we can use the remaining c cases Nd d - 1 drops to determine the floor
exactly, since it must be in the range [1, F(c ,d - t)]. If the case did not break, we proceed to floor
F(c,d - 1) + 1 + F(c + 1,,d - 1).
Therefore, F satisfies the recurrence
F(c + 1,,d) = F(c,d - 1) + 1 + F(c + L,d - 7).
We can compute I using DP as below
def get-height (cases , drops) :
def get-height-helper(cases, drops) :
if cases == O or drops == 0:
return 0
elif 
cases == 1:
return drops
if FIcases][droPs] == -1:
FIcases][drops] = (get-height-helper(cases, drops - 1) +
get-height-helper(cases - 1, drops - 1) + 1)
return FIcases] [drops]
f = tt-fl * (drops + 1) for i in range(cases + 1)l
return get-height-helper(cases, drops)
The time and space complexity are O((c + 1Xd + 1)).
Variant: Solve the same problem with O(c) space.
Varian* How would you compute the minimum number of drops needed to find the breaking
point from 1 to F floors using c cases?
Variant: Men numbered from 1, to n are arranged in a circle in clockwise order. Every kth man is
removed, until only one man remains. What is the number of the last man?
24.30 Frno rnu MAXIMUM 2D sunannav $
The following problem has applications to image processing.
Let A be a\ n x m Boolean 2D array. Design efficient algorithms for the following two problems:
o What is the largest 2D subarray containing only 1s?
o What is the largest square 2D subarray containing only 1s?
\Alhat are the time and space complexities of your algorithms as a function of n ao-rd m?
Hint:How would you efficiently check if A[i,i + allj, j+ b] satisfies the constraints, assuming you have already
performed similar checks?
392
```
