# Exercise 24.6: Rotate an array

**Printed textbook page:** 357. **Reference transcription pages:** 357–358.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 357 (PDF page 371)

```text
Subarray = collections . nanedtuple ('Subarray' , ('start ' , 'end ,) )
def find-longest-increasing-subarray(A) :
result = Subarray(0, 0)
i , max-length = 0, 1
rbile i < len(A) - max_length:
# Backward check and skip if Atjl >= l[j + 1].
for j in range(i + max_length, i, -1):
if Atj - 1l >= A[j]:
i=j
break
else: # Forward check if it is not skippable (the Toop ended nornally)
i += ttl2x-1""nt1t
while i < len(A) and Ali - 1l < A[i]:
i, max_length = i + l, max_Iength + 1
result = Subarray(i - max_length, i - l)
return result
Skipping is a heuristic in that it does not improve the worst-case complexity. If the array consists of
alternating 0s and 1s, we still examine each element, implying an O(n) time bound, but the best-case
comPlexity reduces to O(max(nll, L)), where L is the length of the longest increasing subarray.
24.6 Rorerr AN ARRAv g
Let A be an array of n elements. If memory is not a concem, rotating Aby i positions is trivial; we
createanewarrayBoflengthn,andsetBUl =Al(i+ j)modn]foreachl, If altwehaveisadditional
storage for c elements, we can repeatedly rotate the array by c a total of [/cl times; this increases
the time complexity toO(nlilc\.
Design an algorithm for rotating EIn array A of n elements to the right by I positions. Do not use
library functions implementing rotate.
Hint: use concrete examples to form a hypothesis relating n, i, and the number of cycles.
Solution: There are two brute-force algorithms: perform shift-by-one I times, which has O(nl) time
complexity and O(1) space complexity. The other is to use an additional array of length I as a buffur
to move elements I at a time. This has O(n) time complexity and O(l) space complexity.
The key to achieving both O(n) time complexity and O(1) space complexity is to use the fact that
a permutation can be applied using constant additional storage (Problem 5.10 on Page 50) with the
permutation corresponding to a rotation.
A rotation by itself is not a cyclic permutation. However, a rotation is a permutation, and as
such can be decomposed to a set of cyclic permutations. For example, for the case where n = 6 and
i = 2, the rotation corresponds to the permutation (4,5, 1.,2,3,4>. This permutation can be achieved
by the cyclic permutations (0,2,4) and (1,3,5). Similarly, when n = L5 and i = 6,the cycles are
<0, 6, 12, 3, 9), <1,, 7, 13, 4,'1,0>, arrrd (2, g, 14, 5, 11>.
The examples lead us to conjecture the following:
(1.) All cycles have the same length, and are a shifted version of the cycle (0, imodn,2imod
n,. . . ,(l - 1)l mod r).
357
```

#### Printed page 358 (PDF page 372)

```text
(2.) The number of cycles is the GCD of n Nd i.
These conjectures can be justified on heuristic grounds. (A formal proof requires looking at the
prime factorizations for i and n.)
Assuming these conjectures to be correct, we can apply the rotation one cycle at a time, as follows.
The first elements of the different cyclic permutations are at indices 0,1,2, . . . ,GCD(n,i) - 1. For
each cycle, we apply it by shifting elements in the cycle one-at-a-time.
def rotate-array(rotate-amount, A):
def apply-cyclic-permutation(rotate-anount, offset)
temp = Aloffsetl
for i in range(l, cycle-length):
i6x = (offset + i * rotate-amount) % len(A)
Alidxl, 
temp = telnP, A[idx]
Aloffsetl = temP
rotate-amount %= Ien(A)
if rotate-amount == 0:
return
num-cycles = fractions.gcd(Ien(e), rotate-amount)
cycle-length = Ien(A) /,/ num-cycles
for c in range(num-cycles):
apply-cyclic-permutation(rotate-amount, c)
The time complexity is O(n), since we perform a constant amount of work per entry. The space
complexity is O(1).
We now provide an alternative to the permutation approach. The new solution works well in
practice and is considerably simpler. Assume that A = (L,2,3,4,a,b), arrd I = 2. Then in the rotated
A there are two subarrays, <L,2,3,4) and (a,b) that keep their original orders. Therefore, rotation
can be seen as the exchanges of the two subarrays of A. It is easy to perform these exchanges in O(n)
time. To implement these exchanges to use O(1) space we use an array-reverse function. Using A
and I as an example, we first reverse A to get A' ((1,2,3,4,a,b) becomes (b,a,4,3,2,1)), then reverse
the first I elements of A' ((b,a,4,3,2,'L) becomes (a,b,4,3,2,1)), and reverse the remaining elements
starting from the lth element of A' ((a,b,4,3,2,1> becomes \a,b,1,2,3,4)) which yields the rotated
A.
def rotate-array(i, A)
i %= Ien(A)
def reverse (begin, end) :
rhile begin < end:
Albeginl, Alendl = Alendl, AIbegin]
begin, end = begin + 1, end - 1
reverse(0, Ien(A) - 1)
reverse(0, i - 1)
reverse(i, len(A) - 1)
# Although the foTTowing function is very naturaT way to rotate an atray,
# its use of subfists Teads to copy fron originaT -list, and therefote
# Tinear space compTexity.
def rotate-array-naive (i , A) :
358
```
