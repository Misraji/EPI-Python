# Exercise 20.9: Design TeraSort and PetaSort

**Printed textbook page:** 310. **Reference transcription pages:** 310–310.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 310 (PDF page 324)

```text
209 DEsrcr'r TsxeSonr aruo PEu.Sonr
Modern datasets are huge. For example, it is estimated that a popular social network contains over
two trillion distinct items.
How would you sort a billion 1000 byte strings? How about a trillion L000 byte strings?
Hint: Can a trillion 1000 byte strings fit on one machhe?
Solution: A billion 1000 byte strings carmot fit in the RAM of a single machine, but can fit on the
hard drive of a single machine. Therefore, one approach is to partition the data into smaller blocks
that fit in RAM, sort each block individually, write the sorted block to disk, and then combine the
sorted blocks. The sorted blocks can be merged using for example Solution 10.L on Page 1"34. The
UNIX sort program uses these principles when sorting very large files, and is faster than direct
implementations of the merge-based algorithm just described'
If the data consists of a trillion 1000 byte strings, it cannot fit on a single machine-it must be
distributed across a cluster of machines. The most natural interpretation of sorting in this scenario
is to organize the data so that lookups can be performed via binary search. Sorting the individual
datasets is not sufficient, since it does not achieve a global ordering-lookups entail a binary search
on each machine. The straightforward solution is to have one machine merge the sorted datasets,
but then that machine will become the bottleneck.
A solution which does away with the bottleneck is to first reorder the data so that the ith machine
stores strings in a range, e.g., Machine 3 is responsible for strings that lie between daily Nd ending.
The range-to-machine mapping R can be computed by sampling the individual files and sorting
the sampled values. If the sampled subset is small enough, it can be sorted by a single machine.
The techniques in Solution 1L.8 on Page 153 can be used to determine the ranges assigned to each
machine. Specifically, let A be the sorted array of sampled strings. Suppose there are M machines.
Define ri = iAlnlM], where n is the length of A. Then Machine I is responsible for strings in the
rangefr;,ria1). If the distribution of the data is known apriori, e.g., it is uniform, the sampling step
can be skipped.
The reordering can be performed in a completely distributed fashion by having each machine
route the strings it begins with to the responsible machines.
After reordering, each machine sorts the strings it stores. Consequently queries such as lookups
can be performed by using R to determine which individual machine to forward the lookup to.
20.10 Iuprrr"mNr DISTRIBUTED rr{RorrLING
You have n machines ("crawlers") for downloading the entire web. The responsibility for a given
URL is assigned to the crawler whose ID is Hash(URL) mod n. Downloading a web page takes
away bandwidth from the web server hosting it.
Implement crawling under the constraint that in any given minute your crawlers do not request
more than b bytes from any website.
Hint: lJse a server to coordinate the crawl.
Solution: This problem, as posed, is ambiguous.
310
```
