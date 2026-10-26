# Exercise 5.6: Buy and sell a stock once

**Printed textbook page:** 46. **Reference transcription pages:** 46–46.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 46 (PDF page 60)

```text
Solution: Let A be the array and n its length. If we allow ourselves O(n) additional space, we can
solve the problem by iterating through A and recording values that have not appeared previously
into a hash table. (The hash table is used to determine if a value is new.) New values are also
written to a list. The list is then copied back into A.
Here is a brute-force algorithm that uses O(1) additional space-iterate through A, testing if A[l]
equals Ali + 7), and, if so, shift all elements at and after I + 2 to the left by one. lrVhen all entries are
equal,thenumberofshiftsis(n-l)+(n-2)+...+2+1.,i.e.,O(nz),wherezisthelengthofthe
arTay.
The intuition behind achieving a better time complexity is to reduce the amount of shifting.
Since the array is sorted, repeated elements must appear one-after-anothe1, so we do not need an
auxiliary data structure to check if an element has appeared already. We move just one element,
rather than an entire subarray, and ensure that we move it just once.
For the given example, (2,3,5,5,7,77,11,17,13), when processing the A[3], since we already
have a 5 (which we know by comparing Al3l with A[2]), we advance to A141. Since this is a new
value, we move it to the first vacant entry, namely A[3]. Now the array is <2,3,5,7,7,11.,1,'1,,11.,\3),
and the first vacant entry is A[ ]. We continue from A[5].
# Returns the number of valid entries after deletion
def delete-duplicates (A) :
if not A:
return 0
write-index = 1
for i in range(l, len(A)):
if A[write-index - 1] != A[i]:
Atwrite-indexl = AIi]
write-index += 1
return write-index
The time complexity is O(n), and the space complexity is O(1), since all that is needed is the two
additional variables.
Varianfi Implement a function which takes as input an array and a key, and updates the array so
that all occurrences of the input key have been removed and the remaining elements have been
shifted left to fill the emptied indices. Return the number of remaining elements. There are no
requirements as to the values stored beyond the last valid element.
Varian[ Write a program which takes as input a sorted atay A of integers and a positiveinteger m,
and updates A so that if x appears z times in A it appears exactly mn(Z,m) times in A. The update
to A should be performed in one pass, and no additional storage may be allocated.
5.6 Bw luo sELL A srocK oNCE
This problem is concerned with the problem of optimally buying and selling a stock once,
as described on Page 2. As an example, consider the following sequence of stock prices:
<31.0,31.5,275,295,260,270,290,230,255,250>. 
The maximum profit that can be made with one buy
and one sell is 30-buy at 260 and sell at 290. Note that 250 is not the lowest price, nor 290 the
highest price.
46
```
