# Exercise 12.6: Find the smallest subarray covering all values

**Printed textbook page:** 168. **Reference transcription pages:** 168–170.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 168 (PDF page 182)

```text
latest-equa1-word = word-to-latest-index Iword]
nearest-repeated-distance = nin(nearest-repeated-distance,
i - latest-equal-word)
word-to-latest-indexIword] = i
return nearest-repeated-distance if nearest-repeated-distance != float(
'inf') 
else -1
The time complexity is O(n), since we perform a constant amount of work per entry. The space
complexity is O(d), where d is the number of distinct entries in the array.
72.6 Frup rHr sMALLEST sUBARRAy covERING ALL vALUES
When you type keywords in a search engine, the search engine will return results, and each result
contains a digest of the web page/ i.e., a highlighting within that page of the keywords that you
searched for. For example, a search for the keywords "lJnion" and "save" on a page with the text
of the Emancipation Proclamation should return the result shown in Figure L2.L.
My paramount object in this struggle is to save the Union, and is not either to save or to
destroy slavery. If I could save the Union without freeing any slave I would do it, and if I
could save it by freeing all the slaves I would do it; and if I could save it by freeing some and
leaving others alone I would also do that.
Figure 12.1 : Search result with digest in boldface and search keywords underlined.
The digest for this page is the text in boldface, with the keywords underlined for emphasis. It
is the shortest substring of the page which contains all the keywords in the search. The problem of
computing the digest is abstracted as follows.
Write a program which takes an array of strings and a set of strings, and retum the indices of
the starting and ending index of a shortest subarray of the given array that "covers" the set, i.e.,
contains all strings in the set.
Hint: rNhat is the maximum number of minimal subarrays that can cover the query?
Solution: The brute force approach is to iterate over all subarrays, testing if the subarray contains
all strings in the set. If the array length is n, there arcO(n?) subarrays. Testingwhether the subarray
contains each string in the set is an O(n) operation using a hash table to record which strings are
present in the subarray. The overall time complexity is O(n3).
We can improve the time complexity to O(n2) by growing the subarrays incrementally. Specif-
ically, we can consider all subarrays starting at I in order of increasing length, stopping as soon as
the set is covered. We use a hash table to record which strings in the set remain to be covered. Each
time we increment the subarray length, we need O(1) time to update the set of remaining strings.
We can further improve the algorithm by noting that when we move from I to i + 1 we can reuse
the work performed from i. Specifically,let's say the smallest subarray starting at i covering the set
ends at 7. There is no point in considering subarrays starting at i + 1. and ending before 7, since we
know they cannot cover the set. lvVhen we advance to i + l, either we still cover the set, or we have
to advance f to cover the set. We continuously advance one of I or f, which implies an O(n) time
complexity.
168
```

#### Printed page 169 (PDF page 183)

```text
As a concrete example, consider the array (apple, bnnana, apple, apple, dog, cat, apple, dog, banana,
apple, cat, dog) and the set {banana,catl. The smallest subarray covering the set starting at 0 ends at
5. Next, we advance to 1. Since the element at 0 is not in the set, the smallest subarray covering the
set still ends at 5. Next, we advance to 2. Now we do not cover the set, so we advance from 5 to
&-now the subarray from 2 to 8 covers the set. We update the start index from 2 to 3 to 4 to 5 and
continue to cover the set. When we advance to 6, we no longer cover the set, so we advance the end
index till we get to 10. We can advance the start index to 8 and still cover the set. After we move
past 8, we cannot cover the set. The shortest subarray covering the set is from 8 to 10.
Subarray = collections . namedtuple ('Subarray ' , (' start ' , 'end') )
def find-smallest-subarray-covering-set(paragraph, keywords)
keywords-to*cover = collections. Counter (keywords)
result = Subarray(-1, -1)
remaining-to-cover = len(keywords)
left = 0
for right, p in enuEerate(paragraph):
if p in keywords:
keywords-to-cover tpl -= 1
if keywords-to-cover[p] >= 0:
remaining-to-cover -= 1
# Keeps advancing Left until keywords-to-cover does not contain a77
# keywords.
rhile remaining-to-cover == 0:
if result == (-1, -1) or right - left < resultlll 
- result[0]:
result = (Ieft, 
right)
pI = paragraph[1eft]
if pI in keywords:
keywords-to-cover[pI] += f
if keywords*to_coverIpI] > 0:
remaining-to-cover += 1
Ieft += 1
return result
The complexity is O(n),where n is the length of the array, since for each of the two indices we spend
O(1) time per advance, and each is advanced at most n - 1 times.
The disadvantage of this approach is that we need to keep the subarrays in memory. We can
achieve a streaming algorithm by keeping track of latest occurrences of query keywords as we
process A. We use a doubly linked list L to store the last occurrence (index) of each keyword in Q,
and hash table H to map each keyword in Q to the corresponding node in L. Each time a word
in Q is encountered, we remove its node from L (which we find by using H), create a new node
which records the current index in A, and append the new node to the end of L. We also update
H. By doing this, each ke)'word in L is ordered by its order in A; therefore, if L has np words (i.e.,
all keywords are shown) and the current index minus the index stored in the first node in L is less
than current best, we update current best. The complexity is still O(n).
def find-smaIlest-subarray-covering-subset (stream, query-strings)
class DoublyLinkedListNode :
def --init--(se1f , data=None) :
169
```

#### Printed page 170 (PDF page 184)

```text
self,data = data
self.next = self,prev = None
class Linkedlist:
def --init--(self):
self,head = self.tail 
= None
se1f.-size = 0
def --len--(self):
return self, -size
def insert-after (self, value) :
node = DoublyLinkedListNode(value)
node. prev = se1f, tail
if self.tail:
self.tail.next 
= node
else:
self.head = node
seIf.tai1 = node
self.-size += 1
def remove(self, node)
if node . next :
node.next.pr€v = node.prev
else:
self.tail 
= node,prev
if node,prev:
node.prev.next = node.next
else:
self.head = node.next
node,next = node.prev = None
se1f.-size -= 1
# Tracks the last occurrence (index) of each string in query-strings.
1oc = Linkedlisto
d = {s: None for s in query-strings}
result - Subarray(-1, -1)
for idx, s in enu[erate(strean):
if s in d: # s is in query-strings.
it = d[s]
lf it ls not None:
# ExplicitTy remove s so that when we add it, it's the string rost
# recentTy added to 7oc.
1oc , remove (it)
loc , insert-after (idx)
dlsl = Ioc.tail
if len(1oc) == Ien(query-strings):
# We have seen all strings in query-strings, 7et's get to work
if (result == (-1, -1)
or idx - Ioc. head, data < result [1] - result [0] ) :
result = (10c. head. data , idx)
return result
170
```
