# Exercise 24.18: Find an element that appears only once

**Printed textbook page:** 374. **Reference transcription pages:** 374–374.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 374 (PDF page 388)

```text
By using 2k-1. as the array size, the time complexity to find the kth largest element is almost certain
O(k).It is run every k - 1 elements, implying anO(n) time complexity.
Note that we could use less storage, e.g., an array of length 3k12, and still achieve O(n) time
complexity. The actualrun time would be higher with an array of length 3kl2 since we only discard
k/2 elements for each call to finding the kth largest element. This is a classic space-time trade-off. If
we used a 4k long array, we could discard 3k elements for one call to Solution 11.8 on Page 153. The
time complexity of Solution 11..8 on Page 153 is proportional to the length of the array, so using a
length 4k array compared to a length 3kl2 aruay yields a speed-up of T&Lrr,r, = 2.25. Clearly more
storage leads to faster run times (in the extreme we read all n and do a single call to Solution 11.8
on Page 153), so there is a trade-off with respect to how much storage we want.
24.1,8 FrNo eN ELEMENT rrrAT AppEARs oNLY orvcr $
Given an integer array of length n, where each element except for one appears twice, with the
remaining element appearing only once, we can use O(n) space and O(n) nrrte to find the element
that appears exactly once, e.g., using a hash table. However, there is a better solution: compute
the bitwise-XoR (O) of all the elements in the array. Because x @ x -- 0, all elements that aPPear an
even number of times cancel out, and the element that appears exactly once remains. Therefore,
this problem can be solved using O(1) sPace.
Given an integer array, inwhich each entrybut one appears in triplicate, with the remainingelement
appearing once, find the element appearing once. For example, if the array is (2,4,2,5,2,5,5),you
should retum 4.
Hint: Count the number of 1s at each index.
Solution: The brute-force solutions in Solution 24.18, namely using a hash table or sorting will
work for this problem too, with the same time and sPace complexities.
One way to view Solution 11.10 on Page 757 is that it counts mod 2 for each bit-position the
number of entries in which the bit in that position is 1. Specifically, the XOR of elements at indices
l},i - 1,1, determines exactly which bit-positions have been odd number of times in elements of the
input array whose indices are in [0, ] - 1].
The analogous approach for the current problem is to count mod 3 for each bit-position the
number of times the bit in that position has been 1. The effect of counting mod 3 is to eliminate
the elements that appear three times, and so the bit-positions which have a count of L are precisely
those bit-positions in the count which are set to 1.
The example affay, <2,4,2,5,2,5,5), expressed in binary is ((010)2, (100)2, (010)2, (101)2, (010)2,
(101)2, (101)2). The number of bits set to 1 in position 0 (the LSB) across allT array entries is 3; the
number of bits set to 1 in position 1 is 3, and the number of bits set to 1 in position 2 is 4. By taking
each of these quantities mod 3 we cast out the contributions of elements that appear exactly three
times, which leaves us with a 1 in the MSB and 0 in the remaining two positions, i.e., the element
which only appeared once.
We can implement the above idea using an array C of integers whose length equals the integer
word size. Entry C[] will be used to count the number of 1s in bit-position l, across all the inputs.
374
```
