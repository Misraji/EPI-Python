# Exercise 24.33: The heavy hitter problem

**Printed textbook page:** 399. **Reference transcription pages:** 399–399.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 399 (PDF page 413)

```text
nondecreasing, followed by a region in which the water level is nonincreasing. The transition from
nondecreasing to nonincreasing must take place around the maximum entry in A. Let Almlbe a
maximum value entry. Then we compute the capacity of Al},m - 1l aurtd Afm,n - l)independently.
These capacities are determined via an iteration. For each entry in Al},m - 1] we compute the
difference between its value entry and the running maximum, and add that to the total capacity. We
handle Afm,n - 1l analogously. The tirne complexity is O(n) to find a maximum, and then O(n) for
each of the two iterations, i.e., the total time complexity is O(n). The space complexity is O(1)-all
that is needed is to record several variables.
def calculate-trapping-water(heights) :
# Finds the index with naximun height
max_h = heights. index(nax(heights))
# Assume heightst-11 is naximum height.
def trapping-water_till_end(heights) 
:
partial-sum, highest_level_seen = 0, float('-inf,)
for h in heights:
if h >= highest-level_seen:
highest-level-seen = h
else:
partial-sum += highest-Ievel-seen - h
return partial_sum
return (trapping_water_ti1l_end(heights [ : max_h] ) +
trapping_water_ti1l_end(reversed(heights [max_h + f : ]) ))
Varianfi Solve the water filling problem with an algorithm that accesses A's elements in order and
can read an element only once. Use minimum additional space.
24.33 THr nrew HrrrER rRoBLEM I
This problem is a generalization of Problem 17.5 on Page266. h:r practice we may not be interested
in a majorify token but all tokens whose count exceeds say 1% of the total token count. It is fairly
straightforward to show that it is impossible to compute such tokens in a single pass when you have
limited memory. However, if you are allowed to pass through the sequence twice, it is possible to
identify the common tokens.
You are reading a sequence of strings separated by whitespace. You are allowed to read the sequence
twice. Devise an algorithm that uses O(k) memory to identi$r the words that occur more than f
times, where r is the length of the sequence.
Hinfr Maintain a list of k candidates.
Solution: This is essentially a generalization of Problem 17.5 on Page 266. Here instead of discarding
two distinct words, we discard k distinct words at any given time and we are guartu:rteed that all
the words that occurred more than f times the length of the sequence prior to discarding continue
to appear more than f times in the remaining sequence. To implement this strategy, we need a hash
table of the current candidates.
# Finds the candidates rhicfi nay occur > n / k tines
399
```
