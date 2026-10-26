# Exercise 16.6: The knapsack problem

**Printed textbook page:** 246. **Reference transcription pages:** 246–248.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 246 (PDF page 260)

```text
In the program beloW we cache intermediate results to avoid repeated calls to the recursion
with identical arguments.
def is-pattern-contained-in-grid(grid, S) :
def is-pattern-suffix-contained-starting-at-xy(x, y, offset)
if len(s) == offset:
# Nothing Teft to complete.
return True
# Check if (x, f) Ties outside the grid.
if (0 <= x < len(grid) and 0 <= y < len(grid[x])
and gridIx]tYl 
== Sloffsetl
and (x, y, offset) not in previous-attempts and any(
i s-patt ern- suffi x-c ont ai ne d-st art ing-at-xy (
x+a,y+b,offset+1)
for a, b in ((-1,0), 
(1,0), 
(0, -1), (0, 1))))
return True
previous-attempts.add((x, y, offset))
return FaIse
# Each entry in previous-attempts is a point in the gtid and suffix of
# pattern (jdentified 
by its offset). 
P,'esence in previous-attempts
# indicates the suffix is not contained in the grid starting fron that
# point.
previous-attempts = seto
return any(
is-pattern-suffix-contained-starting-at-xy(i, j, 0)
for i in range(len(grid)) for j in range(Ien(grid[i])))
The complexity is O(nmlSl), where n arrd m are the dimensions of A-we do a constant amount of
work within each call to the match function, except for the recursive calls, and the number of calls
is not more than the number of entries in the 2D array.
Varianh Solve the same problem when you cannot visit an entry inA more than once.
Variant: Enumerate all solutions when you cannot visit an entry in A more than once.
16.6 THU xNapsecK PRoBLEM
A thief breaks into a clock store. Each clock has a weight and a value, which are known to the thief.
His knapsack carmot hold more than a specified combined weight. His intention is to take clocks
whose total value is maximum subject to the knapsack's weight constraint.
His problem is illustrated in Figure 15.8 on the next page. If the knapsack can hold at most
130 ounces, he cannot take all the clocks. If he greedily chooses clocks, in decreasing order of value-
to-weight ratio, he will choose P,H,O,B,I, atrrd L in that order for a total value of $669. However,
lH,l,Ol is the optimum selection, yielding a total value of $595.
Write a program for the knapsack problem that selects a subset of items that has maximum value
and satisfies the weight constraint. All items have integer weights and values. Retum the value of
the subset.
Hint: Greedy approaches are doomed.
Solution: Greedy strategies such as picking the most valuable clock, or picking the clock with
maximum value-to-weight ratio, do not always give the optimum solution.
246
```

#### Printed page 247 (PDF page 261)

