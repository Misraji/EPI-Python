# Exercise 10.4: Compute the k closest stars

**Printed textbook page:** 137. **Reference transcription pages:** 137–138.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 137 (PDF page 151)

```text
Write a Program which takes as input a very long sequence of numbers and prints the numbers in
sorted order. Each number is at most k away from its correctly sorted position. (Such an array is
sometimesreferredtoasbeingk-sorted.) Forexample,nonumberinthesequence(3, -1.,2,6,4,5,8>
is more than 2 away from its final sorted position.
Hint: f{ow many numbers must you read after reading the ith number to be sure you can place it in the correct
location?
Solution: The brute-force approach is to put the sequence in an array, sort it, and then print it. The
time complexity is O(nlogn), where n is the length of the input sequence. The space complexity is
o(n).
We can do better by taking advantage of the almost-sorted property. Specifically, after we have
read k + 1 numbers, the smallest number in that group must be smaller than all following numbers.
For the given example, after we have read the first 3 numbers, 3, -1.,2, the smallest, -1, must be
globally the smallest. This is because the sequence was specified to have the property that every
number is at most 2 away from its final sorted location and the smallest number is at index 0 in
sorted order. After we read in the 4, the second smallest number must be the minimum of 3,2,4,
i.e.,2.
To solve this problem in the general setting, we need to store k + 1 numbers and want to be
able to efficiently extract the minimum number and add a new number. A min-heap is exactly
what we need. We add the first k numbers to a min-heap. Now, we add additional numbers to the
min-heap and extract the minimum from the heap. (When the numbers run out, we just perform
the extraction.)
def sort-approximately-sorted_array (sequence , k) :
result = []
min-heap = []
# Adds the first k e-lefients irto njn_heap. Stop if there are fewer than k
# eTenents.
for x in itertools. islice(sequence, k):
heapq. heappush(min-heap, x)
# For every ne,, e].enent, add it to min_heap and extract the sfia-i.lest
for x in sequence:
smallest - heapq. heappushpop (nrin_heap , x)
result . append ( smallest)
# sequence is exhausted, iteratively 
extracts the remajnjng e-lenrents
rhile min-heap:
smallest = heapq. heappop(min_heap)
result . append ( smallest)
return result
The time complexity is O(nlogk). The space complexity is O(k).
1,0.4 Covrurs rrrs k crosEsr srARS
Consider a coordinate system for the Milky Way, in which Earth is at (0,0,0). Model stars as points,
and assume distances are in light years. The Milky Way consists of approximately 1012 stars, and
their coordinates are stored in a file.
How would you compute the k stars which are closest to Earth?
137
```

#### Printed page 138 (PDF page 152)

```text
[
]
Hinf; Suppose you know the k closest stars in the first r stars. If the (r + 1.)th star is to be added to the set of k
closest stars, which element in that set should be evicted?
Solution: If RAM was not a limitation, we could read the data into an array, and compute the
k smallest elements using sorting. Altematively, we could use Solution 11.8 on Page 153 to find
the kth smallest element, after which it is easy to find the k smallest elements. For both, the space
complexity is O(n), which, for the given dataset, cannot be stored in RAM.
Intuitively, we only care about stars close to Earth. Therefore, we can keep a set of candidates,
and iteratively update the candidate set. The candidates are the k closest stars we have seen so
far. \,Vhen we examine a new star, we want to see if it should be added to the candidates. This
entails comparing the candidate that is furthest from Earth with the new star. To find this candidate
efficiently, we should store the candidates in a container that supports efficiently extracting the
maximum and adding a new member.
A max-heap is perfect for this application. Conceptually, we start by adding the first k stars
to the max-heap. As we process the stars, each time we encounter a new star that is closer to
Earth than the star which is the furthest from Earth among the stars in the max-heap, we delete
from the max-heap, and add the new one. Otherwise, we discard the new star and continue. We
can simplify the code somewhat by simply adding each star to the max-heap, and discarding the
maximum element from the max-heap once it contains k + 1 elements.
class Star:
def --init--(self, 
x, y, z);
self.x, self.y, self.z = x, y, z
@property
def distance (self) :
return math.sqrt(seIf.x*t2 + self.y**2 + se1f,z**2)
def --It--(self, 
rhs):
return self.distance < rhs,distance
def find-closest-k-stars (stars , k) :
# nax-heap to store the closest k stars seen so far.
max-heap = []
for star in stars:
# Add each star to the nax-heap. If the max-heap size exceeds k, remove
# the naxinum efernent fron the nax-heap.
# As python has onTy nin-heap, insert tupTe (negative of distance, star)
# to sott in reversed distance order.
heapq.heappush(max-heap, (-star. distance, star))
if len(max-heaP) == k + 1:
heapq . heappop (max-heap )
# Iteratively extract fron the nax-heap, which yieTds the stars sorted
# according fron furthest to closest.
return Is[1] for s in heapq.nlargest(k, max-heap)l
The time complexity isO(nlogk) and the space complexity is O(k).
Varianh Design an O(nlogk) time algorithm that reads a sequence of n elements and for each
element, starting from the kth element, prints the kth largest element read up to that point. The
138
```
