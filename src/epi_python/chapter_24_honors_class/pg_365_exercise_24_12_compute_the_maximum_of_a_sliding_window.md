# Exercise 24.12: Compute the maximum of a sliding window

**Printed textbook page:** 365. **Reference transcription pages:** 365–365.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 365 (PDF page 379)

```text
start = (Ieft_parentheses_indices [-1]
if left-parentheses_indices else end)
max-length = trar(max_length, i - start)
return max_length
The time and space complexity areO(n).
Variant: Solve the same problem using only O(1) space.
24.12 Coupurr rHE MAXTMUM oF A sLrDrNG wrNDow g
Network traffic control sometimes requires studying traffic volume over time. This problem ex-
plores the development of an efficient algorithm for computing the traffic volumes.
l.b
2.5
1.4
1.3
3.7
1,.7
1.7
0 
1 
2 
3 
4 
5 
5 
7 
8 
9 
10 
11 
12 
13 
1.4
2.2
(a) Traffic at various timestamps.
3.7
3.7 
3.7
2.5
2.6 
2.6
1.7
1.3
0123
4567891011
(b) Maximum lralfic over a window size of 3.
Figure 24.51 Tratfic profile before and after windowing.
1,2 13 
1.4
You are given traffic at various timestamps and a window length. Compute for each input times-
tamp, the maximum traffic over the window length time interval which ends at that timestamp,
See Figure 24.5 for an example.
Hint: You need to be able to identify the maximum element in a queue quickly.
Solution: Assume the input is specified by window length w and an array A of pairs
consisting of integer timestamp and corresponding traffic volume. If A is not sorted
by timestamp, we sort it. 
For example, the traffic in 2a.5@) corresponds to the array
((0, 1.3), (2,2.5), (3,3.7), (5,1..4), (6,2.6), (8,2.2), (9,1..7), (14, 1.1)).
365
```