```text
'to
ll t2t
'ro . 7z
t2
'/
z'
3
'ro 
/2
4r
vi
A,$65,20o2. B,$35,8o2. C,9245,60o2. D,9195,55o2. E,$65,40o2. F,gtSO,70oz. c,gZ7S,85oz. H,$tSS,25oz.
L$120,30o2. l,$320,65o2. K,$75,75o2.
L,$40,10 oz. 
M,$200,95 oz. 
N, $100,50 oz.
Flgure 16.8: A clock store.
0,$220,40o2. P,$9,10o2.
We can always get the optimum solution by considering all subsets, e.g., using Solution 15.4
on Page 225. This has exponential time complexity in the number of clocks. F{owever, brute-force
enumeration is wasteful because it ignores the weight constraint. For example, no subset that
includes Clocks F and G can satisfy the weight constraint.
The better approach is to simultaneously consider the weight constraint. For example, what is
the optimum solution if a given clock is chosen, and what is the optimum solution if that clock is not
chosen? Each of these can be solved recursively with the implied weight constraint. For the given
example, if we choose the Clock A, we need to find the maximum value of clocks from Clocks B-P
with a caPacity of 130 - 20 and add $65 to that value. If we do not choose Clock A, we need to
find the maximum value of clocks from Clocks B-P with a capacity of 130. The larger of these two
values is the optimum solution.
More formally, let the clocks be numbered from O to n - 1, with the weight and the value of the
Ith clock denoted by w; and u;. Denote by Vlilfw) the optimum solution when we are restricted to
Clocks 0,L,2,... ,i - l and can carry 7t) weight. Then V[][ru] satisfies the following recurnence:
Vlillwl =
We take i = 0 or w = 0 asbases cases-for these, Vlillw) = g.
We demonstrate the above algorithm in Figure 16.9 on the next page. Suppose there are four
items, *,fi,V,d whose value and weight are given in Figure 1"6.9(a) on the following page. Then
the corresponding V table is given in Figure 16.9(b) on the next page. As an example, the extreme
lower right entry is the maximum of the entry above (70) and 30 plus the entry for *,8, g *ittt
capacity 5 - 2 (50), i.e., 80.
Item = collections . namedtuple ('Item' , ('weight ' , 'value ') )
def optimum-subject-to-capacity(items, capacity) :
# Returns the optiaun value when r+'e cioose from itens[:k + 1] and have a
# capacity of avaiTabie_capacity.
def optimum-sub j ect-to-item-and-c apaci ty (k, avail able_capacity) :
ifk<0:
# No itens can be chosen,
return 0
max(yU -ll[wl,V[i-lllw - wif + a;), iwi < w;
Vli - llfuil, 
otherwise.
to u 7z'
9 I 
3-
8 
4-
,:.
if VtklIavailable-capacity] =- -1
247
```

#### Printed page 248 (PDF page 262)

```text
80
50
70
70
0
0
30
2
0
01
00
:o.o
00
345
0060
Item
W
0
v
Value
$60
$so
$70
$30
Weight
5 oz.
3 oz.
4 oz.
2 oz.
*
*E
6)08
*fiva
0
0
(a) Value-weight table. 
(b) Knapsack table for lhe items in (a). The columns
correspond to capacities from 0 to 5.
Figure 16.9: A small example of the knapsack problem. The knapsackcapacity is 5 oz.
without-curr-item = optimum-subject-to-item-and-capacity(
k - 1, available-capacity)
with-curr-item = (0 if available-capacity < items[k].weight else (
itemsIk] . value + optimum-subject-to-item-and-capacity(
k - 1, available-capacity - itemslkl.weight)))
VIk] [ available-capacity] = nar(without-curr-item, with-curr-item)
return v Ik] [ available-capacity]
# v|il[j] 
holds the optinun value when we choose froat itens[:i + 1] and have
# a capacity of j.
V = tt-tl * (capacity + 1) for - in itemsl
return optimum-subject-to-item-and-capacity(Ien(items) - 1, capacity)
The algorithm computes Vln - lllwlnO(nw) time, and usesO(nw) sPace.
VarianL Solve the same problem using O(zu) space.
Variant: Solve the same problem using O(C) space, where C is the number of weights between 0
and w that can be achieved. For example, if the weights are 100, 200, 200,500, and ar = 853, then
C = 9, corresponding to the weights 0,100,200,300,400,500,600,700,800.
Variant: Solve the fractional knapsack problem. In this formulatiory the thief can take a fractional
part of an item, e.g., by breaking it. Assume the value of a fraction of an item is that fraction times
the value of the item.
Variant: In the "divide-the-spoils-fairly" problem, two thieves who have successfully completed
a burglary want to know how to divide the stolen items into two groups such that the difference
between the value of these two groups is minimized. For example, they may have stolen the clocks
in Figure 16.8 on the precedingpa3e, and would like to divide the clocks between them so that the
diffurence of the dollar value of the two sets is minimized. For this instance, an optimum split is
lA, G, I, M, O, Pl to one thief and the remaining to the other thief. The first set has value $1J79, and
the second has value $1180. An equal split is impossible, since the sum of the values of all the clocks
is odd. Write a program to solve the divide-the-spoils-fairly problem,
Variant Solve the divide-the-spoils-fairly problem with the additional constraint that the thieves
have the same number of items.
Variant: The US President is electedby the members of the Electoral College. The number of electors
per state and Washington, D.C., are given in Table 16.2 on the next page. All electors from each state
248
```
