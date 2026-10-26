# Exercise 24.32: Trapping water

**Printed textbook page:** 398. **Reference transcription pages:** 398–398.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 398 (PDF page 412)

```text
Flgure 24.10t The area of the horizontal lines is the maximum amount of water that can be trapped by the solid region.
For this container, it is 1 + 2 + | + 3 = 7.
# This node is a 7eaf.
huffman-encodingItree.s.c] = ". join(code)
else: 
# Non-7eaf node.
code . append ('0')
assign-huffman-code (tree. left , code)
code[-1] ='1'
assign-huffman-code (tree . right , code)
de1 code[-1]
huffman-encoding = 11
# Traverses the binary tree, assigning codes to nodes,
assign-huffinan-code(candidates t0l, tl )
return sun(Ien(huffman-encoding[s.c]) o s.freq / 100 for s in symbols)
Since each invocation of Steps (2.) on Page 396 and (3.) on Page 396 requires two extract-min atd
orne insert operation, it takes O(nlogn) time to build the Huffman tree, where n is the number of
characters. It's possible for the tree to be very skewed. In such a situation, the codewords are of
length T, 2,s, . . ., n, sothe time to generate the codebook becomes O(1' + 2 + "' + n) = O(nz).
It is exceedingly unlikely that you would be asked for a rigorous proof of optimality in an
interview setting. The proof that the Huffman algorithm yields the minimum average code length
uses induction on the number of characters. The induction step itself makes use of Proof by
contradiction, with the two leaves in the Huffrnan tree corresponding to the rarest characters
playing a central role.
24.32 TnepprNc warsn 0
The goal of this problem is to compute the capacity of a type of one-dimensional container. The
computation is illustrated in Figure 24.10.
A one-dimensional container is specifiedby an array of n nonnegative integers, specifying the height
of each unit-width rectangle. Design an algorithm for computing the capacity of the container.
Hint: Draw pictures, and focus on the extremes.
Solution: We can get a great deal of insight by visualizing pouring water into the container. \A/hen
the maximum capacity is achieved, the cross-section consists of a region in which the water level is
398
```
