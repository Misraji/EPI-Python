# Exercise 5.1: The Dutch national flag problem

**Printed textbook page:** 39. **Reference transcription pages:** 39–42.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 39 (PDF page 53)

```text
o Checking if a value is present in an array is as simple as a in A. (This operation has O(n) time
complexity, where n is the length of the array.)
o Understandhowcopyworks, i.e., thedifferencebetweenB = AandB = Iist(A). Understand
what a deep copy is, and how it differs from a shallow copy, i.e., how copy. copy(A) differs
from copy. deepcopy(A).
o Key methods for list include min(A), max(A), binary search for sorted lists
(bisect.bisect(A,6), bisect.bisect-left(A,6), and bisect.bisect_right(A,6)),
A.reverseO (in-place), reversed(A) (retums an iterator), A.sortO (in-place), sorted(A)
(retums a copy), del A[i] (deletes the i-th element), and del A[i: j] (removes the slice).
o Slicing is a very succinct way of manipulating arrays. It can be viewed as a generalization of
indexing: the most general form of slice is A [i : j : k], with all of i, j, and k being optional. Let
A = [1, 6, 3, 4, 5, 2, 77. Herearesomeexamplesof slicing: A[2:4] is [3, 4],A[2:] is
[3, 4, 5, 2, 77,A[:4] is [1, 6, 3, 4),A[:-1] is [1, 6, 3, 4, 5, 2],A[-3:] is [5, 2,
77,A1-3:-11 is 15, 2f,A[1:5:2] is [6, 4],A[5:1:-2] is 12,  f,andA[::-1] is L7, 2, 5,
4, 3, 6, 1l (reverseslist). Slicingcanalsobeusedtorotatealist Alk:l + A[:k] rotatesA
bykto theleft. Itcanalsobeusedtocreateacopy: B = A[:] doesa(shallow)copyof Ainto
B.
o Python provides a feature called list comprehension that is a succinct way to create lists. A
list comprehension consists of (1.) an input sequence, (2.) an iterator over the input sequence,
(3.) a logical condition over the iterator (this is optional), and (4.) an expression that yields
theelementsof thederivedlist. Forexample, [x**2 for x in range(6)J yields [0, 1, 4,
9, 16, 25l,and[x**2 for x in range(6) if x%2 == 0]yields[0, 4, 16].
Although list comprehensions can always be rewritten using mapO, filterO, and lamb-
das, they are clearer to read, in large part because they do not need lambdas.
List comprehension supports multiple levels of looping. This can be used to create the
productof sets,e.g.,ifA - [1, 3, 5] andB = ['d', 'b'],then [(x, y) for x in A for y
in B] creates [(1, 'a'), (1, 'b'), (3, 'a'), (3, 'b'), (5, 'a'), (5, 'b')]. It can
alsobeusedtoconverta2DlisttoalDlist,e.g.,ifltl = [['a', 'b', 'c'], ['d', 'e',
'f'7f ,x for row in 11 for x in rowcreates ['a', 'b', 'c', 'd', 'e', 'f ']. TWolev-
els of looping also allow for iterating over each entry in a 2D list, e.g., lf A = [[1,
2, 3f , [4, 5, 6]l then [[xoo2 for x in row] for row in ]Il yields [[1, 4, 9], [16,
25 , 361 1.
As a general rule, it is best to avoid more than two nested comprehensions, and use
conventional nested for loops-the indentation makes it easier to read the program.
Finally, sets and dictionaries also support list comprehensions, with the same benefits.
5,1 Tns DurcH NATToNAL FLAG pRoBLEM
The quicksort algorithm for sorting arrays proceeds recursively-it selects an element (the "pivot"),
reorders the array to make all the elements less than or equal to the pivot appear first, followed by
all the elements greater than the pivot. The two subarrays are then sorted recursively.
Implemented naively, quicksort has large run times and deep function call stacks on arrays with
many duplicates because the subarrays may differ greatly in size. One solution is to reorder the
array so that all elements less than the pivot appear first, followed by elements equal to the pivot,
39
```

#### Printed page 40 (PDF page 54)

```text
followed by elements greater than the pivot. This is known as Dutch national flag partitioning,
because the Dutch national flag consists of three horizontal bands, each in a different color.
As an example, assuming that black precedes white and white precedes gray, Figure 5,1(b) is a
valid partitioning for Figure 5.1(a). lf gray precedes black and black precedes white, Figure 5.1(c)
is a valid partitioning for Figure 5.1(a).
Generalizing, suppose A = (0,1.,2,0,2,1,L), and the pivot index is 3. Then A[3] = 0, so
<0,0,7,2,2,L,1) is a valid partitioning. For the same array, if the pivot index is 2, then Al2l = 2, "o
the arrays <0,7,0,1,1,2,2> as well as (0,0, 7,1,,'1,,2,2> are valid partitionings.
(a) Before partitioning
(b) A three-way partitioning resembling
the Dutch national flag.
(c) Another three-way partitioning: the
Russian national flag.
Figure 5.1 : lllustrating the Dutch national flag problem.
Write a program that takes an array A and an index i rnto A, and rearranges the elements such
that all elements less than A[r] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.
Hinf: Think about the partition step in quicksort.
Solution: The problem is trivial to solve with O(n) additional space/ where n is the length of A.
We form three lists, namely, elements less than the pivot, elements equal to the pivot, and elements
greater than the pivot. Consequently, we write these values into A. The time complexity is O(n).
We can avoid using O(n) additional space at the cost of increased time complexity as follows. In
the first stage, we iterate through A starting from index 0, then index 1, etc. Lr each iteration, we
seek an element smaller than the pivot-as soon as we find it, we move it to the subarray of smaller
elements via an exchange. This moves all the elements less than the pivot to the start of the array.
The second stage is sirnilar to the first one, the difference being that we move elements greater than
the pivot to the end of the array. Code illustrating this approach is shown below.
RED, WHITE, BLUE = range(3)
def dutch-flag-partition(pivot-index, A):
pivot = A[pivot-index]
# First pass: group elernents smaller than pivot
for i in range(1en(A)):
# Look fot a snaTTer el.ernent,
for j in range(i + 1, Ien(A)):
if AIjl < pivot:
Atil, Atjl = AIj], Alil
breaL
40
```

