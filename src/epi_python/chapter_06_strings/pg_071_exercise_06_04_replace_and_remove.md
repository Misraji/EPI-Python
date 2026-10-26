# Exercise 6.4: Replace and remove

**Printed textbook page:** 71. **Reference transcription pages:** 71–71.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 71 (PDF page 85)

```text
Variant: Solve the same problem with "A" corresponding to 0.
Varianh Implement a function that converts an integer to the spreadsheet column id. For example,
you should return "D" for 4, " AN' f.or 27, and "ZZ" for 702.
6.4 Rnpracs AND REMovE
Consider the following two rules that are to be applied to an array of characters.
o Replace each'a'by two'd's.
o Delete each entry containing a'b'.
For example, applying these rules to the array (A,c,d,b,b,c,a) results in the array (d,d,c,d,c,d,d).
Write a program which takes as input an array of characters, and removes each 'b' and replaces
each'a'by two 'd's. Specifically, along with the array, you are provided an integer-valued size. Size
denotes the number of entries of the array that the operation is to be applied to. You do not have
to worry about preserving subsequent entries. For example, if the array is (a,b,A,c,-) and the size
is 4, then you c€ul retum (d,d,d,d,c). You can assume there is enough space in the array to hold the
final result.
Hlnf; Consider performing multiples passes on s.
Solutioru Library array implementations often have methods for inserting into a specific location
(all later entries are shifted right, and the array is resized) and deleting from a specific location
(all later entries are shifted left, and the size of the array is decremented). If the input array had
such methods, we could apply them-howeveD the time complexity would be O(nz),where n is the
array's length. The reason is that each insertion and deletion from the array would have O(n) time
complexity.
This problem is trivial to solve n O(n) time if we write result to a new array-we skip 'b's,
replace 'a'sby two 'd's, and copy over all other characters. However, this entails O(n) additional
space.
If there are no 'a's,we can implement the function without allocating additional space with one
forward iteration by skipping 'b's and copying over the other characters.
If there are no 'b's, we can implement the function without additional space as follows. First, we
compute the final length of the resulting string, which is the length of the array plus the number of
'a's. We can then write the result, character by charactel, starting from the last character, working
our way backwards.
For example, suppose the array is (a,c,a,a,-,-,-), and the specified size is 4. Our algorithm
updates the array to (A, c, a, a, -, d, d>. (Boldface denotes characters that are part of the final result.)
The next update is (a,c,a,d,d,d,d),followedby (a,c,c,d,d,d,d), Nrdfinally \d,d,c,d,d,d,d).
We can combine these two approaches to get a complete algorithm. First, we delete 'b's and
compute the final number of valid characters of the string, with a forr.rzard iteration through the
string. Then we replace each 'a'by two 'd's, iterating backwards from the end of the resulting
string. If there are more 'b's than 'a's, the number of valid entries will decrease, and if there are
more 'a's than 'b's the number will increase. In the program below we refurn the number of valid
entries in the final result.
def replace-and-remove(size, s) :
# Forward iteration: 
temove 'b's and count the number of 'a's
71,
```
