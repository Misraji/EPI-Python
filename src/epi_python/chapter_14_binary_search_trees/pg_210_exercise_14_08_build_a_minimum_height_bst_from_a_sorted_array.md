# Exercise 14.8: Build a minimum height BST from a sorted array

**Printed textbook page:** 210. **Reference transcription pages:** 210–210.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 210 (PDF page 224)

```text
i+=1
if cand-j-plus-sqrt2.val == cand[-1].val
j+=1
return [a.val for a in cand]
Each additional element takes O(1) time to compute, implying anO(n) time complexity to compute
the first n values of the form a + b lr.
14.8 Buno e MINIMUM HEIGnT BST rnorvl A soRTED ARRAY
Given a sorted array, the number of BSTs that can be built on the entries in the array grows
enormously with its size. Some of these trees are skewed, and are closer to lists; others are more
balanced. See Figure 14.3 on Page 205 for an examPle.
How would you build a BST of minimum possible height from a sorted array?
Hlnf; Which element should be the root?
Solution: Brute-force is not much help here---enumerating all possible BSTs for the given array in
search of the minimum height one requires a nontrivial recursion/ not to mention enonnous time
complexity.
Intuitively, to make a minimum height BSf, we want the subtrees to be as balanced as possible-
there's no point in one subtree being shorter than the othef, since the height is determined by the
taller one. More formally, balance can be achieved by keeping the number of nodes in both subtrees
as close as possible.
Let n be the length of the array. To achieve optimum balance we ceu:l make the element in the
middle of the array, i.e., the Lf Jth entry, the root, and recursively compute minimum height BSTs
for the subarrays on either side of this entry.
As a concrete example, if the array is (2,3,5,7,11,13,77,79,23), the root's key will be the middle
element, i.e., 11. This implies the left subtree is to be built from <2,3,5,71, and the right subtree
is to be built from (73,17,19,23>. To make both of these minimum height, we call the procedure
recursively.
def bui Id-min-hei ght-bst-from-sorted-array (A) :
def build-min-height-bst-from-sorted-subarray(start, 
end) :
if start >= end:
return None
mid = (start + end,) // 
2
return BSTNode (Atmidl,
build-min-height-bst-from-sorted-subarray(start, 
mid),
build-min-height-bst-from-sorted-subarray(mid + 1, end))
return build-min-height-bst-from-sorted-subarray(0, len(A))
The time complexity T(n) satisfies the recurrence T(n) = 2T(nl2)+O(1), which solves toT(n) = O(n).
Another explanation for the time complexity is that we make exactly n calls to the recursive function
and spend O(1) within each call.
210
```
