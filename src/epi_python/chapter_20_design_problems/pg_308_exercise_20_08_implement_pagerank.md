# Exercise 20.8: Implement PageRank

**Printed textbook page:** 308. **Reference transcription pages:** 308–309.

> **Unverified OCR transcription:** This section retains the supplied PDF text layer. It is not certified verbatim: code syntax, mathematical symbols, and page boundaries may be corrupted. When two exercises begin on the same page, their excerpts overlap. Do not paste extracted code into a `.py` file without manual verification.

#### Printed page 308 (PDF page 322)

```text
Given a million documents with an average size of 10 kilobytes, design a program that can efficiently
retum the subset of documents containing a given set of words.
Hint:Butld on the idea of a book's index.
Solution: The predominant way of doing this is to build inverted indices. In an inverted index, for
each word, we store a sequence of locations where the word occurs. The sequence itself could be
represented as an array or a linked list. Location is defined to be the document ID and the offuet in
the document. The sequence is stored in sorted order of locations (first ordered by document ID,
then by offtet). When we are looking for documents that contain a set of words, what we need to
do is find the intersection of sequences for each word. Since the sequences are already sorted, the
intersection can be done in time proportional to the aggregate length of the sequences. We list a
few optimizations below.
o Compression--compressing the inverted index helps both with the ability to index more docu-
ments as well as memory locality (fewer cache misses). Since we are storing sorted sequences,
one way of compressing is to use delta compression where we only store the difference
between the successive entries. The deltas can be represented in fewer bits.
o Caching-the distribution of queries is usually fairly skewed and it helps a great deal to cache
the results of some of the most frequent queries.
o Frequency-based optimization---+ince search results often do not need to retum every document
that matches (only top ten or so), only a fraction of highest quality documents can be used to
answer most of the queries. This means that we can make two inverted indices, one with the
high quality documents that stays in RAM and one with the remaining documents that stays
on disk. This way if we can keep the number of queries that require the secondary index to a
small enough numbeq, then we can still maintain a reasonable throughput and latency.
o lntersection order-stnce the total intersection time depends on the total size of sequences, it
would make sense to intersect the words with smaller sets first. For example, if we are looking
for "USA GDP 2009" , it would make sense to intersect the lists for GDP and 2009 before trying
to intersect the sequence for USA.
We could also build a multilevel index to improve accuracy on documents. For a high priority web
page, we can decompose the page into paragraphs and sentences, which are indexed individually.
That way the intersections for the words might be within the same context. We can pick results
with closer index values from these sequences. See the sorted array intersection problem 13.1 on
Page 782 and digest problem 12.6 on Page 168 for related issues.
20.8 lNrprsrlsNr PecsRANr
The PageRank algorithm assigns a rank to a web page based on the number of "important" pages
that link to it. The algorithm essentially amounts to the following:
(1.) Build a matrix A based on the hyperlink structure of the web. Specifically, Art = t rt page j
links to page i;here di is the number of distinct Pages linked from page l.
(2.) Find X satisfying X = e [1] + (1- e)AX. Here e is a constant , e.g., ] , and [1] represents a column
vector of 1s. The value Xft] is the rank of the ith page.
The most commonly used approach to solving the above equation is to start with a value of
X, where each component is f (*n"r" n is the number of pages) and then perform the following
308
```

#### Printed page 309 (PDF page 323)

```text
iteration: Xr = e[L] + (1 * e)AXp-1. The iteration stops when the Xp converges, i.e., the difference
from X1 to Xp,.1 is less than a specified threshold.
Design a system that can compute the ranks of ten billion web pages in a reasonable amount of
time.
Hint: This must be performed on an ensemble of machines. The right data structures will simplify the
computation.
Solution: Since the web graph can have billions of vertices and it is mostly a sparse graph, it is
best to represent the graph as an ad;'acency list. Building the adjacency list representation of the
graph may require a significant amount of computation, depending upon how the information is
collected. Usually, the graph is constructed by downloading the pages on the web and extracting
the hyperlink information from the pages. Since the URL of a page can vary in length, it is often a
good idea to represent the URL by a hash code.
The most expensive part of the PageRank algorithm is the repeated matrix multiplication.
Usually, it is not possible to keep the entire graph information in a single machine's RAM. TWo
approaches to solving this problem are described below
o Disk-based sorting-we keep the column vector X in memory and load rows one at a time.
Processing Row f simply requires adding A;,iX1to X7 for each i such that Ai,1is not zero. The
advantage of this approach is that if the column vector fits in RAM, the entire computation
can be performed on a single machine. This approach is slow because it uses a single machine
and relies on the disk.
o Partitioned graph-we use n servers and partition the vertices (web pages) into n sets. This
partition can be computed by partitioning the set of hash codes in such a way that it is easy
to determine which vertex maps to which machine. Given this partitioning, each machine
loads its vertices and their outgoing edges into RAM. Each machine also loads the portion of
the PageRank vector corresponding to the vertices it is responsible for. Then each machine
does a local matrix multiplication. Some of the edges on each machine may correspond to
vertices that are owned by other machines. Hence the result vector contains nonzero entries
for vertices that are not owned by the local machine. At the end of the local multiplication
it needs to send updates to other hosts so that these values can be correctly added up. The
advantage of this approach is that it can process arbitrarily large graphs.
PageRank runs in minutes on a single machine on the graph consisting of the multi-million pages
that constitute Wikipedia. It takes roughly 70 iterations to converge on this graph. Anecdotally,
PageRank takes roughly 200 iterations to converge on the graph consisting of the multi-billion pages
that constitute the World-Wide Web.
When operating on a graph the scale of the webgraph, PageRank must be run on many thou-
sands of machines. ln such situations, it is very likely that a machine will fail, e.g., because of a
defective Power supply. The widely used Map-Reduce framework handles efficient parallelization
as well as fault-tolerance. Roughly speaking, fault-tolerance is achieved by replicating data across
a distributed file system, and having the master reassign jobs on machines that are not responsive.
309
```
