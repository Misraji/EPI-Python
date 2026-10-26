# Exercise 17.5: Find the majority element

**Printed textbook page:** 266. **Reference transcription pages:** 266–266.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 266 (PDF page 280)

```text
Alpl <Alrl < Alsl.
Varianh Write a program that takes as input an array of integers A and an integer T, and retums
the number of 3-tuples (p,q,r) such that Ald + Ald + Alrl < T and Alpl < Alql s Alrl.
17.5 FrNo rnr MAJoRITY ELEMENT
Several applications require identification of elements in a sequence which occur more than a
specified fraction of the total number of elements in the sequence. For example, we may want
to identify the users using excessive network bandwidth or IP addresses originating the most
Hypertext Transfer Protocol (HTTP) requests. Here we consider a simplified version of this problem.
You are reading a sequence of strings. You know a priori thatmore than half the strings are repetitions
of a single string (the "majority element") but the positions where the majority element occurs are
unknown. Write a program that makes a single pass over the sequence and identifies the majority
element. For example, if the input is \b,a,c,A,a,b,a,a,c,a>, then a is the majority element (it appears
in 6 out of the 10 places).
Hint:Take advantage of the existence of a majority element to perform elimination.
Solution: The brute-force approach is to use a hash table to record the repetition count for each
distinct element. The time complexity isO(n), where n is the number of elements in the input, but
the space complexity is also O(n).
Randomized sampling can be used to identify a majority element with high probability using
less storage, but is not exact.
The intuition for a better algorithm is as follows. We can Soup entries into two subgroups-
those containing the majority element, and those that do not hold the majority element. Since the
first subgroup is given to be larger in size than the second, if we see two entries that are different,
at most one cim be the majority element. By discarding both, the difference in size of the first
subgroup and second subgroup remains the same, so the majority of the remaining entries remains
unchanged.
The algorithm then is as follows. We have a candidate for the majority element, and track its
count. It is initialized to the first entry. We iterate through remaining entries. Each time we see an
entry equal to the candidate, we increment the count. If the entry is different, we decrement the
count. If the count becomes zero, we set the next entry to be the candidate.
Here is a mathematical justification of the approach. Let's say the majority element occurred m
times out of n entries. By the definition of majority element, 1 , i. At most one of the two distinct
entries that are discarded can be the majority element. Hence, after discarding them, the ratio of
the number of remaining majority elements to the total number of remaining elements is either
1r-44 (neither discarded element was the majority element) ", ffi (one discarded element was the
majorityelement). Itis simpletoverifythatif l r l,thenboth ffi, 
+arrrdffi > +.
For the given example, (b,a,c,a,a,b,a,a,c,a), we initialize the candidate to b. The next element,
a is different from the candidate, so the candidate's count goes to 0. Therefore, we pick the next
element c to be the candidate, and its count is 1. The next element, a, is dTfterent so the count goes
back to 0. The next element is a, which is the new candidate. The subsequent b decrements the
count to 0. Therefore the next element, a, is the new candidate, and it has a nonzero count till the
end.
def majority-search (input-stream) :
candidate , candidate-count = None, 0
266
```