#### Printed page 41 (PDF page 55)

```text
# Second pass: gtoup elernents Targer than pivot.
for i in reversed(range(Ien(A))):
if A[i] < pivot:
break
# Look for a Targer element. Stop when we reach an efernent less than
# pivot, since first pass has moved them to the start of A.
for j in reversed(range(i)):
if Atjl > pivot:
AIil, Atjl = etjl, atil
break
The additional space complexity is now O(1),but the time complexity is O(n2), e.g., i i = nl2
and all elements before I are greater than A[l], and all elements after I are less than Aft]. Intuitively,
this approach has bad time complexity because in the first pass when searching for each additional
element smaller than the pivot we start from the beginning, However, there is no reason to start
from so far back-we can begin from the last location we advanced to. (Similar comments hold for
the second pass.)
To improve tirne complexity, we make a single pass and move all the elements less than the pivot
to the beginning. In the second pass we move the larger elements to the end. It is easy to perform
each pass in a single iteration, moving out-of-place elements as soon as they are discovered.
RED, WHITE, BLUE = range(3)
def dutch-flag_partition(pivot-index, A) :
pivot = AIpivot-index]
# First pass: group elernents smal-ler than pivot
smaller = 0
for i in range(Ien(A)):
if Atil < pivot:
AIi], AIsmaller] = AIsmaIler], AIi]
smaller += I
# Second pass; group elements Targer than pivot
larger=Ien(A)-1
for i in reversed(range(Ien(A))):
if Atil < pivot:
break
elif A[i] > pivot:
Alil, l[arger] = AIlarger] , AIi]
larger -= 1
The time complexity isO(n) and the space complexity is O(1).
The algorithm we now present is similar to the one sketched above. The main difference is that
it performs classification into elements less than, equal to, and greater than the pivot in a single
pass. This reduces runtime, at the cost of a trickier implementation. We do this by maintaining four
subarrays: bottom (elements less than pivot), middle (elements equal to pivot), unclassified, ar.d top
(elements greater than pivot). Initially, all elements areinunclassified. We iterate through elements
inunclassified, andmove elements into one of bottom,mi.ddle, andtop groups according to the relative
order between the incoming unclassified element and the pivot.
41
```

#### Printed page 42 (PDF page 56)

```text
As a concrete example, suppose the array is currently A - <-3,0,-L,").,').,?,?,?,4,2>, where the
pivot is 1 and ? denotes unclassified elements. There are three possibilities for the first unclassified
element, A[5].
o A[5] is less than the pivot, e.9., A[5] = -5. We exchange it with the first 1, i.e., the new array
is (-3, 0, -1, -5, 1,'1., ?, ?, 4, 2).
o A[5] is equal to the pivot, i.e., A[5] = L. We do not need to move it, we just advance to the next
unclassified element, i.e., the array is <-3,0,-1,L,1.,1.,?,?,4,2>.
r A[5] is greater than the pivot, e.9., A[5] = 3. We exchange it with the last unclassified element,
i.e., the new array is (-3,0, -1.,1.,1.,?,?,3,4,2).
Note how the number of unclassified elements reduces by one in each case.
RED, WHITE, BLUE = range(3)
def dutch-flag-partition(pivot-index, 
A) :
pivot = Alpivot-indexl
# Keep the following invariants during partitioning:
# botton group: A[:sma]IerJ.
# niddle gtoup: lfsnal]er:equa7l.
# unc]assifi ed. group: A[equal: Targer] .
# top group: A[Targer: ] .
smaller, equal, larger = 0, 0, len(A)
# Keep iterating as -Iong as there is an unclassified elenent
while equal < larger:
# A[equa7] is the inconing unclassjfied element,
if AIequal] < pivot:
Alsmallerl, AIequal] = AIequaI], AIsmaller]
smaller , equal = smaller + 1, equal + 1
elif AIequa1] == pivot:
equal += 1
else: 
# A[equal] > pivot.
Iarger -= I
AIequal], AIIarger] = AIlarger] ' AIequal]
Each iteration decreases the size of unclassifiedby 1,, and the time spent within each iteration is O(1),
implying the time complexity is O(n). The space complexity is clearly 0(L).
Variant Assuming that keys take one of three values, reorder the array so that all objects with the
same key appear together. The order of the subarrays is not important. For example, both Figures
5.1(b) and 5.1(c) on Page 40 are valid answers for Figure 5.1(a) on Page 40. Use O(1) additional
sPace and o(n) time.
Variant: Given an array A of n objects with keys that takes one of four values, reorder the array so
that all objects that have the same key appear together. Use O(1) additional space and O(n) time.
Variant Given an array A of n objects with Boolean-valued keys, reorder the array so that objects
that have the key false appear first. Use O(1) additional space and O(n) time.
Varianh Given em array A of n objects with Boolean-valued keys, reorder the array so that objects
that have the key false appear first. The relative ordering of objects with key true should not change.
Use O(1) additional space and O(n) time.
42
```
