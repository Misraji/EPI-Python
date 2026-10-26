# Exercise 5.14: Compute a random permutation

**Printed textbook page:** 56. **Reference transcription pages:** 56–56.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 56 (PDF page 70)

```text
The formal proof that the algorithm works correctly, uses induction on the number of packets
that have been read. Specifically, the induction hypothesis is that all k-sized subsets are equally
likely after rz > k packets have been read.
As an example, suppose k = 2, aurrd the packets are read in the order p,Q,t,t,u,u. We keep the
first fwo packets in the subset, which is lp,ql. We select the next packet, r, with probability 2/3.
Suppose it is not selected. Then the subset after reading the first three packets is still lp,ql. We
select the next packet, f, with probability 214. Suppose it is selected. Then we choose one of the
packets in lp,ql uniformly, and replace it with t. Let q be the selected packet-now the subset is
{p,tl. We select the next packet u with probability 2/5. Suppose it is selected. Then we choose one
of the packets in {p, f } uniformly, and replace it with u. Let tbe the selected packet-now the subset
is {p,ul. We select the next packet u with probability 216. Suppose it is not selected. The random
subset remains {p, u}.
# Assumption: there are at least k elements in the strean
def online-random-sanple (it , k) :
# Stores the first k el.erents.
sampling-results = list(itertools.islice(it, 
k))
# Ilave read the first k e-Zements.
num-seen-so-far = k
for x in it:
num-seen-so-far += 1
# Generate a randon number in [0, nufl-seen-so-far - 1], and if thjs
# nunber is jn [0, k - 1], we replace that e.lement fron the sanpTe with
# x.
idx-to-replace = random. randrange (num-seen-so-far)
if idx-to-replace < k:
sampling-results Iidx-to-replace] = ;
return sampling-results
The tirne complexity is proportional to the number of elements in the stream, since we spend O(1)
time per element. The space complexity is O(k).
Note that at each iteration, every subset is equally likely. However, the subsets are not indepen-
dent from iteration to iteration-successive subsets differ in at most one element. [r contrast the
subsets computed by brute-force algorithm are independent from iteration to iteration.
5.1.4 Coupurr A RANDoM PERMUTATIoN
Generating random permutations is not as straightforward as it seems. For example, iterating
through <0,7, . . . ,n - l) and swapping each element with another randomly selected element does
nof generate all permutations with equal probability. One way to see this is to consider the case
n = 3. The number of permutations is 3! = 6. The total number of ways in which we can choose
the elements to swap is 33 = 27 and all are equally likely. Since2T is not divisibleby 6, some
permutations correspond to more ways than others, so not all permutations are equally likely.
Design an algorithm that creates uniformly random permutations of {0, 1,.. .,fl - 1}. You are given
a random number generator that returns integers in the set 10,1, . . . ,n - 7l with equal probability;
use as few calls to it as possible.
56
```
