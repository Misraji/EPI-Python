# Exercise 14.7: Enumerate numbers of the form a + b sqrt(2)

**Printed textbook page:** 207. **Reference transcription pages:** 207–209.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 207 (PDF page 221)

```text
with left endpoint s containing elements from each array must be [s, f], since the remaining two
values are the minimum possible.
Now remove s from the triple and bring the next smallest element from the array it belongs to
into the triple. Let s' and f'be the next minimum and maximum values in the new triple. Observe
[s', f'] must be the smallest interval whose left endpoint is s': the other two values are the smallest
values in the corresponding arrays that are greater than or equal to s'. By iteratively examining
and removing the smallest element from the triple, we compute the minimum interval starting at
that element. Since the minimum interval containing elements from each array must begin with
the element of some array, we are guaranteed to encounter the minimum element.
For example, we begin with (5,3,8). The smallest interval whose left endpoint is 3 has length
8 - 3 = 5. The element after 3 is 6, so we continue with the triple (5,6,8). The smallest interval
whose left endpoint is 5 has length 8- 5 = 3. The element after 5 is 10, so we continue with the triple
(10,6,8). The smallest interval whose left endpoint is 6 has length 10 - 6 = 4. The element after 6
is 9, so we continue with the triple (L0,9,8). Proceeding in this way, we obtain the triples (\0,9,16),
(10,\2,16), (15,12,76), (15, 15, 16). Out of all these triples, the one contained in a minimum length
interval is (15, 15, 16).
In the following code, we implement a general purpose function which finds the closest entries
in k sorted arrays. Since we need to repeatedly insert, delete, find the minimum, and find the
maximum amongst a collection of k elements, a BST is the natural choice.
def find-closest-elenents-in-sorted_arrays ( sorted_arrays)
min-distance_so_far = float('inf 
')
# Stores array iterators in each entry.
iters = bintrees.RBTreeo
for idx, sorted_array in enuuerate(sorted_arrays) :
it = iter(sorted_array)
first-min = nert(it, 
None)
if first-min is not None:
iters. insert ((first_min, 
idx) , it)
rhile True:
min-value , min_idx = iters . min_key o
max_vaIue = iters.nax_keyO [0]
min-distance-so-far = nin(max_va1ue - min_value, min_distance_so_far)
it = iters. pop_minO [lJ
next-min = nert(it, None)
# Retutn if sone array has no renaining elements.
if next-min is ilone:
return min-di stance_so_far
iters. insert ((next-min , min_idx) , it)
The time complexity is O(nlogk), where n is the total number of elements in the k arrays. For the
sPecial case k = 3 specified in the problem statement, the time complexity is O(n log3) = O(n).
74.7 ENurrasnATE NUMBERS oF THE FoRM a + b.'11
Numbers of the form a + b \f-q, where a andb are nonnegative integers, and q is an integer which is
not the square of another integer, have special properties, e.g., they are closed under addition and
multiplication. fome of the first few numbers of this form are given in Figure 14.4 on the following
Page.
207
```

#### Printed page 208 (PDF page 222)

```text
(0+0f)
(1+0112) (0+1f) 
1z*0,'12) 1r+r{y e+z,'le e+1\f\ 0.+211)
Q*Zrll)
0.0
1.0 
1.41.4
2.0 
2.41.4 2.828
3.474 3.828
4.828
Figure 14.4: Some points of the form a + b r/1. (For typographical reasons, this figure does not include all numbers of
theforma+b,,llbetween0and2+2.,11,e.g.,3+otll,q+O\lr,O+3t11,3+ll'lztieintheintervat 
burarenot
included.)
Design an algorithm for efficiently computing the k smallest numbers of the form a + b ll tor
nonnegative integers a arrdb.
Hln f: Systematically enumerate points.
Solution: A key fact about lD is that it is irrational,i.e., it cannot equal to fi for aurry integers a,b.
This implies that if x + y fi = x' + y",ll, where x and yare integers, then r = xt and y = y' (since
otherr.rrise ,,1, = v_y,t=L).
Here is a brute-force solution. Generate all numbers of the form a + b,'llwhere a attd b are
integers, O 1 a,b < k - 1. This yields exactly k2 numbers and the k smallest numbers must lie in
this collection. We can sort these numbers and refum the k smallest ones. The time complexity is
O (P toe(tC)) = O (P tog k).
Intuitively, it is wasteful to generate k2 numbers, since we only care about a small fraction of
them.
We know the smallest number is 0 + 0 f. fn" candidates for next smallest number are 1, + 0',11
and 0 + 1f. From this, we can deduce the following algorithm. We want to maintain a collection
of real numbers, initialized to 0 + 0lE. We perform k extractions of the smallest element, call it
a + b {2, followed by insertion of (a + 1) + b.,1, and a + (b + 1 ) f to th" collection.
The operations on this collection are extract the minimum and insert. Since it is possible that
the same number may be inserted more than once, we need to ensure the collection does not create
duplicates when the same item is inserted twice. A BST satisfies these operations efficiently, and
is used in the implementation below. It is initialized to contain 0 + 0 f. We extract the minimum
from the BST,which is 0+0 .'l2,arrdinsert l. +0.'lland 0+ 1,'llto the BST. We extract the minimum
from the BSI which is 1+ 0,,ll,aodinsert2 +0,'lland 1+ t.'lito the BST, which now consists of
0 + 11D = 1.474,2 + 0,'11= 2,1+ t,'ll = 2.474. \Ne extract the minimum from the BST, which is
O + 1..,12, and insert 1, + 7,,12 and 0 + Ztll. fne first value is already present, so the BST updates to
2+Olr=2,1+tfi-=2.414,0+2fi-=2.828.(Althoughit'snotapparentfromthissmallexample,
the values we add back to the BST may be smaller than values already present in it, so we really
need the BST to hold values.)
class ABSqrt2:
def --init--(self, 
a, b):
self.a, se1f.b = a, b
self.val = a + b * math.sqrt(2)
def --1t--(seIf, 
other):
return self.val < other.val
def --eq--(self , other) :
return self.val == other,val
208
```

