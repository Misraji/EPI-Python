# Exercise 5.16: Generate nonuniform random numbers

**Printed textbook page:** 58. **Reference transcription pages:** 58–59.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 58 (PDF page 72)

```text
approach suffers from the same performance degradation when k is close to n, and it also requires
O(k) additional space.
We could mimic the offIine sampling algorithm described in Solution 5.12 on Page 54, with
Alil = I initially, stopping after k iterations. This requires O(n) space and O(n) time to create the
array. After creating <0,1.,2,... ,n - 1), we need O(k) time to produce the subset.
Note that when k << ,1, most of the array is untouched, i.e., Ali) = l. The key to reducing the
space complexity to O(k) is simulating A with a hash table. We do this by only tracking entries
whose values are modified by the algorithm-the remainder have the default value, i.e., the value
of an entry is its index.
Specifically, we maintain ahash table H whose keys and values are from |.0,1,. . . ,n-ll.Concep-
tually, H tracks entries of the array which have been touched in the process of randomization-these
are entries A[] which may not equal l. The hash table H is updated as the algorithm advances.
o If i is in H, then its value in H is the value stored at AIil in the brute-force algorithm.
r If I is not in H, then this implicitly implies Alil = i.
Since we track no more than k entries, when k is small compared to n, we save tirne and space over
the brute-force approach, which has to initialize and update an array of length n.
Initially,Hisempty.Wedokiterationsofthefollowing. Choosearandomintegerrtn[O,n-L-i],
where I is the current iteration count, starting at 0. There are four possibilities, corresponding to
whether the two entries in A that are being swapped are already present or not present in H. The
desired result is in A[0, k - 1], which can be determined from H.
For example, suppose n = 100 and k = 4. In the first iteration, suppose we get the random
number 28. We update H to (0,28),(28,0). This means that A[0] is 28 and A[28] is G-for all other
i, AliT = i. In the second iteration, suppose we get the random number 42. We update H to
(0,28),(28,0),(7,42),(42,1).In the third iteration, suppose we get the random number 28 again. We
update H to (0,28),(28,2),('i,,42),(42,1),(2,0). In the third iteration, suppose we get the random
number 64. We update H to (0,28), (28,2),(1,,42),(42,1),(2,0),(3,64),(@,3). The random subset is
the 4 elements corresponding to indices 0,7,2,3, i.e., (28,42,0,64).
def random-subset (n, k) :
changed-elements = {}
for i in range (k) :
# Generate a random index between j and n - 7, inclusive.
rand-idx = random.randrange(i, n)
rand-idx-mapped = changed-elements. get (rand-idx , rand-idx)
i-mapped = changed-elements . get (i , i)
changed-elements Irand-idx] = i-mapped
changed-elements Ii] = rand-idx-mapped
return Ichanged-elementsIi] for i in range(k)l
The time complexity is O(k), since we perform a bounded number of operations per iteration. The
space complexity is also O(k), since H and the result array never contain more than k entries.
5,16 GBuunanr NoNUNIFoRM RANDoM NUMBERs
Suppose you need to write a load test for a server. You have studied the inter-arrival time of
requests to the server over a period of one year. From this data you have computed a histogram
58
```

#### Printed page 59 (PDF page 73)

```text
of the distribution of the inter-arrival time of requests. In the load test you would like to generate
requests for the seryer such that the inter-arrival times come from the same distribution that was
observed in the historical data. The following problem formalizes the generation of inter-arrival
times.
Youaregivenrnumbersaswellasprobabilitiespo,pt,...,pn-r,whichsumuptol. 
Givenarandom
number generator that produces values in [0, 1) uniformly, how would you generate one of the n
numbers according to the specified probabilities? For example, if the numbers are 3,5,7,11, and
the probabilities are 9118,611.8,2118,1118, then in 1000000 calls to your program,3 should appear
roughly 500000 times,5 should appear roughly 333333 times, 7 should appear roughly 111111 times,
and 11 should appear roughly 55555 times.
Hint: l-ook at the graph of the probability that the selected number is less than or equal to a. What do the
jumps correspond to?
Solution: First note that actual values of the numbers is immaterial-we want to choose from one
of n outcomes with probabilities po,pr, . . . ,pn-1.. If all probabilities were the same, i.e., 1. f n, we could
make a single call to the random number generator, and choose outcome I if the number falls lies
between i I n and (i + 1) I n.
For the case where the probabilities are not the s6une, we can solve the problem by partitioning
the unit interval [0,1] into n disjoint segments, in a way so that the length of the fth interval is
proportional to pi. Then we select a number uniformly at random in the unit interval, [0, 1], and
retum the number corresponding to the interval the randomly generated number falls in.
An easy way to create these intervals is to useps,ps+pl,po+p1 +p2,...,p0+pt+pz+... +
Pn-t as the endpoints. Using the example given in the problem statement, the four intervals are
[0.0,0.5), [0.5,0.833),10.833,0.944),10.944,1.0]. 
Now, for example, if the random number generated
uniformly in [0.0, 1.0] is 0.873, since 0.873 lies in [0.833,0.944), which is the third interval, we retum
the third numbeq, which is 7.
In general, searching an array of n disjoint intervals for the interval containing a number takes
O(n ) time. However, we can dobetter, since the array <po,po+pr,po+p1+pz, . . . ,py+pr+p2+. - .+pn-rl
is sorted, we can use binary search to find the interval in O(1ogn) time.
def nonuniform-randon-number_generation 
(values, probabili ti es ) :
prefix-sum-of-probabilities 
= list (itertools 
. accunulate (probabilities) )
interval-idx = bisect.bisect(prefix-sum-of-probabilities, 
randon.random())
return values Iinterval_idx]
The time complexity to compute a single value is O(n), which is the time to create the array of
intervals. This array also implies anO(n) space complexity.
Once the array is constructed, computing each additional result entails one call to the uniform
random number generator, followed by a binary search, i.e., O(logn).
Varianh Given a random number generator that produces values in [0,1] uniformly, how would
you generate a value X from T according to a continuous probability distribution, such as the
exponential distribution?
59
```
