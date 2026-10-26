# Exercise 12.7: Find smallest subarray sequentially covering all values

**Printed textbook page:** 171. **Reference transcription pages:** 171–172.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 171 (PDF page 185)

```text
Variant: Given an array A, find a shortest subarray A[], i] such that each distinct value present in A
is also present in the subarray.
Varianh Given an array A, rearrange the elements so that the shortest subarray containing all the
distinct values in A has maximum possible length.
Variant: Given an array A and a positive integer k, rearrange the elements so that no two equal
elements are k or less apart.
12.7 Frruo sulrrrsr suBARRAy sEeuENTrALLy covERrNG ALL VALUES
In Problem 12.6 on Page 168 we did not differentiate between the order in which keywords appeared.
If the digest has to include the keywords in the order in which they appear in the search textbox,
we may get a different digest. For example, for the search keywords "IJnion" arrd "save", in that
order, the digest would be "Uniory and is not either to save".
Write a program that takes two arrays of strings, and return the indices of the starting and ending
index of a shortest subarray of the first array (the "paragraph" array) that "sequentially covers",
i.e., contains all the strings in the second array (the "keywords" array), in the order in which they
aPPear in the keywords array. You can assume all keywords are distinct. For example, let the
paragraph array be (apple,banana,cat,apple), and the keywords array be (banana,apple). The
paragraph subarray starting at index 0 and ending at index L does not fulfill the specification, even
though it contains all the keywords, since they do not appear in the specified order. On the other
hand, the subarray starting at index 1 and ending at index 3 does fulfill the specification.
Hint: For each index in the paragraph array, compute the shortest subarray ending at that index which fulfills
the specification.
Solution: The brute-force approach is to iterate over all subarrays of the paragraph array. To
check whether a subarray of the paragraph array sequentially covers the keyword afiay,we search
for the first occurrence of the first keyword. We never need to consider a later occurrence of the
first keyword, since subsequent occurrences do not give us any additional power to cover the
keywords. Next we search for the first occurrence of the second keyword that appears after the first
occurrence of the first keyword. No earlier occurrence of the second keyword is relevant, since those
occurrences can never appear in the correct order. This observation leads to arrO(n) time algorithm
for testing whether a subarray fulfiIls the specification, where n is the length of the paragraph array.
Since there are O(nz) subarrays of the paragraph array, the overall time complexity is O(n1).
The brute-force algorithm repeats work. We can improve the time complexity to O(n2) by
computing for each index, the shortest subarray starting at that index which sequentially covers
the keyword array. The idea is that we can compute the desired subarray by advancing from the
start index and marking off the keywords in order.
The improved algorithm still repeats work-as we advance through the paragraph array, we
can reuse our computation of the earliest occurrences of keywords. To do this, we need auxiliary
data strucfures to record previous results.
Specifically, we use a hash table to map keywords to their most recent occurrences in the
paragraph array as we iterate through it, and a hash table mapping each keyword to the length of
the shortest subarray ending at the most recent occurrence of that keyword.
171,
```

#### Printed page 172 (PDF page 186)

```text
These two hash tables give us is the ability to determine the shortest subarray sequentially
covering the first k keywords given the shortest subarray sequentially covering the first k - 1
keywords.
When processing the lth string in the paragraph array, if that string is the lth keyword, we
update the most recent occurrence of that keyword to i. The shortest subarray ending at I which
sequentially covers the first i keywords consists of the shortest subarray ending at the most recent
occurrence of the first 7 - 1 keywords plus the elements from the most recent occurrence of the
U - 1)th keyword to l. This computation is implemented below
Subarray = collections.namedtuple('Subarray', ('start','end'))
def find-smallest-sequentially-covering-subset (paragraph, keywords)
# Ilaps each keyword to its index in the keywords array.
keyword-to-i61 = {k: i for i, k in enu[erate(keywords)]
# Since keywords are uniquely identified by their indices in keywords
# array, we can use tiose indices as keys to Tookup in an array.
latest_occurrence = t-tl * len(keywords)
# For each keyword (identified by its index in keywords array), the length
# of the shortest subarray ending at the nost recent occurrence of that
# keyword that sequentiaTTy cover a7l keywords up to that keyword,
shortest-subarray-Iength = [float('inf')] 
* Ien(keywords)
shortest-distance = float(' inf ')
result = Subarray(-1, -1)
for i, p in enunerate(paragraph):
if p in keyword-to-idx:
keyword-idx = keyword-to-idxlpl
if keyword-idx == 0: # First keyword,
shortest-subarray-length Ikeyword-idx] = f
elif shortest-subarray-lengthIkeyword-idx - 1] != float('inf'):
distance-to-previous-keyword = (
i - latest-occurrenceIkeyword-idx - 1])
shortest-subarray-length Ikeyword-idx] = I
distance-to-previous-keyword +
shortest-subarray-lengthIkeyword-idx - 1])
latest-occurrence Ikeyword-idx] = i
# Last keyword, for improved. subarray.
if (keyword-idx == Ien(keywords) - 1
and shortest-subarray-length[-1] < shortest-distance)
shortest-distance = shortest-subarray-length[-1]
result = Subarray(i - shortest-distance + 1, i)
return result
Processing each entry of the paragraph array entails a constant number of lookups and updates,
leading to an O(n) time complexity, where n is the length of the paragraph array. The additional
space complexity is dominated by the three hash tables, i.e., O(m), where ln is the number of
keywords.
172
```