#### Printed page 209 (PDF page 223)

```text
def generate_first_k_a_b_sqrt2 (k) :
# Initial for 0 + 0 * sqrt(2).
candidates = bintrees.RBTree([(ABSqrt2(0, 0), None)])
result = []
rhile len(result) < k:
next_smallest = candidates.pop_minO tol
result . append (next-srnallest , vaI)
# Adds the next two numbers derived frorn next_snallest,
candidatesIABSqrt2(next-smallest.a + I, next_smallest.b)] = None
candidatesIABSqrt2(next_smalIest.a, next_smalIest.b + f)] = None
return result
In each iteration we perform a deletion and two insertions. There are k such insertions, so the time
comPlexity is O(klogk). The space complexity is O(k), since there are not more than 2k insertions.
Now we describe anO(n) time solution. It is simple to implement, but is less easy to understand
than the one based on BST. The idea is that the (n + 1)th value will be the sum of 1. or \D with a
Previous value. We could iterate through all the entries in the result and track the smallest such
value which is greater than nth value. However, this takes time O(n) to compute the (n + 1)th
element.
Intuitively, there is no need to examine all prior values entries when computing (n + 1)th value.
Let's say we are storing the result in an array A. Then we need to track just two entries-I, the
smallest index such that A[] + 1, > Aln - 11, and /, smallest index such that A[i] + \D > Aln - 11.
Clearly, the (n + l)th entry will be the smaller of Alil+ 1 and Aljl + ,11. lftu, obtaining the (n + 1)th
entry, if it is Aftl + L, we increment i. If it is Af,jl + ^f-2,we increment i. If Ali) + 1 equals eljl + l-2,
we increment both I and 7.
To illustrate, suppose.4 is initialized to (0), and I and j are 0. The computation proceeds as
follows:
(1.) SinceA[0]+L = 1. <A[0]+ .'fl=T.4l4,wepushlintoAandincrementi. Now A- <0,1),
i=l,j=0.
(2.) Since A[1] + 'J. = 2 > A[0] + "'f2 = 1.41,4, we push 1.414 into A and increment f. Now
A = (0,1.,L.414>, i = 1, j = 1.
(3.) SinceA[1] +'1. = 2 < AIU + fi = 2.41,4,we push2intoA and incrementl. NowA =
<0, 1.,'1..41.4, 2), i = 2, j = l.
(4.) Since A[2] + 1 = 2.474 = A[L1+ ,'ll = 2.4L4,we push 2.414 into A and inqement both i and, j.
Now A * <0,1,7.474,2,2.414), i = 3, j = 2.
(5.) SinceA[3] +1= 3 > Al2)+ fr= 2.828,we push2.823intoAandincrementi. Now
A = (0,1, 1.41.4,2,2.828), i = 3, j = 3.
(6.) Since ALSI+ 1 = 3 < AlSl+ \/1 = 3.414,we push3intoAand.incrementi. NowA =
<0, 1., 1..474, 2, 2.929, 3>, i = 4, j = 3.
def generate_first-k-a-b_sqrt2 (k) :
# Will store the first k nunbers of the forn a + b sqrt(2)
cand = [ABSqrt2(0, 0)]
i=j=S
for - in range(l, k):
cand_i_plus*1 = ABSqrt2(candIi].a + 1, candtil.b)
cand-j-plus_sqrt2 = ABSqrt2(candIj].a, candljl.b + t)
cand. append(nin(cand_i_pIus_1, cand_j_pIus_sqrt2))
if cand-i-plus-1.val == cand[-t] .val:
209
```
