# Exercise 10.1: Merge sorted files

**Printed textbook page:** 134. **Reference transcription pages:** 134–134.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 134 (PDF page 148)

```text
heapq. For objects, implement --1tO-- appropriately. Problem 10.4 on Page 137 illustrates how
use a max-heap.
10.1 Msncr soRTED FILES
This problem is motivated by the following scenario. You are given 500 files, each containing stock
trade information for an S&P 500 company. Each trade is encoded by a line in the following format:
L232LLL, AAPL, 30, 456. 12.
The first number is the time of the trade expressed as the number of milliseconds since the start
of the day's trading. Lines within each file are sorted in increasing order of time. The remaining
values are the stock symbol, number of shares, and price. You are to create a single file containing
all the trades from the 500 files, sorted in order of increasing trade times. The individual files are
of the order of 5-100 megabytes; the combined file will be of the order of five gigabytes. In the
abstract, we are trying to solve the following problem.
Write a program that takes as input a set of sorted sequences and computes the union of these
sequences as a sorted sequence. For example, if the input is <3,5,7>, (0,5), and <0,6,28>, then the
output is (0, 0, 3, 5, 6, 6,7, 28).
Hln f: Which part of each sequence is significant as the algorithm executes?
Solution: A brute-force approach is to concatenate these sequences into a single array and then sort
it. The time complexity is O(nlogn), assuming there are n elements in total.
The brute-force approach does not use the fact that the individual sequences are sorted. We
can take advantage of this fact by restricting our attention to the first remaining element in each
sequence. Specifically, we repeatedly pick the smallest element arnongst the first element of each of
the remaining part of each of the sequences.
A min-heap is ideal for maintaining a collection of elements when we need to add arbitrary
values and extract the smallest element.
For ease of exposition, we show how to merge sorted arrays, rather than files. As a concrete
example, suppose there are three sorted arrays tobe merged: (3,5,7>, <0,6>, and (0,6,28). For
simplicity, we show the min-heap as containing entries from these three arrays. In practice, we
need additional information for each entry, namely the array it is from, and its index in that array.
(Lr the file case we do not need to explicitly maintain an index for next unprocessed element in each
sequence-the file I/O library tracks the first unread entry in the file.)
The min-heap is initialized to the first entry of each arcay, i.e., it is {3, 0, 0}. We extract the smallest
entry, 0, and add it to the output which is (0). Then we add 6 to the min-heap which is {3,0,6} now
(We chose the 0 entry corresponding to the third array arbitrarily, it would be perfectly acceptable
to choose from the second array.) Next, extract 0, and add it to the output which is (0,0); then add
6 to the min-heap which is 13,6,61. Next, extract 3, and add it to the output which is (0,0,3); then
add 5 to the min-heap which is {5,6,6}. Next, extract 5, and add it to the output which is (0,0,3,5);
then add 7 to the min-heap which is 17,6,61. Next, extract 6, and add it to the output which is
(0,0,3,5,6); assuming 5 is selected from the second array, which has no remaining elements, the
min-heap is {7,6]1. Next, extract 6, and add it to the output which is (0,0,3,5,6,6); then add 28 to
the min-heap which is 17,281. Next, extractT, and add it to the output which is (0,0,3,5,6,6,7); the
min-heap is {28}. Next, extract 28, and add it to the output which is (0,0,3, 5,6,6,7,28); now, all
elements are processed and the output stores the sorted elements.
def merge-sorted-arrays (sorted-arrays)
134
```
