# Exercise 12.9: Find the length of a longest contained interval

**Printed textbook page:** 174. **Reference transcription pages:** 174–174.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 174 (PDF page 188)

```text
- 
The time complexity is O(n), since we perform a constant number of operations per element.
12.9 FrNp rHs LENGTII oF A LoNGEsr CoNTAINED INTERVAL
Write a proglam which takes as input a set of integers represented by an array, and retums the size
of a largest subset of integers in the array having the property that if two integers are in the subset,
then so are all integers between them. For example, if the input is (3,-2,7,9,8,7,2,0, -1,5,8), the
largest such subset is {-2, -1,,0,1,2,3}, so you should retum 6.
Hint:Do you really need a total ordering on the input?
Solution: The brute-force algorithm is to sort the array and then iterate through it, recording for
each entry the largest subset with the desired property ending at that entry.
On closer inspection we see that sorting is not essential to the functioning of the algorithm. We
do not need the total ordering-allwe care are about is whether the integers adjacent to a givenvalue
are present. This suggests using a hash table to store the entries. Now we iterate over the entries in
the array. If an entry e is present in the hash table, we compute the largest interval including e such
that all values in the interval are contained in the hash table. We do this by iteratively searching
entriesinthehashtableof theform e+L,et2,...,ande-1,e - 2,.... Whenwearedone,toavoid
doing duplicated computation we remove all the entries in the computed interval from the hash
table, since all these entries are in the same largest contained interval.
As a concrete example, consider A - <10,5,3,'L'1,6,'100,4). We initialize the hash table to
{6,10,3,11.,5,700,41. The first entry in A is L0, and we find the largest interval contained in A
including 10 by expanding from 10 in each direction by doing lookups in the hash table. The largest
set is {10,11} and is of size 2. This computation updates the hash table to 16,3,5,100,4}. The next
entry in A is 5. Since it is contained in the hash table, we know that the largest interval contained in
A including 5 has not been computed yet. Expanding from 5, we see that3,4,6 are all in the hash
table, and 2 and7 are not in the hash table, so the largest set containing 5 is {3,4,5,6}, which is of
size 4. We update the hash table to {100}. The three entries after 5, namely 3,11.,6 are not present in
the hash table, so we know we have already computed the longest intervals inA containing each of
these. Then we get to 100, which cannot be extended, so the largest set containing it is {100}, which
is of size 1. We update the hash table to {}. Since 4 is not in the hash table, we can skip it. The largest
of the three sets is {3,4,5,61, i.e., the size of the largest contained interval is 4.
def longest-contained-range (A) :
# unprocessed-entries records the existence of each entry in A
unprocessed-entries = set(A)
max-interval-size = 0
xhile unprocessed-entries 
:
a = unprocessed-entries.popo
# Finds the ]orer bound of the largest range containing a.
Iower-bound=a-1
rhile lower-bound in unprocessed-entries:
unproce ssed-entri e s . remove ( lower-bound)
lower-bound -= I
174
```
