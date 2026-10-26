# Exercise 5.13: Sample online data

**Printed textbook page:** 55. **Reference transcription pages:** 55–55.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 55 (PDF page 69)

```text
Intuitively, if all subsets of size k are equally likely, then the construction process ensures that
the subsets of size k + 1 are also equally likely. A formal proof, which we do not present, uses
mathematical induction-the induction hypothesis is that every pennutation of every size k subset
of A is equally likely to be in A[0, k - 1].
As a concrete example, let the input be / = (3,7,5,11) and the size be 3. In the first iteration, we
use the random number generator to pick a random integer in the interval [0,3]. Let the retumed
random number be 2. We swap .4[0] with A[2]-now the array is <5,7,3,11). Now we pick a
random integer in the interval [1,3]. Let the retumed random number be 3. We swap A[1] with
A[3]-now the resulting array is <5,1L,3,7). Now we pick a random integer in the interval [2,3]. Let
the retumed random number be 2. \rVhen we swap A[2] with itself the resulting array is unchanged.
The random subset consists of the first three entries, i.e., {5, 1.1,3}.
def random-sampling (k, A) :
for i in range(k):
# cenerate a random index in [i, len(A) - 1]
r = random.randint(i, len(A) - 1)
Atil, Atrl = A[r], AIil
The algorithm clearly runs in additional O(1) space. The time complexity is O(k) to select the
elements.
The algorithm makes k calls to the random number generator. \Alhen k is bigger than f, we
can optimize by computing a subset of n - k elements to remove from the set. For example, when
k=n-l,thisreplacesn-lcallstotherandomnumbergeneratorwithasinglecall.
Varianft The randO function in the standard C library retums a uniformly random number in
[0, RAND-]IAX - 11. Does randO mod n generate a number uniformly distributed in [0, n - 1]?
5.13 Sluprr oNLTNE DATA
This problem is motivated by the design of a packet sniffer that provides a uniform sample of
packets for a network session.
Design a program that takes as input a size k, and reads packets, continuously maintaining a
uniform random subset of size k of the read packets.
Hlnf: Suppose you have a procedure which selects k packets from the first n > k packets as specified. How
would you deal with the (n + 1)th packet?
Solution: A brute force approach would be to store all the packets read so far. After reading in each
packet, we apply Solution 5.12 on the preceding page to compute a random subset of k packets.
The space complexity is high--O(n), after n packets have been read. The time complexity is also
high-4(nk), since each packet read is followed by a call to Solution 5.12 on the facing page.
At first glance it may seem that it is impossible to do better than the brute-force approach,
since after reading the nth packet, we need to choose k packets uniformly from this set. However,
suppose we have read the first n packets, and have a random subset of k of them. When we read
the (n + 1)th packet, it should belong to the new subset with probability kl(n + 1). If we choose one
of the packets in the existing subset uniformly randomly to remove, the resulting collection will be
a random subset of the n + 1 packets.
55
```
